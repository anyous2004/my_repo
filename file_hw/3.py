def task3():
    name_1 = input('f')
    name_2 = input('f1')
    full_name1 = r'C:\Users\sirius\my_repo\file_hw/' + name_1
    full_name2 = r'C:\Users\sirius\my_repo\file_hw/' + name_2
    stack = []
    print(full_name1)
    with open(full_name1, 'r+', encoding="utf-8") as f1:
        for line in f1:
            stack.append(line)
    with open(full_name2, 'w+', encoding="utf-8") as f2:
        for i in range(0, len(stack)):
            f2.writelines(str(i + 1) + ': ' + stack[i])
    with open(full_name2, 'r+') as f3:
        print(f3.read())


task3()