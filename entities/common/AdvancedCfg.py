from dataclasses import dataclass

from entities.common.WorklogExportSettings import WorklogExportSettings


@dataclass
class AdvancedCfg:
    worklogExportSettings: WorklogExportSettings
