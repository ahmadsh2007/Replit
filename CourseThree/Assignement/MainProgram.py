
from termcolor import colored
from art import *
from prettytable import PrettyTable
import inquirer
import SQLFunctions_Enhanced as SQLFunctions

def notifyUser(message):
    print(colored(text2art(message), 'green'))

def main():
    actions = [
        "Create User",
        "Update User Information",
        "Delete User",
        "Create User Details",
        "Update User Details",
        "Delete User Details",
        "Create Task",
        "Update Task Details",
        "Delete Task",
        "Create Tag",
        "Update Tag Name",
        "Delete Tag",
        "Assign Tag to Task",
        "Remove Tag from Task",
        "View User Details",
        "List Tags for a Task",
        "List Tasks for a Tag",
        "Exit"
    ]

    while True:
        action = inquirer.prompt([inquirer.List(
            "action",
            message="What do you want to do?",
            choices=actions
        )])["action"]

        if action == "Exit":
            notifyUser("Goodbye!")
            break

        elif action == "Update User Information":
            user_id = input("Enter User ID: ")
            name = input("Enter new User Name: ")
            email = input("Enter new User Email: ")
            SQLFunctions.update_user_info(user_id, name, email)
            notifyUser("User Updated!")

        elif action == "Update User Details":
            details_id = input("Enter User Details ID: ")
            phone = input("Enter new Phone Number: ")
            preferences = input("Enter new Preferences: ")
            address = input("Enter new Address: ")
            SQLFunctions.update_user_details(details_id, phone, preferences, address)
            notifyUser("User Details Updated!")

        elif action == "Update Task Details":
            task_id = input("Enter Task ID: ")
            description = input("Enter new Description: ")
            due_time = input("Enter new Due Date (YYYY-MM-DD HH:MM): ")
            status = input("Enter new Status: ")
            SQLFunctions.update_task_details(task_id, description, due_time, status)
            notifyUser("Task Updated!")

        elif action == "Update Tag Name":
            tag_id = input("Enter Tag ID: ")
            new_name = input("Enter new Tag Name: ")
            SQLFunctions.update_tag_name(tag_id, new_name)
            notifyUser("Tag Updated!")

        elif action == "View User Details":
            user_id = input("Enter User ID: ")
            details = SQLFunctions.view_user_details(user_id)
            table = PrettyTable(["Details ID", "Phone", "Preferences", "Address"])
            for row in details:
                table.add_row(row)
            print(table)

        elif action == "List Tags for a Task":
            task_id = input("Enter Task ID: ")
            tags = SQLFunctions.list_tags_for_task(task_id)
            print("Tags associated with Task:", tags)

        elif action == "List Tasks for a Tag":
            tag_id = input("Enter Tag ID: ")
            tasks = SQLFunctions.list_tasks_for_tag(tag_id)
            print("Tasks associated with Tag:", tasks)

        # Other actions already present would remain unchanged.

if __name__ == "__main__":
    main()
