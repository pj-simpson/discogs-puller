from starlite.handlers import get
from starlite import MediaType

@get(path="/",media_type=MediaType.TEXT)
def health_check() -> str:
    return "At least this works!"