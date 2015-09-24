import hashlib
import time

def get_request_signature(private_key):
    current_time = int(time.time())

    message = '{}{}'.format(current_time, private_key)

    digest = hashlib.md5(message).hexdigest()

    return current_time, digest
