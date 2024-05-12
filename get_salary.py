import pathlib


def total_salary(path):
    try:
        with open(path, 'r', encoding="utf-8") as file: # Відкриваємо файл з правильним кодуванням
            salaries = file.readlines() # Зберігаємо кожен рядок у списку
            total = 0 # загальна сума
            count = 0 # кількість розробників 
            for salary in salaries:
                temp_list = salary.split(",") # розділяємо рядок на розробника і його зарплату
                number = temp_list[1].strip() # Зберігаємо зарплату
                total += int(number)
                count += 1
            return [total, total/count] # повертаємо список з загальною та середньою зарплатою
    except FileNotFoundError:
        return ['File not found']
    except IndexError:
        return ['File does not support valid syntax. Make sure to split all the lines with a comma']


current_dir = pathlib.Path(__file__).parent # Знаходимо шлях до поточної папки
result = total_salary(current_dir / "total_salary.txt")
if len(result) > 1: # Якщо в списку декілька елементів, то все вийшло
    print(f"Загальна сума заробітної плати: {result[0]}, Середня заробітна плата: {result[1]}")
else: # Якщо 1 елемент, то скоріш за все помилка, виводимо її
    print(result[0])
