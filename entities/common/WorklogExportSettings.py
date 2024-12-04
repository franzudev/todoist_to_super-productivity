from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union


@dataclass
class WorklogExportSettings:
    cols: List[str]
    roundWorkTimeTo: Optional[int] = None
    roundStartTimeTo: Optional[int] = None
    roundEndTimeTo: Optional[int] = None
    separateTasksBy: str = " | "
    groupBy: str = "DATE"
