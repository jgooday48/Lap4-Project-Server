from enum import Enum, auto

class Specialisation(Enum):
    HISTORICAL=auto()
    OUTDOOR_ACTIVITIES=auto()
    CULTURAL=auto()
    DINING=auto()
    MUSIC=auto()
    FEMALE_FRIENDLY=auto()
    DISABILITY_FRIENDLY=auto()

class Status(Enum):
    PLANNED=auto()
    ONGOING=auto()
    COMPLETED=auto()
