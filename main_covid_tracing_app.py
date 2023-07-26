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
        search = self.inputSearch.get().lower()
        print("Searching for:", search)

    # checks input
        if not search:
            messagebox.showerror("Data does not exist")
            return
       
        dataFound = []
    # Read csv file
        with open("registeredList.csv", "r") as file:
            reader = csv.reader(file)
            header = next(reader)   # Locate Headers in row

            for row in reader:
                match = False
    # checks each criteria
                for field in row:
                    if search in field.lower():
                        match = True
                        break
                if match:
                    dataFound.append(row)
        ## renaming
        defvaccineStatus = {
            1: "None",
            2: "1st dose",
            3: "2nd dose",
            4: "1st booster shot",
            5: "2nd booster shot",
        }
        if dataFound:
            for entry in dataFound:
                dataV=[int(val) for val in {entry[10]}.split() ] 
                dataVacStat=[defvaccineStatus[val] for val in dataV]
    # show result
        if dataFound:
            results = "\n".join(
                [
                    f"\tPersonal Information: \n Name: {entry[0]} {entry[1]} {entry[2]}\t Age: {entry[3]} \n Birth Date: {entry[4]} \t Gender: {entry[5]} \n Occupation: {entry[6]}\t E-mail: {entry[8]}\n Address: {entry[7]} \n Contact No.: {entry[9]} \n\n\t Emergency Contact: \n Name: {entry[10]} \t Relation: {entry[11]} \n PhoneNo. : {entry[12]} \t E-mail: {entry[13]} \n\n\t COVID ASSESSMENT: \n Vaccination Status: {dataVacStat} "
                    for entry in dataFound
                ]
            )
    # message for found or no result
            messagebox.showinfo("Result Found: ", f"There are {len(dataFound)} data that matched your queries. Here they are!! :\n\n{results}")
        else:
            messagebox.showinfo("No Result: ", "No Data Entries Found")
            
# run the main menu
start=mainMenu()
start.runMain()