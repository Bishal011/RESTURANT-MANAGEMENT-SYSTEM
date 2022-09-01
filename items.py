# Items page for customers after successful login
import random

def itemslist():

   print("===="*21)
   print(f"\n  --------------------- 🍔🌭🍕🍔🍟🍕🍔🍟🍕 ITEMS LIST 🍔🌭🍕🍔🍟🍕🍔🍟🍕---------------------  \n")
   print("===="*21)

   fp = open('items.txt','r')
   contents = fp.readlines()
   fp.close()
   print("No, Dish, price\n")

   for i in contents:
      print(i)

def items():

   fp = open('items.txt','r')
   contents = fp.readlines()
   fp.close()
   list_price = []
   qty = []
   name = []

   while True:
      num = input("\nChoose your Dish Number: ")
      print()
      q = input("Enter quantity: ")
      print()

      for i in contents:
         i = i.rstrip().split(',')

         if i[0] == num:
                name.append(i[1])
                list_price.append((i[2]))
                qty.append(q)
                break 
         else:
            continue

      ch = input('Hit "y" to choose another dish: ')
      if ch != 'y':
         break
      else:
         continue

   a = [float(i) * int(j) for i, j in zip(list_price, qty) ]
   b = list(zip(name, qty))
   total = sum(a)

   print(f"\n************* 🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗 Your Order 🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗 ****************")
   print()
   order=random.randint(1,500) + random.randint(100,1000)
   print(f"\nOrderno:",order)
   print()

   for i in range(len(b)):
      print(b[i][0], end=' ')
      print(b[i][1]) 

   print(f"------------------------------------> Total Amount: Rs.{total} <-------------------------------------------------")
   print()
   confirm = input("Confirm(y) your order: ")
   if confirm == 'y':
      aa = ' '

      for i in range(len(b)):
               aa += b[i][0] + ' ' + b[i][1] +','

      details = str(order) + ',' + aa + '\n' 
      fp = open('orderslist.txt','a')
      fp.write(details)
      fp.close()
      print(f"\n============🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉Congrats!!!🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉 Order Received!😍😍😍😍 Visit Again 😎😎😎===========\n")
      print(f"**"*20)
      print()

   else:
      print(f"**"*20)
      print(f"----------🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰 THANK YOU! Relogin for a new Order 🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰 ---------")
      print("##"*20)
        
   # Options for updation of items of the owner

def update():

   print(f"\n-----------------------What do You Want to change in itemslist????--------------------------------------\n")
   print(f"1. Add an Item to List\n")
   print(f"2. Delete an Existing item from list\n")
   print(f"3. Update the Price of an Item in the list\n")

   choice = input("Enter your choice: ")
   print()
   count = 0
   details = ''

   fp = open('items.txt','r')
   l = fp.readlines()
   fp.close()

   if choice == '1':
        num = input("Enter Unique Item Number: ")
        print()
        i_name = input("Enter Name Of Item To be Added: ")
        print()
        price = input("Enter Price Of the The Item: ")
        print()

        for i in l:
            i = i.rstrip().split(',')
            if num == i[0]:
                break
            else:
                count += 1

        if count == len(l):
            details = num + ',' + i_name + ',' + price + '\n'
            print("\n--------------------🍔🌭🍕🍔🍟🍕🍔🍟🍕 Item Successfully Added 🍔🌭🍕🍔🍟🍕🍔🍟🍕---------------------------\n")
        else:
            print(f" --------------------Item Already Present In The Item List")
        
        fp = open("items.txt",'a')
        fp.write(details)
        fp.close()

   elif choice == '2':
      d = input("Enter the item no. to be deleted: ")
      fp = open('items.txt','r')
      con = fp.readlines()
      fp.close()

      for i in con:
        i = i.rstrip().split(',')
        if i[0] == d:
            i = ','.join(i) + '\n'
            con.remove(i)
            break
        else:
            continue

      else:
        print(f"\n---------------------------------------Item no. not found---------------------------------------------------------\n")
      fp=open('items.txt','w')
      fp.writelines(con)
      fp.close()
      print(f"\n**********************************************************Item deleted successfully!****************************************\n")  

   elif choice == '3':
      num1 = input("Enter Item Number:")
      print()
      u_price = input("Enter Updated Price:")
      print()
      v = u_price.isdigit()
      if v == True:

         for i in range(len(l)):
         
               if num1 in l[i]:
                  string = l[i].rstrip().split(',')
                  l[i]=num1 + ',' + string[1] + ',' + u_price + '\n'
                  print("\n**********************************Price Was Updated**************************************************************\n")
                  break

         else:
               print("\n###################################Item Not Present in The List######################################################\n")

         fp=open("items.txt",'w')
         fp.writelines(l)
         fp.close()

      else:
         print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Invalid Type Of Price!!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

   else:
      print("Invalid Choice!!")
