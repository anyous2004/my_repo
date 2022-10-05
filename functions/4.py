"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""

def imt(weight, height):
    index = weight / (height ** 2)
    return index

res = imt(100, 2)

def check_imt():
    if (res) < 18.5:
        print("Недостаточный вес")
    elif 18.5 < res < 25:
        print("ИМТ в норме")
    elif res >= 25:
        print("Избыточный вес")

check_imt()



