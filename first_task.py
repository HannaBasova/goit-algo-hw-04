'''

function that calculates the average and total salary of employees
:input: path(str) - path to text file
:output: Tuple (total salary, average salary)
'''


def total_salary(path):
    try:

        with open(path, 'r', encoding='utf-8') as file:
            lines = [el.strip() for el in file.readlines()]
            list_of_salary = []
            for line in lines:
                parts = line.split(',')
                list_of_salary.append(int(parts[1]))
        total = sum(list_of_salary)
        average = round(total / len(list_of_salary))

        return total, average

    except FileNotFoundError:
        print('Incorrect path')
        return 0,0


total, average = total_salary("/Users/hanna/Desktop/PROJECTS/modul_3_theory/test.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
print(total_salary("/Users/hanna/Desktop/PROJECTS/modul_3_theory/test.txt"))

