import tkinter as tk
import sys
import os

def currentDirectory():
    # Get the directory of the current script
    scriptDir: str = os.path.dirname(os.path.abspath(__file__))

    # Add this directory to the system path
    return sys.path.append(scriptDir)

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Manangement System")
        self.geometry("900x600")
        self.createWidgets()

    def createWidgets(self):
        titleLabel = tk.Label(self, text="Student Manangement System", font=("Helvetica", 10))
        titleLabel.pack(side='top', fill='x')




if __name__ == "__main__":
    currentDirectory()
    app = MainApplication()
    app.mainloop()