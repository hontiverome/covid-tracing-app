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
        titleLabel = tkinter.Label(self.window, text="COVID-19 TRACE APP", fg="black" , bg="white", font=("Century Gothic", 40))
        titleLabel.pack(pady=40)
        # button for the form
        register_button = tkinter.Button(self.window, text="Open Form", bg="white", fg="black", command=self.openForm, width=30, height=2, font=("Century Gothic", 15))
        register_button.pack(pady=20)
        # search entry
        inputSearch = tkinter.Entry(self.window, width="30")
        inputSearch.pack(pady=20)

        # button for search
    def openForm(self):
        open=covidForm()
        open.mainloop()
    def run(self):
        self.window.mainloop()

# run the main menu
start=mainMenu()
start.run()