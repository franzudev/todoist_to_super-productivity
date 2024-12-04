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
