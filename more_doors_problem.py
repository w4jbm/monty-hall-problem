#!/usr/bin/python3
#
# Monty Hall Problem with More Doors (more_doors_problem.py)
#
# A Python tool to explore possible outcomes by Jim McClanahan W4JBM
#
# The Original Scenario:
#
# "Suppose you're on a game show, and you're given the choice of three doors:
# Behind one door is a car; behind the others, goats. You pick a door, say
# No. 1, and the host, who knows what's behind the doors, opens another door,
# say No. 3, which has a goat. He then says to you, "Do you want to pick door
# No. 2?" Is it to your advantage to switch your choice?"
#
# But what if there are 4 doors? Or 5?
#
# You still pick a door, a remaining door is opened, to reveal a goat. Should
# you stay with your original pick or switch by picking one of the other
# closed doors?

import sys
import random
from tqdm.auto import tqdm

ROUNDS = 1000000
NUM_DOORS = 4 # A default value
VERBOSE = False

num_rounds = 0
num_stay = 0
num_switch = 0
num_nojoy = 0

# This function return a random number between i and j, but
# exclude any in list k
def random_exclude(start, stop, excluded):
    value = random.randint(start, stop-1)
    if value >= excluded:
        value += 1
    return(value)

# How many doors?
if(len(sys.argv)) == 1:
    print("The number of doors can be entered on the command line.")
else:
    NUM_DOORS = int(sys.argv[1])

# Do the realy work...
print("Monty Hall Puzzle with", NUM_DOORS, "doors.")

for i in tqdm(range(0, ROUNDS)):
    car_behind_door = random.randint(1, NUM_DOORS)

    # Our first choice, Door 1
    original_door = 1

    # Monty opens a door revealing a Goat
    open_door = random_exclude(2, NUM_DOORS, car_behind_door)

    # Our new choice, if we switch
    door_switch = random_exclude(2, NUM_DOORS, open_door)

    if VERBOSE:
        print("Picked door", original_door, "then Monty opened", open_door, "and we switch to", door_switch)
        if original_door == car_behind_door:
            print("STAY choice was right, car was behind door", car_behind_door)
        elif door_switch == car_behind_door:
            print("SWITCH choise was right, car was behind door", car_behind_door)
        else:
            print("NO JOY, neither STAY nor SWITCH wins, car was behind door", car_behind_door)
        print()

    num_rounds += 1
    if original_door == car_behind_door:
        num_stay += 1
    elif door_switch == car_behind_door:
        num_switch += 1
    else:
        num_nojoy += 1

print("Ran for",num_rounds,"rounds")
print("STAY won in",num_stay,"rounds or",100*num_stay/num_rounds,"percent")
print("SWITCH won in",num_switch,"rounds or",100*num_switch/num_rounds,"percent")
print("NEITHER won in",num_nojoy,"rounds or",100*num_nojoy/num_rounds,"percent")

print()
print("Calculated STAY win rate is",100*1/NUM_DOORS,"percent")
print("Calculated SWITCH win rate is",100* ((NUM_DOORS-1)/NUM_DOORS) * 1/(NUM_DOORS-2),"percent")
