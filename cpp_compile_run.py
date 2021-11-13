import sys
import os

#file path
script_path = 'D:\Scripts\cpp_compile_run.py'

# current directory
dir = os.getcwd()

# filename from argument
file_name = sys.argv[1];
if(file_name.endswith(".cpp")):
    file_name = file_name[0:-4]

if(file_name[0:2] == "./" or file_name[0:2] == ".\\"):
    file_name = file_name[2:]


# compiling
os.system(f'g++ -std=c++17 -Wall -Werror -O2 -DROHIT {file_name + ".cpp"} -o {file_name}')

# executing
os.system(f'{dir}\\{file_name}')

print()
choice = input(f'Do you want to compile again? (y / n) : ')
choice = choice.lower()

if choice != 'y' and choice != 'n':
    choice = input(f'Invalid input. Do you want to compile again? (y / n) : ')

if choice == 'y':
    os.system(f'python.exe {script_path} {file_name}')
else :
    print('Done.\n')
