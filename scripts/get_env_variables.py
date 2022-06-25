import os

def get_discogs_token():
    return os.environ['DISCOGS_PERSONAL_ACCESS_TOKEN']

def get_discogs_artist_id():
    return os.environ['DISCOGS_ARTIST_ID']