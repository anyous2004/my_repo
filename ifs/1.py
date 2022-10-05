eating = input('Завтрак? Обед? Ужин? \n')

if eating == 'Завтрак':
    print('Поешь каши')
else:
    density = input('Плотно? \n')
    if density == 'плотно':
        print('Поешь плов')
    else:
        print('Поешь котлетку с пюре')