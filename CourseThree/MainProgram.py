from termcolor import colored
from art import *
import inquirer
import sys  
import os

# MY CODES
import SQLdataset
import SQLFunctions


def currentDirectory():
    # Get the directory of the current script
    scriptDir: str = os.path.dirname(os.path.abspath(__file__))

    # Add this directory to the system path
    return sys.path.append(scriptDir)


def notifyUser(Message) -> None:
    print(colored(text2art(Message), 'green'))

def main() -> None:
    currentDirectory()
    ASCIIBanner = text2art("Task Manager")
    
    print(colored(ASCIIBanner, 'green'))
    print('This is a Task Manager application to manage your daily tasks.\n')
    print('Please choose what do you want to do: ')

    '''actions: list = [
        "Create User",
        "Create User Details",
        "Create Task",
        "Create Tag",
        "Assign Tag to Task",
        "Delete Task Tag Relation",
        "Fetch All Users",
        "Fetch a User",
        "Fetch User Details",
        "Fetch All Tasks",
        "Fetch All Tags",
        "Fetch Tags for Task",
        "Fetch Tasks for Tag",
        "Update User",
        "Update User Details",
        "Update Task",
        "Update Tag",
        "Delete User",
        "Delete User Details",
        "Delete Task",
        "Delete Tag",
        "Exit"
    ]'''

    actions: list = [
        "Create User",
        "Create User Details",
        "Create Task",
        "Create Tag",
        "Assign Tag to Task",
        "Fetch All Users",
        "Fetch All Tasks",
        "Exit"
    ]


    while True:
        action = inquirer.prompt([inquirer.List(
            "action",
            message="What do you want to do?",
            choices=actions
        )])['action']

        if action == 'Exit':
            print(text2art('Goodbye!'))
            break
        elif action == 'Create User':
            name = input('What is the User Name? ')
            email = input('What is the User Email? ')
            SQLFunctions.createUser(name, email)
            notifyUser('User Created!')
        elif action == 'Create User Details':
            userID = input('What is the User ID? ')
            PhoneNumber = input('What is the User Phone Number? ')
            Prefrences = input('What is the User Prefrences? ')
            Address = input('What is the User Address? ')
            SQLFunctions.createUserDetails(userID, PhoneNumber, Prefrences, Address)
            notifyUser('User Details Created!')
        elif action == 'Create Task':
            userID = input('What is the User ID? ')
            Description = input('What is the Task Description? ')
            DueTime = input('What is the Task Due Time? ')
            Status = input('What is the Task Status? ')
            SQLFunctions.createTask(userID, Description, DueTime, Status)
            notifyUser('Task Created!')
        elif action == 'Create Tag':
            Name = input('What is the Tag Name? ')
            SQLFunctions.createTag(Name)
            notifyUser('Tag Created!')
        elif action == 'Assign Tag to Task':
            TagID = input('What is the Tag ID? ')
            TaskID = input('What is the Task ID? ')
            SQLFunctions.createTaskTagRelation(TagID, TaskID)
            notifyUser('Tag Assigned to Task!')
        elif action == 'Fetch All Users':
            users = SQLFunctions.readUsers()
            print(f'All Users: {str(users)}\n')
        elif action == 'Fetch All Tasks':
            tasks = SQLFunctions.readTasks()
            print(f'(TaskID, UserID, Description, Due Time, Status)')
            print(f'All Tasks: {str(tasks)}\n')
        else:
            notifyUser('Invalid action!')


if __name__ == '__main__':
    main()