try:
  import simplejson as json
except ImportError:
  import json
import requests
import six

from scup.exceptions import *
from scup.auth import get_request_signature


class ScupAPI(object):
  def __init__(self, private_key, public_key, url='http://api.scup.com/1.1', timeout=None):
    """
    Initialize ScupAPI with user's private and public keys.

    :param private_key: User's private key, obtained by contacting a Scup representative.
    :param public_key: User's public key, obtained by contacting a Scup representative.
    """

    self.session = requests.Session()
    self.private_key = private_key
    self.public_key = public_key
    self.url = url.strip('/')
    self.timeout = timeout

  def getMonitorings(self):
    """
    Get all available monitorings for account
    Endpoint: /monitorings
    """

    response = self._query(
      method = 'GET', 
      path = '/monitorings',
    )

    if not response:
      raise ScupError('Could not get monitorings.')
    
    return response

  def getSearches(self, monitoring_id):
    """
    Get all available searches for given monitoring
    Endpoint: /searches/{monitoring_id}

    :param monitoring_id: The monitoring ID.
    """

    response = self._query(
      method = 'GET', 
      path = '/searches/{}'.format(monitoring_id),
    )

    if not response:
      raise ScupError('Could not get searches for monitoring {}.'.format(monitoring_id))
    
    return response

  def getMentions(self, monitoring_id, **params):
    """
    Get all available mentions for given monitoring
    Endpoint: /mentions/{monitoring_id}

    :param monitoring_id: The monitoring ID.
    :param searches_ids: The search ID. It accepts multiple IDs separated by pipe. Example: 19478|19479.
    :param published_date: The date interval the mentions where published (YYYY-MM-DD). Example: 2014-10-22 01:00:00|2014-10-23 23:00:00.
    :param tags_ids: The tag ID. It accepts multiple IDs separated by pipe. Example: <tag1>|<tag2>|<tag3>|...|<tagn>.
    :param sentiment: The sentiment of the mention (positive, negative, mixed or neutral). Example: positive.
    :param user_id: The user ID. Example: 225598.
    :param social_network: The Social Network of the user ('linkedin', 'googleplus','foursquare', 'twitter', 'blog', 'flickr', 'youtube', 'yahooanswers', 'facebook', 'slideshare', 'vimeo', 'instagram'). Required if "social_network_user_id" is set. Example: facebook.
    :param social_network_user_id: The Social Social Network user ID. Required if "social_network" is set. Example: john.lemmnh59.
    :param document: The user's document (Brazilian CPF, for example). Example: 48199876609.
    :param email: The user's e-mail. Example: client@hotmail.com.
    :param mention_id: The mention ID. Example: 33455.
    :param ipp: Number of items per page. Limited to 100. Example: 100.
    :param page: The page number to filter the results. Example: 5.
    """

    response = self._query(
      method = 'GET', 
      path = '/mentions/{}'.format(monitoring_id),
      params = params
    )

    if not response:
      raise ScupError('Could not get mentiojns for monitoring {}.'.format(monitoring_id))
    
    return response

  def _query(self, method, path, params=None, retry=0, page=False):
    if not path.startswith('/'):
        if six.PY2:
            path = '/' + six.text_type(path.decode('utf-8'))
        else:
            path = '/' + path

    params = {param: params[param] for param in params 
      if params[param] is not None} if params is not None else None

    try:
      return self._request(method, path, params)
    except ScupPythonError:
      if retry:
        return self._query(method, path, params, retry - 1)
      else:
        raise

  def _request(self, method, path, params=None):
    if params:
      for key in params:
        value = params[key]
        if isinstance(value, (list, dict, set)):
          params[key] = json.dumps(value)
    else:
      params = {}

    # Generate auth params
    time, signature = get_request_signature(self.private_key)

    # Add auth params to request
    params['time'] = time
    params['signature'] = signature
    params['publickey'] = self.public_key

    try:
      if method == 'GET':
        response = self.session.request(
          method          = method,
          url             = self.url + path,
          params          = params,
          allow_redirects = True,
          timeout         = self.timeout
        )
      # TODO: implement other methods
      if method in ['POST', 'PUT', 'DELETE']:
        raise Exception('TODO: implement other methods')

    except requests.RequestException as e:
      raise HTTPError(e)

    result = self._parse(response.content)

    return result

  def _parse(self, data):
    if type(data) == type(bytes()):
      data = data.decode('utf-8')
    data = json.loads(data)

    return data

