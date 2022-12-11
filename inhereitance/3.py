class SpaceObject:

    def __init__(self, size):
        self.size = size


class Star(SpaceObject):

    def __init__(self, size, yarkost):
        super().__init__(size)
        self.yarkost = yarkost

    def shine(self):
        print(f'Яркость звезды: {self.yarkost}')


class Planet(SpaceObject):

    def __init__(self, size, people, uvelich):
        super().__init__(size)
        self.people = people
        self.uvelich = uvelich

    def people_in_years(self, years):
        print(f'Через {years} лет населения будет {self.people + self.uvelich * years}')


def main():
    star = Star(590, 1010)
    star.shine()

    planet = Planet(400, 250, 50)
    planet.people_in_years(5)


main()