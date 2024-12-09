from tkinter import ttk
import tkinter as tk

from ADatabaseHandler import DatabaseHandler


class StudentListFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.createWidgets()
        self.loadStudents()

    def createWidgets(self):
        """
        Creates the tree view widget with the columns as specified, and sets
        the column widths to 100 pixels each.
        """
        self.tree = ttk.Treeview(self, columns=("StudentID", "Name", "Age", "Email", "Phone", "Gender"), show="headings")

        for column in self.tree["columns"]:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=100)

        self.tree.pack(fill=tk.BOTH, expand=True)

    def loadStudents(self):
        """
        Loads student data from the database and populates the tree view with 
        this data. Clears any existing entries in the tree before inserting 
        the new data. to avoid duplicates
        """
        self.tree.delete(*self.tree.get_children())
        for student in DatabaseHandler.fetchAllStudents():
            self.tree.insert('', tk.END, values=(student[0], student[1], student[2], student[3], student[4], student[5]))