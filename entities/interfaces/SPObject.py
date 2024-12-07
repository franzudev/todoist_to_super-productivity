from abc import ABC, abstractmethod


class SPObject(ABC):

    @classmethod
    @abstractmethod
    def from_todoist(cls, todoist_object):
        pass

    @abstractmethod
    def to_dict(self):
        pass
