
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font as tkfont
from tkinter import messagebox
from list import List
from settings import Setting


# Create database
data = List('events.db')
settingsData = Setting('settings.db')


# Database functions fot list
def updateList():
    eventList.delete(0, END)
    for row in data.getEvents(): 
        eventList.insert(END, (str(row[0]) + " Name: " + row[1] + "    Priority: " + str(row[2]) + "    Due: " + row[3]) )  


def addEvent():

    if (nameText.get() == '' or priorityText.get() == ''  or dueText.get()== '') :
        messagebox.showerror('Required Fields', 'Please include all fields. Make sure priority is a number.')
        return

    data.insert(nameText.get(), priorityText.get(), dueText.get())

    nameBox.delete(0, END)
    priorityBox.delete(0, END)
    dueBox.delete(0, END)

    priorityBox.insert(0, "0")

    updateList()

def removeEvent():

    index = eventList.curselection()[0]
    selected = eventList.get(index)
    
    data.remove(selected[0])
    
    updateList()
    

# Database functions for settings
def saveSetting():
    
    if (emailText.get() == '' or numberText.get() == '' ) :
        messagebox.showerror('Required Fields', 'Please include Email and Phone Number')
        return

    settingsData.insert(numberText.get(), emailText.get())

    emailBox.delete(0, END)
    phoneBox.delete(0, END)

    updateSettings()


def updateSettings():

    setEmailBox.delete(0, END)

    setNumberBox.delete(0, END)

    settingNames = settingsData.getNames()
    
    if not (settingNames):
        return

    setEmailBox.insert(END, settingNames[2])

    setNumberBox.insert(END, settingNames[1])

    

# Centers window
def centerWindow():
    
    x_cord = int((screen_width/2) - (width/2))
    y_cord = int((screen_height/2) - (height/2))
    root.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))


#Shows start page from home page
def HomeToStart():

    home.forget()
    start.pack(fill='both', expand=1)

#Shows home page from start page
def StartToHome():

    start.forget()
    home.pack(fill='both', expand=1)

#Shows start page from home page
def HomeToSettings():

    home.forget()
    settings.pack(fill='both', expand=1)

#Shows start page from home page
def SettingsToHome():

    settings.forget()
    home.pack(fill='both', expand=1)

#Shows add page from start page
def StartToAdd():

    start.forget()
    add.pack(fill='both', expand=1)

#Shows start page from add page
def AddToStart():

    add.forget()
    start.pack(fill='both', expand=1)

#Shows view page from start page
def StartToView():

    start.forget()
    view.pack(fill='both', expand=1)
    updateList()

#Shows start page from view page
def ViewToStart():

    view.forget()
    start.pack(fill='both', expand=1)



################################################
# Begin Window

root = Tk()

#Set title
root.title("To.Day - Productivity App")

#Sets the start height and width of the app
width, height = 600, 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
centerWindow()

#Configure Grid
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

###########################################
# Home Frame
###########################################

home = tk.Frame(root, bg= "grey")

head = tk.Label(home, text= "To.Day", fg= "white", bg= "grey", font= "Imprint 20 bold")

start = ttk.Button(home, text= 'Start', command=HomeToStart)

settingsButton = ttk.Button(home, text= 'Settings', command=HomeToSettings)

quit = ttk.Button(home, text="Quit", command=root.destroy)


#Configure Grid
head.grid(column=1, row=0)
start.grid(column=1, row=1)
settingsButton.grid(column=1, row=2)
quit.grid(column=1, row=3)


home.columnconfigure(0, weight=1)
home.columnconfigure(1, weight=1)
home.columnconfigure(2, weight=1)

home.rowconfigure(0, weight=5)
home.rowconfigure(1, weight=1)
home.rowconfigure(2, weight=1)
home.rowconfigure(3, weight=1)

home.pack(fill='both', expand=1)

###########################################
# Start Frame
###########################################

start = tk.Frame(root, bg= "grey")

viewListButton = tk.Button(start, text= 'View List',  padx=50, pady=20, command=StartToView)

addToListButton = tk.Button(start, text= 'Add to list', padx=50, pady=20, command=StartToAdd)

backHome = ttk.Button(start, text="Back", command=StartToHome)

#Configure Grid
viewListButton.grid(column=0, row=0)
addToListButton.grid(column=1, row=0)
backHome.grid(row=1, columnspan=2)

start.columnconfigure(0, weight=1)
start.columnconfigure(1, weight=1)

start.rowconfigure(0, weight=5)
start.rowconfigure(1, weight=1)

###########################################
# Settings Frame
###########################################

settings = tk.Frame(root)

emailText = StringVar()
email = tk.Label(settings, text="Add Email:")
emailBox = tk.Entry(settings, width=50, textvariable= emailText)


numberText = StringVar()
phone = tk.Label(settings, text="Phone Number(000-000-0000):")
phoneBox = tk.Entry(settings, width=50, textvariable= numberText)
  

phoneProvider = tk.Label(settings, text="Phone Provider:")
provider = Listbox(settings, selectmode=SINGLE)
provider.insert(1,"Verizon")
provider.insert(2,"AT&T")


backButton3 = ttk.Button(settings, text="Back", command= SettingsToHome)

saveSettings = ttk.Button(settings, text="Save Settings", command= saveSetting)


currentEmail = tk.Label(settings, text="Current Email:")
setEmailBox = tk.Entry(settings, width=50)

currentNumber = tk.Label(settings, text="Current Phone Number:")
setNumberBox = tk.Entry(settings, width=50)


#Configure Grid
email.grid(column=0, row=0)
emailBox.grid(column=1, row=0, sticky= "W")

phone.grid(column=0, row=1)
phoneBox.grid(column=1, row=1, sticky= "W")

phoneProvider.grid(columnspan= 2, row=2, sticky= "S")
provider.grid(columnspan= 2, row=3, sticky= "N")


backButton3.grid(column= 0, row=6)
saveSettings.grid(column= 1, row=6)


currentEmail.grid(column= 0, row=4)
setEmailBox.grid(column= 1, row=4, sticky= "W")

currentNumber.grid(column= 0, row=5)
setNumberBox.grid(column= 1, row=5, sticky= "W")

settings.columnconfigure(0, weight=1)
settings.columnconfigure(1, weight=1)

settings.rowconfigure(0, weight=1)
settings.rowconfigure(1, weight=1)
settings.rowconfigure(2, weight=1)
settings.rowconfigure(3, weight=1)
settings.rowconfigure(4, weight=1)
settings.rowconfigure(5, weight=1)
settings.rowconfigure(6, weight=1)


updateSettings()

###########################################
# Add Frame
###########################################

add = tk.Frame(root)

name = tk.Label(add, text= "Event Name", fg= "black", font= "Imprint 12")
nameDesc = tk.Label(add, text= "(enter name for event)", fg= "grey", font= "Imprint 8")

priority = tk.Label(add, text= "Priority", fg= "black", font= "Imprint 12")
priorityDesc = tk.Label(add, text= "(enter numbers only for priority)", fg= "grey", font= "Imprint 8")


due = tk.Label(add, text= "Due", fg= "black", font= "Imprint 12")
dueDesc = tk.Label(add, text= "(6-12-22, tommorrow, monday, ect.)", fg= "grey", font= "Imprint 8")


addButton = ttk.Button(add, text="Add", command=addEvent)

backButton1 = ttk.Button(add, text="Back", command=AddToStart)


nameText = StringVar()
nameBox = ttk.Entry(add, width=50, textvariable=nameText)

priorityText = IntVar()
priorityBox = ttk.Entry(add, width=50, textvariable=priorityText)

dueText = StringVar()
dueBox = ttk.Entry(add, width=50, textvariable=dueText)


#Configure Grid
name.grid(column=0, row=0, sticky= "S")
nameBox.grid(column=1, row=0, sticky= "SW")
nameDesc.grid(column=1, row=1, sticky= "NW")

priority.grid(column=0, row=2, sticky= "S")
priorityBox.grid(column=1, row=2, sticky= "SW")
priorityDesc.grid(column=1, row=3, sticky= "NW")

due.grid(column=0, row=4, sticky= "S")
dueBox.grid(column=1, row=4, sticky= "SW")
dueDesc.grid(column=1, row=5, sticky= "NW")

addButton.grid(column=1, row=6)
backButton1.grid(column=0, row=6)



add.columnconfigure(0, weight=2)
add.columnconfigure(1, weight=1)

add.rowconfigure(0, weight=1)
add.rowconfigure(1, weight=1)
add.rowconfigure(2, weight=1)
add.rowconfigure(3, weight=1)
add.rowconfigure(4, weight=1)
add.rowconfigure(5, weight=1)
add.rowconfigure(6, weight=1)


###########################################
# View Frame
###########################################

view = tk.Frame(root)

eventList = tk.Listbox(view, font= "Imprint 12", height=10)     #, width=50

scrollbarList = tk.Scrollbar(view, orient="vertical")

backButton2 = ttk.Button(view, text="Back", command=ViewToStart)

removeButton = ttk.Button(view, text="Remove", command=removeEvent)

eventList.config(yscrollcommand= scrollbarList.set)
scrollbarList.config(command= eventList.yview)


#Configure Grid
eventList.grid(columnspan=2, row=0, sticky= "N, E, W, S")
scrollbarList.grid(column=3, row=0, sticky= "N, S")
backButton2.grid(column=0, row=1)
removeButton.grid(column=1, row=1)

view.columnconfigure(0, weight=1)
view.columnconfigure(1, weight=1)

view.rowconfigure(0, weight=1)
view.rowconfigure(1, weight=1)


# add list to listbox
updateList()


###########################################
# temp Frame
###########################################



###########################################
# temp Frame
###########################################

root.mainloop()
