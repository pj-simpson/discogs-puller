from starlite.handlers import get
from starlite import MediaType


@get(path="/health", media_type=MediaType.TEXT)
def health_check() -> str:
    return "At least this works!"
