from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Protocol


class Model(Protocol):  # pylint: disable=too-few-public-methods
    pk: int


T = TypeVar('T', bound=Model)


class AbstractRepository(ABC, Generic[T]):

    @abstractmethod
    def get_all(self, where: dict[str, any] = None) -> list[T]:
        """ Получить все записи по некоторому условию """


