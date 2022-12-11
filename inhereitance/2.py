class Genii:

    def __init__(self, name):
        self.name = name

    def write_genii(self):
        return f'{self.name} гений'


class MyClass(Genii):

    def __init__(self, name):
        super().__init__(name)

    def make_object(self):
        one = Genii(self.name)
        return one

    def action(self):
        print(f'{self.make_object().write_genii()}, но его отчислят если он не будет учить ООП')


def main():
    test = MyClass('Аня')
    test.action()


main()