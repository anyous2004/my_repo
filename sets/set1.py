def task1(_list1, _list2):
    print(sorted(set(_list1).intersection(set(_list2))))


list1 = [1,2,3,4,5,6]
list2 = [4,16,1,3,8,2]
task1(list1, list2)