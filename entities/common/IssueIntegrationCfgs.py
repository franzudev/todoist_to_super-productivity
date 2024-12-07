from dataclasses import dataclass

from entities.common.IntegrationConfig import IntegrationConfig


@dataclass
class IssueIntegrationCfgs:
    JIRA: IntegrationConfig
    GITHUB: IntegrationConfig
    GITLAB: IntegrationConfig
    CALDAV: IntegrationConfig
    OPEN_PROJECT: IntegrationConfig
    GITEA: IntegrationConfig
    REDMINE: IntegrationConfig

    def to_dict(self):
        return {
            "JIRA": self.JIRA.to_dict(),
            "GITHUB": self.GITHUB.to_dict(),
            "GITLAB": self.GITLAB.to_dict(),
            "CALDAV": self.CALDAV.to_dict(),
            "OPEN_PROJECT": self.OPEN_PROJECT.to_dict(),
            "GITEA": self.GITEA.to_dict(),
            "REDMINE": self.REDMINE.to_dict()
        }
