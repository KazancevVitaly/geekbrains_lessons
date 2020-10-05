# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

workers = open('text_3.txt', 'r', encoding='utf-8')

worker_list = []
for el in workers:
    w_list = el.split()
    worker_list.append(w_list)

worker_dict = dict(worker_list)

all_salary = 0
i = 0
for worker, salary in worker_dict.items():
    salary = float(salary)
    all_salary += salary
    i += 1
    if salary < 20000.00:
        print(f'Зарплата сотрудника {worker}, меньше 20 тыс')

middle_salary = all_salary / i
print(f'Средняя зарплата сотрудников равна {middle_salary}')
workers.close()
