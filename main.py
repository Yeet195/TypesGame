import pokebase as pb
import random
import tkinter as tk
from variables import *

font = "Fixedsys", 20

# Get multiplyers for types
def type_multiplier(attack: str, defense: str) -> float:
    atk_type = pb.type_(attack)
    if defense in [t.name for t in atk_type.damage_relations.no_damage_to]:
        return 0.0
    elif defense in [t.name for t in atk_type.damage_relations.half_damage_to]:
        return 0.5
    elif defense in [t.name for t in atk_type.damage_relations.double_damage_to]:
        return 2.0
    else:
        return 1.0
    
# Generate random numbers
def get_random(x: int,y: int) -> int:
    return random.randint(x, y)

def start_game():
    global button_result
    # Get the type to ask for multipliers and apply special modifiers depending on the type selected 
    z = get_random(0, 17)
    type_ = TYPES[z]
    x = 2 if type_ in ["ghost", "electric", "fighting", "poison", "ground", "psychic", "dragon"] else 1
    j = 1 if type_ == "normal" else 0
    y = get_random(j, x)
    answer_count = 0
    score = 0
    out_message = ""
    
    if y == 0:
        out_message += f"Name Types that are hit super effective by the {type_} type:\n"
        i = 2
        answer_count += WEAKNESSCHART[z][y]
        out_message += f"There are {WEAKNESSCHART[z][y]} Types hit super effective by the {type_} Type"
        
    elif y == 1:
        out_message += f"Name Types that are hit not very effective by the {type_} type:\n"
        i = 0.5
        answer_count += WEAKNESSCHART[z][y]
        out_message += f"There are {WEAKNESSCHART[z][y]} Types hit not very effective by the {type_} Type"
        
    elif y == 2:
        out_message += f"Name Types that are immune to the {type_} type:\n"
        i = 0
        answer_count += WEAKNESSCHART[z][y]
        out_message += f"There are {WEAKNESSCHART[z][y]} Types immune to the {type_} Type"

    output.config(text=out_message, anchor=tk.CENTER)
    
    
    button_result= tk.StringVar()
# Prompt for Answers 
    for n in range(WEAKNESSCHART[z][y]):
        button_result.set("")
        window.wait_variable(button_result)
        answer = button_result.get()
        
        if type_multiplier(type_, answer) == i:
            score += 1
    message = '\n'
    return message, score, answer_count


# Initiate game
def game(number_of_rounds):    
    max_score = 0
    total_score = 0

    for n in range(number_of_rounds):
        message, score, answer_count = start_game()
        total_score += score
        max_score += answer_count
    game_finished_text = f"you scored {total_score} out of {max_score} Points\nYou got {(total_score  / max_score) * 100:.0f}% correct answers"
    output.config(text=game_finished_text, anchor=tk.CENTER)

def button_click(element):
    button_result.set(element)

def start_game_gui():
    output.pack(anchor=tk.CENTER)  # Pack the output label in the top-left corner
    start_game_button.config(state="disabled")
    num_of_rounds = get_num_of_rounds()
    if num_of_rounds is not None:
        create_type_button(TYPES)
        
        game(num_of_rounds)

def get_num_of_rounds():
    try:
        integer = int(entry.get())
        return integer
    except ValueError:
        return None

def create_type_button(x):
    # Calculate number of rows needed
    num_rows = (len(x) + 5) // 6

    for row in range(num_rows):
        # Create a frame for each row of buttons
        frame = tk.Frame(window)
        frame.pack(side=tk.TOP, anchor=tk.CENTER)

        # Create buttons for each type in the row
        for idx in range(row * 6, min((row + 1) * 6, len(x))):
            button_text = x[idx]
            button = tk.Button(frame, text=button_text, 
                               command=lambda e=button_text: button_click(e), 
                               background=TYPECOLORS[idx], 
                               foreground="black", 
                               font=(font),
                               padx="5",
                               pady="5")
            button.pack(side=tk.LEFT)


window = tk.Tk()
window.geometry("1100x600")
window.title("Types")
window.configure(background='gray10')

exit_button = tk.Button(window,
                        text="Quit",
                        command=window.destroy,
                        font=(font), background='gray12',
                        foreground='white')
exit_button.pack(side="bottom",
                 anchor=tk.CENTER)


label = tk.Label(window,
                 text="Enter the number of rounds:",
                 background='gray10',
                 foreground="white",
                 font=(font))
label.pack(anchor=tk.CENTER)

entry = tk.Entry(window,
                 background='gray12', 
                 foreground="white", 
                 font=(font))
entry.pack()

start_game_button = tk.Button(window, 
                              text="Start Game", 
                              command=start_game_gui, 
                              background='gray12', 
                              foreground="white", 
                              font=(font))
start_game_button.pack()

output = tk.Label(window, text="", 
                  background='gray10', 
                  foreground="white", 
                  font=(font))
output.pack(anchor=tk.CENTER)  # Initialize the output label, but keep it hidden initially

window.mainloop()