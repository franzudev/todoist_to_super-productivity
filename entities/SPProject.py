from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Union

from todoist_api_python.models import Project

from entities.common.AdvancedCfg import AdvancedCfg
from entities.common.IntegrationConfig import IntegrationConfig
from entities.common.IssueIntegrationCfgs import IssueIntegrationCfgs
from entities.common.Theme import Theme
from entities.common.WorklogExportSettings import WorklogExportSettings


@dataclass
class SPProject:
    id: str
    title: str
    isHiddenFromMenu: bool
    isArchived: bool
    isEnableBacklog: bool
    issueIntegrationCfgs: IssueIntegrationCfgs
    backlogTaskIds: List[str]
    noteIds: List[str]
    advancedCfg: AdvancedCfg
    theme: Theme
    workStart: Dict[str, Union[str, int]]
    workEnd: Dict[str, Union[str, int]]
    breakTime: Dict[str, Union[str, int]]
    breakNr: Dict[str, Union[str, int]]
    taskIds: List[str]
    icon: str = ""

    @classmethod
    def from_todoist(cls, project: Project):
        return cls(
            id=project.id,
            title=project.name,
            isHiddenFromMenu=False,
            isArchived=False,
            isEnableBacklog=False,
            taskIds=[],
            backlogTaskIds=[],
            noteIds=[],
            issueIntegrationCfgs=IssueIntegrationCfgs(
                JIRA=IntegrationConfig(isEnabled=False),
                GITHUB=IntegrationConfig(isEnabled=False),
                GITLAB=IntegrationConfig(isEnabled=False),
                CALDAV=IntegrationConfig(isEnabled=False),
                OPEN_PROJECT=IntegrationConfig(isEnabled=False),
                GITEA=IntegrationConfig(isEnabled=False),
                REDMINE=IntegrationConfig(isEnabled=False)),
            advancedCfg=AdvancedCfg(worklogExportSettings=WorklogExportSettings(
                cols=[
                    "DATE", "START", "END", "TIME_CLOCK", "TITLES_INCLUDING_SUB"
                ])),
            theme=Theme(isAutoContrast=True,
                        isDisableBackgroundGradient=False,
                        primary="#26c6da",
                        huePrimary="500",
                        accent="#ff4081",
                        hueAccent="500",
                        warn="#e11826",
                        hueWarn="500"),
            workStart={},
            workEnd={},
            breakTime={},
            breakNr={},
        )
