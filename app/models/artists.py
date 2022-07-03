from sqlalchemy import Column, Integer, String, ForeignKey

from .model_helpers import JsonMixin, Base

class Artist(Base, JsonMixin):
    __tablename__ = "artist"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    biog = Column(String)
    releases_uri = Column(String)
    external_id = Column(Integer)

    __mapper_args__ = {"eager_defaults": True}