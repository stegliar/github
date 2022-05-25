import random
import abc
import time
import yaml


class Pokemon:
    def __init__(self, name, type, hp, attack, defence):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defence = defence
        # self.moves = moves

    def fight(self, Pokemon2):
        print(f"{self.name} against {Pokemon2.name}")

        PokemonType = ["Fire", "Water", "Plant"]
        for i, t in enumerate(PokemonType):
            if self.type == t:
                if Pokemon2.type == t:
                    attack_1 = "not effective"
                    attack_2 = "not effective"

                if Pokemon2.type == PokemonType[(i + 1) % 3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defence *= 2
                    self.attack /= 2
                    self.defence /= 2
                    attack_1 = "not effective"
                    attack_2 = "very effective"

                # Pokemon2 is WEAK
                if Pokemon2.type == PokemonType[(i + 2) % 3]:
                    self.attack *= 2
                    self.defence *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defence /= 2
                    attack_1 = "very effective"
                    attack_2 = "not effective"

                # if poisoned
                # if sleeping
                # if paralized

        while (self.hp > 0) and (Pokemon2.hp > 0):
            print(f"\n{self.name} {self.hp}")
            print("against")
            print(f"{Pokemon2.name} {Pokemon2.hp}\n")
            print(attack_1)

            Pokemon2.hp -= self.attack

            if Pokemon2.hp <= 0:
                print("\n" + Pokemon2.name + " fainted")
                break
            else:
                print(Pokemon2.name, Pokemon2.hp)
                break

            print(f"\n{Pokemon2.name} {Pokemon2.hp}")
            print("against")
            print(f"{self.name} {self.hp}")
            print(attack_2)

            self.hp -= Pokemon2.attack

            if self.hp <= 0:
                print("\n" + self.name + " fainted")
                break
            else:
                print(self.name, self.hp)
                break


class Trainer():
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.pokemoninbag = []
        self.items = []

    # HealItems(Items):
    # heal 20 hp
    # heal 50 hp
    # heal 100 hp
    # heal poison
    # heal paralize
    # heal sleeping
    pass


if __name__ == "__main__":
    Ilayda = Pokemon("Ilayda", "Water", 150, 50, 50)
    Yoko = Pokemon("Yoko", "Water", 150, 50, 50)
    Chilly = Pokemon("Chilly", "Fire", 150, 50, 50)
    Xia = Pokemon("Xia", "Fire", 150, 50, 50)
    Cyclamen = Pokemon("Cyclamen", "Plant", 150, 50, 50)
    Hanako = Pokemon("Hanako", "Plant", 150, 50, 50)

    Pokemongame = "save.yaml"

    with open(Pokemongame, "w") as f:
        yaml.dump(Ilayda, f)
    with open(Pokemongame, "r") as f:
        reloaded_Ilayda = yaml.load(f)
        # print (reloaded_Ilayda)

    # Pokemongame = "save.yaml" #?

    with open(Pokemongame, "a") as f:
        yaml.dump(Yoko, f)
    with open(Pokemongame, "r") as f:
        reloaded_Yoko = yaml.load(f)
        # print (reloaded_Yoko)

    with open(Pokemongame, "a") as f:
        yaml.dump(Chilly, f)
    with open(Pokemongame, "r") as f:
        reloaded_Chilly = yaml.load(f)
        # print (reloaded_Chilly)

    with open(Pokemongame, "a") as f:
        yaml.dump(Xia, f)
    with open(Pokemongame, "r") as f:
        reloaded_Xia = yaml.load(f)
        # print (reloaded_Xia)

    with open(Pokemongame, "a") as f:
        yaml.dump(Cyclamen, f)
    with open(Pokemongame, "r") as f:
        reloaded_Cyclamen = yaml.load(f)
        # print (reloaded_Cyclamen)

    with open(Pokemongame, "a") as f:
        yaml.dump(Hanako, f)
    with open(Pokemongame, "r") as f:
        reloaded_Hanako = yaml.load(f)
        # print (reloaded_Hanako)

    with open(Pokemongame, "a") as f:
        yaml.dump(Trainer, f)
    with open(Pokemongame, "r") as f:
        reloaded_Trainer = yaml.load(f)
        # print (reloaded_Trainer)

    # Pokelist = [Ilayda, Yoko, Chilly, Xia, Cyclamen, Hanako]

    # Skittles = Pokemon()
    # random.choices(Ilayda, Yoko, Chilly, Xia, Cyclamen, Hanako)

    # print("Choose your Pokemon")
    # print("Ilayda", "Yoko", "Chilly", "Xia", "Cyclamen", "Hanako")
    # Pokemon1 = input("")
    # print("Choose the enemy Pokemon")
    # Pokemon2 = input("")
    # Pokemon1.fight(Pokemon2)

    # time.sleep(.5)

    Hanako.fight(Yoko)
