import threading
import time

def remember():
    user_note = input('О чем напомнить?:\n')
    user_time = int(input('Через сколько напомнить?'))
    time.sleep(user_time)
    print(user_note)

th = threading.Thread(target=remember())
th.start()
th.join()
time.sleep(2)
print('программа завершается')