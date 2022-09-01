# Dispatch order of the customers

def dispatch():

    print(f"\n###############🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀 LIVE ORDERS 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀###############################\n")
    fp = open('orderslist.txt','r')
    print(fp.read())
    fp.close()
    
    order = input("Enter the order number to be dispatched: ")
    fp = open('orderslist.txt','r')
    l2 = fp.readlines()
    fp.close()

    l1 = []
    count = 0
    for i in l2:

        if order == i.rstrip().split(",") [0]:
            count = 1
            continue

        else:
            l1.append(i)

    if count == 1:
        fp = open('orderslist.txt','w')
        fp.writelines(l1)
        fp.close()
        print(f"*************🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩 Order Dispatched successfully 🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩***************\n")

    else:
        print(f"***************😞😞😣😣😣😣😣😣😣😣😣😣 Order Number Entered is not in the Orderslist 😞😞😣😣😣😣😣😣😣😣😣😣******************************\n")
        