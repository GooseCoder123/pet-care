import datetime
from pets import Dog, Pet

def mainMenu() -> None:
    print("1. Feed")
    print("2. Play")
    print("3. Clean")
    print("4. Stats")
    print("5. Change pet")
    print("6. Exit")

def userChoice(text: str = "> ") -> str:
    return input(text)

def changePet():
    pass

choice = 0
pet = Pet()

while choice != 6:
    mainMenu()
    choice = int(userChoice("Please choose one of the options: "))

    if choice == 1:
        pet.feed()
    elif choice == 2:
        pet.play()
    elif choice == 3:
        pet.clean()
    elif choice == 4:
        pet.showStats()
    elif choice == 5:
        changePet()
    elif choice == 6:
        print("Closing...")
    else:
        print("There's no choice like that, try again")
