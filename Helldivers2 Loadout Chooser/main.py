from functions import stratagem_chooser

print("[1] Stratagem")
print(" ")
initilize = input("What randomized loadout do you want?: ").lower().strip()

while initilize != "1" and initilize != "stratagem":
    print("INVALID")
    initilize = input("What randomized loadout do you want?: ").lower().strip()

if initilize == "1" or initilize == "stratagem":
    print(" ")
    stratagem_chooser.start()