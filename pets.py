class Pet():
    def __init__(self):
        self.name = input("Enter your pets name: ")
        self.hp = 10
        self.hunger = 0
        self.cleanliness = 10
        self.happines = 10
        self.mood = "happy"
    
    def feed(self):
        self.hunger -= 2
        self.hp += 3
        self.happines += 2
        self.cleanliness -= 1
        print(f"{self.name} now has {self.hunger} hunger and {self.hp} hp")

    def clean(self):
        self.cleanliness += 2
        self.happines += 1
        self.hp -= 1
        print(f"{self.name} now has {self.cleanliness} cleanliness level")
    
    def play(self):
        self.hp += 2
        self.happines += 3
        self.hunger += 2
        self.cleanliness -= 2
        print(f"{self.name} now has {self.hp} hp")

    def update(self):
        pass

    def updateMood(self):
        pass

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)

    def goOnWalk(self):
        pass