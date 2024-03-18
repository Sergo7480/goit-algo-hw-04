import os

from pathlib import Path
from colorama import Fore, Style

def display_directory_structure(directory_path, indent=''):
    try:
        directory_path = Path(directory_path)
        if not directory_path.is_dir():
            print(f"{Fore.RED}Error: {directory_path} is not a valid directory.{Style.RESET_ALL}")
            return

        print(f"{Fore.GREEN}Directory structure for: {directory_path}{Style.RESET_ALL}")

        for item in sorted(directory_path.iterdir()):
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}📁 {item.name}{Style.RESET_ALL}")
                display_directory_structure(item, indent + '    ')
            else:
                print(f"{indent}{Fore.YELLOW}📄 {item.name}{Style.RESET_ALL}")

    except FileNotFoundError:
        print(f"{Fore.RED}Error: Directory '{directory_path}' not found.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    directory_to_display = input("Enter the directory path: ")
    display_directory_structure(directory_to_display)