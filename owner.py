import items
import orders

def login():

    print("\n------------------------- π¨βπ³π¨βπ³π¨βπ³π¨βπ³π¨βπ³π¨βπ³π¨βπ³π¨βπ³π¨βπ³π¨βπ³ OWNER'S PAGE π¨βπ³π¨βπ³π¨βπ³π¨βπ³π¨βπ³π¨βπ³π¨βπ³π¨βπ³π¨βπ³π¨βπ³ ------------------------- \n")
    print()
    print(f"***" * 40)

    # Login as a owner

    password = input("Enter the password of(atleast 6 characters): ")

    # Check the password
    if password == 'Dom@123':
        print(f"\n----------------------- β¨β¨β¨β¨β¨β¨β¨β¨β¨β¨LOGGED IN SUCCESSFULLY β¨β¨β¨β¨β¨β¨β¨β¨β¨β¨-----------------------\n")
        print()
        while True:

            print(f"----------------------------What do you want to do ???-----------------------------------------------\n")

            # Options for owner

            print(f"      1. Update Items list\n")
            print(f"      2. Dispatch Order\n")
            print(f"      3. View The Items List\n")
            print(f"      4. Close\n")
            print()
        # Choice for the owner

            choice = input("\nEnter the Choice you want: ")
            if choice == '1':
                items.update()
            elif choice == '2':
                orders.dispatch()
            elif choice == '3':
                items.itemslist()
            elif choice == '4':
                exit
                break

        print(f"\n----------------------π₯°π₯°π₯°π₯°π₯°π₯°π₯°π₯°π₯°π₯°THANK YOU!!!π₯°π₯°ππ₯°π₯°π₯°π₯°π₯°π₯°π₯°--------------------")
        print()

    else:
        print(f"INVALID PASSWORD\n")
    