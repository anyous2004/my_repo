while True:
    choice = input('Введите game/off \n')

    if choice == 'off':
        break

    elif choice == 'game':
        print('Игра "угадай число" У тебя 3 попытки, вводи число \n')
        trying = 0
        for _ in range(0, 3):
            answer = int(input())
            if answer == 5:
                print('Победа!')
                break
            else:
                print('Неверно! Еще попытка ')
                continue
        else:
            print('Попытки кончились :(')
            continue
    else:
        continue

