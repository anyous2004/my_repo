while True:
    name = input()
    if name != 'off':
        a = lambda name_, slovo: print(name_, slovo)
        a(name, 'гений')
    else:
        break