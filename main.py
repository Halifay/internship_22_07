import os
import sys


def read_structure(filename='base.tex'):
    with open(filename) as base_file:
        base_structure = base_file.read()
    return base_structure


def main(*args):
    print(f'Number of arguments: {len(sys.argv)}')
    for argument in sys.argv:
        print(argument)
    in_filename = sys.argv[1]
    out_filename = sys.argv[2]
    n_vars = sys.argv[3]
    with open(in_filename) as base_file:
        base_structure = base_file.read()
    file_start, base_structure = base_structure.split('%%doc_start')
    base_structure, file_end = base_structure.split('%%doc_end')
    tasks = base_structure.split('%%task_start')




if __name__ == '__main__':
    main()

