class Pet():
    def __init__(self, name, hp = 10, maxHp = 10, hunger = 0, minHunger = 0, dust = 0):
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.hunger = hunger
        self.minHunger = minHunger
        self.dust = dust
    
    def feed(self):
        self.hunger -= 2
        self.hp += 1
        if self.hunger < self.minHunger:
            self.hunger = self.minHunger
        if self.hp > self.maxHp:
            self.hp = self.maxHp
        print(f"{self.name} now has {self.hunger} hunger and {self.hp} hp")
        

class Dog(Pet):
    def __init__(self):
        super().__init__()

class Cat(Pet):
    def __init__(self):
        super().__init__()

class Rabbit(Pet):
    def __init__(self):
        super().__init__()

class Parrot(Pet):
    def __init__(self):
        super().__init__()