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
        open.run()
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
    # reads csv file
        with open("registeredList.csv", "r") as file:
            reader = csv.reader(file)
            header = next(reader) 
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
                dataV=[int(val) for val in {entry[14]} ] 
                dataVacStat=[defvaccineStatus[val] for val in dataV]

        defSymptoms1 = {
            1: "/",
            0: "x",
        }
        
        if dataFound:
            for entry in dataFound:
                dataS1=[int(val) for val in {entry[15]} ] 
                dataSymptoms1=[defSymptoms1[val] for val in dataS1]

        defSymptoms2 = {
            1: "/",
            0: "x",
        }
        
        if dataFound:
            for entry in dataFound:
                dataS2=[int(val) for val in {entry[16]} ] 
                dataSymptoms2=[defSymptoms2[val] for val in dataS2]
                
        defSymptoms3 = {
            1: "/",
            0: "x",
        }
        
        if dataFound:
            for entry in dataFound:
                dataS3=[int(val) for val in {entry[17]} ] 
                dataSymptoms3=[defSymptoms3[val] for val in dataS3]

        defSymptoms4 = {
            1: "/",
            0: "x",
        }
        
        if dataFound:
            for entry in dataFound:
                dataS4=[int(val) for val in {entry[18]} ] 
                dataSymptoms4=[defSymptoms4[val] for val in dataS4]

        defSymptoms5 = {
            1: "/",
            0: "x",
        }
        
        if dataFound:
            for entry in dataFound:
                dataS5=[int(val) for val in {entry[19]} ] 
                dataSymptoms5=[defSymptoms5[val] for val in dataS5]


        defSymptoms6 = {
            1: "/",
            0: "x",
        }
        
        if dataFound:
            for entry in dataFound:
                dataS6=[int(val) for val in {entry[20]} ] 
                dataSymptoms6=[defSymptoms6[val] for val in dataS6]

        defSymptoms7 = {
            1: "/",
            0: "x",
        }
        
        if dataFound:
            for entry in dataFound:
                dataS7=[int(val) for val in {entry[21]} ] 
                dataSymptoms7=[defSymptoms7[val] for val in dataS7]
                
        defSymptoms8 = {
            1: "/",
            0: "x",
        }
        
        if dataFound:
            for entry in dataFound:
                dataS8=[int(val) for val in {entry[22]} ] 
                dataSymptoms8=[defSymptoms8[val] for val in dataS8]

        defSymptoms9 = {
            1: "/",
            0: "x",
        }
        
        if dataFound:
            for entry in dataFound:
                dataS9=[int(val) for val in {entry[23]} ] 
                dataSymptoms9=[defSymptoms9[val] for val in dataS9]

        defSymptoms10 = {
            1: "/",
            0: "x",
        }
        
        if dataFound:
            for entry in dataFound:
                dataS10=[int(val) for val in {entry[24]} ] 
                dataSymptoms10=[defSymptoms10[val] for val in dataS10]

        defExposure = {
            1: "yes",
            2: "no",
            3: "unsure",
        }
        
        if dataFound:
            for entry in dataFound:
                dataExposure1=[int(val) for val in {entry[25]} ] 
                dataExposure=[defExposure[val] for val in dataExposure1]

        defcovidTest = {
            1: "no",
            2: "yes, positive",
            3: "yes, negative",
            4: "yes, pending",
        }
        
        if dataFound:
            for entry in dataFound:
                datacovidTest1=[int(val) for val in {entry[25]} ] 
                datacovidTest=[defcovidTest[val] for val in datacovidTest1]

    # show result
        if dataFound:
            results = "\n".join(
                [
                    f"\tPersonal Information: \n Name: {entry[0]} {entry[1]} {entry[2]}\t Age: {entry[3]} \n Birth Date: {entry[4]} \t Gender: {entry[5]} \n Occupation: {entry[6]}\t E-mail: {entry[8]}\n Address: {entry[7]} \n Contact No.: {entry[9]} \n\n\t Emergency Contact: \n Name: {entry[10]} \t Relation: {entry[11]} \n PhoneNo. : {entry[12]} \t E-mail: {entry[13]} \n\n\t COVID ASSESSMENT: \n Vaccination Status: {dataVacStat} \n\nSymptoms:\nFever?: {dataSymptoms1} \t Cough?: {dataSymptoms2} \t Headache?: {dataSymptoms3} \n SoB?: {dataSymptoms4} \t Common Cold?: {dataSymptoms5} \n Sore Throat?: {dataSymptoms6} \t Lost of ToS?: {dataSymptoms7} \t Diarrhea?: {dataSymptoms8} \t Muscle/Body Pains?: {dataSymptoms9} \t None: {dataSymptoms10}\n\n Exposure to probable/confirmed/symptom the last 7 days?: {dataExposure} \n Tested for COVID-19 the last 14 days: {datacovidTest}"
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