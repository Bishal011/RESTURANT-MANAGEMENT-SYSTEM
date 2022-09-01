import items

# Check for password validation of customers whether valid or not

def password_check(password):
    low = 0
    up = 0
    special_char = 0
    num = 0
    if len(password) >= 6:

        for i in password:

            if i.islower():
                low += 1
            elif i.isupper():
                up += 1
            elif i.isdigit():
                num += 1
            elif (i == '#' or i == '@' or i == '*' or i == '%'):
                special_char += 1
                                            
    if (low >= 1) and (up >= 1) and (num >= 1) and (special_char >= 1):
        return True

    else:
        return False


# check for duplicate customer name present in a file or not

def duplicates(name):

    fp = open('customer.txt','r')
    contents = fp.readlines()
    fp.close()
    for i in contents:  # if for loop will successfully execute then else will execute

        i = i.rstrip().split(',')
        if i[0] == name:
            return True
    else:
        return False

# Login page of customers

def login():

    print("\n--------------------------- 👨‍🍳👨‍🍳👨‍🍳👨‍🍳👨‍🍳👨‍🍳👨‍🍳👨‍🍳 CUSTOMERs PAGE 👨‍🍳👨‍🍳👨‍🍳👨‍🍳👨‍🍳👨‍🍳👨‍🍳👨‍🍳 --------------------------- \n")
    print(f"1. NEW USER\n 2. EXISTING USER\n")
    choice = input("Enter your choice (1/2): ")
    print()
    print(f"***" * 40)
    print()

    # Login as a New user

    if choice == '1':
        while True:
            print("##"*30)
            name = input("Enter the Name: ")
            print()
            if duplicates(name):
                print(f"UESR ALREADY EXITS. GIVE ANOTHER NAME\n")
            else:
                break
        # Main part of password validation
        
        while True:
            print(f" Password should contain atleast 1 UPPERCASE, 1 LOWERCASE, 1 DIGIT, 1SPECIAL CHARACTER \n")
            password = input("Enter the password of(atleast 6 characters): ")
            if password_check(password):
                print(f"{password}---------------> is a valid password\n")
                break
            else:
                 print(f"{password}---------------> is not a valid password\n")

        # Appending customer details to the file

        details = name+ ', '+ password + '\n'
        fp=open('customer.txt','a')
        fp.write(details)
        fp.close()    
        print(f"\n ---------------✨✨✨✨✨✨✨✨ CONGRATULATIONS YOUR ACCOUNT IS CREATED ✨✨✨✨✨✨✨✨--------------- \n")
        print(f"====="*50)
        items.itemslist()
        items.items()

    # Choice for existing user

    elif choice == '2':
        name = input("Enter the Name: ")
        print()
        password = input("Enter the password: ")
        details = name + ',' + password + '\n'
        fp = open('customer.txt','r')
        contents = fp.readlines()
        fp.close()

        for i in contents:

            if name in i:
                print(f"\n ---------------✨✨✨✨✨✨✨✨ CONGRATULATIONS LOGIN SUCCESSFUL ✨✨✨✨✨✨✨✨--------------- \n")
                print("====="*50)
                items.itemslist()
                items.items()

    # If out of given choice
    
    else:
        print(f"INVALID USER CREDENTIALS\n")

