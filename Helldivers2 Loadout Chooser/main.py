from functions import stratagem_chooser
from functions import booster_chooser

print("[1] Stratagem")
print("[2] Booster")
print(" ")
initilize = input("What randomized loadout do you want?: ").lower().strip()

while initilize != "1" and initilize != "stratagem" and initilize != "2" and initilize != "booster":
    print("INVALID")
    initilize = input("What randomized loadout do you want?: ").lower().strip()

if initilize == "1" or initilize == "stratagem":
    print(" ")
    stratagem_chooser.start_strats()

elif initilize == "2" or initilize == "booster":
	print(" ")
	booster_chooser.start_boost()