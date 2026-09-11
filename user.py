from dataclasses import *
import random
import databaseManager as dm
from input import *

rank = ["CTO", "SE", "JE"]

@dataclass
class user:
    UNIQUE_ID: int
    USERNAME: str
    EMAIL: str
    PASS: str
    RANK: str
    ACTIVE: bool