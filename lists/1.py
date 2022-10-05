games = list()
while True:
    game = input("Введите название игры \n")
    if game == '0':
        break
    elif game in games:
        print('Эта игра уже записана')
    else:
        games.append(game)
        print(f'Все игры: {sorted(games)}')
        