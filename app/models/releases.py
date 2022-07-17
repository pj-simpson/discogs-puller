from sqlalchemy import Column, Integer, String, ForeignKey

from .model_helpers import JsonMixin, Base


class Releases(Base, JsonMixin):
    __tablename__ = "releases"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    link = Column(String)
    external_id = Column(Integer)
    artist_external_id = Column(Integer, ForeignKey("artist.external_id"))
    artist_id = Column(Integer, ForeignKey("artist.id"))


class ReleaseImages(Base, JsonMixin):
    __tablename__ = "release_images"

    id = Column(Integer, primary_key=True)
    width = Column(String)
    height = Column(String)
    uri = Column(String)
    release_id = Column(Integer, ForeignKey("release.id"))
    artist_external_id = Column(Integer, ForeignKey("artist.external_id"))
    artist_id = Column(Integer, ForeignKey("artist.id"))
