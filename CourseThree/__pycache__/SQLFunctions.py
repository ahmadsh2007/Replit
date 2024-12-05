import sqlite3
import sys
import os

def currentDirectory():
    # Get the directory of the current script
    scriptDir: str = os.path.dirname(os.path.abspath(__file__))

    # Add this directory to the system path
    return sys.path.append(scriptDir)


# ===============USERS DATABASE===============
def getConnection():
    return sqlite3.connect('HTUxCourseDatabase.db')

def readUsers() -> list[any]:
    connection = getConnection()
    cursor = connection.execute('SELECT * FROM Users;')
    users = cursor.fetchall()

    connection.close()

    return [user[0] for user in users]

def readUser(UserID) -> list[any]:
    connection = getConnection()
    cursor = connection.execute('SELECT * FROM Users WHERE UserID = ?;', (UserID,))
    user = cursor.fetchone()

    connection.close()

    return user

def createUser(name, email) -> None:
    connection = getConnection()
    connection.execute('INSERT INTO Users (UserName, EmailAddress) VALUES (?, ?);', (name, email))

    connection.commit()
    connection.close()

def updateUser(UserID, name, email) -> None:
    connection = getConnection()
    connection.execute('UPDATE Users SET UserName = ?, EmailAddress = ? WHERE UserID = ?;', (name, email, UserID))

    connection.commit()
    connection.close()

def deleteUser(UserID) -> None:
    connection = getConnection()
    connection.execute('DELETE FROM Users WHERE UserID = ?;', (UserID,))

    connection.commit()
    connection.close()


# ===============USER DETAILS DATABASE===============
def readUserDetails(UserDetailsID) -> list[any]:
    connection = getConnection()
    cursor = connection.execute('SELECT * FROM UserDetails WHERE UserDetailsID = ?;', (UserDetailsID,))
    details = cursor.fetchone()

    connection.close()

    return details

def createUserDetails(UserID, PhoneNumber, Prefrences, Address) -> None:
    connection = getConnection()
    connection.execute('INSERT INTO UserDetails (UserID, PhoneNumber, Prefrences, Address) VALUES (?, ?, ?);', 
                       (UserID, PhoneNumber, Prefrences, Address))

    connection.commit()
    connection.close()

def updateUserDetails(UserDetailsID, PhoneNumber, Prefrences, Address) -> None:
    connection = getConnection()
    connection.execute('UPDATE UsersDetails SET PhoneNumber = ?, Prefrences = ?, Address = ? WHERE UserDetailsID = ?;', 
                       (PhoneNumber, Prefrences, Address, UserDetailsID))

    connection.commit()
    connection.close()

def deleteUserDetails(UserDetailsID) -> None:
    connection = getConnection()
    connection.execute('DELETE FROM UserDetails WHERE UserDetailsID = ?;', (UserDetailsID,))

    connection.commit()
    connection.close()


# ===============TASKS DATABASE===============
def readTask(TaskID) -> list[any]:
    connection = getConnection()
    cursor = connection.execute('SELECT * FROM Tasks WHERE TaskID = ?;', (TaskID,))
    tasks = cursor.fetchall()

    connection.close()

    return tasks

def createTask(UserID, Description, DueTime, Status) -> None:
    connection = getConnection()
    connection.execute('INSERT INTO Tasks (UserID, Description, DueTime, Status) VALUES (?, ?, ?, ?);', 
                       (UserID, Description, DueTime, Status))

    connection.commit()
    connection.close()

def updateTask(UserID, Description, DueTime, Status) -> None:
    connection = getConnection()
    connection.execute('UPDATE Tasks SET Description = ?, DueTime = ?, Status = ? WHERE TaskID = ?;', (Description, DueTime, Status, UserID))

    connection.commit()
    connection.close()

def deleteTask(TaskID) -> None:
    connection = getConnection()
    connection.execute('DELETE FROM Tasks WHERE TaskID = ?;', (TaskID,))

    connection.commit()
    connection.close()


# ===============TAGS DATABASE===============
def readTags(TagID) -> list[any]:
    connection = getConnection()
    cursor = connection.execute('SELECT * FROM Tags WHERE TagID = ?;', (TagID,))
    tags = cursor.fetchall()

    connection.close()

    return tags

def createTag(tagName) -> None:
    connection = getConnection()
    connection.execute('INSERT INTO Tags (TagName) VALUES (?);', (tagName,))

    connection.commit()
    connection.close()

def updateTag(TagID, tagName) -> None:
    connection = getConnection()
    connection.execute('UPDATE Tags SET TagName = ? WHERE TagID = ?;', (tagName, TagID))

    connection.commit()
    connection.close()

def deleteTag(TagID) -> None:
    connection = getConnection()
    connection.execute('DELETE FROM Tags WHERE TagID = ?;', (TagID,))

    connection.commit()
    connection.close()


# ===============TASK TAGS DATABASE===============
def createTaskTagRelation(TaskID, TagID) -> None:
    connection = getConnection()
    connection.execute('INSERT INTO TaskTags (TaskID, TagID) VALUES (?, ?);', (TaskID, TagID))

    connection.commit()
    connection.close()

def readTagsForTask(TaskID) -> list[any]:
    connection = getConnection()
    cursor = connection.execute('SELECT TagID FROM TaskTags WHERE TaskID = ?;', (TaskID,))
    tags = cursor.fetchall()

    connection.close()

    return [tag[0] for tag in tags]

def readTasksForTag(TagID) -> list[any]:
    connection = getConnection()
    cursor = connection.execute('SELECT TaskID FROM TaskTags WHERE TagID = ?;', (TagID,))
    tasks = cursor.fetchall()

    connection.close()

    return [task[0] for task in tasks]

def deleteTaskTagRelation(TaskID, TagID) -> None:
    connection = getConnection()
    connection.execute('DELETE FROM TaskTags WHERE TaskID = ? AND TagID = ?;', (TaskID, TagID))

    connection.commit()
    connection.close()



def main() -> None:
    currentDirectory()

if __name__ == '__main__':
    main()