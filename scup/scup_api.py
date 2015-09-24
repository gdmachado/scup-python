from scup.bind import bind_method

class ScupAPI(object):
  def __init__(self, public_key, private_key, url='http://api.scup.com/1.1', timeout=None):
    """
    Initialize ScupAPI with user's public and private keys.

    :param public_key: User's public key, obtained by contacting a Scup representative.
    :param private_key: User's private key, obtained by contacting a Scup representative.
    """

    self.session = requests.Session()
    self.private_key = private_key
    self.public_key = public_key
    self.url = url.strip('/')
    self.timeout = timeout

  monitorings = bind_method(
    path='/monitorings',
    method='GET'
  )

  searches = bind_method(
    path='/searches/{monitoring_id}',
    method='GET',
    accepts_parameters=['monitoring_id']
  )

  mentions = bind_method(
    path='/mentions/{monitoring_id}',
    method='GET',
    accepts_parameters=['monitoring_id', 'searches_ids', 'published_date', 'tags_ids', 'sentiment', 'user_id', 'social_network', 'social_network_user_id', 'document', 'email', 'mention_id', 'ipp', 'page']
  )

  users = bind_method(
    path='/users/{monitoring_id}',
    method='GET',
    accepts_parameters=['monitoring_id', 'social_network_user_id', 'social_network', 'user_id', 'document', 'internal_id', 'email', 'ipp', 'page']
  )

  tags = bind_method(
    path='/tags/{monitoring_id}',
    method='GET',
    accepts_parameters=['monitoring_id', 'type']
  )

  tag_mentions = bind_method(
    path='/tagmentions/{monitoring_id}',
    method='POST',
    accepts_parameters=['monitoring_id', 'mentions_ids', 'tags_to_add', 'tags_to_remove']
  )

  classify_mentions = bind_method(
    path='/sentiment/{monitoring_id}',
    method='POST',
    accepts_parameters=['monitoring_id', 'mentions', 'sentiment']
  )

  reply_mention = bind_method(
    path='/replymention/{monitoring_id}',
    method='POST',
    accepts_parameters=['monitoring_id', 'mention', 'account', 'message']
  )

  remove_mentions = bind_method(
    path='/removementions/{monitoring_id}',
    method='POST',
    accepts_parameters=['monitoring_id', 'mentions']
  )

  mention_log = bind_method(
    path='/logmentions/{monitoring_id}',
    method='GET',
    accepts_parameters=['monitoring_id', 'mention_id', 'action', 'ipp', 'page']
  )

  mention_replies = bind_method(
    path='/mentionreplies/{monitoring_id}',
    method='GET',
    accepts_parameters=['monitoring_id', 'mention_id', 'ipp', 'page']
  )

  monitoring_statistics = bind_method(
    path='/monitoringstatistics/{monitoring_id}',
    method='GET',
    accepts_parameters=['monitoring_id', 'tag_id', 'search_id', 'published_date', 'ipp', 'page']
  )

  post = bind_method(
    path='/post/{monitoring_id}',
    method='POST',
    accepts_parameters=['monitoring_id', 'account_id', 'message', 'shared_url']
  )

  tickets = bind_method(
    path='/tickets/{monitoring_id}',
    method='GET',
    accepts_parameters=['monitoring_id', 'ticket_id', 'mention_id', 'date', 'ipp', 'page']
  )

  ticket_log = bind_method(
    path='/logtickets/{monitoring_id}',
    method='GET',
    accepts_parameters=['monitoring_id', 'ticket_id', 'ipp', 'page']
  )

