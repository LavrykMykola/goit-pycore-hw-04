import pathlib


def total_salary(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            salaries = file.readlines()
            total = 0
            count = 0
            for salary in salaries:
                temp_list = salary.split(",")
                number = temp_list[1].strip()
                total += int(number)
                count += 1
            return [total, total/count]
    except FileNotFoundError:
        return ['File not found']
    except IndexError:
        return ['File does not support valid syntax. Make sure to split all the lines with a comma']


current_dir = pathlib.Path(__file__).parent
result = total_salary(current_dir / "total_salary.txt")
if len(result) > 1:
    print(f"Загальна сума заробітної плати: {result[0]}, Середня заробітна плата: {result[1]}")
else:
    print(result[0])
