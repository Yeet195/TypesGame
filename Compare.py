import pokebase as pb
import random
from Types import *

# Generate random numbers
def get_random(x: int,y: int) -> int:
    return random.randint(x, y)

def start_game():

# Get the type to ask for multiplyers and apply special modifiers depending on the type selected 
    z = get_random(0, 17)
    
    type_ = TYPES[z]
    
    x = 2 if type_ in ["ghost", "electric", "fighting", "poison", "ground", "psychic", "dragon"] else 1

    j = 1 if type_ == "normal" else 0
    
    y = get_random(j, x)
    answer_count = 0
    score = 0
    
    if y == 0:
        print(f"Name Types that are hit super effective by the {type_} type:")
        i = 2
        answer_count += WEAKNESSCHART[z][y]
        print(f"There are {WEAKNESSCHART[z][y]} Types hit super effective by the {type_} Type")    
    elif y == 1:
        print(f"Name Types that are hit not very effective by the {type_} type:")
        i = 0.5
        answer_count += WEAKNESSCHART[z][y]
        print(f"There are {WEAKNESSCHART[z][y]} Types hit not very effective by the {type_} Type")   
    elif y == 2:
        print(f"Name Types that are immune to the {type_} type:")
        i = 0
        answer_count += WEAKNESSCHART[z][y]
        print(f"There are {WEAKNESSCHART[z][y]} Types immune to the {type_} Type")


# Prompt for Answers 
    for n in range(WEAKNESSCHART[z][y]):
        answer = input("")
        print(WEAKNESSCHART[z][y] , " " , answer_count)
        if type_multiplier(type_, answer) == i:
            score += 1
    message = '\n'
    return message, score, answer_count