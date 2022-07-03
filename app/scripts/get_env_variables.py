import os

def get_discogs_token():
    return os.environ.get('DISCOGS_PERSONAL_ACCESS_TOKEN','')

def get_discogs_artist_id():
    return os.environ.get('DISCOGS_ARTIST_ID','')