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
        self.window.geometry("850x900")
        #color
        self.window.configure(bg='#8db5db')
        # create frame
        self.frame = tkinter.Frame(self.window)
        self.frame.pack()
        self.frame.configure(bg='#95bfe6')
        self.frame_label = tkinter.LabelFrame(self.frame, text="Personal and Contact Information", font='Helvetica 12 bold')
        self.frame_label.grid (row=0, column=2, padx=15, pady=15)
        self.frame_label.configure(bg='#a3d1fb')
        # create label and entry for user first name
        self.firstName_input = tkinter.Entry(self.frame_label, justify='center')
        self.firstName_input.grid(row=1, column=0)
        firstName_label = tkinter.Label(self.frame_label, bg='#a3d1fb', text="First Name", font='Courier 12')
        firstName_label.grid (row=0, column=0, padx=15)
        # create label and entry for user middle name
        self.middleName_input = tkinter.Entry(self.frame_label, justify='center')  
        self.middleName_input.grid(row=1, column=1)
        middleName_label = tkinter.Label(self.frame_label, bg='#a3d1fb', text="Middle Name", font='Courier 12')
        middleName_label.grid (row=0, column=1, padx=15)
        # create label and entry for user last name
        self.lastName_input = tkinter.Entry(self.frame_label, justify='center')
        self.lastName_input.grid(row=1, column=2)
        lastName_label = tkinter.Label(self.frame_label, bg='#a3d1fb', text="Last Name", font='Courier 12')
        lastName_label.grid (row=0, column=2, padx=15)
        # create label and entry for user age
        self.age_input = tkinter.Entry(self.frame_label, justify='center')
        self.age_input.grid(row=1, column=3)
        age_label = tkinter.Label(self.frame_label, bg='#a3d1fb', text="Age", font='Courier 12')
        age_label.grid (row=0, column=3, padx=50)
        # create label and entry for user birth date
        self.birthDate_input = tkinter.Entry(self.frame_label, justify='center')
        self.birthDate_input.grid(row=1, column=4)
        birthDate_label = tkinter.Label(self.frame_label, bg='#a3d1fb', text="Birth Date", font='Courier 12')
        birthDate_label.grid (row=0, column=4, padx=15)
        birthDate_blabel = tkinter.Label(self.frame_label, bg='#a3d1fb', text="mm/dd/yy", font='Courier 8')
        birthDate_blabel.grid (row=2, column=4, padx=15)
        # create label and entry for user gender
        self.gender_input = tkinter.Entry(self.frame_label, justify='center')
        self.gender_input.grid(row=4, column=0)
        gender_label = tkinter.Label(self.frame_label, bg='#a3d1fb', text="Gender", font='Courier 12')
        gender_label.grid (row=3, column=0, padx=15)
        # create label and entry for user occupation
        self.occupation_input = tkinter.Entry(self.frame_label, justify='center')
        self.occupation_input.grid(row=4, column=1)
        occupation_label = tkinter.Label(self.frame_label, bg='#a3d1fb', text="Occupation", font='Courier 12')
        occupation_label.grid (row=3, column=1, padx=0)
        # create label and entry for user address
        self.address_input = tkinter.Entry(self.frame_label, justify='center')
        self.address_input.grid(row=4, column=2)
        address_label = tkinter.Label(self.frame_label, bg='#a3d1fb', text="Address", font='Courier 12')
        address_label.grid (row=3, column=2, padx=0)
        # create label and entry for user email
        self.emailInput = tkinter.Entry(self.frame_label, justify='center')
        self.emailInput.grid(row=4, column=3)
        email_label = tkinter.Label(self.frame_label, bg='#a3d1fb', text="E-mail", font='Courier 12')
        email_label.grid (row=3, column=3, padx=0)
        # create label and entry for user contact info
        self.contactInfo_input = tkinter.Entry(self.frame_label, justify='center')
        self.contactInfo_input.grid(row=4, column=4, pady=10)
        contactInfo_label = tkinter.Label(self.frame_label, bg='#a3d1fb', text="Contact Info", font='Courier 12')
        contactInfo_label.grid (row=3, column=4, padx=0)
        # create 2ndframe
        self.frame2 = tkinter.Frame(self.window)
        self.frame2.pack()
        self.frame2.configure(bg='#95bfe6')
        self.frame2_label = tkinter.LabelFrame(self.frame2, text="Emergency Contact", font='Helvetica 12 bold')
        self.frame2_label.grid (row=0, column=2, padx=15, pady=25)
        self.frame2_label.configure(bg='#a3d1fb')
        # create label and entry for contact person name
        self.contactPersonName_input = tkinter.Entry(self.frame2_label, justify='center')
        self.contactPersonName_input.grid(row=1, column=0)
        contactPersonName_label = tkinter.Label(self.frame2_label, bg='#a3d1fb', text="Contact Person Name", font='Courier 12')
        contactPersonName_label.grid(row=0, column=0, padx=15)
        # create label and entry for contact person relation
        self.contactPersonRelation_input = tkinter.Entry(self.frame2_label, justify='center')
        self.contactPersonRelation_input.grid(row=1, column=1, pady=20)
        contactPersonRelation_label = tkinter.Label(self.frame2_label, bg='#a3d1fb', text="Relationship", font='Courier 12')
        contactPersonRelation_label.grid(row=0, column=1, padx=15)
        # create label and entry for contact person contact info
        self.contactPersonContactInfo_input = tkinter.Entry(self.frame2_label, justify='center')
        self.contactPersonContactInfo_input.grid(row=3, column=0)
        contactPersonContactInfo_label = tkinter.Label(self.frame2_label, bg='#a3d1fb', text="Contact Info", font='Courier 12')
        contactPersonContactInfo_label.grid(row=2, column=0, padx=15)
        # create label and entry for contact person e-mail address
        self.contactPersonEmail_input = tkinter.Entry(self.frame2_label, justify='center')
        self.contactPersonEmail_input.grid(row=3, column=1, pady=20)
        contactPersonEmail_label = tkinter.Label(self.frame2_label, bg='#a3d1fb', text="E-mail", font='Courier 12')
        contactPersonEmail_label.grid(row=2, column=1, padx=15)
        # create 3rdframe
        self.frame3 = tkinter.Frame(self.window)
        self.frame3.pack()
        self.frame3.configure(bg='#95bfe6')
        self.frame3_label = tkinter.LabelFrame(self.frame3, text="Assessment", font='Helvetica 12 bold')
        self.frame3_label.grid (row=0, column=2, padx=15, pady=25)
        self.frame3_label.configure(bg='#a3d1fb')
        # create label and radio buttons for vaccination status
        self.vacStat=tkinter.IntVar()
        self.vaccinationStatus1 = tkinter.Radiobutton(self.frame3_label, bg='#a3d1fb', text='none            ', justify='center', font='Courier', variable=self.vacStat, value=1)
        self.vaccinationStatus1.grid(row=1, column=0)
        self.vaccinationStatus2 = tkinter.Radiobutton(self.frame3_label, bg='#a3d1fb', text='1st dose        ', justify='center', font='Courier', variable=self.vacStat, value=2)
        self.vaccinationStatus2.grid(row=2, column=0)
        self.vaccinationStatus3 = tkinter.Radiobutton(self.frame3_label, bg='#a3d1fb', text='2nd dose        ', justify='center', font='Courier', variable=self.vacStat, value=3)
        self.vaccinationStatus3.grid(row=3, column=0)
        self.vaccinationStatus4 = tkinter.Radiobutton(self.frame3_label, bg='#a3d1fb', text='1st booster shot', justify='left', font='Courier', variable=self.vacStat, value=4)
        self.vaccinationStatus4.grid(row=4, column=0)
        self.vaccinationStatus5 = tkinter.Radiobutton(self.frame3_label, bg='#a3d1fb', text='2nd booster shot', justify='left', font='Courier', variable=self.vacStat, value=5)
        self.vaccinationStatus5.grid(row=5, column=0)
        vaccinationStatus_label = tkinter.Label(self.frame3_label, bg='#a3d1fb', text="Vaccination Status", font='Courier 12 bold')
        vaccinationStatus_label.grid (row=0, column=0, padx=15)
        # create label and checkmarks for felt symptoms
        self.symptomsFelt1=tkinter.IntVar()
        self.symptomscFelt1 = tkinter.Checkbutton(self.frame3_label, bg='#a3d1fb', text='fever', justify='left', font='Courier', variable=self.symptomsFelt1, onvalue=1, offvalue=0)
        self.symptomscFelt1.place(x=280, y=40)
        self.symptomsFelt2=tkinter.IntVar()
        self.symptomscFelt2 = tkinter.Checkbutton(self.frame3_label, bg='#a3d1fb', text='cough', justify='left', font='Courier', variable=self.symptomsFelt2, onvalue=1, offvalue=0)
        self.symptomscFelt2.place(x=280, y=65)
        self.symptomsFelt3=tkinter.IntVar()
        self.symptomscFelt3 = tkinter.Checkbutton(self.frame3_label, bg='#a3d1fb', text='headache', justify='left', font   ='Courier', variable=self.symptomsFelt3, onvalue=1, offvalue=0)
        self.symptomscFelt3.place(x=280, y=90)
        self.symptomsFelt4=tkinter.IntVar()
        self.symptomscFelt4 = tkinter.Checkbutton(self.frame3_label, bg='#a3d1fb', text='shortness of breath', justify='left', font='Courier', variable=self.symptomsFelt4, onvalue=1, offvalue=0)
        self.symptomscFelt4.place(x=280, y=115)
        self.symptomsFelt5=tkinter.IntVar()
        self.symptomscFelt5 = tkinter.Checkbutton(self.frame3_label, bg='#a3d1fb', text='common cold', justify='left', font='Courier', variable=self.symptomsFelt5, onvalue=1, offvalue=0)
        self.symptomscFelt5.place(x=280, y=140)
        self.symptomsFelt6=tkinter.IntVar()
        self.symptomscFelt6 = tkinter.Checkbutton(self.frame3_label, bg='#a3d1fb', text='sore throat', justify='left', font='Courier', variable=self.symptomsFelt6, onvalue=1, offvalue=0)
        self.symptomscFelt6.place(x=520, y=40)
        self.symptomsFelt7=tkinter.IntVar()
        self.symptomscFelt7 = tkinter.Checkbutton(self.frame3_label, bg='#a3d1fb', text='loss of taste or smell', justify='left', font='Courier', variable=self.symptomsFelt7, onvalue=1, offvalue=0)
        self.symptomscFelt7.place(x=520, y=65)
        self.symptomsFelt8=tkinter.IntVar()
        self.symptomscFelt8 = tkinter.Checkbutton(self.frame3_label, bg='#a3d1fb', text='diarrhea', justify='left', font='Courier', variable=self.symptomsFelt8, onvalue=1, offvalue=0)
        self.symptomscFelt8.place(x=520, y=90)
        self.symptomsFelt9=tkinter.IntVar()
        self.symptomscFelt9= tkinter.Checkbutton(self.frame3_label, bg='#a3d1fb', text='muscle/body pains', justify='left', font='Courier', variable=self.symptomsFelt9, onvalue=1, offvalue=0)   
        self.symptomscFelt9.place(x=520, y=115)
        self.symptomsFelt10=tkinter.IntVar()
        self.symptomscFelt10 = tkinter.Checkbutton(self.frame3_label, bg='#a3d1fb', text='none', justify='left', font='Courier', variable=self.symptomsFelt10, onvalue=1, offvalue=0)
        self.symptomscFelt10.place(x=520, y=140)
        symptomsFelt_label = tkinter.Label(self.frame3_label, bg='#a3d1fb', text="Have you felt these symptoms\n the last 7 days?", font='Courier 11 bold', justify='center')
        symptomsFelt_label.grid (row=0, column=1, padx=120)
        # create label and radio buttons for exposure
        self.exposure=tkinter.IntVar()
        self.exposure1 = tkinter.Radiobutton(self.frame3_label, bg='#a3d1fb', text='yes   ', justify='center', font='Courier', variable=self.exposure, value=1)
        self.exposure1.grid(row=12, column=0)
        self.exposure2 = tkinter.Radiobutton(self.frame3_label, bg='#a3d1fb', text='no    ', justify='center', font='Courier', variable=self.exposure, value=2)
        self.exposure2.grid(row=13, column=0)
        self.exposure3 = tkinter.Radiobutton(self.frame3_label, bg='#a3d1fb', text='unsure', justify='center', font='Courier', variable=self.exposure, value=3)
        self.exposure3.grid(row=14, column=0)
        exposure_label = tkinter.Label(self.frame3_label, bg='#a3d1fb', text="Exposure to a \nprobable/confirmed/extreme\n symptom case the last 7 days?", font='Courier 11 bold', justify='center')
        exposure_label.grid (row=11, column=0)
        # create label and radio buttons for covid-19 test
        self.covidTest=tkinter.IntVar()
        self.covidTest1 = tkinter.Radiobutton(self.frame3_label, bg='#a3d1fb', text='no           ', justify='center', font='Courier', variable=self.covidTest, value=1)
        self.covidTest1.grid(row=12, column=1)
        self.covidTest2 = tkinter.Radiobutton(self.frame3_label, bg='#a3d1fb', text='yes, positive', justify='center', font='Courier', variable=self.covidTest, value=2)
        self.covidTest2.grid(row=13, column=1)
        self.covidTest3 = tkinter.Radiobutton(self.frame3_label, bg='#a3d1fb', text='yes, negative', justify='center', font='Courier', variable=self.covidTest, value=3)
        self.covidTest3.grid(row=14, column=1)
        self.covidTest4 = tkinter.Radiobutton(self.frame3_label, bg='#a3d1fb', text='yes, pending ', justify='center', font='Courier', variable=self.covidTest, value=4)
        self.covidTest4.grid(row=15, column=1)
        covidTest_label = tkinter.Label(self.frame3_label, bg='#a3d1fb', text="Have you undergone a \ncovid-19 test the last 14 days?", font='Courier 11 bold', justify='center')
        covidTest_label.grid (column=1, row=11, padx=120)
        # create submit button
        self.submit = tkinter.Button(self.window, bg='#ffffff', text="Submit", command=self.register())
        self.submit.place(x=400, y=850)
    # test function
    def run(self):
        self.window.mainloop()
    # register inputs
    def register(self):
        # gets input
        getFirstName=self.firstName_input.get()
        getMiddleName=self.middleName_input.get()
        getLastName=self.lastName_input.get()
        getAge=self.age_input.get()
        getBirthDate=self.birthDate_input.get()
        getGender=self.gender_input.get()
        getOccupation=self.occupation_input.get()
        getAddress=self.address_input.get()
        getEmail=self.emailInput.get()
        getContactInfo=self.contactInfo_input.get()
        getContactPersonName=self.contactPersonName_input.get()
        getContactPersonRelation=self.contactPersonRelation_input.get()
        getContactPersonContactInfo=self.contactPersonContactInfo_input.get()
        getContactPersonEmail=self.contactPersonEmail_input.get()
        getVaccinationStatusr=self.vacStat.get()
        getSymptom1=self.symptomsFelt1.get()
        getSymptom2=self.symptomsFelt2.get()
        getSymptom3=self.symptomsFelt3.get()
        getSymptom4=self.symptomsFelt4.get()
        getSymptom5=self.symptomsFelt5.get()
        getSymptom6=self.symptomsFelt6.get()
        getSymptom7=self.symptomsFelt7.get()
        getSymptom8=self.symptomsFelt8.get()
        getSymptom9=self.symptomsFelt9.get()
        getSymptom10=self.symptomsFelt10.get()
        getExposure=self.exposure.get()
        getCovidTest=self.covidTest.get()
        # raises error if no input detected
        if not getFirstName or not getMiddleName or not getLastName or not getAge or not getBirthDate or not getGender or not getOccupation or not getAddress or not getEmail or not getContactInfo or not getContactPersonName or not getContactPersonRelation or not getContactPersonContactInfo or not getContactPersonEmail or not getVaccinationStatusr or not getSymptom1 or not getSymptom2 or not getSymptom3 or not getSymptom4 or not getSymptom5 or not getSymptom6 or not getSymptom7 or not getSymptom8 or not getSymptom9 or not getSymptom10 or not getExposure or not getCovidTest:
            messagebox.showerror("Error: Please Fill All Entry")    
            return
        # create data and label to be written in csv file
        headerLabel=["First Name", "Middle Name", "Last Name", "Age", "Birth Date", "Gender", "Occupation", "Address", "E-mail", "Contact Info", "Contact Person Name", "Contact Person Relation", "Contact Person Contact Info", "Contact Person E-mail", "Vaccination Status", "Symptom 1", "Symptom 2", "Symptom 3", "Symptom 4", "Symptom 5", "Symptom 6", "Symptom 7", "Symptom 8", "Symptom 9", "Symptom 10", "Exposure", "Covid-19 Test"]
        inputData=[getFirstName, getMiddleName, getLastName ,getAge, getBirthDate, getGender, getOccupation, getAddress, getEmail, getContactInfo, getContactPersonName, getContactPersonRelation, getContactPersonContactInfo, getContactPersonEmail, getVaccinationStatusr, getSymptom1, getSymptom2, getSymptom3, getSymptom4, getSymptom5, getSymptom6, getSymptom7, getSymptom8, getSymptom9, getSymptom10, getExposure, getCovidTest]

        
test=covidForm()
test.run()