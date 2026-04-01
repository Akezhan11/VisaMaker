from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    name: str
    surname: str
    surname_birth: str
    date_of_birth: str
    place: str
    country: str
    nationality: str
    nationality_birth: str
    gender: str
    family_side: str
    email: str
    phone_number: str
    phone_code: str
    nationality_other: Optional[str] = None


@dataclass
class UserKid:
    surname: str
    name: str
    address: Optional[str] = None
    phone_number: str = ""
    email: str = ""
    citizenship: str = ""