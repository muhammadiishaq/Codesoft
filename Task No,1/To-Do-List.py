import customtkinter
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
app.title("To-Do List")
app.geometry("325x450")
app.config(bg='#09112e')

font1 = ('Arial', 30, 'bold')
font2 = ('Arial', 18, 'bold')
font3 = ('Arial', 10, 'bold')


def add_task():
    task = task_entry.get()
    if task:
        tasks_list.insert(0, task)
        task_entry.delete(0, END)
        save_tasks()
    else:
        messagebox.showerror('Error', 'Enter a task.')


def remove_task():
    selected = tasks_list.curselection()
    if selected:
        tasks_list.delete(selected[0])
        save_tasks()
    else:
        messagebox.showerror('Error', 'Choose a task to delete.')


def save_tasks():
    with open("tasks.txt", 'w') as f:
        tasks = tasks_list.get(0, END)
        for task in tasks:
            f.write(task + '\n')


def load_tasks():
    try:
        with open("tasks.txt", 'r') as f:  # Corrected file name here
            tasks = f.readlines()
            for task in tasks:
                tasks_list.insert(0, task.strip())
    except FileNotFoundError:
        pass
        # messagebox.showerror('Error', 'Cannot load tasks.')


title_label = customtkinter.CTkLabel(app, text="To-Do List", font=font1, text_color="#fff", bg_color="#09112e")
title_label.place(x=100, y=20)

add_button = customtkinter.CTkButton(app, text="Add Task", font=font2, text_color="#fff", bg_color="#06911f",
                                     hover_color="#06911f", command=add_task, cursor='hand2', corner_radius=5,
                                     width=120)
add_button.place(x=30, y=80)

remove_button = customtkinter.CTkButton(app, text='Remove Task', font=font2, text_color='#fff', bg_color='#96061c',
                                        hover_color='#96061c', cursor='hand2', corner_radius=5,command=remove_task)
remove_button.place(x=180, y=80)

task_entry = customtkinter.CTkEntry(app, font=font2, text_color='#000', fg_color='#fff', width=250)
task_entry.place(x=35, y=110)

tasks_list = Listbox(app, width=44, height=21, font=font3)
tasks_list.place(x=40, y=180)

load_tasks()

app.mainloop()