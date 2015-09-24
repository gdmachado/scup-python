try:
    import simplejson as json
except ImportError:
    import json
import six
import re

from six.moves.urllib.parse import quote
from scup.exceptions import *
from scup.auth import get_request_signature
from requests import Request

re_path_template = re.compile('{\w+}')

def encode_string(value):
        return value.encode('utf-8') \
                if isinstance(value, six.text_type) else str(value)

def bind_method(**config):

    class ScupAPIMethod(object):
        path = config['path']
        method = config.get('method', 'GET')
        accepts_parameters = config.get('accepts_parameters', [])
        paginates = config.get('paginates', False)

        def __init__(self, api, *args, **kwargs):
            self.api = api
            self.as_generator = kwargs.pop('as_generator', False)
            self.parameters = {}
            self._build_parameters(args, kwargs)
            self._build_path()

        def _build_parameters(self, args, kwargs):
            for index, value in enumerate(args):
                if value is None:
                    continue

                try:
                    self.parameters[self.accepts_parameters[index]] = encode_string(value)
                except IndexError:
                    raise ScupPythonError('Too many arguments supplied')

            for key, value in six.iteritems(kwargs):
                if value is None:
                    continue
                if key in self.parameters:
                    raise ScupPythonError('Parameter {} already supplied'.format(key))
                self.parameters[key] = encode_string(value)

        def _build_path(self):
            for variable in re_path_template.findall(self.path):
                name = variable.strip('{}')

                try:
                    value = quote(self.parameters[name])
                except KeyError:
                    raise ScupPythonError('Parameter value missing: {}'.format(name))
                del self.parameters[name]

                self.path = self.path.replace(variable, value)

        def _do_api_request(self, prepared_request):
            response = self.api.session.send(prepared_request, timeout=self.api.timeout)
            status_code = response.status_code

            try:
                content = json.loads(response.content)
            except ValueError:
                raise ScupClientError('Unable to parse response, not valid JSON.', code=status_code, error_data=response.content)

            if status_code == 200:
                if content['success']:
                    return content
                else:
                    # Accomodate for Scup API's variability on error response 
                    # message param can be either message or message_error
                    # code param can be either cod_error or error_code
                    # data can be a list or a dict
                    # This happens because api errors are not standardized :(
                    if type(content['data']) == list:
                        # As this is an error, the list will only have one object
                        data = content['data'][0]
                    else:
                        data = content['data']
                    if 'message_error' in data:
                        raise ScupError(message=data['message_error'], 
                                                        code=data['error_code'])
                    elif 'message' in data:
                        raise ScupError(message=data['message'], 
                                code=data['cod_error'])
                    else:
                        raise ScupError(message='Unexpected error occurred.', 
                                                        code=data['cod_error'])
            else:
                raise ScupError(message=content['erro'], code=status_code)

        def execute(self):
            # Generate auth params
            time, signature = get_request_signature(self.api.private_key)
            self.parameters['time'] = time
            self.parameters['signature'] = signature
            self.parameters['publickey'] = self.api.public_key

            prepared_request = self.api.session.prepare_request(
                Request(
                    method  = self.method, 
                    url     = self.api.url + self.path,
                    params  = self.parameters))

            content = self._do_api_request(prepared_request)

            return content

    def _call(api, *args, **kwargs):
        method = ScupAPIMethod(api, *args, **kwargs)
        return method.execute()

    return _call


