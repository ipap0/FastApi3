import uuid
from typing import Any

from pydantic import BaseModel, Field


class Human(BaseModel):
    name: str=None
    age: int=Field(ge=1, lt=123, description='возраст бывает от 1 до 123')
    id: str =None

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(**kwargs)
        # self.name = name
        # self.age = age
        if self.id is None:
            self.id = uuid.uuid4()

    def __str__(self):
        return f'Human ({self.id}, {self.name}, {self.age})'

    def __repr__(self):
        return self.__str__()

    def celebrate_birtsday(self):
        self.age+=1
        return f'ура, мне {self.age}'