from regex import findall
from requests import Session as sess
from db.repository import Repo


def init_repo() -> Repo:
    return Repo() # создание экземпляра репозитория, с ктр буду работать


def get_page(address: str) -> str:
    with sess() as s:
        resp = s.get(address, timeout=2)
        return resp.text


def get_numbers(page: str) -> list[str]:
    page_text = get_page(page)
    if page_text == "":
        return []
    all_nums = findall(r'(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})', page_text) # +7 111 222 33 44
    all_nums.extend(findall(r'(\d{3}).*?(\d{2}).*?(\d{2})', page_text)) # 111 22 33
    res = []
    for num in all_nums: # all_nums - это list из tuple
        if type(num) is not tuple:
            continue
        pieces_count = len(num)
        if pieces_count != 3 and pieces_count != 5:
            continue
        number = "8"
        if pieces_count == 3:
            number += "495"
        i = 0
        for piece in num:
            if pieces_count == 5 and i == 0:
                i += 1
                continue
            number += piece
            i += 1
        res.append(number)
    return res
