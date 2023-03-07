from pydantic import BaseModel, EmailStr
from pydantic.networks import IPv4Address, IPv6Address
from pydantic.types import PastDate, FutureDate, List, PaymentCardNumber

from examples import computer
from src.enums.user_enums import Statuses
from src.schemas.physical import Physical


class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr


class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]


class Computer(BaseModel):
    id: int
    status: Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo


if __name__ == '__main__':
    comp = Computer.parse_obj(computer)
    print(comp)
