from pydantic import BaseModel, validator
from src.enums.user_enums import Genders, Statuses, UserErrors


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Statuses

    @validator('email')
    def check_that_dog_presented_in_email_address(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)


data_of_validation = {
         "id": 5913706,
         "name": "Kalyani Nayar I",
         "email": "i_nayar_kalyani@howe.test",
         "gender": "female",
         "status": "active"
      }

"""
possibility use Enums in validation -> "Genders", "Statuses"
"""
