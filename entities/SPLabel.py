from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional

from todoist_api_python.models import Label

from entities.common.AdvancedCfg import AdvancedCfg
from entities.common.Theme import Theme
from entities.common.WorklogExportSettings import WorklogExportSettings
from entities.interfaces.SPObject import SPObject


@dataclass
class SPLabel(SPObject):
    id: str
    title: str
    icon: Optional[str]
    color: Optional[str]
    created: int
    advancedCfg: AdvancedCfg
    theme: Theme
    workStart: Dict[str, int]
    workEnd: Dict[str, int]
    breakTime: Dict[str, int]
    breakNr: Dict[str, int]
    taskIds: List[str]

    @classmethod
    def from_todoist(cls, label: Label):
        return cls(
            id=label.id,
            title=label.name,
            icon=None,
            color=label.color,
            created=int(datetime.timestamp(datetime.now())),
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
            taskIds=[])

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "icon": self.icon,
            "color": self.color,
            "created": self.created,
            "advancedCfg": self.advancedCfg.to_dict(),
            "theme": self.theme.to_dict(),
            "workStart": self.workStart,
            "workEnd": self.workEnd,
            "breakTime": self.breakTime,
            "breakNr": self.breakNr,
            "taskIds": self.taskIds
        }
