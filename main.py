import argparse
import json
import os
import platform
from dataclasses import dataclass
from typing import List, Type

from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Label, Project, Task

from entities.interfaces.SPObject import SPObject
from entities.SPLabel import SPLabel
from entities.SPProject import SPProject
from entities.SPTask import SPTask


@dataclass
class ExporterConfig:
    projects: bool
    labels: bool
    path: str
    token: str
    tasks: bool = True


class TodoistScraper:
    api: TodoistAPI
    projects: List[Project]
    tasks: List[Task]
    config: ExporterConfig

    def __init__(self, config: ExporterConfig):
        """
        Initializes the TodoistScraper with a provided API token.

        Args:
            token (str): The API token used to authenticate with the Todoist API.
        """
        self.api = TodoistAPI(config.token)
        self.config = config

    def get_todoist_objects(self, cls: Type[SPObject]):
        obj = cls.__name__.replace("SP", "")
        if obj == "Project":
            return self.api.get_projects()
        elif obj == "Task":
            return self.api.get_tasks()
        elif obj == "Label":
            return self.api.get_labels()
        else:
            raise Exception("Unknown object type")

    def todoist_to_superprod(self, cls: Type[SPObject]) -> List[SPObject]:
        objs: List[Project | Task | Label] = self.get_todoist_objects(cls)
        return [cls.from_todoist(obj).to_dict() for obj in objs]

    def export_objects(self):
        # objects = self.collect_objects()
        objects = {}

        if self.config.projects:
            objects["projects"] = self.todoist_to_superprod(SPProject)

        if self.config.tasks:
            objects["tasks"] = self.todoist_to_superprod(SPTask)

        if self.config.labels:
            objects["labels"] = self.todoist_to_superprod(SPLabel)

        if self.config.path is not None and os.path.exists(self.config.path):
            with open(self.config.path, "w") as f:
                f.write(json.dumps(objects, indent=4))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--token',
                        required=True,
                        type=str,
                        help='Todoist API token for querying tasks')
    parser.add_argument(
        '--path',
        type=str,
        help=
        'Path to the directory where you want to save the file, current directory by default'
    )
    parser.add_argument(
        '--labels',
        '-l',
        default=False,
        action='store_true',
        help='Whether to add subtasks as tasks or not add them at all')
    parser.add_argument(
        '--projects',
        '-p',
        default=False,
        action='store_true',
        help='Whether to add subtasks as tasks or not add them at all')

    args = parser.parse_args()
    path = r"~/Library/Application Support/superProductivity/"

    if platform.system() == 'Windows':
        path = "C:/Users/" + os.getlogin(
        ) + "/AppData/Roaming/superProductivity/"
    elif platform.system() == 'Linux':
        path = "~/.config/superProductivity/"

    exporter_config = ExporterConfig(projects=args.projects,
                                     labels=args.labels,
                                     path=path,
                                     token=args.token)
    todoist_scraper = TodoistScraper(exporter_config)
    todoist_scraper.export_objects()
