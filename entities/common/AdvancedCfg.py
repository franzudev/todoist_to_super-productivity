from dataclasses import dataclass

from entities.common.WorklogExportSettings import WorklogExportSettings


@dataclass
class AdvancedCfg:
    worklogExportSettings: WorklogExportSettings

    def to_dict(self):
        return {"worklogExportSettings": self.worklogExportSettings.to_dict()}
