import sys
import os

#file path
script_path = 'F:\\Scripts\\cpp_compile_run.py'

# current directory
dir = os.getcwd()

# filename from argument
file = sys.argv[1]

if(file[0:2] == "./" or file[0:2] == ".\\"):
    file = file[2:]

if not file.endswith('.cpp'):
    file = file + '.cpp'

file_name = os.path.splitext(file)[0]

if len(file_name) == 1:
    file_name = file_name.lower()
    file = file_name + 'cpp'

# compiling and running
def compile_run():
    if os.system(f'g++ -std=c++17 -Wall -DLOCAL {file} -o {file_name}.exe') == 0:
        run()
    else:
        print("Compilation Failed!")

# executing
def run():
    os.system(f'{dir}/{file_name}.exe')
    os.system

def choice_is_bad(choice):
    return choice != 'c' and choice != 'r' and choice != 'q'

print()
# executing first time
compile_run()

while True:
    choice = input(f'\nCompile, Run again or Quit? (c / r / q) : ').lower()
    while choice_is_bad(choice):
        choice = input(f'\nInvalid Input. Enter again : ')
    print()
    
    if choice == 'c':
        compile_run()    
    elif choice == 'r':
        run()
    else :
        print('Done.\n')
        exit()
