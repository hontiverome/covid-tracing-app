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
        self.frame = tkinter.Frame(self.window)
        self.frame.pack(fill=tkinter.BOTH, expand=tkinter.YES)
        # create label for user first name
        self.label1 = tkinter.Label(self.frame, text="First Name", font=("Arial", 12))
    def run(self):
        self.window.mainloop()


test=covidForm()
test.run()