# import the required modules in the file 
from tkinter import *
from tkinter import messagebox

# fucntion to add a new task in the list where we show all the task 
def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

# function to delete the task from the list 
def deleteTask():
    lb.delete(ANCHOR)
    
# user window where user can see all the things     
ws = Tk()
ws.geometry('500x450+500+200') #size of the window screen
ws.title('To do list') #title of the project
ws.config(bg='#223441') #color of the window
ws.resizable(width=False, height=False) #if we can changee the size of the window

frame = Frame(ws) #dialogue box where all the things in to do list will appear
frame.pack(pady=10) 

#here we have give the required details such as padding font color, selected color which shows up when we select the line, height width of there line etc.
lb = Listbox( #lines present in the box 
    frame,
    width=25,
    height=8,
    font=('Poppins', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)

#here we are going to place all the content on the left side of the screen
lb.pack(side=LEFT, fill=BOTH)

task_list = [ #some of the task that are being assinged from initial stage
    'Eat apple',
    'drink water',
    'go gym',
    'write software',
    'write documentation',
    'take a nap',
    'Learn something',
    'paint canvas'
    ]

#add new task
for item in task_list:
    lb.insert(END, item)

#scrool bar to see al the available task
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

#display where we can enter new task
my_entry = Entry(
    ws,
    font=('times', 24)
)

my_entry.pack(pady=20)

#buttons that will be used by us
button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button( #button to add new task
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT) #giving side to button

delTask_btn = Button( #button to delete task
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT) #side to button

ws.mainloop()