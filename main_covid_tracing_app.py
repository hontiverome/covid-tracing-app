# HONTIVEROS, JEROME ANDREI O.
# BSCPE 1-5
# main menu

# | FINAL PROJECT |

# pseudocode
# import modules
# import class
# create window
# create the gui for the main menu
    # button for the form
    # search entry
    
# import modules
import tkinter
from tkinter import messagebox, ttk
# import class
from covid_form import covidForm
class mainMenu:
    def __init__(self):
        self.window = tkinter.Tk()
        # title
        self.window.title("COVID-19 Contact Tracing App")
        # size
        self.window.geometry("600x400")
        # color
        self.window.configure(bg='#8db5db')
        # label
        titleLabel = tkinter.Label(self.window, text="COVID-19 TRACE APP", fg="white" , bg="grey", font=("Century Gothic", 30))
        titleLabel.pack(pady=60)  