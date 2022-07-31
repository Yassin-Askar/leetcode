"""
    ! Script to Generate folder and file for the solution.

    """

import os
import pathlib
import re
import sys


class Color:
    GREEN = '\x1b[7;30;42m'
    RED = '\x1b[7;30;41m'
    WHITE = '\x1b[7;33;40m'
    YELLOW = '\x1b[1;37;43m'

    END = '\x1b[0m'


def get_valid_filename(s):
    s = str(s).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', s)


def create_folder(problem_title=""):
    while not problem_title:
        print(
            f" \n\t{Color.YELLOW}[-] Please provide folder tile. {Color.END}\n")
        problem_title = input(f"{Color.WHITE}Folder Name:{Color.END}  ")

    path = pathlib.Path(__file__).parent.resolve()  # ? get path
    problem_title = get_valid_filename(problem_title)
    folder_path = os.path.join(path, problem_title)
    try:
        os.mkdir(folder_path)
        print(
            f" \n\t{Color.GREEN}[√] Folder Created: {folder_path}{Color.END}\n")
        return folder_path
    except FileExistsError:
        print(
            f" \n\t{Color.RED}[x] Folder already exists: {folder_path}{Color.END}\n")

        return folder_path


def create_file(folder):
    exist = pathlib.Path(folder).exists()
    if exist:
        choice = input(
            f"{Color.WHITE}[-] The file already exist are you sure you wanna overwrite the file :(Enter 'y' to continue){Color.END}  ")
        if choice.lower() != 'y':
            sys.exit()
    print(f"{Color.WHITE}Code:{Color.END}  ")
    file_data = sys.stdin.read()
    file_data = file_data.replace('List', 'list')
    try:
        with open(f'{folder}/s1.py', 'w') as f:
            f.write(file_data)
        if exist:
            print(
                f" \n\t{Color.GREEN}[√] File overwritten: {folder}\\s1.py{Color.END}\n")
        else:
            print(
                f" \n\t{Color.GREEN}[√] File created: {folder}\\s1.py{Color.END}\n")
    except FileNotFoundError:
        print(f"The '{folder[-1]}' directory does not exist")


def main():
    problem_title = input(f"{Color.WHITE}[-] Folder Name:{Color.END}  ")
    folder = create_folder(problem_title)
    create_file(folder=folder)


if __name__ == "__main__":
    main()
