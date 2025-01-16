# Name: Eddie Hogans
# Class: PROG12974 1249_83349, fall 2024
# Assignment: Assignment 3
# Date: November 21, 2024
# Program: assignment3_Hogan.py
# Description: This program makes a file, then tries to read from the new file.
# After that the program takes usernames from the user and if they work as 
# username the program adds them to the file. Then the program displays the 
# users, then tries to use function 7 which does nothing, then displays the 
# users again.
import random

def create_db(file_name): # 1/7 Creates file.

    try: # Tries to create/wipe file.
        with open(f"{file_name}.txt", "w"): # Opens file.
            return True # Returns true if no error appears. 
    except:
        return False # Returns false if a error occures.

def read_users(file_name): # 2/7 Gets names from a file.
    # This assumes the file is in:
    # Username, Password
    # Username, Password
    # Etc

    try: # Try except in case of error.

        # Opens file and declares variables.
        with open(f"{file_name}.txt", "r") as file:
            username_list, password_list = [], []

            # Gets the words of the first line of file in a list. 
            input = file.readline().split(",")

            # Appends usernames and passwords to their respective lists.
            while input[0] != "" and input[1] != "": 
                username_list.append(input[0])
                password_list.append(input[1])

                # Gets next line of the file.
                input = file.readline().split(",")
              
        return username_list, password_list # Returns list when done.
        
    except: # Returns None, None if a error occures
        return None, None
    
def display_users(names, passwords): # 3/7 Displays names and passwords.

    try: # Try except in case of error.

        if len(names) == len(passwords) == 0: # If nothing in lists, print msg.
            print("No users found")

        else: # Other wise print lists.

            # Printed in addition to the lists.
            print(f"No.\tName\t\t Password") 
            print("-----------------------------------")

            display_users_loops = 0 # Loop counter.
            while display_users_loops < len(names): # Loops until done.

                # The first line of this print the number next to the username.
                # The second line of this prints the username.
                # The Third line changes spacing as needed, a name of 7 chr or 
                # less gets two \t, a name of 15 or less gets one \t, otherwise
                # the name is too long to be displayed in the table format so 
                # it gets one space.
                # The fourth line prints the password. 
                print(f"{ display_users_loops + 1 }\t{ \
                    names[display_users_loops] }{ \
                    "\t" * ( 2-len(names[display_users_loops]) // 8 )}{ \
                    passwords[display_users_loops] }", end="")

                # Increases loop number.
                display_users_loops += 1

    except:
        print("!display_user error!") # Prints error msg if a error occurs.

def valid_name(name): # 4/7 Checks if a name is valid.

    try: # Try except in case of error.
        
        if (len(name) < 3): # Returns false for name shorter then 3 chr.
            return False

        else:

            abc_progress = 0 # To keep track of which number have been tested.
            name = list(name.lower()) # Coverts name to a lowercase list.
            abc = list("abcdefghijklmnopqrstuvwxyz") # List of acceptable chr.
            
            while len(name) != 0: # Repeat until nothing is in name.
                
                # Returns false if a-z have been removed and there are chr 
                # left.
                if (abc_progress > 25): 
                    return False
                
                # If the chr is in name then removes that chr. 
                elif (abc[abc_progress] in name):
                    name.remove(abc[abc_progress])
                    
                # If chr is not in name then moves onto next chr.
                else: abc_progress += 1
        
            else: # Returns true if removing a-z results in a empty list.
                return True

    except:
        print("!valid_name error!") # Prints error msg if needed.
                   
def generate_password(name): # 5/7 Generates password based on name.

    try: # Try except in case of error.

        if name == "": # If no name then return None.
            return None

        # List of acceptable chr broken down into smaller lists for readablity.
        chr_list = list("abcdefghijklmnopqrstuvwxyz") + \
            list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + list("1234567890") + \
            list("+-*/_#$")
        
        # Generates the last 6 chr of the password.
        password_end = ""
        while len(password_end) != 6: # Repeats 6 times.
            password_end += random.choice(chr_list) # Adds random chr to str.

        # Returns first chr of name, name length, and 6 random chr.
        return name[0] + str(len(name)) + str(password_end)

    except:
        print("!generate_password error!") # Prints error msg if required.

def sign_up(file_name): # 6/7

    try: # Try except in case of error.
        
            used_name_list = []
            
            while True: # Repeats until function returns something.

                name = input("Enter name ('s' to stop): ") # Gets input.

                # Ends function and returns used name when the user types "s".
                if name == "s": return len(used_name_list) 
                
                # If the name is invalid then this prints a msg.
                elif valid_name(name) == False: print("Name is invalid.")

                # If the name is used then this prints a msg.
                elif name in used_name_list: print("Name already exists.")

                else: # If the name is valid and not used then this happens.

                    # Appends name to used_name_list and generates a password.
                    used_name_list.append(name)    
                    password = generate_password(name)
                        
                    # Adds username and password to file.
                    print(f"Hello {name}, your password is: {password}")
                    with open(f"{file_name}.txt", "a") as file2:
                        file2.write(f"{name}, {password}\n")

    except: # Returns -1 in case of error.
        return -1

def change_password(file_name, name, new_password):
    # TODO 7/7
    pass

USER_DB = 'assignment3_Hogan.csv'

# == DO NOT MODIFY ANY CODE BELOW THIS LINE ==

def main(): 
    print('Create DB:', create_db(USER_DB)) # Create DB: True
    names, passwords = read_users(USER_DB)
    display_users(names, passwords)  # No user found

    print('Count:', sign_up(USER_DB))
    names, passwords = read_users(USER_DB)
    display_users(names, passwords)

    print('Change first name:',      # Change first name: True
          change_password(USER_DB, names[0], 
                          generate_password(names[0]))) 
    print('Change last name: ',      # Change last name: True
          change_password(USER_DB, names[len(names) - 1], 
                          generate_password(names[len(names) - 1])))
    print('Change dumb name: ',      # Change dumb name: False
          change_password(USER_DB, 'ProfSun', # Username does not exist
                          generate_password('ProfSun'))) 

    names, passwords = read_users(USER_DB)
    display_users(names, passwords)
    
if __name__ == '__main__':
    main()

    