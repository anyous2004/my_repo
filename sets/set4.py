first_ = "0 0 0 0 0 0 0" #Вывод должен быть 0
second_ = "1 1 1 0 0 0 0" # Вывод должен быть 3
third_ = "1 1 1 1 1 1 1" # Вывод должен быть 1


def task_4(first, second, third):
    A, B, C, D, E, F, G = map(int, first.split())
    print(A + B + C - F + D + E - G)
    A, B, C, D, E, F, G = map(int, second.split())
    print(A + B + C - F + D + E - G)
    A, B, C, D, E, F, G = map(int, third.split())
    print(A + B + C - (F + D + E - G))


task_4(first_, second_, third_)