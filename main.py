class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True

class Knight(Warrior):
    def __init__(self):
        self.health = 50
        self.attack = 7
        self.is_alive = True


def fight(unit_1, unit_2):
    while True:
        unit_2.health -= unit_1.attack
        if unit_2.health < 0:
            unit_2.is_alive = False
            return True
        unit_1.health -= unit_2.attack
        if unit_1.health < 0:
            unit_1.is_alive = False
            return False

class Army:
    def __init__(self):
        self.army = []

    def add_units(self, unit, count):
        for i in range(count):

            self.army.append(unit())

class Battle():

    def fight(self, army_1, army_2):
        self.i = 0
        self.j = 0
        while True:
            army_2.army[self.j].health -= army_1.army[self.i].attack
            if army_2.army[self.j].health < 0:
                army_2.army[self.j].is_alive = False

                if self.j + 1 == len(army_2.army):
                    return True
                else:
                    self.j += 1
                    continue

            army_1.army[self.i].health -= army_2.army[self.j].attack
            if army_1.army[self.i].health < 0:
                army_1.army[self.i].is_alive = False

                if self.i + 1 == len(army_1.army):
                    return False
                else:
                    self.i += 1
                    continue









if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    # print(fight(chuck, bruce))
    # print(fight(dave, carl))
    # print(chuck.is_alive)
    # print(bruce.is_alive)
    # print(carl.is_alive)
    # print(dave.is_alive)
    # print(fight(carl, mark))
    # print(carl.is_alive)

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    print(enemy_army.army)
    print(my_army.army)
    print(army_3.army)
    print(army_4.army)
    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False