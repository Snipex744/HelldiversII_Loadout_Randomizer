import random

boosters = ["Hellpod Space Optimization", "Vitality Enhancement", "UAV Recon Booster", "Stamina Enhancement", "Muscle Enhancement", "Increased Reinforcement Budget", "Flexible Reinforcement Budget", "Armed Resupply Pods"]

def choose_one_boost():
    if boosters:
      chosen_booster = random.choice(boosters)
      print(chosen_booster)
      boosters.remove(chosen_booster)

def start_boost():
  for _ in range(1):
    choose_one_boost()
    print(" ")
  question = input("Reroll?(Y/N): ").lower().strip()
  
  while question != "y" and question != "yes" and question != "n" and question != "no":
    print("INVALID")
    print(" ")
    question = input("Reroll?(Y/N): ").lower().strip()
  
  while question == "y" or question == "yes":
    print(" ")
    for _ in range(1):
      choose_one_boost()
      print(" ")
    question = input("Reroll?(Y/N): ").lower().strip()
  if question == "n" or question == "no":
    print(" ")
    print("Good luck Helldiver!")