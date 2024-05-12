import pathlib


def get_cats_info(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            cats = file.readlines()
            list_of_cats = []
            for cat in cats:
                info_list = cat.split(",")
                ID = info_list[0].strip()
                name = info_list[1].strip()
                age = info_list[2].strip()
                list_of_cats.append({'id': ID, 'name': name, 'age': age})
            return list_of_cats

    except FileNotFoundError:
        return ['Файл не знайдено']
    except IndexError:
        return ['Файл очікує три аргументи на кожен рядок. Переконайтеся, що усі рядки розділені комами']


current_dir = pathlib.Path(__file__).parent
result = get_cats_info(current_dir / "cats_info.txt")
if len(result) > 1:
    print(result)
else:
    print(result[0])
