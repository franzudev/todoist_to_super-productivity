from dataclasses import dataclass
from typing import Optional


@dataclass
class Theme:
    isAutoContrast: bool
    isDisableBackgroundGradient: bool
    primary: str
    huePrimary: str
    accent: str
    hueAccent: str
    warn: str
    hueWarn: str
    backgroundImageDark: Optional[str] = None
    backgroundImageLight: Optional[str] = None
