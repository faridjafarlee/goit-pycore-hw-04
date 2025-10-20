import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def display_directory_structure(directory_path, indent=""):
    try:
        path = Path(directory_path)
        
        if not path.exists():
            print(f"{Fore.RED} Помилка: Шлях '{directory_path}' не існує.")
            return
        
        if not path.is_dir():
            print(f"{Fore.RED} Помилка: '{directory_path}' не є директорією.")
            return
        
        print(f"{Fore.BLUE}{indent}{path.name}/")
        
        items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name))
        
        for item in items:
            if item.is_dir():
                display_directory_structure(item, indent + "  ")
            else:
                print(f"{Fore.GREEN}{indent}  {item.name}")
    
    except PermissionError:
        print(f"{Fore.RED}{indent}  [Доступ заборонено]")
    except Exception as e:
        print(f"{Fore.RED} Виникла помилка: {e}")


def main():
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW} Використання: python task3_directory.py <шлях_до_директорії>")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    print(f"{Fore.CYAN} Структура директорії:")
    print(f"{Fore.CYAN} {'=' * 50}")
    display_directory_structure(directory_path)


if __name__ == "__main__":
    main()
