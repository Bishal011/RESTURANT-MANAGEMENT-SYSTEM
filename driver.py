# Main program of the project

import users
import owner

print(f"\n------------------ 🤩🤩🤩🤩😍😍😍😍😍😍 WELCOME TO THE RESTURANT MANAGEMENT APP 🤩🤩🤩🤩😍😍😍😍😍😍 -----------------  \n")
print(f" ************************************** Who Are you ?????************************************************\n ")
print(f"1. Customer\n2. Resturant Owner\n")
login = input("Enter your choice (1/2): ")
print()
print("###" * 40)
print()

# Customers login

if login == '1':
    # File present in users.py
    users.login() 

# Owner's login

elif login == '2':
    owner.login()
   
else:
    print(f"INVALID INPUT\n")

