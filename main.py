import argparse
import json
import os
import platform
from dataclasses import dataclass
from typing import List

from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Label, Project, Task

from entities.SPProject import SPProject
from entities.SPTag import SPTag
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
        print(config)
        self.api = TodoistAPI(config.token)
        self.config = config

    @staticmethod
    def _obj_to_dict(list_objs: List[Project | Task | Label]):
        """
        Converts a list of Todoist objects (Project, Task, or Label) to a list of dictionaries.

        Args:
            list_objs (List[Project | Task | Label]): A list of Todoist objects to convert.

        Returns:
            List[dict]: A list of dictionaries, where each dictionary represents a Todoist object.
        """
        dict_objs = []

        for obj in list_objs:
            try:
                if hasattr(obj.__class__, "to_dict") and callable(
                        getattr(obj.__class__, "to_dict")):
                    dict_objs.append(obj.to_dict())
                    continue
                dict_objs.append(obj.__dict__)
            except Exception as error:
                f = open("error.txt", "a")
                dict_error = {
                    "type": obj.__class__.__name__,
                    "id": obj.id,
                    "name": obj.name if hasattr(obj, "name") else obj.content,
                    "error": str(error)
                }
                f.write(json.dumps(dict_error, indent=4) + "\n")

        return dict_objs

    def _get_tasks(self):
        """
        Converts a list of Tasks obtained from the Todoist API to a list of dictionaries.

        Returns:
            List[dict]: A list of dictionaries, where each dictionary represents a Task.
        """
        return self._obj_to_dict(self.api.get_tasks())

    def _get_projects(self):
        """
        Converts a list of Projects obtained from the Todoist API to a list of dictionaries.

        Returns:
            List[dict]: A list of dictionaries, where each dictionary represents a Project.
        """
        return self._obj_to_dict(self.api.get_projects())

    def _get_labels(self):
        """
        Converts a list of Labels obtained from the Todoist API to a list of dictionaries.

        Returns:
            List[dict]: A list of dictionaries, where each dictionary represents a Label.
        """
        return self._obj_to_dict(self.api.get_labels())

    def collect_objects(self):
        """
        Collects objects from the Todoist API according to the `ExporterConfig`
        attributes `tasks`, `projects` and `labels`.

        Returns:
            dict: A dictionary with keys "tasks", "projects" and "labels", each
            containing a list of dictionaries representing the respective objects.
        """
        return {
            "tasks": self._get_tasks() if self.config.tasks else [],
            "projects": self._get_projects() if self.config.projects else [],
            "labels": self._get_labels() if self.config.labels else []
        }

    def todoist_task_to_superprod(self) -> List[SPTask]:
        tasks: List[Task] = self.api.get_tasks()
        sptasks = []
        for task in tasks:
            sptasks.append(SPTask.from_todoist(task))
        return sptasks

    def todoist_project_to_superprod(self) -> List[SPProject]:
        projects: List[Project] = self.api.get_projects()
        spprojects = []
        for project in projects:
            spprojects.append(SPProject.from_todoist(project))
        return spprojects

    def todoist_label_to_superprod(self) -> List[SPTag]:
        return []

    def todoist_to_superprod(self):
        pass

    def export_objects(self):
        # objects = self.collect_objects()
        objects = {}

        if self.config.projects:
            objects["projects"] = self.todoist_project_to_superprod()

        if self.config.tasks:
            objects["tasks"] = self.todoist_task_to_superprod()

        if self.config.labels:
            objects["labels"] = self.todoist_label_to_superprod()

        if self.config.path is not None and os.path.exists(self.config.path):
            with open(self.config.path, "w") as f:
                f.write(json.dumps(objects, indent=4))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--token',
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
    path = "~/Library/Application Support/superProductivity/"

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
