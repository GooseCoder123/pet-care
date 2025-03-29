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
        self.hunger += 1
        self.cleanliness -= 1
        if self.hunger > 5:
            self.hp -= 1
        if self.cleanliness < 3:
            self.hp -= 1
        if self.happines < 5:
            self.hp -= 1
        if self.hp <= 0:
            print(f"Sorry, {self.name} has passed away")
        self.updateMood()

    def updateMood(self):
        if self.happines > 8:
            self.mood = "very happy"
        elif self.happines > 5:
            self.mood = "happy"
        elif self.happines > 2:
            self.mood = "okey"
        else:
            self.mood = "sad"

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)