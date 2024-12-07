from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional

from todoist_api_python.models import Task

from entities.interfaces.Object import SPObject


@dataclass
class SPTask(SPObject):
    id: str = ''
    projectId: Optional[str] = None
    subTaskIds: List[str] = field(default_factory=list)
    timeSpentOnDay: Dict[str, float] = field(default_factory=dict)
    timeSpent: int = 0
    timeEstimate: int = 0
    isDone: bool = False
    doneOn: Optional[int] = None
    title: str = ''
    notes: str = ''
    tagIds: List[str] = field(default_factory=list)
    parentId: Optional[str] = None
    reminderId: Optional[str] = None
    created: int = field(default=int(datetime.timestamp(datetime.now())))
    repeatCfgId: Optional[str] = None
    plannedAt: Optional[datetime] = None
    _showSubTasksMode: int = 2
    attachments: List[str] = field(default_factory=list)
    issueId: Optional[str] = None
    issueProviderId: Optional[str] = None
    issuePoints: Optional[int] = None
    issueType: Optional[str] = None
    issueAttachmentNr: Optional[int] = None
    issueLastUpdated: Optional[datetime] = None
    issueWasUpdated: Optional[bool] = None
    issueTimeTracked: Optional[float] = None

    @classmethod
    def from_todoist(cls, task: Task):
        dt_object = datetime.strptime(task.created_at, '%Y-%m-%dT%H:%M:%S.%fZ')
        created = int(dt_object.timestamp())

        return cls(id=task.id,
                   projectId=task.project_id,
                   isDone=task.is_completed,
                   title=task.content,
                   notes=task.description,
                   tagIds=task.labels,
                   parentId=task.parent_id,
                   created=created)

    def to_dict(self):
        return self.__dict__
