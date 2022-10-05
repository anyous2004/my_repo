while True:
    cost = int(input('Введите сумму покупки: '))
    discount = int(input('Введи скидку в %: '))
    if cost == 0:
        break
    else:
        price = cost - (cost / 100 * discount)
        print(f'Цена за товар: {price}')
        continue


