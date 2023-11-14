from task import init_repo, get_numbers


def execute() -> list[str]:
    print('Enter company name:')
    company_name = input()
    repo = init_repo()
    all_contact_pages = repo.get_contact_pages_for_company(company_name)
    if len(all_contact_pages) == 0:
        print('Error: company ' + company_name + ' not found')
        return []
    numbers = []
    for page in all_contact_pages:
        numbers.extend(get_numbers(page))
    print(numbers)
    return numbers


if __name__ == '__main__':
    execute()
