list1 = []


def task_3(list_):  # у меня не получилось без аргументов :(((

    user = input('Enter number: ')
    if user != '':
        list_.append(int(user))
        task_3(list_)
    else:
        if user == '' and list_ == ['']:
            print(0.0)
        else:
            print(sum(list_))


task_3(list1)