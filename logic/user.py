from dataclasses import *
import random
import logic.databaseManager as dm
from helper.input import *

rank = ["CTO", "SE", "JE"]

@dataclass
class user:
    UNIQUE_ID: int
    USERNAME: str
    EMAIL: str
    PASS: str
    RANK: str
    ACTIVE: bool