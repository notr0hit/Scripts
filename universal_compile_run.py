import sys
import os

#file path
script_path = 'F:\\Scripts\\univeral_compile_run.py'

# current directory
dir = os.getcwd()

# filename from argument
file = sys.argv[1];
if(file[0:2] == "./" or file[0:2] == ".\\"):
    file = file[2:]



file_name, file_extension = os.path.splitext(file)

# make default extension to cpp if there is no extension
if file_extension == '':
    file = file + '.cpp'
    file_extension = '.cpp'

# compile arguments
compile_args = {
    ".java" : f'javac {file}',
    ".cpp" : f'g++ -std=c++17 -Wall -O2 -DOFFLINE {file} -o {file_name}',
}

#run arguments
run_args = {
    ".java" : f'java {file_name}',
    ".py" : f'python {file}',
    ".cpp" : f'{dir}/{file_name}'
}

def compile():
    if compile_args.get(file_extension) != None:
        os.system(compile_args[file_extension])
    else:
        print("No compile arguments for this file.")

def run():
    if run_args.get(file_extension) != None:
        os.system(run_args[file_extension])
    else:
        print("No run arguments for this file.")
    print()

def compile_run():
    if compile_args.get(file_extension) == None and run_args.get(file_extension) == None:
        print('No compile and run arguments for this file.')
    
    else:
        if compile_args.get(file_extension) != None:
            compile()
        if run_args.get(file_extension) != None:
            run()
    

# Compiling and running atleast once
print()
compile_run()


def choice_is_bad(choice):
    return choice != 'c' and choice != 'r' and choice != 'q'

while True:
    choice = input(f'Compile, Run again or Quit? (C / R / Q) : ').lower()
    while choice_is_bad(choice):
        choice = input(f'Invalid Input. Enter again : ')

    print()
    if choice == 'c':
        compile_run()
    
    elif choice == 'r':
        run()

    else :
        print('Done.\n')
        exit()
