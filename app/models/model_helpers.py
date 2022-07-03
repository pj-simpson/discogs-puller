from sqlalchemy.orm import declarative_base

Base = declarative_base()

class JsonMixin(object):
    def resp_for_json(self):
        resp_dict = self.__dict__.copy()
        del resp_dict["_sa_instance_state"]
        return resp_dict
