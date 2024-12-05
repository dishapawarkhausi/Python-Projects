import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

root = tk.Tk()
root.title("To-Do List")

# Input Field
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Task List
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

root.mainloop()
