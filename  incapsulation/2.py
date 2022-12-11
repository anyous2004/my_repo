class Hero:
    def __init__(self, health, power, rank):
        self.health = health
        self.power = power
        self.__rank = rank

    def set_rank(self, rank):
        self.__rank = rank

    def get_rank(self):
        return self.__rank

    def del_rank(self):
        del self.__rank

    def fight(self, enemy):
        while self.power > 0:
            enemy.health -= 4
            self.power -= 20
        if enemy.health < 0:
            self.set_rank('Победитель арены')
            print(self.get_rank())
        else:
            self.del_rank()
            print('лузер')


def main():
    hero1 = Hero(200, 1000, 'ранг 1')
    hero2 = Hero(200, 2000, 'ранг 0')
    hero1.fight(hero2)


main()