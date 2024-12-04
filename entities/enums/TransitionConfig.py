from enum import Enum


class TransitionConfig(Enum):
    OPEN = "DO_NOT"
    IN_PROGRESS = "ALWAYS_ASK"
    DONE = "ALWAYS_ASK"
