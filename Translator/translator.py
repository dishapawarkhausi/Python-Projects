from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    try:
        trans = Translator()
        trans1 = trans.translate(text, src=src.lower(), dest=dest.lower())
        return trans1.text
    except Exception as e:
        return f"Error: {str(e)}"

def data():
    s = comb_source.get()
    d = comb_dest.get()
    masg = Source_txt.get(1.0, END).strip()
    
    if not masg:
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, "Please enter text to translate.")
        return
    
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='blue')

lab_title = Label(root, text="Translator", font=("Times New Roman", 40, "bold"), bg='blue', fg='white')
lab_title.place(x=100, y=40, height=50, width=300)

lab_src = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), fg='Black', bg="blue")
lab_src.place(x=100, y=100, height=30, width=300)

Source_txt = Text(root, font=("Times New Roman", 14), wrap=WORD)
Source_txt.place(x=10, y=140, height=150, width=480)

list_text = list(LANGUAGES.values())
comb_source = ttk.Combobox(root, value=list_text, state="readonly", font=("Times New Roman", 12))
comb_source.place(x=10, y=310, height=40, width=190)
comb_source.set("english")

button_change = Button(root, text="Translate", relief=RAISED, font=("Times New Roman", 14, "bold"), bg="white", command=data)
button_change.place(x=200, y=310, height=40, width=100)

comb_dest = ttk.Combobox(root, value=list_text, state="readonly", font=("Times New Roman", 12))
comb_dest.place(x=300, y=310, height=40, width=190)
comb_dest.set("hindi")

lab_dest = Label(root, text="Destination Text", font=("Times New Roman", 20, "bold"), fg='Black', bg="blue")
lab_dest.place(x=100, y=360, height=30, width=300)

dest_txt = Text(root, font=("Times New Roman", 14), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)

root.mainloop()
