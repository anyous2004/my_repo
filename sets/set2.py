def task2(_list):
    printSet = set()
    for element in _list:
        if type(element) == list or type(element) == dict or type(element) == set:
            _list.remove(element)
        else:
            printSet.add(element)
    if len(printSet) > 0:
        print(True)
        print(_list)
    else:
        print(False)


testList = [1, 2, 2, [3, 4], (1, 2, 3), "1", {1, 2, 3}]
task2(testList)