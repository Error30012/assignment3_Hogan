import random 

print("test")

def create_db(file_name):
    # TODO 1/7
    pass

def read_users(file_name):
    # TODO 2/7
    pass

def display_users(names, passwords):
    # TODO 3/7
    pass

def valid_name(name):
    # TODO 4/7
    pass

def generate_password(name):
    # TODO 5/7
    pass

def sign_up(file_name):
    # TODO 6/7
    pass

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
