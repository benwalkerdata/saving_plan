import random


ENVELOPES = []
FULL_ENVELOPES = []
def new_envelopes():
    for i in range(1, 101):
        ENVELOPES.append(i)
    with open("envelopes.txt", "w") as file:
        file.write(str(ENVELOPES))
    with open("full_envelopes.txt", "w") as file:
        file.write(str(FULL_ENVELOPES))
    print("Envelopes created")

def pick_envelope():
    todays_envelope = ENVELOPES[random.randint(1,100)]
    print(f"This week's envelope is {todays_envelope}")
    FULL_ENVELOPES.append(todays_envelope)
    ENVELOPES.remove(todays_envelope)
    with open("envelopes.txt", "w") as file:
        file.write(str(ENVELOPES))
    with open("full_envelopes.txt", "w") as file:
        file.write(str(FULL_ENVELOPES))
        
def load_envelopes():
    with open("envelopes.txt", "r") as file:
        envelopes = file.read()
    return envelopes
    
def load_fullenvelopes():
    with open("full_envelopes.txt", "r") as file:
        full_envelopes = file.read()
    return full_envelopes
    
def list_full():
    print(f"{FULL_ENVELOPES} \n")
    
def empty_envelopes():
    print(f"{ENVELOPES} \n")
    
def total_saved():
    total = 0
    for i in FULL_ENVELOPES:
        total += i
    print(f"So far you have saved £{total}")


running = True
while running == True:
    print("Hi welcome to the Enverlope saving app. \n\n")
    option = int(input("What would you like to do? (type 1-6) or type 0 to quit. \n\n 1) Create new envelopes \n 2) Load previous envelopes \n 3) Pick this weeks envelope \n 4) List full envelopes\n 5) List empty envelopes \n 6) Display total saved \n 0) to quit. \n"))
    if option == 1:
        new_envelopes()
    elif option == 2:
        ENVELOPES = load_envelopes()
        FULL_ENVELOPES = load_fullenvelopes()
        print(ENVELOPES)
        print(FULL_ENVELOPES)
        print("Envelopes loaded")
    elif option == 3:
        pick_envelope()
    elif option == 4:
        list_full()
    elif option == 5:
        print(ENVELOPES)
    elif option == 6:
        total_saved()
    elif option == 0:
        running = False