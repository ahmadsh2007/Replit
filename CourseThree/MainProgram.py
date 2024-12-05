from termcolor import colored
from art import *
import inquirer
import sys  
import os

# MY CODES
import SQLdataset

def currentDirectory():
    # Get the directory of the current script
    scriptDir: str = os.path.dirname(os.path.abspath(__file__))

    # Add this directory to the system path
    return sys.path.append(scriptDir)




def main() -> None:
    currentDirectory()
    ASCIIBanner = text2art("Task Manager")
    
    print(colored(ASCIIBanner, 'green'))
    print('This is a Task Manager application to manage your daily tasks.\n')
    print('Please choose what do you want to do: ')

    actions: list = [
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
    ]

    action: list | any = inquirer.List(
        "action",
        message="What do you want to do?",
        choices=actions
    )

    actionPrompting = inquirer.prompt([action])

    print(actionPrompting['action'])



if __name__ == '__main__':
    main()