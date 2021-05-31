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


Company = namedtuple('Company', 'quarters_income, avg_income')


def task_1(count_of_companies: int):

    names = []
    companies = {}
    companies_above_avg = []
    companies_below_avg = []

    # запросим названия компаний
    print('Введите названия компаний')
    for num in range(count_of_companies):
        names.append(input(f'{num + 1}: '))

    # запросим доход за 4 квартала для каждой компании
    for name in names:
        income = []
        for quarter in range(1, 5):
            income.append(int(input(f'Введите прибыль компании {name} за {quarter}-й квартал: ')))
        companies[name] = Company(quarters_income=income, avg_income=sum(income))

    # считаем средний годовой доход всех компаний
    avg_income_of_all = sum(value.avg_income for value in companies.values()) // len(companies)

    # отсортируем компании с доходом выше/ниже среднего
    for name, values in companies.items():
        if values.avg_income > avg_income_of_all:
            companies_above_avg.append(name)
        elif values.avg_income < avg_income_of_all:
            companies_below_avg.append(name)

    # вернем кортеж со средним доходом и словари с доходами компаний
    return avg_income_of_all, companies_above_avg, companies_below_avg


if __name__ == '__main__':
    user = int(input('Введите количество компаний\n>>> '))
    result = task_1(user)
    print(f'Средний доход компаний за год - {result[0]}\n'
          f'Компании с доходом выше среднего - {result[1]}\n'
          f'Компании с доходом ниже среднего - {result[2]}\n')
