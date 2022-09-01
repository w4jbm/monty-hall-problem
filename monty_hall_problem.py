#!/usr/bin/python3
#
# Monty Hall Problem (monty_hall_problem.py)
#
# A Python tool to explore possible outcomes by Jim McClanahan W4JBM
#
# The Scenario:
#
# "Suppose you're on a game show, and you're given the choice of three doors:
# Behind one door is a car; behind the others, goats. You pick a door, say
# No. 1, and the host, who knows what's behind the doors, opens another door,
# say No. 3, which has a goat. He then says to you, "Do you want to pick door
# No. 2?" Is it to your advantage to switch your choice?"
#
# Originally posed (and solved) in a letter by Steve Selvin to the American
# Statistician in 1975. It became famous as a question from reader Craig F.
# Whitaker's letter quoted in Marilyn vos Savant's "Ask Marilyn" column in
# Parade magazine in 1990. (https://en.wikipedia.org/wiki/Monty_Hall_problem)

import random
from tqdm.auto import tqdm

ROUNDS = 100000
VERBOSE = False

num_rounds = 0
num_stay = 0
num_switch = 0

# This function return a random door for the car to be behind
def random_door(i,j):
    return(random.randint(1,3))

# Pick which door to show between 2 or 3 (but never show the car) when
# given the door number the car is behind
def goat_door(i):
    if i==1:
        return(random.randint(2,3))
    elif i == 2:
        return 3
    elif i == 3:
        return 2
    else:
        # We should never get here...
        print("Error!!! Cannot pick door to reveal!")
        return 0

# Start the real work...
for i in tqdm(range(0, ROUNDS)):
    car_behind_door = random_door(1,3)

    # Our first choice, Door 1
    original_door = 1

    # Monty opens a door revealing a Goat
    open_door = goat_door(car_behind_door)

    # Our new choice, if we switch
    if open_door == 2:
        door_switch = 3
    else:
        door_switch = 2

    if VERBOSE:
        print("Picked door", original_door, "then Monty opened", open_door, "and we could switch to", door_switch)
        if original_door == car_behind_door:
            print("STAY choice was right, car was behind door", car_behind_door)
        else:
            print("SWITCH choise was right, car was behind door", car_behind_door)
        print()

    num_rounds += 1
    if original_door == car_behind_door:
        num_stay += 1
    else:
        num_switch += 1

print("Ran for",num_rounds,"rounds")
print("STAY won in",num_stay,"rounds or",100*num_stay/num_rounds,"percent")
print("SWITCH won in",num_switch,"rounds or",100*num_switch/num_rounds,"percent")
