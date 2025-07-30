import sys
from pathlib import Path
from colorama import Fore, Back, Style


'''

Function  which accepts a directory path as a command line argument 
and visualizes the structure of that directory. 
All the directories and files are marked in different colors

input: path
output: None
'''

def show_structure(path:Path, indention:str = ''):
    print(f'{Back.GREEN}{indention}{path.name}{Style.RESET_ALL}/') #make directories at the green back

    for item in sorted(path.iterdir()):
        if item.is_dir():
            show_structure(item, indention + '  ')
        else:
            print(Fore.LIGHTGREEN_EX + indention + ' ' + item.name + Style.RESET_ALL) #make the files green




if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Path is not found')
    else:
        show_structure(Path(sys.argv[1]))    #launch the file by entering the path in the terminal