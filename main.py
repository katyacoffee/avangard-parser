import datetime

from task import *
import json


def execute() -> list[str]:
    print("Starting script...")
    knownOgrns = {}
    try:
        with open("known_ogrns.json", "r", encoding="utf-8") as f1:
            knownOgrns = json.load(f1)
    except Exception:
        pass

    res = []
    ogrn_list = get_ogrn_list()

    print(f"Got OGRN list ({len(ogrn_list)} items)")

    ogrns_to_check = []
    for ogrn in ogrn_list:
        if ogrn in knownOgrns.keys():
            if knownOgrns[ogrn] == 'True':
                res.append(ogrn)
            continue
        ogrns_to_check.append(ogrn)

    print(f"Filtered known OGRNs, {len(ogrns_to_check)} left to check")

    batch_size = 50
    ogrn_batch = {}
    cnt = 0
    batch_cnt = 0
    hi_tech_complexes = {}
    n = len(ogrns_to_check)

    print("Check process started...")

    for ogrn in ogrns_to_check:
        cnt += 1
        if cnt % batch_size == 0 or cnt == n-1:
            batch_cnt += 1
            new_info = {}

            for try_num in range(1, 10):
                try:
                    new_info = get_info(ogrn_batch)
                except Exception: # retry
                    print(f"WARNING: connection error, retrying... ({try_num} retry out of 10)")
                    continue
                break
            if len(new_info) == 0:
                print("ERROR: connection aborted while fetching data. "
                      "Processed data saved. "
                      "Retry to get full data.")
                break
            hi_tech_complexes.update(new_info)
            ogrn_batch = {}
            print(f"{batch_cnt} batches passed ({n // batch_size - batch_cnt + 1} left...)")
        ogrn_batch[ogrn] = 'https://trudvsem.ru/iblocks/prr_public_company_profile?companyId=' + ogrn

    for ogrn in hi_tech_complexes.keys():
        hi_tech_complex = hi_tech_complexes[ogrn]
        if hi_tech_complex == 'True':
            res.append(ogrn)
    knownOgrns.update(hi_tech_complexes)
    with open("log.txt", "a", encoding="utf-8") as f2:
        f2.write(f"{datetime.datetime.now()}: total ogrns = {len(knownOgrns)}, total hi_tex_complex = {len(res)}, last check total = {len(hi_tech_complexes)}\n")
    with open("known_ogrns.json", "w", encoding="utf-8") as f1:
        json.dump(knownOgrns, f1)
    print(res)
    f3 = open("hiTexComplex.txt", "w")
    f3.write(str(res))
    f3.close()
    return res


if __name__ == '__main__':
    execute()
