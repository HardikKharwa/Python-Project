from tkinter import *
from tkinter import messagebox


# Function to add a task to the Listbox
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(END, task)
        entry_task.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "You must enter a task.")


# Function to delete a selected task from the Listbox
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task.")


# Function to mark a task as completed
def mark_completed():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(END, task + " - Completed")
    except:
        messagebox.showwarning("Warning", "You must select a task.")


# Create the main window
window = Tk()
window.title("To-Do List")

# Create a Frame for the Listbox and Scrollbar
frame_tasks = Frame(window)
frame_tasks.pack()

# Create a Listbox
listbox_tasks = Listbox(
    frame_tasks, bg="black", fg="white", height=15, width=50, font="helvetica"
)
listbox_tasks.pack(side=LEFT)

# Create a Scrollbar and attach it to the Listbox
scrollbar_tasks = Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=RIGHT, fill=Y)
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Create an Entry widget for new tasks
entry_task = Entry(window, width=50)
entry_task.pack(pady=10)

# Create Buttons for adding, deleting, and marking tasks as completed
button_add_task = Button(window, text="Add Task", width=20, command=add_task)
button_add_task.pack(pady=5)

button_delete_task = Button(window, text="Delete Task", width=20, command=delete_task)
button_delete_task.pack(pady=5)

button_mark_completed = Button(
    window, text="Mark as Completed", width=20, command=mark_completed
)
button_mark_completed.pack(pady=5)

# Run the main loop
window.mainloop()
