class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power


class Magician(Hero):
    def __init__(self, health, power):
        super().__init__(health, power)

    def hello(self):
        print('блаблабла')

    def attack(self, another_gamer):
        another_gamer.health -= self.power * 4
        self.power -= 5
        print('удар')


def main():
    hero = Hero(200, 20)
    mag = Magician(100, 20)
    mag.hello()
    mag.attack(hero)
    print(f'сила мага: {mag.power}')
    print(f'здоровье героя: {hero.health}')


main()
