from pydantic import BaseModel
from enum import Enum


# Enums
class AnimalGender(str, Enum):
    male = "male"
    female = "female"


class Animal(BaseModel):
    name: str
    species: str
    sex: AnimalGender
    birthday: str
    weight: float
