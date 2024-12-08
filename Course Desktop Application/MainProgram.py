import tkinter as tk
import sys
import os

from DatabaseHandler import DatabaseHandler
from RegistrationForm import RegistrationForm

def currentDirectory():
    """
    Return the current directory of this script and add it to the system path.

    The reason for doing this is because the SQL database is stored in a
    relative path from the location of this script. This function is used to
    get the current location of the script and add it to the system path so
    we can import the database from the relative path.

    Returns:
        None
    """
    scriptDir: str = os.path.dirname(os.path.abspath(__file__))

    # Add this directory to the system path
    return sys.path.append(scriptDir)



class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Management System")
        self.geometry("900x600")
        self.createWidgets()

    def createWidgets(self):
        titleLabel = tk.Label(self, text="Student Management System", font=("Helvetica", 10))
        titleLabel.pack(side='top', fill='x')

        self.RegistrationForm = RegistrationForm(self)
        self.RegistrationForm.pack(side='left', fill='y', padx=10, pady=10)



if __name__ == "__main__":
    currentDirectory()
    app = MainApplication()
    app.mainloop()
    db = DatabaseHandler()
    print(db.fetchAllStudents())