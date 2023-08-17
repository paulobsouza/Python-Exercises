import os

tasks = []
redo_tasks = []


def listing(tasks):
    print()
    if not tasks:
        print('Não há nenhuma tarefa a ser listada.')
        return
    print('Tarefas: ')
    for task in tasks:
        print(f'\t{task}')
    print()


def undo(tasks, redo_tasks):
    print()
    if not tasks:
        print('Não há nenhuma tarefa a ser desfeita.')
        return
    task = tasks.pop()
    print(f'{task=} removida da lista de tarefas.')
    redo_tasks.append(task)
    print()


def redo(tasks, redo_tasks):
    print()
    if not tasks:
        print('Não há nenhuma tarefa a ser refeita.')
        return
    task = redo_tasks.pop()
    print(f'{task=} adicionada a lista de tarefas.')
    tasks.append(task)
    print()


def add(task, tasks):
    print()
    task = task.strip()
    if not task:
        print('Não há nenhuma tarefa a ser adicionada.')
        return
    f'{task=} adicionada a lista de tarefas.'
    tasks.append(task)
    print()


while True:
    print('Os comandos são: Listar, Desfazer, Defazer e Limpar.')
    task = input('Digite uma tarefa ou comando: ')

    if task == 'listar':
        listing(tasks)
        continue
    elif task == 'desfazer':
        undo(task, redo_tasks)
        listing(tasks)
        continue
    elif task == 'refazer':
        redo(tasks, redo_tasks)
        listing(tasks)
        continue
    elif task == 'limpar':
        os.system('clear')
    else:
        add(task, tasks)
        listing(tasks)
        continue
