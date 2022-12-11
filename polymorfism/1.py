class Person:

    def say(self):
        print('Человеческое кря')

    def wear(self):
        print('Ношу одежду как человек')


class Duck:

    def say(self):
        print('Утиное кря')

    def wear(self):
        print('Ношу одежду как утка')


def main():
    my_list = [Person(), Duck()]
    for i in my_list:
        i.say()
        i.wear()


main()