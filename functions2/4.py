def task_5(colour, number, **kwargs):
    print(f'{colour}: {number}')
    for kw in kwargs:
        print(f'{kw}: {kwargs[kw]}')


task_5(input(), int(input()), white=100, black=404, yellow=200, green=303)
