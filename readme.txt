Инструкция по применению.
1) Запустить скрипт с помощью Python интерпретатора (тестировался только Python3). Если нет каких-то библиотек - установить их.
2) Ввести путь к папке с базовым шаблоном варианта (должен называться base.tex) и перечням заданий (должны иметь названия вида ProblemN.tex, где N - номер задания).
3) Ввести необходимое количество вариантов.
4) Найти готовый файл (путь указан в последней строчке вывода скрипта).

Файл базовой структуры
%%doc_start - начальная часть документа. Будет отображаться только один раз для файла независимо от количества вариантов.
%%doc_end - завершающая часть документа. Будет отображаться один раз.
%%var_ph — (variant_placeholder) место для номера варианта.
%%task_del [deprecated] - разделитель для разных задач. Первое вхождение соответствует первой задаче, второе соответствует второй и так далее.
%%subtask_ph - заполнитель для подзадач в задаче. N-е вхождение соответствует n-й подзадаче.
%%word_ph - заполнитель для слов, различающихся между вариантами

Файл проблемы
%%new_st - разделитель между пакетами подзадач. Внутри одного пакета варианты подзадач делятся на %%st_del.
%%st_del - разделитель между подзадачами внутри одного пакета.
%%items_del - разделитель для списка слов, зависящих от подзадачи. Слова должны быть написаны на следующей
     строка, заканчиваться новой строкой и использовать следующий формат: [первое, второе,..., последнее]


Instructions for use.
1) Run the script using the Python interpreter (only Python3 was tested). If there are no libraries, install them.
2) Enter the path to the folder with the base variant template (should be named base.tex) and task lists (should have names like ProblemN.tex, where N is the task number).
3) Enter the required number of variants.
4) Find the finished file (the path is indicated in the last line of the script output).

Base structure file
%%doc_start - starting part of the document. Will show up only one time for a file independent on number of variants.
%%doc_end - finishing part of the document. Will show up once per document.
%%var_ph - (variant_placeholder) placeholder for variant number.
%%task_del - delimiter for different tasks. First occurrence matches first task, second matches second and so on.
%%subtask_ph - placeholder for subtasks in the task. N-th occurrence corresponds to the n-th subtask.
%%word_ph - placeholder for varying words

Problem file
%%new_st - delimiter between batches of subtasks. Inside one batch subtask variants are divided by %%st_del.
%%st_del - delimiter betweeen subtasks inside one batch.
%%items_del - delimiter for list of words that depend on subtask. Words should be written on the next
    line, end with new line and use following format: [first,second,...,last]
