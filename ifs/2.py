payment = int(input('Введите сумму к оплате: '))
hour = int(input('Введите текущий час: '))

if 8 <= hour <= 22:
    if 10 <= hour <= 12:
        print(f'сумма к оплате равна - {payment / 2}')
    elif 20 <= hour <= 22:
        print(f'сумма к оплате равна - {payment / 4}')
    else:
        print(f'сумма к оплате равна - {payment}')
else:
    print('Мы закрыты что врешь')
