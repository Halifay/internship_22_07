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
