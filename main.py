from task import *


def execute() -> list[str]:
    # TODO: open json file with {'orgn': true/false}
    knownOgrns = {} # TODO: write json here
    newOgrns = {}
    res = []
    ogrn_list = get_ogrn_list()
    print(ogrn_list)
    for ogrn in ogrn_list:
        if ogrn in knownOgrns.keys():
            if knownOgrns[ogrn]:
                res.append(ogrn)
            continue
        hi_tech_complex = get_info('https://trudvsem.ru/iblocks/prr_public_company_profile?companyId=' + ogrn)
        # print(hiTechComplex)
        newOgrns[ogrn] = hi_tech_complex
        if hi_tech_complex == 'True':
            res.append(ogrn)
    knownOgrns.update(newOgrns)
    # TODO: open log.txt <- ДОписать сюда дату, время и длину newOgrns
    # TODO: write in json file with {'orgn': true/false}
    print(res)
    # TODO: rewrite res in hiTexComplex.txt file
    return res


if __name__ == '__main__':
    execute()
