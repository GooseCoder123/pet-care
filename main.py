import datetime

def mainMenu() -> None:
    print("1. Feed")
    print("2. Play")
    print("3. Clean")
    print("4. Change pet")
    print("5. Exit")

def userChoice(text: str = "> ") -> str:
    return input(text)

def feed():
    pass

def clean():
    pass

def play():
    pass

def changePet():
    pass

choice = 0

while choice != 5:
    mainMenu()
    int(userChoice("Please choose one of the options"))
    
    if choice == 1:
        feed()
    elif choice == 2:
        play()
    elif choice == 3:
        clean()
    elif choice == 4:
        changePet()
    elif choice == 5:
        print("Closing...")
    else:
        print("There's no choice like that, try again")