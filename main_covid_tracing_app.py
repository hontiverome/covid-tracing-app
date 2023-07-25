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
        titleLabel.pack(pady=45)
        # button for the form
        register_button = tkinter.Button(self.window, text="Open Form", bg="white", fg="black", command=self.openForm, width=30, height=2, font=("Century Gothic", 15))
        register_button.pack(pady=20)
        # search entry
        searchLabel=tkinter.Label(self.window, text="Search Function:", fg="black", bg="#8db5db", font=("Century Gothic", '9', "bold"))
        searchLabel.place(x=250, y=260)
        inputSearch = tkinter.Entry(self.window, width="40")
        inputSearch.pack(pady=20)
        # button for search
        searchButton=tkinter.Button(self.window, command=self.search_engine, text="Search", bg="white", fg="black", width=8, height=1, font=("Century Gothic", 10))
        searchButton.place(x=260, y=310)
    # opens covid form
    def openForm(self):
        open=covidForm()
        open.mainloop()
    # runs main menu
    def run(self):
        self.window.mainloop()
    # search method
    def search_engine(self):
    # Create an Object for the variables
        access=covidForm()
        search = None
    # Determine the search value
        if access.firstName_input():
            search = access.firstName_input.get().lower()
        elif access.middleName_input():
            search = access.middleName_input.get().lower()
        elif access.lastName_input():
            search = access.lastName_input.get().lower()
        elif access.age_input():
            search = access.age_input.get().lower()
        elif access.gender_input():
            search = access.gender_input.get().lower()
        elif access.birthDate_input():
            search = access.birthDate_input.get().lower()
        elif access.occupation_input():
            search = access.occupation_input.get().lower()
        elif access.address_input():
            search = access.address_input.get().lower()
        elif access.email_input():
            search = access.email_input.get().lower()

# run the main menu
start=mainMenu()
start.run()