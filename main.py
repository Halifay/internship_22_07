import sys
import random
import webbrowser


def read_structure(filename='base.tex'):
    with open(filename) as base_file:
        base_structure = base_file.read()
    return base_structure


def main(in_filename = 'files/base.tex', out_filename='files/output.tex', n_vars=4, *args):
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
    # creating lists with length of number of tasks
    task_variants = [[] for i in range(len(tasks))]
    word_lists = [[] for i in range(len(tasks))]

    # read task variants
    for i in range(len(tasks)):
        variants_filename = f'files/Problem{i+1}.tex'
        with open(variants_filename) as input_file:
            task_variants[i] = input_file.read().split('%%new_st')
            word_lists[i] = [[] for x in task_variants[i]]
            for j in range(len(task_variants[i])):
                task_variants[i][j] = task_variants[i][j].split('%%st_del')
                task_variants[i][j] = list(filter(None, task_variants[i][j]))
                # print([[] for x in task_variants[i][j]])
                word_lists[i][j] = [[] for x in task_variants[i][j]]
                for k, variant in enumerate(task_variants[i][j]):
                    if len(variant.split('%%items_del')) == 2:
                        task_variants[i][j][k] = variant.split('%%items_del')[0]
                        word_lists[i][j][k] = variant.split('%%items_del')[1][2:-2].split(',')
                        # print(variant.split('%%items_del')[1], len(variant.split('%%items_del')[1]))

    # write variants to the file
    final_file = file_start
    tasks_numbers = [[[] for j in range(len(task_variants[i]))] for i in range(len(task_variants))]
    for i in range(n_vars):
        #create variant
        variant = variant_start
        variant = variant.replace('%%var_ph', str(i+1))
        for i, _ in enumerate(tasks):
            variant += tasks[i]
            for j, _ in enumerate(task_variants[i]):
                if tasks_numbers[i][j] == []:
                    tasks_numbers[i][j] = [k for k in range(len(task_variants[i][j]))]
                variant_choice_number = random.choice(tasks_numbers[i][j])
                tasks_numbers[i][j].remove(variant_choice_number)
                variant = variant.replace('%%subtask_ph', task_variants[i][j][variant_choice_number], 1)
                for word in word_lists[i][j][variant_choice_number]:
                    # print(word, len(word))
                    variant = variant.replace('%%word_ph', word, 1)
        final_file += variant
    final_file += file_end

    with open(out_filename, 'w') as output_file:
        output_file.write(final_file)

    # webbrowser.open(out_filename)

if __name__ == '__main__':
    main()
