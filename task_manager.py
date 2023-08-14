#=====Importing Library===========
from datetime import datetime

#=====Opening & Reading Files===========
file_user = open("user.txt", "r+")
file_tasks = open("tasks.txt", "r+")

user_data = file_user.readlines()
task_data = file_tasks.readlines()

#====Creating Variables, Empty Lists & Storing Data====

# For current date
date = datetime.now()

# To count number of tasks
task_counter = len(task_data)

# Lists for user data
user_list = []
password_list = []

# Lists for task data
assignee_list = []
title_list = []
description_list = []
assign_date_list = []
due_date_list = []
status_list = []

# For loop to store user data in lists
for item in user_data:
  temp = item.strip()
  temp = temp.split(", ")
  user_list.append(temp[0])
  password_list.append(temp[1])

# For loop to store task data in lists
for item in task_data:
  temp = item.strip()
  temp = temp.split(", ")
  assignee_list.append(temp[0])
  title_list.append(temp[1])
  description_list.append(temp[2])
  assign_date_list.append(temp[3])
  due_date_list.append(temp[4])
  status_list.append(temp[5])

#====Login Section====

# Asking the user to enter their username and password for login
while True:
  break_loop = False  # Created to end this while loop
  user = input("Please enter your username (case sensitive): ")
  if user not in user_list:
    print("The username you have entered does not exist\n")
  else:
    password = input("Please enter your password (case sensitive): ")
    for index in range(len(user_list)):
      if user_list[index] == user and password_list[index] == password:
        break_loop = True  # Checking if password entered is for the correct username and changing break loop to true to move past login screen
    if not break_loop:
      print("You have entered an invalid password for this username\n")
  if break_loop:
    print(f"\nWelcome {user}!")
    break

while True:
  # Presenting the menu to the user, with 'admin' user having an extra option
  # Making sure that the user input is converted to lower case.
  if user != "admin":
    menu = input('''\nSelect one of the following options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my tasks
e - Exit
: ''').lower()
  else:
    menu = input('''\nSelect one of the following options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my tasks
vs - View user and task statistics
e - Exit
: ''').lower()

# Registering the new user by asking for a username and password
  if menu == 'r':
    if user != "admin":  # Only the 'admin' user is allowed to register new users
      print("\nYou are not authorised to register new users")
    else:
      print("\nNote: Commas are not allowed as valid input")  # Username & password cannot contain commas. This is to prevent any issues when reading and storing line data from files
      while True:
        new_user = input("\nPlease enter a new username (case sensitive): ")
        if new_user.find(",") != -1:
          print("Username cannot contain a comma")
        elif new_user in user_list:  # Usernames must be unique
          print("This username already exists, please try a different one")
        else:
          while True:
            new_password = input("Please enter a password (case sensitive): ")
            if new_password.find(",") != -1:
              print("Password cannot contain a comma\n")
            else:
              check_password = input("Please confirm your password: ")
              if check_password != new_password:
                print("Passwords do not match, please try again\n")
              else:
                file_user.write(f"\n{new_user}, {new_password}")
                user_list.append(new_user)  # Appending the user list so that tasks can be assigned to the new user in the same session without having to 'exit' the program first
                print("\nYou have successfully registered a new user!")
                break
          break

# Adding a new task to the list by asking for the various task details
  elif menu == 'a':
    print("\nNote: Commas are not allowed as valid input")  # Task details cannot contain commas. This is to prevent any issues when reading and storing line data from files
    while True:
      new_assignee = input("\nWho would you like to assign this new task to (usernames are case sensitive): ")
      if new_assignee not in user_list:
        print("This user does not exist")  # Only allowed to add tasks for existing users
      else:
        while True:
          new_title = input("What is the title of the new task: ")
          if new_title.find(",") != -1:
            print("Title cannot contain a comma\n")
          else:
            break
        while True:
          new_description = input("What is the description of the task: ")
          if new_description.find(",") != -1:
            print("Description cannot contain a comma\n")
          else:
            break
        while True:
          new_due_date = input("What is the due date for this task: ")
          if new_due_date.find(",") != -1:
            print("Due date cannot contain a comma\n")
          else:
            break
        file_tasks.write(f'\n{new_assignee}, {new_title}, {new_description}, {date.strftime("%d %b %Y")}, {new_due_date}, No')
        # Appending task lists so new tasks can be seen with 'va', 'vm' & 'vs' options in the same session without having to 'exit' the program first
        assignee_list.append(new_assignee)
        title_list.append(new_title)
        description_list.append(new_description)
        assign_date_list.append(date.strftime("%d %b %Y"))
        due_date_list.append(new_due_date)
        status_list.append("No")
        task_counter += 1  # Increasing task counter for the for loop used in 'va' and 'vm' options below, so that it includes the new task added
        print("\nYou have successfully created a new task!")
        break

# For loop to display task details for all tasks created
  elif menu == 'va':
    for index in range(task_counter):
      print(f'''
Task:\t\t\t\t{title_list[index]}
Assigned to:\t\t{assignee_list[index]}
Date assigned:\t\t{assign_date_list[index]}
Due date:\t\t\t{due_date_list[index]}
Task complete:\t\t{status_list[index]}
Task description:\t{description_list[index]}''')

# For loop to display task details for all tasks assigned to the user currently logged in
  elif menu == 'vm':
    if user not in assignee_list:
      print("\nYou have no tasks assigned to you")
    else:
      for index in range(task_counter):
        if assignee_list[index] == user:
          print(f'''
Task:\t\t\t\t{title_list[index]}
Assigned to:\t\t{assignee_list[index]}
Date assigned:\t\t{assign_date_list[index]}
Due date:\t\t\t{due_date_list[index]}
Task complete:\t\t{status_list[index]}
Task description:\t{description_list[index]}''')

# Displaying user and task statistics to the 'admin' user since only they can access this menu option
  elif menu == 'vs' and user == "admin":
    print(f'''
Number of users:\t{len(user_list)}
Number of tasks:\t{len(title_list)}''')

# Closing the program if the user chooses to exit
  elif menu == 'e':
    print('Goodbye!!!')
    exit()

# Error message if the user inputs an option that is incorrect
  else:
    print("\nYou have made a wrong choice, please try again")

#=====Closing Files===========
file_user.close()
file_tasks.close()
