from enum import Enum

class RunStatus(str, Enum):
    CREATED = "created"
    RESEARCHED = "researched"
    DRAFTED = "drafted"
    GENERATED = "generated"
    PUBLISHED = "published"
