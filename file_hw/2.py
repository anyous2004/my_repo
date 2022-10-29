def task2():
    with open(r'C:\Users\sirius/new.txt', 'w+') as f2:
        f2.write('но у меня не получается')
    with open(r'C:\Users\sirius/gotovo.txt', 'w+') as final:
        with open(r'C:\Users\sirius/homework.txt', 'r+') as f1:
            with open(r'C:\Users\sirius/new.txt', 'r+') as f2:
                final.write(f1.read() + ' ')
                final.write(f2.read())
    with open(r'C:\Users\sirius/gotovo.txt', 'r+') as final1:
        print(final1.read())


task2()