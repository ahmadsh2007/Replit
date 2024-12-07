import tkinter as tk
from DatabaseHandler import DatabaseHandler

class RegistrationForm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        tk.Label(self, text="Full Name").pack()
        self.nameEntry = tk.Entry(self)
        self.nameEntry.pack()

        tk.Label(self, text="Age").pack()
        self.ageEntry = tk.Spinbox(self, to=127)
        self.ageEntry.pack()

        tk.Label(self, text="Email").pack()
        self.emailEntry = tk.Entry(self)
        self.emailEntry.pack()

        tk.Label(self, text="Phone").pack()
        self.phoneEntry = tk.Entry(self)
        self.phoneEntry.pack()

        tk.Label(self, text="Gender").pack()
        self.genderVar = tk.StringVar()
        tk.Radiobutton(self, text= 'Male', variable=self.genderVar, value= "Male").pack()
        tk.Radiobutton(self, text= 'Female', variable=self.genderVar, value= "Female").pack()

        self.submitButton = tk.Button(self, text="Submit", command= self.submitForm).pack()

    def submitForm(self) -> None:
        name = self.nameEntry.get()
        age = self.ageEntry.get()
        email = self.emailEntry.get()
        phone = self.phoneEntry.get()
        gender = self.genderVar.get()

        if name and age and email and phone and gender:
            DatabaseHandler.insertStudent(name, age, email, phone, gender)

            # Clear the form
            self.nameEntry.delete(0, tk.END)
            self.ageEntry.delete(0, tk.END)
            self.emailEntry.delete(0, tk.END)
            self.phoneEntry.delete(0, tk.END)
            self.genderVar.set(None)

            self.parent.showInfo("Registration successful")
        