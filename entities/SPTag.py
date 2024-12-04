from dataclasses import dataclass
from typing import Dict, List, Optional

from entities.common.AdvancedCfg import AdvancedCfg
from entities.common.Theme import Theme


@dataclass
class SPTag:
    id: str
    title: str
    icon: str
    color: Optional[str]
    created: int
    advancedCfg: AdvancedCfg
    theme: Theme
    workStart: Dict[str, int]
    workEnd: Dict[str, int]
    breakTime: Dict[str, int]
    breakNr: Dict[str, int]
    taskIds: List[str]
