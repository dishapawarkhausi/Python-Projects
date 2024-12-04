import tkinter as tk

# root = tk.Tk()
# root.title("My Tkinter App")

# label = tk.Label(root, text="Hello, Tkinter!")
# label.pack()

# root.mainloop()

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END) 

def button_equal():
    try: 
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")           

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, borderwidth=5, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10)

button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*", 
    "1", "2", "3", "-", 
    "C", "0", "=", "+"
]

row = 1
col = 0

for text in button_texts:
    if text == "C":
        button = tk.Button(root, text = text, padx=20, pady=20, command=button_clear)
    elif text == "=":
        button = tk.Button(root, text=text, padx=20, pady=20, command=button_equal)
    else: 
        button = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: button_click(t))


    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()                    