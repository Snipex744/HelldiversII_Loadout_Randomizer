import random

stratagems = ["MG-43 Machine Gun", "APW-1 Anti-Material Rifle", "M-105 Stalwart", "EAT-17 Expendable Anti-Tank", "GR-8 Recoilless Rifle", "FLAM-40 Flamethrower", "AC-8 Autocannon", "MG-206 Heavy Machine Gun", "RL-77 Airburst Rocket Launcher", "MLS-4X Commando", "RS-422 Railgun", "FAF-14 Spear", "StA-X3 W.A.S.P. Launcher", "Orbital Gatling Barrage", "Orbital Airburst Strike", "Orbital 120mm HE Barrage", "Orbital 380mm HE Barrage", "Orbital Walking Barrage", "Orbital Laser", "Orbital Napalm Barrage", "Orbital Railcannon Strike", "Eagle Strafing Run", "Eagle Airstrike", "Eagle Cluster Bomb", "Eagle Napalm Airstrike", "LIFT-850 Jump Pack", "Eagle Smoke Strike", "Eagle 110mm Rocket Pods", "Eagle 500kg Bomb", "M-102 Fast Recon Vehicle", "Orbital Precision Strike", "Orbital Gas Strike", "Orbital EMS Strike", "Orbital Smoke Strike", "E/MG-101 HMG Emplacement", "FX-12 Shield Generator Relay", "A/ARC-3 Tesla Tower", "MD-6 Anti-Personnel Minefield","B-1 Supply Pack", "GL-21 Grenade Launcher", "LAS-98 Laser Cannon", "MD-I4 Incendiary Mines", "AX/LAS-5 Guard Dog Rover", "SH-20 Ballistic Shield Backpack", "ARC-3 Arc Thrower", "MD-17 Anti-Tank Mines", "LAS-99 Quasar Cannon", "SH-32 Shield Generator Pack", "MD-8 Gas Mines", "A/MG-43 Machine Gun Sentry", "A/G-16 Gatling Sentry", "A/M-12 Mortar Sentry", "AX/AR-23 Guard Dog", "A/AC-8 Autocannon Sentry", "A/MLS-4X Rocket Sentry", "A/M-23 EMS Mortar Sentry", "EXO-45 Patriot Exosuit", "EXO-49 Emancipator Exosuit", "SH-51 Directional Shield", "E/AT-12 Anti-Tank Emplacement", "A/FLAM-40 Flame Sentry"]

def choose_four():
    if stratagems:
      chosen_stratagems = random.choice(stratagems)
      print(chosen_stratagems)
      stratagems.remove(chosen_stratagems)

def start():
  for _ in range(4):
    choose_four()
    print(" ")
  question = input("Reroll?(Y/N): ").lower().strip()
  
  while question != "y" and question != "yes" and question != "n" and question != "no":
    print("INVALID")
    print(" ")
    question = input("Reroll?(Y/N): ").lower().strip()
  
  while question == "y" or question == "yes":
    print(" ")
    for _ in range(4):
      choose_four()
      print(" ")
    question = input("Reroll?(Y/N): ").lower().strip()
  if question == "n" or question == "no":
    print(" ")
    print("Good luck Helldiver!")