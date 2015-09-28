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

    """
    Get all available monitorings for account
    Endpoint: /monitorings
    """
    monitorings = bind_method(
        path='/monitorings',
        method='GET'
    )

    """
    Get all available searches for given monitoring
    Endpoint: /searches/{monitoring_id}
    :param monitoring_id: The monitoring ID.
    """
    searches = bind_method(
        path='/searches/{monitoring_id}',
        method='GET',
        accepts_parameters=['monitoring_id']
    )

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

    post = bind_method(
        path='/post/{monitoring_id}',
        method='POST',
        accepts_parameters=['monitoring_id', 'account_id', 'message', 'shared_url']
    )

