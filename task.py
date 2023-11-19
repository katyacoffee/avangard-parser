import json
import requests
from requests import Session as sess


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru",
    #"Host": "httpbin.org",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "X-Amzn-Trace-Id": "Root=1-6556617a-54ba8625589b120c154b7431"
    }

def get_page(address: str) -> str:
    with sess() as s:
        #header_resp = s.get('https://httpbin.org/headers', timeout=2)
        #headers = json.loads(header_resp.text)
        resp = s.get(address, timeout=2, headers=headers)
        return resp.text


def download_dataset():
    URL = "https://trudvsem.ru/csv/company.csv"
    response = requests.get(URL, headers=headers)
    open("company.csv", "wb").write(response.content)


def get_ogrn_list() -> list[str]:
    file = 'company.csv'
    try:
        with open(file):
            pass
    except FileNotFoundError:
        print("FILE company.csv not found, downloading...")
        download_dataset()

    ogrns = []
    i = 0
    orgn_index = 0

    debug_limit = 20 #TODO: убрать
    try:
        with open(file) as f:
            for line in f:
                if i == 0:
                    i = 1
                    print(line)
                    headers = line.split('|')
                    for index in range(0, len(headers)):
                        if headers[index].lower() == 'ogrn':
                            orgn_index = index
                            break
                    continue
                ogrn = line.split('|')[orgn_index]
                ogrns.append(ogrn)
                i += 1
                if i == debug_limit:
                    break
    except FileNotFoundError:
        ogrns = [] #'1037700038254'
    return ogrns


def get_info(page: str) -> str:
    page_text = get_page(page)
    if page_text == "":
        return ''
    info = json.loads(page_text)
    data = info.get('data', {})
    res = data.get('hiTechComplex', 'False')
    return str(res)
