from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
import tkinter as tk

from ADatabaseHandler import DatabaseHandler

class RegistrationForm(tk.Frame):
    def __init__(self, parent, refreshCallback):
        super().__init__(parent, padx=10, pady=10)

        self.refreshCallback = refreshCallback

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

        # Add Visualize Gender Distribution button
        self.visualizeButton = tk.Button(self, text="Visualize Gender Distribution", command=self.visualize_gender_distribution)
        self.visualizeButton.pack(fill='x')

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

        if all((name, age, email, phone, gender)):
            DatabaseHandler.insertStudent(name, age, email, phone, gender)

            self.clearForm()
            self.refreshCallback()
            self.showInfo("Registration Successful")
        else:
            self.showInfo("Please Fill in All the Fields.")    


    def visualize_gender_distribution(self):
        """
        Fetch gender data from the database, generate a pie chart,
        and display it in a new window.
        """
        try:
            # Fetch students from database
            students = DatabaseHandler.fetchAllStudents()
            if not students:
                messagebox.showinfo("No Data", "No students registered yet!")
                return

            # Count males and females
            male_count = sum(1 for student in students if student[5].lower() == 'male')
            female_count = sum(1 for student in students if student[5].lower() == 'female')

            if male_count == 0 and female_count == 0:
                messagebox.showinfo("No Data", "No gender data to visualize.")
                return

            # Plot pie chart
            labels = ['Male', 'Female']
            sizes = [male_count, female_count]
            colors = ['blue', 'pink']

            plt.figure(figsize=(5, 5))
            plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
            plt.title('Gender Distribution of Students')
            plt.show()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")