import time
from multiprocessing import Process


def hurry():
    while True:
        print('Вводите быстрее')
        time.sleep(3)

process = Process(daemon=True, target=hurry)
process.start()
password = '666666'
user_pswd = input('Code: \n')
if user_pswd == password:
    print('Бомба разминирована')
else:
    print('Вы взорвались')