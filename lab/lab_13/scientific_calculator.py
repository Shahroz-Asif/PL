import tkinter
import math

window = tkinter.Tk()
window.title("Scientific Calculator")
window.minsize(250, 400)
window.maxsize(250, 400)

title_label = tkinter.Label(window, text="SCIENTIFIC CALCULATOR", font=("Roboto", 12), bg="#66ff99", pady=10)
title_label.pack(fill="both", padx=15, pady=(20, 0))

interface = tkinter.Frame(window)
interface.pack(fill="both", padx=15, pady=15)

input_a = tkinter.StringVar(value="0")
input_b = tkinter.StringVar(value="0")
display_value = tkinter.StringVar(value="0")

calculation_methods = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "×": lambda a, b: a * b,
    "÷": lambda a, b: a / b,
    "sin": lambda a: math.sin(a),
    "cos": lambda a: math.cos(a),
    "tan": lambda a: math.tan(a),
    "log": lambda a, b: math.log(a, base=b),
    "exp": lambda a, b: a ** b,
    "root": lambda a, b: a ** (1 / b)
}

def get_display_text(operator, operands, result):
    if operands == 2:
        return  "{inp_a} {operator} {inp_b} = {result}".format(
            inp_a=input_a.get(),
            operator=operator,
            inp_b=input_b.get(),
            result=str(result)
        )
    else:
        return "{operator} {inp_a} = {result}".format(
            operator=operator,
            inp_a=input_a.get(),
            result=str(result)
        )

def calculate(operator, operands):
    value_a = int(input_a.get() or 0)
    value_b = int(input_b.get() or 0)
    result = 0

    try:
        result = calculation_methods[operator](value_a, value_b) if operands == 2 else calculation_methods[operator](value_a)
    except:
        result = "UNDEFINED"

    display_value.set(get_display_text(operator, operands, result))

calculation_buttons = [
    {
        "buttons": [ [ ["sin",1], ["cos",1], ["tan",1] ], [ ["log", 2], ["exp", 2], ["root", 2] ] ],
        "style": { "width": 5, "height": 2, "font": ("Arial", 8), "pady": 0, "bg": "#993333" },
        "placement": {
            "columnspan": 2
        }
    },
    {
        "buttons": [ [ ["+", 2], ["-", 2] ], [ ["×", 2], ["÷", 2] ] ],
        "style": { "width": 2, "bg": "#ffcc66" },
        "placement": {
            "columnspan": 3
        }
    }
]

interface.grid_columnconfigure(0, weight=1)
interface.grid_columnconfigure(1, weight=1)
interface.grid_columnconfigure(2, weight=1)
interface.grid_columnconfigure(3, weight=1)
interface.grid_columnconfigure(4, weight=1)
interface.grid_columnconfigure(5, weight=1)

display_label = tkinter.Label(interface, textvariable=display_value, bg="#99ccff", padx=20, pady=20, width=20, height=3, font=("Montserrat", 14), wraplength=200)
display_label.grid(row=0, column=0, columnspan=6, pady=(0, 20))

entry_a = tkinter.Entry(interface, textvariable=input_a, width=10)
entry_a.grid(row=1, column=0, columnspan=3, pady=(0, 20))

entry_b = tkinter.Entry(interface, textvariable=input_b, width=10)
entry_b.grid(row=1, column=3, columnspan=3, pady=(0, 20))

def generate_button(label, operands, styleset):
    button_action = lambda: calculate(label, operands)
    button_widget = tkinter.Button(interface, text=label, command=button_action, **styleset)

    return button_widget

row = 2
for button_set in calculation_buttons:
    for button_row in button_set["buttons"]:
        column = 0
        for [ button_label, button_operands ] in button_row:
            button_widget = generate_button(label=button_label, operands=button_operands, styleset=button_set["style"])
            button_widget.grid(row=row, column=column, **button_set["placement"])

            column = column + button_set["placement"]["columnspan"]
        
        row = row + 1

window.mainloop()