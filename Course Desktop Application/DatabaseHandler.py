import sqlite3

class DatabaseHandler:
    DatabaseName: str = r"Course Desktop Application/students.db"

    @staticmethod
    def _connect() -> sqlite3.Connection:
        return sqlite3.connect(DatabaseHandler.DatabaseName)
    
    @staticmethod
    def createTable() -> None:
        with DatabaseHandler._connect() as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS students (
                            StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Name TEXT NOT NULL,
                            Age INTEGER NOT NULL,
                            Email TEXT NOT NULL,
                            Phone TEXT NOT NULL,
                            Gender TEXT NOT NULL
            );''')

    @staticmethod
    def insertStudent(name: str, age: int, email: str, phone: str, gender: str) -> None:
        with DatabaseHandler._connect() as conn:
            conn.execute("INSERT INTO students (Name, Age, Email, Phone, Gender) VALUES (?, ?, ?, ?, ?)",
                         (name, age, email, phone, gender))  # Insert the student
            
    @staticmethod
    def fetchAllStudents() -> list:
        with DatabaseHandler._connect() as conn:
            return conn.execute("SELECT * FROM students").fetchall()
        
try:
    DatabaseHandler.createTable()
except sqlite3.Error as e:
    print(f"Error creating table: {e}")
    