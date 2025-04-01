from datetime import datetime

class Pet():
    def __init__(self):
        self.name = input("Enter your pets name: ")
        self.hp = 10
        self.hunger = 0
        self.cleanliness = 10
        self.happines = 10
        self.mood = "happy"

    def ifSleep(self):
        now = datetime.now()
        currentTime = int(now.strftime("%H"))

        if currentTime > 6 and currentTime < 22:
            return False
        else:
            return True

    
    def printStatsBar(self, statName, statValue):
        print(f"{statName}: [{"#" * statValue + "-" * (10 - statValue)}] {statValue:.2f}/10")

    def isMax(self, currentValue, maxValue = 10, minValue = 0):
        if currentValue > maxValue:
            return maxValue
        elif currentValue < minValue:
            return minValue
        else:
            return currentValue

    def showStats(self):
        print(f"Name: {self.name.capitalize()}")
        self.printStatsBar("Hp", self.hp)
        self.printStatsBar("Hunger", self.hunger)
        self.printStatsBar("Cleanliness", self.cleanliness)
        self.printStatsBar("Happines", self.happines)
        print(f"Mood: {self.mood.capitalize()}")

    def feed(self):
        self.hunger -= 2
        self.hp += 3
        self.happines += 2
        self.cleanliness -= 1
        print(f"{self.name} is now full of food")
        
    def clean(self):
        self.cleanliness += 2
        self.happines += 1
        self.hp -= 1
        print(f"{self.name} is now clean")
        
    def play(self):
        self.hp += 2
        self.happines += 3
        self.hunger += 2
        self.cleanliness -= 2
        print(f"{self.name} is happy for playing with you")
        
    def goWalk(self):
        self.hp += 1
        self.hunger += 2
        self.cleanliness -= 2
        self.happines += 3
        print(f"{self.name} is so dirty now")
        
    def sleep(self):
        self.hp += 3
        self.hunger += 3
        self.happines += 2
        print(f"{self.name} got some good sleep")
        
    def update(self):
        if self.hunger > 5:
            self.hp -= 1
        if self.cleanliness < 3:
            self.hp -= 1
        if self.happines < 5:
            self.hp -= 1
        if self.hp <= 0:
            print(f"Sorry, {self.name} has passed away")
            quit()

        self.hunger = self.isMax(self.hunger)
        self.hp = self.isMax(self.hp)
        self.happines = self.isMax(self.happines)
        self.cleanliness = self.isMax(self.cleanliness)

        self.updateMood()

    def updateMood(self):
        if self.happines > 8:
            self.mood = "very happy"
        elif self.happines > 5:
            self.mood = "happy"
        elif self.happines > 2:
            self.mood = "okay"
        else:
            self.mood = "sad"

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)