import os
from Compare import *

# Set up clear function
name = "clear" if os.name == "posix" else "cls"
clear = lambda: os.system(name)

# Initiate game
def game():    
    max_score = 0
    total_score = 0

    x = int(input("How many rounds do you want to play\nEnter to confirm\n"))
    #clear()
    for n in range(x):
        message, score, answer_count = start_game()
        total_score += score
        max_score += answer_count
        #clear()
    print(total_score, " ", max_score)
    return f"you scored {total_score} out of {max_score} Points\nYou got {(total_score  / max_score) * 100:.0f}% correct answers"

if __name__ == "__main__":
    print(game())
    input("Press Enter to exit...")