error_symbols = "=?*^$№@_"

login = input('Введете логин: ')

errors = list()
for i in login:
    if i in error_symbols:
        errors.append(i)
    else:
        continue

print('запрещенные символы: ', list(set(errors)))


