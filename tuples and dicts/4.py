dictionary = {
    1: 'мама',
    2: 'папа',
    3: 'деда',
    4: 'баба',
    5: 'брат'
}
addr = id(dictionary)

dictionary[1], dictionary[5] = dictionary[5], dictionary[1]
dictionary.pop(2)
dictionary['new_key'] = 'new_value'
print(dictionary)

print(id(dictionary) == addr)

