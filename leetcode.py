"""
    ! Script to Generate folder and file for the solution.

    """


import os
import pathlib
import re
import sys

from click import Parameter


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
        return folder_path, False
    except FileExistsError:
        print(
            f" \n\t{Color.RED}[x] Folder already exists: {folder_path}{Color.END}\n")

        return folder_path, True


def create_file(folder, exist=False):

    if exist:
        choice = input(
            f"{Color.WHITE}[-] The file already exist are you sure you wanna overwrite the file :(Enter 'y' to continue){Color.END}  ")
        if choice.lower() != 'y':
            sys.exit()
    print(f"{Color.WHITE}Code:{Color.END}  ")
    file_data = sys.stdin.readline()
    file_data = file_data.strip()
    file_data = file_data.replace('List', 'list')
    try:
        with open(f'{folder}/s1.py', 'w') as f:
            f.write("class Solution:\n")
            f.write(f"\t{file_data}\n")
            f.write("\t\tpass")
            f.write("\n" * 10)
        file_data = file_data.replace(':', ' =')
        if exist:
            print(
                f" \n\t{Color.GREEN}[√] File overwritten: {folder}\\s1.py{Color.END}\n")
        else:
            print(
                f" \n\t{Color.GREEN}[√] File created: {folder}\\s1.py{Color.END}\n")
        prepare_output(f'{folder}/s1.py', file_data)
        print(
            f" \n\t{Color.GREEN}[√] You are ready to Go.{Color.END}\n")
    except FileNotFoundError:
        print(f"The '{folder[-1]}' directory does not exist")


def get_func_name(file_data):
    if not file_data:
        print(
            f" \n\t{Color.RED}[x] The function name not found.{Color.END}\n")
        return

    start_func = 0
    end_func = 0

    start_func = file_data.find('f ')
    end_func = file_data.find('(')
    func_name = file_data[start_func+1:end_func]

    print(
        f" \n\t{Color.GREEN}[√] GET Function Name: {func_name}{Color.END}\n")
    return func_name


def get_func_args(file_data):
    if not file_data:
        print(
            f" \n\t{Color.RED}[x] No arguments not found {Color.END}\n")
        return

    start_args = 0
    end_args = 0

    start_args = file_data.find('(')
    end_args = file_data.find(')')
    args = file_data[start_args+1:end_args]
    args = args.split(',')
    if 'self' in args:
        args.remove('self')

    print(
        f" \n\t{Color.GREEN}[√] GET Function args: {args}{Color.END}\n")
    return args


def prepare_output(path, file_data):
    func_name = get_func_name(file_data)
    args = get_func_args(file_data)
    if args == None:
        args = []
    file = open(path, 'a')
    file.write("\n")
    func_args = []

    for arg in args:
        arg = arg.strip()
        file.write(arg)
        file.write("\n")
        parameter = arg.split('=')
        parameter = parameter[0] + '= '+parameter[0]

        func_args.append(parameter)

    print_ = (f"print(Solution().{func_name}(")
    for arg in func_args:
        print_ = print_ + arg + ', '
    print_ = print_ + '))'
    file.write(print_)
    file.close()


def main():
    problem_title = input(f"{Color.WHITE}[-] Folder Name:{Color.END}  ")
    folder = create_folder(problem_title)
    create_file(folder=folder[0], exist=folder[1])


if __name__ == "__main__":
    main()
