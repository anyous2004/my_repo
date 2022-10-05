list_of_num = [1, 2, 3, 4, 5]
list_of_num1 = [1, 3, 4, 5]
list_of_num2 = [1]


def check(l):
    if len(l) == 1:
        return 'Нет'
    for i in range(1, len(l)):
        if l[i - 1] + 1 == l[i]:
            continue
        else:
            return 'Нет'
    else:
        return 'Да'