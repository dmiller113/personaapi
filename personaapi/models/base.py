from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer

Base = declarative_base()


class Model(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)

    _printed_keys = []

    _printed_relations = []

    def get_return_response(self):
        return_value = {}
        for key in sorted(self._printed_keys):
            return_value[key] = getattr(self, key)
        for key in self._printed_relations:
            try:
                return_value[key] = []
                for item in iter(getattr(self, key)):
                    return_value[key].append(
                        item.get_return_response())
            except TypeError:
                return_value[key] = getattr(self, key).get_return_response()
        return return_value
