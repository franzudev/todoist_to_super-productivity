from dataclasses import dataclass
from typing import Optional

from entities.enums.TransitionConfig import TransitionConfig


@dataclass
class IntegrationConfig:
    isEnabled: bool
    isAutoPoll: bool = False
    isAutoAddToBacklog: bool = False
    filterUsername: Optional[str] = None
    scope: Optional[str] = None
    token: Optional[str] = None
    host: Optional[str] = None
    repo: Optional[str] = None
    gitlabBaseUrl: Optional[str] = None
    caldavUrl: Optional[str] = None
    categoryFilter: Optional[str] = None
    resourceName: Optional[str] = None
    api_key: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    searchJqlQuery: Optional[str] = None
    autoAddBacklogJqlQuery: Optional[str] = None
    worklogDialogDefaultTime: Optional[str] = None
    transitionConfig: Optional[TransitionConfig] = None

    def to_dict(self):
        return self.__dict__
