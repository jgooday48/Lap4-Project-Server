
from enum import Enum, auto

class UserType(Enum): 
    TOURIST = 'TOURIST'
    GUIDE = 'GUIDE'
    ADMIN = 'ADMIN'


class Filters(Enum):
    HISTORICAL = 'Historical'
    OUTDOOR_ACTIVITIES = 'Outdoor activities'
    CULTURAL = 'Cultural'
    DINING = 'Dining'
    MUSIC = 'Music'
    FEMALE_FRIENDLY = 'Female friendly'
    DISABILITY_FRIENDLY = 'Disability friendly'
    ART = 'Art'
    SPORTS = 'Sports'
    EDUCATIONAL = 'Educational'
    ENTERTAINMENT = 'Entertainment'
    NATURE = 'Nature'
    SHOPPING = 'Shopping'
    TECHNOLOGY = 'Technology'
    SCIENCE = 'Science'
    FITNESS = 'Fitness'
    FAMILY_FRIENDLY = 'Family friendly'
    ADVENTURE = 'Adventure'
    WORKSHOPS = 'Workshops'
    HOLIDAY_EVENTS = 'Holiday events'
    LITERATURE = 'Literature'
    GAMING = 'Gaming'
    PHOTOGRAPHY = 'Photography'
    WELLNESS = 'Wellness'


class Status(Enum):
    PLANNED='Planned'
    ONGOING='Ongoing'
    COMPLETED='Completed'
    

