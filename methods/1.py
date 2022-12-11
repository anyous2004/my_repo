from datetime import *


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'

    def print_info(self):
        print(f'Имя: {self.name}\n'
              f'Возраст: {self.age}')

    @classmethod
    def generate_person(cls, name, year):
        now = datetime.now()
        age = now.year - year
        return cls(name, age)

    @staticmethod
    def check_adult(person):
        if person.age >= 18:
            return True
        else:
            return False


def main():
    kek = Person('Kek', 15)
    kek.print_info()

    lol = Person.generate_person('Lol', 1999)
    print(lol)

    print(Person.check_adult(lol))
    print(Person.check_adult(kek))


main()