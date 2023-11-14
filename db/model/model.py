from dataclasses import dataclass
from typing import TypeVar, Protocol


class Model(Protocol):  # pylint: disable=too-few-public-methods
    pk: int


T = TypeVar('T', bound=Model)


@dataclass
class CompanyInfo(Model):
    """
    Информация о компании с номером телефона
    """
    pk: int = 0
    name: str = "no_name" # название компании
    address: str = "no_address" # веб-адрес компании
    contacts: str = "" # пути к страницам контактов через запятую