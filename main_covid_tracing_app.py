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
    
# import modules
import tkinter
from tkinter import messagebox, ttk
# import csv
import csv
# import class
from covid_form import covidForm
class mainMenu:
    # initialize the main menu
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
        titleLabel.pack(pady=45)
        # button for the form
        register_button = tkinter.Button(self.window, text="Open Form", bg="white", fg="black", command=self.openForm, width=30, height=2, font=("Century Gothic", 15))
        register_button.pack(pady=20)
        # search entry
        searchLabel=tkinter.Label(self.window, text="Search Function:", fg="black", bg="#8db5db", font=("Century Gothic", '9', "bold"))
        searchLabel.place(x=250, y=260)
        self.inputSearch = tkinter.Entry(self.window, width="40")
        self.inputSearch.pack(pady=20)
        # button for search
        searchButton=tkinter.Button(self.window, command=self.searchFunction, text="Search", bg="white", fg="black", width=8, height=1, font=("Century Gothic", 10))
        searchButton.place(x=260, y=310)
        
    # opens covid form
    def openForm(self):
        open=covidForm()
        open.run
        
    # runs main menu
    def runMain(self):
        
        self.window.mainloop()
    # search method
    def searchFunction(self):
        match = []
        record = {}
    # checks search input
        #use for searching for keywords in the search entry
        search = self.inputSearch.get().lower()
        print("Searching for:", search)

    # checks input
        if not search:
            messagebox.showerror("Data does not exist")
            return

# run the main menu
start=mainMenu()
start.runMain()