from random import *
while True:
    n = input("Для продолжения напишите 'Да', а для завершения 'off': ")
    if n == 'off':
        break
    print(f'Ваш номер: {randint(1, 100)}')
    print(f"«Участников в первом забеге: {randint(1, 10)}», «Участников во втором забеге: {randint(1, 10)}»")