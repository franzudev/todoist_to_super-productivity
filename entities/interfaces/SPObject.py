from abc import ABC, abstractmethod


class SPObject(ABC):

    @abstractmethod
    def from_todoist(self, todoist_object):
        pass

    @abstractmethod
    def to_dict(self):
        pass
