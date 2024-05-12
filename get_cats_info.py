import pathlib


def get_cats_info(path):
    try:
        with open(path, 'r', encoding="utf-8") as file: # відкриваємо файл з правильним кодуванням
            cats = file.readlines() # Зберігаємо кожен рядок у список cats
            list_of_cats = [] # Створюємо список з інформацією про котів, який будемо повертати
            for cat in cats: # Для кожного рядка обробляємо інформацію
                info_list = cat.split(",") # Розділяємо рядок
                ID = info_list[0].strip()
                name = info_list[1].strip()
                age = info_list[2].strip()
                list_of_cats.append({'id': ID, 'name': name, 'age': age}) # Додаємо до списку словники
            return list_of_cats

    except FileNotFoundError:
        return ['Файл не знайдено']
    except IndexError:
        return ['Файл очікує три аргументи на кожен рядок. Переконайтеся, що усі рядки розділені комами']


current_dir = pathlib.Path(__file__).parent # Знаходимо шлях до поточної папки
result = get_cats_info(current_dir / "cats_info.txt")
if len(result) > 1: # Якщо все вдалося і повернуло декілька словників
    print(result)
else: # Якщо тільки один елемент у списку - це скоріш за все помилка. Виводимо її.
    print(result[0])
