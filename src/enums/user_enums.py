from enum import Enum
from src.base_classes.py_enum import PyEnum


class Genders(Enum):
    female = 'female'
    male = 'male'


class Statuses(PyEnum):
    INACTIVE = 'inactive'
    ACTIVE = 'active'
    DELETED = 'deleted'
    BANNED = 'banned'


class UserErrors(Enum):
    WRONG_EMAIL = 'Email doesn`t contain @'


if __name__ == '__main__':
    print(Statuses.list())
