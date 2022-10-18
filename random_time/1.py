from time import *


def igra():
   start = time()
   while time() - start < 18000:
       hod = input('Введите ход: ')
       if hod.lower() == 'off':
           break
       else:
           print(f'Вы потратили на ход: {round(time() - start, 2)} секунд')
       print(f'Оставшееся время: {30 -  round((time() - start) / 60, 2)} минут')


igra()