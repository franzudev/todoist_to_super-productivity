# from todoist_api_python.api_async import TodoistAPIAsync
import argparse
import json
import os
from dataclasses import dataclass
from datetime import datetime
from random import choice
from string import ascii_uppercase
from typing import List

from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Label, Project, Task


@dataclass
class ExporterConfig:
    projects: bool
    tasks: bool
    labels: bool
    path: str


class TodoistScraper:
    api: TodoistAPI
    projects: List[Project]
    tasks: List[Task]
    config: ExporterConfig

    def __init__(self, args):
        """
        Initializes the TodoistScraper with a provided API token.

        Args:
            token (str): The API token used to authenticate with the Todoist API.
        """
        self.api = TodoistAPI(args.token)

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

    def todoist_task_to_superprod(self):
        pass

    def todoist_project_to_superprod(self):
        pass

    def todoist_label_to_superprod(self):
        pass

    def todoist_to_superprod(self):
        pass

    def export_objects(self):
        objects = self.collect_objects()

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

    print(args)
