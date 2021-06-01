"""
Пользователь вводит данные
    о количестве предприятий,
    их наименования
    и прибыль за 4 квартала для каждого предприятия.

Программа должна определить
    среднюю прибыль (за год для всех предприятий)
    и отдельно вывести наименования предприятий,
        чья прибыль выше среднего
        и ниже среднего.
"""
from collections import namedtuple


def task_1(count_of_companies: int):
    Company = namedtuple('Company', 'name, quarters_income, avg_income')
    companies = []
    names = []

    # запросим названия компаний
    print('Введите названия компаний')
    for num in range(count_of_companies):
        names.append(input(f'{num + 1}: '))

    # запросим доход за 4 квартала для каждой компании
    for name in names:
        income = []
        for quarter in range(1, 5):
            income.append(int(input(f'Введите прибыль компании {name} за {quarter}-й квартал: ')))
        companies.append(Company(name=name, quarters_income=income, avg_income=sum(income)))

    # считаем средний годовой доход всех компаний
    avg_income_of_all = sum(company.avg_income for company in companies) // len(companies)

    # отсортируем компании с доходом выше/ниже среднего
    companies_above_avg = []
    companies_below_avg = []
    for company in companies:
        if company.avg_income > avg_income_of_all:
            companies_above_avg.append(company)
        elif company.avg_income < avg_income_of_all:
            companies_below_avg.append(company)

    # вернем кортеж со средним доходом и словари с доходами компаний
    return avg_income_of_all, companies_above_avg, companies_below_avg


if __name__ == '__main__':
    user = int(input('Введите количество компаний\n>>> '))
    avg, comp_above, comp_below = task_1(user)
    names_comp_above = [comp.name for comp in comp_above]
    names_comp_below = [comp.name for comp in comp_below]

    print(f'Средний доход компаний за год - {avg}\n'
          f'Компании с доходом выше среднего - {names_comp_above}\n'
          f'Компании с доходом ниже среднего - {names_comp_below}\n')
