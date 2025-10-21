import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="],
]

right_symbols = ["÷", "x", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

A = "0"
B = None
operator = None

def clear_all():
    global A, B, operator
    A = "0"
    B = None
    operator = None
    label["text"] = "0"

def remove_zero_decimal(num):
    if isinstance(num, str):
        return num
    if num % 1 == 0:
        num = int(num)
    return str(num)

def button_clicked(value):
    global A, B, operator

    if value in right_symbols:
        if value == "=":
            if operator and A is not None:
                B = label["text"]
                try:
                    a = float(A)
                    b = float(B)
                    if operator == "+":
                        result = a + b
                    elif operator == "-":
                        result = a - b
                    elif operator == "x":
                        result = a * b
                    elif operator == "÷":
                        result = a / b if b != 0 else "Error"

                    label["text"] = remove_zero_decimal(result) if result != "Error" else result
                    operator = None
                except Exception:
                    label["text"] = "Error"

        elif value in "+-x÷":
            A = label["text"]
            operator = value
            label["text"] = "0"

    elif value in top_symbols:
        if value == "AC":
            clear_all()
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)

    elif value == "√":
        result = float(label["text"]) ** 0.5
        label["text"] = remove_zero_decimal(result)

    else:
        if value == ".":
            if "." not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value

# Window setup
window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(
    frame, text="0", font=("Arial", 45),
    background=color_black, foreground=color_white,
    anchor="e", width=len(button_values[0])
)
label.grid(row=0, column=0, columnspan=len(button_values[0]), sticky="we")

for row in range(len(button_values)):
    for column in range(len(button_values[row])):
        value = button_values[row][column]
        button = tkinter.Button(
            frame, text=value, font=("Arial", 30),
            width=len(button_values[0])-1, height=1,
            command=lambda value=value: button_clicked(value)
        )
        if value in top_symbols:
            button.config(foreground=color_black, background=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_dark_gray)
        button.grid(row=row+1, column=column)

frame.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()