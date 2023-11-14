from .repo import SqliteRepository
from .model import model


class Repo:
    def __init__(self):
        self.company_repo = SqliteRepository[model.CompanyInfo]("db.sqlite3")

    def get_contact_pages_for_company(self, name: str) -> list[str]: # ищем все полные адреса страниц контактов определенных компаний
        # companies = self.company_repo.get_all(where={"name":name}) #тут запрос в базу!
        # companies = [model.CompanyInfo(1, name, 'https://repetitors.info', '')] # пример
        companies = [model.CompanyInfo(1, name, 'https://hands.ru', 'company/about')] # пример
        if len(companies) == 0:
            return []
        company_info = companies[0]
        contact_pages = company_info.contacts.split(",")
        result_addresses = []
        for cp in contact_pages:
            result_addresses.append(company_info.address + "/" + cp)
        return result_addresses

