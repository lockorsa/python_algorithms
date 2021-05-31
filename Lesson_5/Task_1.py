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


def task_1(count_of_companies):
    Company = namedtuple('Company', 'quarters, avg_profit')
    companies = {}
    for _ in range(count_of_companies):
        name = input('Введите название компании\n>>> ')
        quarters_ = []
        for quarter in range(1, 5):
            quarters_.append(int(input(f'Введите прибыль компании {name} за {quarter} квартал: ')))
        companies[name] = Company(quarters=quarters_, avg_profit=sum(quarters_))

    avg_profit_of_all = sum(value.avg_profit for value in companies.values()) // len(companies)
    print(f'Средняя прибыль всех компаний за 4 квартала: {avg_profit_of_all}')

    print('Следующие компании получили больше среднего:')
    for name, values in companies.items():
        if values.avg_profit > avg_profit_of_all:
            print(f'{name},  прибыль {values.avg_profit}')

    print('Следующие компании получили меньше среднего:')
    for name, values in companies.items():
        if values.avg_profit < avg_profit_of_all:
            print(f'{name},  прибыль {values.avg_profit}')


if __name__ == '__main__':
    user = int(input('Введите количество компаний\n>>> '))
    task_1(user)
