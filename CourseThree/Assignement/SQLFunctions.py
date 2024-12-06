
import sqlite3
import os

# Helper Functions
def getConnection():
    return sqlite3.connect('HTUxCourseDatabase.db')

def currentDirectory():
    # Get the directory of the current script
    scriptDir: str = os.path.dirname(os.path.abspath(__file__))
    return sys.path.append(scriptDir)

# Update Operations
def update_user_info(user_id, name, email):
    connection = getConnection()
    connection.execute(
        'UPDATE Users SET UserName = ?, EmailAddress = ? WHERE UserID = ?;',
        (name, email, user_id)
    )
    connection.commit()
    connection.close()

def update_user_details(details_id, phone, preferences, address):
    connection = getConnection()
    connection.execute(
        'UPDATE UserDetails SET PhoneNumber = ?, Prefrences = ?, Address = ? WHERE UserDetailsID = ?;',
        (phone, preferences, address, details_id)
    )
    connection.commit()
    connection.close()

def update_task_details(task_id, description, due_time, status):
    connection = getConnection()
    connection.execute(
        'UPDATE Tasks SET Description = ?, DueTime = ?, Status = ? WHERE TaskID = ?;',
        (description, due_time, status, task_id)
    )
    connection.commit()
    connection.close()

def update_tag_name(tag_id, new_name):
    connection = getConnection()
    connection.execute(
        'UPDATE Tags SET TagName = ? WHERE TagID = ?;',
        (new_name, tag_id)
    )
    connection.commit()
    connection.close()

# Delete Operations
def delete_user(user_id):
    connection = getConnection()
    connection.execute('DELETE FROM Users WHERE UserID = ?;', (user_id,))
    connection.commit()
    connection.close()

def delete_user_details(details_id):
    connection = getConnection()
    connection.execute('DELETE FROM UserDetails WHERE UserDetailsID = ?;', (details_id,))
    connection.commit()
    connection.close()

def delete_task(task_id):
    connection = getConnection()
    connection.execute('DELETE FROM Tasks WHERE TaskID = ?;', (task_id,))
    connection.commit()
    connection.close()

def delete_tag(tag_id):
    connection = getConnection()
    connection.execute('DELETE FROM Tags WHERE TagID = ?;', (tag_id,))
    connection.commit()
    connection.close()

def remove_tag_from_task(task_id, tag_id):
    connection = getConnection()
    connection.execute(
        'DELETE FROM TaskTags WHERE TaskID = ? AND TagID = ?;', (task_id, tag_id)
    )
    connection.commit()
    connection.close()

# Read Operations
def view_user_details(user_id):
    connection = getConnection()
    cursor = connection.execute(
        'SELECT * FROM UserDetails WHERE UserID = ?;', (user_id,)
    )
    details = cursor.fetchall()
    connection.close()
    return details

def list_tags_for_task(task_id):
    connection = getConnection()
    cursor = connection.execute(
        'SELECT TagName FROM Tags WHERE TagID IN (SELECT TagID FROM TaskTags WHERE TaskID = ?);',
        (task_id,)
    )
    tags = cursor.fetchall()
    connection.close()
    return [tag[0] for tag in tags]

def list_tasks_for_tag(tag_id):
    connection = getConnection()
    cursor = connection.execute(
        'SELECT Description FROM Tasks WHERE TaskID IN (SELECT TaskID FROM TaskTags WHERE TagID = ?);',
        (tag_id,)
    )
    tasks = cursor.fetchall()
    connection.close()
    return [task[0] for task in tasks]
