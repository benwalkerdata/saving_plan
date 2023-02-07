import random
import pandas

envelopes = []
full_envelopes = []
def new_envelopes():
    for i in range(1, 101):
        envelopes.append(i)
    with open("envelopes.txt", "w") as file:
        file.write(str(envelopes))
    with open("full_envelopes.txt", "w") as file:
        file.write(str(full_envelopes))
    print("Envelopes created")

def pick_envelope():
    todays_envelope = envelopes[random.randint(1,100)]
    print(f"This week's envelope is {todays_envelope}")
    full_envelopes.append(todays_envelope)
    envelopes.remove(todays_envelope)
    with open("envelopes.txt", "w") as file:
        file.write(str(envelopes))
    with open("full_envelopes.txt", "w") as file:
        file.write(str(full_envelopes))
def load_envelopes():
    with open("envelopes.txt", "r") as file:
        envelopes = file.read()
    with open("full_envelopes.txt", "r") as file:
        full_1envelopes = file.read()
    print("envelopes loaded.")
        
def list_full():
    print(full_envelopes)
    
def empty_envelopes():
    print(envelopes)
    
def total_saved():
    total = 0
    for i in full_envelopes:
        total += i
    print(f"So far you have saved £{total}")


running = True
while running == True:
    print("Hi welcome to the Enverlope saving app. \n\n")
    option = int(input("What would you like to do? (type 1-6) or type exit to quit. \n\n 1) Create new envelopes \n 2) Load previous envelopes \n 3) Pick this weeks envelope \n 4) List full envelopes\n 5) List empty envelopes \n 6) Display total saved \n"))
    if option == 1:
        new_envelopes()
    elif option == 2:
        load_envelopes()
    elif option == 3:
        pick_envelope()
    elif option == 4:
        list_full()
    elif option == 5:
        print(envelopes)
    elif option == 6:
        total_saved()
    elif option == "exit":
        running = False