import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama для підтримки кольорів у консолі
init(autoreset=True)


def show_dir_content(directory_path, indent=0):
    directory = Path(directory_path)
    if not directory.exists() or not directory.is_dir():
        print(f"{Fore.RED}Директорія '{directory_path}' не існує або не є директорією.")
        return

    # Відступи для кращого візуального представлення
    indent_str = "    " * indent

    # Виводимо ім'я поточної директорії
    print(f"{Style.BRIGHT}{Fore.BLUE}{indent_str}{directory.name}/")

    # Обробляємо файли у директорії
    for file in directory.iterdir():
        if file.is_dir():
            # Якщо це директорія, викликаємо функцію рекурсивно
            show_dir_content(file, indent + 1)
        else:
            # Якщо це файл, виводимо його ім'я
            print(f"{Style.BRIGHT}{Fore.GREEN}{indent_str}    {file.name}")


def main():
    # Перевіряємо, чи вказаний шлях до директорії як аргумент командного рядка
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Не вірно вказаний синтакс. Правильний синтакс: python directory.py <шлях_до_директорії>")
        sys.exit(1)

    # Отримуємо шлях до директорії з аргументу командного рядка
    directory_path = sys.argv[1]

    # Візуалізуємо структуру директорії
    show_dir_content(directory_path)


if __name__ == "__main__":
    main()
