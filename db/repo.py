import sqlite3 as sql
from .abstract_repo import AbstractRepository, T


class SqliteRepository(AbstractRepository[T]):

    def __init__(self, db: str) -> None:
        self.db_addr = db # адрес базы данных

        conn = sql.connect(self.db_addr) # коннектимся к базе
        #with conn ... - тут подключаемся к базе данных

    def get_all(self, where: dict[str, any] = None) -> list[T]:
        pass # тут реализация SQL-запроса с WHERE