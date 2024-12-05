import sqlite3
import sys
import os

def currentDirectory():
    # Get the directory of the current script
    scriptDir: str = os.path.dirname(os.path.abspath(__file__))

    # Add this directory to the system path
    return sys.path.append(scriptDir)

def createDataBase() -> None:
    connection = sqlite3.connect('HTUxCourseDatabase.db')

    connection.execute('PRAGMA foreign_keys = ON')
    
    # Tables Script Creation
    connection.execute('''
    CREATE TABLE IF NOT EXISTS Users(
        UserID INTEGER PRIMARY KEY,
        UserName TEXT,
        EmailAddress TEXT
    );
    ''')

    connection.execute('''
    CREATE TABLE IF NOT EXISTS UserDetails(
        UserDetailsID INTEGER PRIMARY KEY,
        UserID TEXT,
        PhoneNumber TEXT,
        Prefrences TEXT,
        Address TEXT,
        FOREIGN KEY(UserID) REFERENCES Users(UserID)
    );
    ''')

    connection.execute('''
    CREATE TABLE IF NOT EXISTS Tasks(
        TaskID INTEGER PRIMARY KEY,
        UserID TEXT,
        Description TEXT,
        DueTime DATE,
        Status TEXT,
        FOREIGN KEY(UserID) REFERENCES Users(UserID)
    );
    ''')

    connection.execute('''
    CREATE TABLE IF NOT EXISTS Tags(
        TagID INTEGER PRIMARY KEY,
        TagName TEXT
    );
    ''')

    connection.execute('''
    CREATE TABLE IF NOT EXISTS TaskTags(
        TaskID INTEGER,
        TagID INTEGER,
        PRIMARY KEY(TaskID, TagID),
        FOREIGN KEY(TaskID) REFERENCES Tasks(TaskID),
        FOREIGN KEY(TagID) REFERENCES Tags(TagID)
    );
    ''')


    connection.commit()
    connection.close()

def main() -> None:
    currentDirectory()
    createDataBase()

if __name__ == '__main__':
    main()