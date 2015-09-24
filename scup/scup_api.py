try:
  import simplejson as json
except ImportError:
  import json
import requests
import six

from scup.exceptions import *
from scup.bind import bind_method
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

  getMonitorings = bind_method(
    path='/monitorings',
    method='GET'
  )

