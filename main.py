import sys
import random
import webbrowser


def read_structure(filename='base.tex'):
    with open(filename) as base_file:
        base_structure = base_file.read()
    return base_structure


def main(in_filename = 'files/base.tex', out_filename='files/output.tex', n_vars=3, *args):
    final_file = []
    print(f'Number of arguments: {len(sys.argv)}')
    for argument in sys.argv:
        print(argument)

    # read doc structure
    with open(in_filename) as base_file:
        base_structure = base_file.read()
    file_start, base_structure = base_structure.split('%%doc_start')
    base_structure, file_end = base_structure.split('%%doc_end')
    variant_start = base_structure.split('%%task_start')[0]
    tasks = base_structure.split('%%task_start')[1:]
    task_variants = {}

    # read task variants
    for i, _ in enumerate(tasks):
        variants_filename = f'files/Problem{i+1}.tex'
        with open(variants_filename) as input_file:
            task_variants[i] = input_file.read().split('%%new_st')
            for j, _ in enumerate(task_variants[i]):
                task_variants[i][j] = task_variants[i][j].split('\n')
                task_variants[i][j] = list(filter(None, task_variants[i][j]))

    # write variants to file
    final_file = file_start
    for i in range(n_vars):
        #create variant
        variant = variant_start
        variant = variant.replace('%%var_ph', str(i+1))
        for i, _ in enumerate(tasks):
            variant += tasks[i]
            for j, _ in enumerate(task_variants[i]):
                variant = variant.replace('%%subtask_ph', random.choice(task_variants[i][j]), 1)
        final_file += variant
    final_file += file_end

    with open(out_filename, 'w') as output_file:
        output_file.write(final_file)

    webbrowser.open(out_filename)

if __name__ == '__main__':
    main()
