import uuid
from typing import Any

from pydantic import BaseModel


class Human():
    id: int
    name: str
    age: int



    def __init__(self, *args, **kwargs) -> None:

        self.name = args[0]
        self.age = args[1]
        self.id = uuid.uuid4()

    def __str__(self):
        return f'Human ({self.id}, {self.name}, {self.age})'

    def __repr__(self):
        return self.__str__()
