from abc import ABC, abstractmethod
from random import randint


class Creature(ABC):
    def __init__(self, hp, name, size, gold):
        self.hp = hp
        self.name = name
        self.size = size
        self._gold = gold

    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, value):
        self._gold = value

    @abstractmethod
    def roll_dice(self, value):
        pass

    @abstractmethod
    def fist_hit(self):
        pass

    def introduction(self):
        pass


class Warrior(Creature):
    def __init__(self, hp, name, size, gold):
        super().__init__(hp, name, size, gold)

    def roll_dice(self, value):
        return randint(1, value)

    def fist_hit(self):
        return self.roll_dice(4)

    def introduction(self):
        print("Geh mal Bier holen, ich warte schon mal.")


class Mage(Creature):
    def __init__(self, hp, name, size, gold):
        super().__init__(hp, name, size, gold)

    def roll_dice(self, value):
        return randint(1, value)

    def fist_hit(self):
        return self.roll_dice(3)

    def introduction(self):
        print("Gott zum Gruße, ihr Gottlosen!")


if __name__ == "__main__":
    # Erzeugen der Klassen
    gandalf = Mage(140, "Gandalf", "200", 9)
    aragorn = Warrior(200, "Aragorn", "190", 4)

    print(gandalf.name, "fists first: ", gandalf.fist_hit())
    print(aragorn.name, "fists now: ", aragorn.fist_hit())
    print()
    print(gandalf.name, "gets 5 Gold")
    print("Gold before:", gandalf.gold)
    gandalf.gold += 5
    print("Gold now:", gandalf.gold)
