product1 = int(input('Цена за первый товар: '))
product2 = int(input('Цена за второй товар: '))
product3 = int(input('Цена за третий товар: '))

if product1 < product2 < product3:
    print('Акция!!!!')
    print(f'К оплате: {round((product1 + product2 + product3) / 2, 2)}')
elif product3 < product2 < product1:
    print('Акция!!!!')
    print(f'К оплате: {round((product1 + product2 + product3) / 3, 2)}')
else:
    print(f'К оплате: {product1 + product2 + product3}')

