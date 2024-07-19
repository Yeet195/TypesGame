<<<<<<< HEAD
import pokebase as pb
import random
import tkinter as tk
from PIL import ImageTk,Image
from variables import *

lower = lambda s: s[:1].lower() + s[1:] if s else ''

def type_multiplier(attack: str, defense: str) -> float:
    attack = lower(attack)
    defense = lower(defense)
    atk_type = pb.type_(attack)
    if defense in [t.name for t in atk_type.damage_relations.no_damage_to]:
        return 0.0
    elif defense in [t.name for t in atk_type.damage_relations.half_damage_to]:
        return 0.5
    elif defense in [t.name for t in atk_type.damage_relations.double_damage_to]:
        return 2.0
    else:
        return 1.0

def get_random(x: int, y: int) -> int:
    return random.randint(x, y)

def start_game():
    global button_result
    enable_all_buttons()
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
    
    button_result = tk.StringVar()

    for n in range(WEAKNESSCHART[z][y]):
        button_result.set("")
        window.wait_variable(button_result)
        answer = button_result.get()
        if type_multiplier(type_, answer) == i:
            score += 1
    message = '\n'

    return message, score, answer_count

def game(number_of_rounds: int):    
    max_score = 0
    total_score = 0

    for n in range(number_of_rounds):
        message, score, answer_count = start_game()
        total_score += score
        max_score += answer_count
    
    for button in buttons.values():
        button.config(state=tk.DISABLED)
    game_finished_text = f"You scored {total_score} out of {max_score} Points\nYou got {(total_score  / max_score) * 100:.0f}% correct answers"
    output.config(text=game_finished_text, anchor=tk.CENTER)

def button_click(element: str, button):
    button_result.set(element)
    button.config(state=tk.DISABLED)
    
def enable_all_buttons():
    for button in buttons.values():
        button.config(state=tk.NORMAL)

def start_game_gui():
    output.pack(anchor=tk.CENTER)
    num_of_rounds = get_num_of_rounds()
    
    if num_of_rounds is not None:
        start_game_button.config(state="disabled")
        create_type_button(TYPES)
        game(num_of_rounds)

def get_num_of_rounds():
    try:
        integer = int(entry.get())
        return integer
    except ValueError:
        return None

def create_type_button(x: str):
    global buttons  
    buttons.clear()  
    num_rows = (len(x) + 5) // 6

    for row in range(num_rows):
        frame = tk.Frame(window)
        frame.pack(side=tk.TOP, anchor=tk.CENTER)

        for idx in range(row * 6, min((row + 1) * 6, len(x))):
            button_text = x[idx]
            button = tk.Button(frame, text=button_text,
                               background=TYPECOLORS[idx],
                               foreground="black",
                               font=(FONT),
                               padx="5",
                               pady="5")
            button.pack(side=tk.LEFT)
            button.config(command=lambda e=button_text, b=button: button_click(e, b))
                     
            buttons[button_text] = button

window = tk.Tk()
window.geometry("1100x688")
window.title("Types")
window.configure(background='gray10')
window.iconbitmap("icon.ico")
window.resizable(height=False,width=False)

bg = "background.png"
img = ImageTk.PhotoImage(Image.open(bg))

bg_label = tk.Label(window, image = img)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

exit_button = tk.Button(window,
                        text="Quit",
                        command=window.destroy,
                        font=(FONT),
                        background='gray12',
                        foreground='white')
exit_button.pack(side="bottom",
                 anchor=tk.CENTER)

label = tk.Label(window,
                 text="Enter the number of rounds:",
                 background=BUTTON_BG,
                 foreground="white",
                 font=(FONT))
label.pack(anchor=tk.CENTER)

entry = tk.Entry(window,
                 background=BUTTON_BG, 
                 foreground="white", 
                 font=(FONT))
entry.pack()

start_game_button = tk.Button(window, 
                              text="Start Game", 
                              command=start_game_gui, 
                              background='gray12', 
                              foreground="white", 
                              font=(FONT))
start_game_button.pack()

output = tk.Label(window, text="", 
                  background=BUTTON_BG, 
                  foreground="white", 
                  font=(FONT))
output.pack(anchor=tk.CENTER)

window.mainloop()
=======
import pokebase as pb
import random
import tkinter as tk
import json
from datetime import datetime
import time
from PIL import ImageTk, Image
import vars

lower = lambda s: s[:1].lower() + s[1:] if s else ''

def type_multiplier(attack: str, defense: str) -> float:
    attack = lower(attack)
    defense = lower(defense)
    atk_type = pb.type_(attack)
    
    if defense in [t.name for t in atk_type.damage_relations.no_damage_to]:
        return 0.0
    elif defense in [t.name for t in atk_type.damage_relations.half_damage_to]:
        return 0.5
    elif defense in [t.name for t in atk_type.damage_relations.double_damage_to]:
        return 2.0
    else:
        return 1.0

def get_random(x: int, y: int) -> int:
    return random.randint(x, y)

class TypeGameGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1100x688")
        self.window.title("Types")
        self.window.configure(background='gray10')
        self.window.resizable(height=False, width=False)
        
        ico = Image.open("icon.ico")
        photo = ImageTk.PhotoImage(ico)
        self.window.wm_iconphoto(False, photo)
        
        bg = "background.png"
        self.img = ImageTk.PhotoImage(Image.open(bg))
        
        bg_label = tk.Label(self.window, image=self.img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.output = tk.Label(self.window, text="", background=vars.BUTTON_BG, foreground="white", font=(vars.FONT))
        self.output.pack(anchor=tk.CENTER)
        
        self.create_exit_button()
        self.create_round_input()
        self.create_start_button()
        
        self.button_result = tk.StringVar()
        self.num_of_rounds = 0
        
        self.window.mainloop()

    def create_exit_button(self):
        exit_button = tk.Button(
            self.window,
            text="Quit",
            command=self.window.destroy,
            font=(vars.FONT),
            background='gray12',
            foreground='white'
        )
        exit_button.pack(side="bottom", anchor=tk.CENTER)

    def create_round_input(self):
        self.label = tk.Label(
            self.window,
            text="Enter the number of rounds:",
            background=vars.BUTTON_BG,
            foreground="white",
            font=(vars.FONT)
        )
        self.label.pack(anchor=tk.CENTER)
        
        self.entry = tk.Entry(
            self.window,
            background=vars.BUTTON_BG,
            foreground="white",
            font=(vars.FONT)
        )
        self.entry.pack()

    def create_start_button(self):
        self.start_game_button = tk.Button(
            self.window,
            text="Start Game",
            command=self.start_game_gui,
            background='gray12',
            foreground="white",
            font=(vars.FONT)
        )
        self.start_game_button.pack()

    def start_game_gui(self):
        self.num_of_rounds = self.get_num_of_rounds()
        
        if self.num_of_rounds is not None:
            self.hide_round_input()
            self.create_type_button(vars.TYPES)
            self.game(self.num_of_rounds)
    
    def get_num_of_rounds(self):
        try:
            integer = int(self.entry.get())
            return integer
        except ValueError:
            return None
    
    def hide_round_input(self):
        self.label.pack_forget()
        self.entry.pack_forget()
        self.start_game_button.pack_forget()

    def create_type_button(self, types):
        vars.buttons.clear()
        num_rows = (len(types) + 5) // 6

        for row in range(num_rows):
            frame = tk.Frame(self.window)
            frame.pack(side=tk.TOP, anchor=tk.CENTER)

            for idx in range(row * 6, min((row + 1) * 6, len(types))):
                button_text = types[idx]

                button = tk.Button(
                    frame, text=button_text,
                    background=vars.TYPECOLORS[idx],
                    foreground="black",
                    font=(vars.FONT),
                    padx="5",
                    pady="5"
                )

                button.pack(side=tk.LEFT)
                button.config(command=lambda e=button_text, b=button: self.button_click(e, b))
                vars.buttons[button_text] = button
    
    def button_click(self, element: str, button):
        self.button_result.set(element)
        button.config(state=tk.DISABLED, bg="gray10")
    
    def enable_all_buttons(self):
        for button in vars.buttons.values():
            button.config(state=tk.NORMAL)
    
    def start_game(self):
        self.enable_all_buttons()
        
        z = get_random(0, 17)
        type_ = vars.TYPES[z]
        x = 2 if type_ in [
            "ghost",
            "electric",
            "fighting",
            "poison",
            "ground",
            "psychic",
            "dragon"
        ] else 1
        j = 1 if type_ == "normal" else 0
        y = get_random(j, x)
        answer_count = 0
        score = 0
        out_message = ""

        if y == 0:
            out_message += f"Name Types that are hit super effective by the {type_} type:\n"
            i = 2
            answer_count += vars.WEAKNESSCHART[z][y]
            out_message += f"There are {vars.WEAKNESSCHART[z][y]} Types hit super effective by the {type_} Type"
        
        elif y == 1:
            out_message += f"Name Types that are hit not very effective by the {type_} type:\n"
            i = 0.5
            answer_count += vars.WEAKNESSCHART[z][y]
            out_message += f"There are {vars.WEAKNESSCHART[z][y]} Types hit not very effective by the {type_} Type"
        
        elif y == 2:
            out_message += f"Name Types that are immune to the {type_} type:\n"
            i = 0
            answer_count += vars.WEAKNESSCHART[z][y]
            out_message += f"There are {vars.WEAKNESSCHART[z][y]} Types immune to the {type_} Type"

        self.output.config(text=out_message, anchor=tk.CENTER)
        self.button_result = tk.StringVar()

        for n in range(vars.WEAKNESSCHART[z][y]):
            self.button_result.set("")
            self.window.wait_variable(self.button_result)
            answer = self.button_result.get()
            if type_multiplier(type_, answer) == i:
                score += 1
                
        message = '\n'
        return message, score, answer_count

    def game(self, number_of_rounds: int):
        max_score = 0
        total_score = 0

        for n in range(number_of_rounds):
            message, score, answer_count = self.start_game()
            total_score += score
            max_score += answer_count
        
        for button in vars.buttons.values():
            button.config(state=tk.DISABLED)
        
        percent_correct = round((total_score  / max_score) * 100)
        game_finished_text = f"You scored {total_score} out of {max_score} Points\nYou got {percent_correct}% correct answers"
        self.output.config(text=game_finished_text, anchor=tk.CENTER)
        
        timestamp = str(datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M'))
        score = {
            "time": timestamp,
            "# of rounds": self.num_of_rounds,
            "total score": total_score,
            "max score": max_score,
            "% correct answers": percent_correct
        }
        
        try:
            with open("save.json", "r", encoding="UTF-8") as f:
                if f.read().strip() == "":
                    data = []
                else:
                    f.seek(0)
                    data = json.load(f)
        except FileNotFoundError:
            data = []
        
        if not isinstance(data, list):
            data = []
        
        data.append(score)
        
        with open("save.json", "w", encoding="UTF-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    TypeGameGUI()
>>>>>>> master
