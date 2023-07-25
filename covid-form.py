# HONTIVEROS, JEROME ANDREI O.
# BSCPE 1-5
# covid form

# | FINAL PROJECT |

# pseudocode
# import modules
# create window
# create the gui for the covid form, which contains each user input regarding
    # user first name
    # user middle name
    # user last name
    # user age
    # user contact info
    # use birth date
    # user occupation 
    # user email
    # user address
    # vaccination status
    # symptoms status
    # contact person details
    
# import modules
import tkinter
from tkinter import messagebox, ttk
# import csv 
import csv
# create class for covid form gui
class covidForm:
    def __init__(self):
        # create window
        self.window = tkinter.Tk()
        # title
        self.window.title("COVID-19 FORM")
        # size
        self.window.geometry("800x600")
        # create frame
        self.frame = tkinter.Frame(self.window)
        self.frame.pack()
        self.frame_label = tkinter.LabelFrame(self.frame, text="Personal and Contact Information", font='Helvetica 12 bold')
        self.frame_label.grid (row=0, column=2, padx=15, pady=15)
        # create label and entry for user first name
        self.firstName_input = tkinter.Entry(self.frame_label)
        self.firstName_input.grid(row=1, column=0)
        firstName_label = tkinter.Label(self.frame_label, text="First Name", font='Courier 12')
        firstName_label.grid (row=0, column=0, padx=15)
        # create label for user middle name
        self.middleName_input = tkinter.Entry(self.frame_label)  
        self.middleName_input.grid(row=1, column=1)
        middleName_label = tkinter.Label(self.frame_label, text="Middle Name", font='Courier 12')
        middleName_label.grid (row=0, column=1, padx=15)
        # create label for user last name
        self.lastName_input = tkinter.Entry(self.frame_label)
        self.lastName_input.grid(row=1, column=2)
        lastName_label = tkinter.Label(self.frame_label, text="Last Name", font='Courier 12')
        lastName_label.grid (row=0, column=2, padx=15)
    def run(self):
        self.window.mainloop()


test=covidForm()
test.run()