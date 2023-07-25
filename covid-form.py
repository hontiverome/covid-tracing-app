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
        firstName_label = tkinter.Label(self.frame_label, text="First Name", font='Courier 12')
        firstName_label.grid (row=0, column=0, padx=15)
        # create label and entry for user middle name
        self.middleName_input = tkinter.Entry(self.frame_label, justify='center')  
        self.middleName_input.grid(row=1, column=1)
        middleName_label = tkinter.Label(self.frame_label, text="Middle Name", font='Courier 12')
        middleName_label.grid (row=0, column=1, padx=15)
        # create label and entry for user last name
        self.lastName_input = tkinter.Entry(self.frame_label, justify='center')
        self.lastName_input.grid(row=1, column=2)
        lastName_label = tkinter.Label(self.frame_label, text="Last Name", font='Courier 12')
        lastName_label.grid (row=0, column=2, padx=15)
        # create label and entry for user age
        self.age_input = tkinter.Entry(self.frame_label, justify='center')
        self.age_input.grid(row=1, column=3)
        age_label = tkinter.Label(self.frame_label, text="Age", font='Courier 12')
        age_label.grid (row=0, column=3, padx=50)
        # create label and entry for user birth date
        self.birthDate_input = tkinter.Entry(self.frame_label, justify='center')
        self.birthDate_input.grid(row=1, column=4)
        birthDate_label = tkinter.Label(self.frame_label, text="Birth Date", font='Courier 12')
        birthDate_label.grid (row=0, column=4, padx=15)
        birthDate_blabel = tkinter.Label(self.frame_label, text="mm/dd/yy", font='Courier 8')
        birthDate_blabel.grid (row=2, column=4, padx=15)
        # create label and entry for user gender
        self.gender_input = tkinter.Entry(self.frame_label, justify='center')
        self.gender_input.grid(row=4, column=0)
        gender_label = tkinter.Label(self.frame_label, text="Gender", font='Courier 12')
        gender_label.grid (row=3, column=0, padx=15)
        # create label and entry for user occupation
        self.occupation_input = tkinter.Entry(self.frame_label, justify='center')
        self.occupation_input.grid(row=4, column=1)
        occupation_label = tkinter.Label(self.frame_label, text="Occupation", font='Courier 12')
        occupation_label.grid (row=3, column=1, padx=0)
        # create label and entry for user address
        self.address_input = tkinter.Entry(self.frame_label, justify='center')
        self.address_input.grid(row=4, column=2)
        address_label = tkinter.Label(self.frame_label, text="Address", font='Courier 12')
        address_label.grid (row=3, column=2, padx=0)
        # create label and entry for user email
        self.email_input = tkinter.Entry(self.frame_label, justify='center')
        self.email_input.grid(row=4, column=3)
        email_label = tkinter.Label(self.frame_label, text="E-mail", font='Courier 12')
        email_label.grid (row=3, column=3, padx=0)
        # create label and entry for user contact info
        self.contact_info_input = tkinter.Entry(self.frame_label, justify='center')
        self.contact_info_input.grid(row=4, column=4, pady=10)
        contactInfo_label = tkinter.Label(self.frame_label, text="Contact Info", font='Courier 12')
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
        contactPersonName_label = tkinter.Label(self.frame2_label, text="Contact Person Name", font='Courier 12')
        contactPersonName_label.grid(row=0, column=0, padx=15)
        # create label and entry for contact person relation
        self.contactPersonRelation_input = tkinter.Entry(self.frame2_label, justify='center')
        self.contactPersonRelation_input.grid(row=1, column=1, pady=20)
        contactPersonRelation_label = tkinter.Label(self.frame2_label, text="Relationship", font='Courier 12')
        contactPersonRelation_label.grid(row=0, column=1, padx=15)
        # create label and entry for contact person contact info
        self.contactPersonContactInfo_input = tkinter.Entry(self.frame2_label, justify='center')
        self.contactPersonContactInfo_input.grid(row=3, column=0)
        contactPersonContactInfo_label = tkinter.Label(self.frame2_label, text="Contact Info", font='Courier 12')
        contactPersonContactInfo_label.grid(row=2, column=0, padx=15)
        # create label and entry for contact person e-mail address
        self.contactPersonEmail_input = tkinter.Entry(self.frame2_label, justify='center')
        self.contactPersonEmail_input.grid(row=3, column=1, pady=20)
        contactPersonEmail_label = tkinter.Label(self.frame2_label, text="E-mail", font='Courier 12')
        contactPersonEmail_label.grid(row=2, column=1, padx=15)
        # create 3rdframe
        self.frame3 = tkinter.Frame(self.window)
        self.frame3.pack()
        self.frame3.configure(bg='#95bfe6')
        self.frame3_label = tkinter.LabelFrame(self.frame3, text="Assessment", font='Helvetica 12 bold')
        self.frame3_label.grid (row=0, column=2, padx=15, pady=25)
        self.frame3_label.configure(bg='#a3d1fb')
        # create label and radio buttons for vaccination status
        vacStat=tkinter.IntVar()
        self.vaccinationStatus1 = tkinter.Radiobutton(self.frame3_label, text='none            ', justify='center', font='Courier', variable=vacStat, value=1)
        self.vaccinationStatus1.grid(row=1, column=0)
        self.vaccinationStatus2 = tkinter.Radiobutton(self.frame3_label, text='1st dose        ', justify='center', font='Courier', variable=vacStat, value=2)
        self.vaccinationStatus2.grid(row=2, column=0)
        self.vaccinationStatus3 = tkinter.Radiobutton(self.frame3_label, text='2nd dose        ', justify='center', font='Courier', variable=vacStat, value=3)
        self.vaccinationStatus3.grid(row=3, column=0)
        self.vaccinationStatus4 = tkinter.Radiobutton(self.frame3_label, text='1st booster shot', justify='left', font='Courier', variable=vacStat, value=4)
        self.vaccinationStatus4.grid(row=4, column=0)
        self.vaccinationStatus5 = tkinter.Radiobutton(self.frame3_label, text='2nd booster shot', justify='left', font='Courier', variable=vacStat, value=5)
        self.vaccinationStatus5.grid(row=5, column=0)
        vaccinationStatus_label = tkinter.Label(self.frame3_label, text="Vaccination Status", font='Courier 12 bold')
        vaccinationStatus_label.grid (row=0, column=0, padx=15)
        # create label and checkmarks for felt symptoms
        symptomsFelt1=tkinter.IntVar()
        self.symptomscFelt1 = tkinter.Checkbutton(self.frame3_label, text='fever', justify='left', font='Courier', variable=symptomsFelt1, onvalue=1, offvalue=0)
        self.symptomscFelt1.place(x=280, y=40)
        symptomsFelt2=tkinter.IntVar()
        self.symptomscFelt2 = tkinter.Checkbutton(self.frame3_label, text='cough', justify='left', font='Courier', variable=symptomsFelt2, onvalue=1, offvalue=0)
        self.symptomscFelt2.place(x=280, y=65)
        symptomsFelt3=tkinter.IntVar()
        self.symptomscFelt3 = tkinter.Checkbutton(self.frame3_label, text='headache', justify='left', font   ='Courier', variable=symptomsFelt3, onvalue=1, offvalue=0)
        self.symptomscFelt3.place(x=280, y=90)
        symptomsFelt4=tkinter.IntVar()
        self.symptomscFelt4 = tkinter.Checkbutton(self.frame3_label, text='shortness of breath', justify='left', font='Courier', variable=symptomsFelt4, onvalue=1, offvalue=0)
        self.symptomscFelt4.place(x=280, y=115)
        symptomsFelt5=tkinter.IntVar()
        self.symptomscFelt5 = tkinter.Checkbutton(self.frame3_label, text='common cold', justify='left', font='Courier', variable=symptomsFelt5, onvalue=1, offvalue=0)
        self.symptomscFelt5.place(x=280, y=140)
        symptomsFelt6=tkinter.IntVar()
        self.symptomscFelt6 = tkinter.Checkbutton(self.frame3_label, text='sore throat', justify='left', font='Courier', variable=symptomsFelt6, onvalue=1, offvalue=0)
        self.symptomscFelt6.place(x=520, y=40)
        symptomsFelt7=tkinter.IntVar()
        self.symptomscFelt7 = tkinter.Checkbutton(self.frame3_label, text='loss of taste or smell', justify='left', font='Courier', variable=symptomsFelt7, onvalue=1, offvalue=0)
        self.symptomscFelt7.place(x=520, y=65)
        symptomsFelt8=tkinter.IntVar()
        self.symptomscFelt8 = tkinter.Checkbutton(self.frame3_label, text='diarrhea', justify='left', font='Courier', variable=symptomsFelt8, onvalue=1, offvalue=0)
        self.symptomscFelt8.place(x=520, y=90)
        symptomsFelt9=tkinter.IntVar()
        self.symptomscFelt9= tkinter.Checkbutton(self.frame3_label, text='muscle/body pains', justify='left', font='Courier', variable=symptomsFelt9, onvalue=1, offvalue=0)   
        self.symptomscFelt9.place(x=520, y=115)
        symptomsFelt10=tkinter.IntVar()
        self.symptomscFelt10 = tkinter.Checkbutton(self.frame3_label, text='none', justify='left', font='Courier', variable=symptomsFelt10, onvalue=1, offvalue=0)
        self.symptomscFelt10.place(x=520, y=140)
        symptomsFelt_label = tkinter.Label(self.frame3_label, text="Have you felt these symptoms\n the last 7 days?", font='Courier 11 bold', justify='center')
        symptomsFelt_label.grid (row=0, column=1, padx=120)
        # create label and radio buttons for exposure
        exposure=tkinter.IntVar()
        self.exposure1 = tkinter.Radiobutton(self.frame3_label, text='yes   ', justify='center', font='Courier', variable=exposure, value=1)
        self.exposure1.grid(row=12, column=0)
        self.exposure2 = tkinter.Radiobutton(self.frame3_label, text='no    ', justify='center', font='Courier', variable=exposure, value=2)
        self.exposure2.grid(row=13, column=0)
        self.exposure3 = tkinter.Radiobutton(self.frame3_label, text='unsure', justify='center', font='Courier', variable=exposure, value=3)
        self.exposure3.grid(row=14, column=0)
        exposure_label = tkinter.Label(self.frame3_label, text="Exposure to a \nprobable/confirmed/extreme\n symptom case the last 7 days?", font='Courier 11 bold', justify='center')
        exposure_label.grid (row=11, column=0)
        # create label and radio buttons for covid-19 test
        covidTest=tkinter.IntVar()
        self.covidTest1 = tkinter.Radiobutton(self.frame3_label, text='no           ', justify='center', font='Courier', variable=covidTest, value=1)
        self.covidTest1.grid(row=12, column=1)
        self.covidTest2 = tkinter.Radiobutton(self.frame3_label, text='yes, positive', justify='center', font='Courier', variable=covidTest, value=2)
        self.covidTest2.grid(row=13, column=1)
        self.covidTest3 = tkinter.Radiobutton(self.frame3_label, text='yes, negative', justify='center', font='Courier', variable=covidTest, value=3)
        self.covidTest3.grid(row=14, column=1)
        self.covidTest4 = tkinter.Radiobutton(self.frame3_label, text='yes, pending ', justify='center', font='Courier', variable=covidTest, value=4)
        self.covidTest4.grid(row=15, column=1)
        covidTest_label = tkinter.Label(self.frame3_label, text="Have you undergone a \ncovid-19 test the last 14 days?", font='Courier 11 bold', justify='center')
        covidTest_label.grid (column=1, row=11, padx=120)
        # create submit button
        self.submit = tkinter.Button(self.window, text="Submit")
        self.submit.place(x=400, y=850)
    # test function
    def run(self):
        self.window.mainloop()


test=covidForm()
test.run()