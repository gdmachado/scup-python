try:
	import simplejson as json
except ImportError:
	import json
import requests

from scup.exceptions import *
from scup.auth import get_request_signature


class ScupAPI(object):
	def __init__(self, private_key, public_key, url='http://api.scup.com/1.1', timeout=None):
		"""
		Initialize ScupAPI with user's private and public keys.

		:param private_key: User's private key, obtained by contacting a Scup representative.
		:param public_key: User's public key, obtained by contacting a Scup representative.
		"""

		self.private_key = private_key
		self.public_key = public_key
		self.url = url.strip('/')
		self.timeout = timeout

	def _request(self, method, path, params):
		if params:
			for key in params:
				value = params[key]
				if isinstance(value, (list, dict, set)):
					params[key] = json.dumps(value)

		# Generate auth params
		time, signature = get_request_signature(self.private_key)

		# Add auth params to request
		params['time'] = time
		params['signature'] = signature

		try:
			if method == 'GET':
				response = self.session.request(
					method 					= method,
					url 						= self.url + path,
					params 					= params,
					allow_redirects = True,
					timeout 				= self.timeout,
					headers 				= self.headers
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

