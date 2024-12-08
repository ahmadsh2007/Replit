from tkinter import ttk
import tkinter as tk

from DatabaseHandler import DatabaseHandler

class RegistrationForm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padx=10, pady=10)

        tk.Label(self, text="Full Name").pack()
        self.nameEntry = tk.Entry(self)
        self.nameEntry.pack(fill='x')

        tk.Label(self, text="Age").pack()
        self.ageEntry = ttk.Spinbox(self, to=127)
        self.ageEntry.pack(fill='x')

        tk.Label(self, text="Email").pack()
        self.emailEntry = tk.Entry(self)
        self.emailEntry.pack(fill='x')

        tk.Label(self, text="Phone").pack()
        self.phoneEntry = tk.Entry(self)
        self.phoneEntry.pack(fill='x')

        tk.Label(self, text="Gender").pack(fill='x')
        self.genderVar = tk.StringVar()
        tk.Radiobutton(self, text= 'Male', variable=self.genderVar, value= "Male").pack(anchor='w')
        tk.Radiobutton(self, text= 'Female', variable=self.genderVar, value= "Female").pack(anchor='w')

        self.submitButton = tk.Button(self, text="Submit", command= self.submitForm).pack(fill='x')
    
    def clearForm(self) -> None:
        self.nameEntry.delete(0, tk.END)
        self.ageEntry.delete(0, tk.END)
        self.emailEntry.delete(0, tk.END)
        self.phoneEntry.delete(0, tk.END)
        self.genderVar.set(None)

    def showInfo(self, message: str) -> None:
        tk.Message(self, text=message).pack()

    def submitForm(self) -> None:
        name = self.nameEntry.get()
        age = self.ageEntry.get()
        email = self.emailEntry.get()
        phone = self.phoneEntry.get()
        gender = self.genderVar.get()

        if name and age and email and phone and gender:
            DatabaseHandler.insertStudent(name, age, email, phone, gender)

            # Clear the form
            self.clearForm()

            # Show success message
            self.showInfo("Registration successful!")        