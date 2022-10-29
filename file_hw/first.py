def task1():
    with open(r'C:\Users\sirius\homework.txt', 'w+') as f:
        f.write('Я гений и стараюсь учить питон')
    with open(r'C:\Users\sirius\homework.txt', 'r+') as f:
        print((f.read())[0:7])


task1()