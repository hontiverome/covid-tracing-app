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
        self.window.geometry("800x650")
        # create frame
        self.frame = tkinter.Frame(self.window)
        self.frame.pack()
        self.frame_label = tkinter.LabelFrame(self.frame, text="Personal and Contact Information", font='Helvetica 12 bold')
        self.frame_label.grid (row=0, column=2, padx=15, pady=15)
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
        self.frame2_label = tkinter.LabelFrame(self.frame2, text="Emergency Contact", font='Helvetica 12 bold')
        self.frame2_label.grid (row=0, column=2, padx=15, pady=25)
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
    # test function
    def run(self):
        self.window.mainloop()


test=covidForm()
test.run()