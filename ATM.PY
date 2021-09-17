def jls_extract_def():
    print("Welcome to bank")
    p = int (input("Enter your 4 digit pin number:"))
    m = 25000
    if (p == 1234):
        print("1- withdraw")
        print("2- Balance Enquiry")
        print("3- fast cash")
        C = int(input("please choose transactions:"))
        if (C == 1):
            w = int(input("please choose transactions: "))
            if (w < m  and w%100 == 0):
                print("please take your amount:",w)
            else:
                print("invalid cash")
    
        elif(C==2):
                print("your available amount: ",m)
        elif(C==3):
            print("1 -> 5,000")
            print("2 -> 10,000")
            print("3 -> 15,000")
            print("4 -> 20,000")
            f = int(input("Enter fast cash option:"))
            if (f == 1 and 5000<m):
                print("please take cash 5000")
            elif(f == 2 and 10000):
                print("please take cash 10000")
            elif(f == 3 and 15000):
                print("please take cash 15000")
            elif(f ==4 and 20000):
                print("please take cash 20000")
            else:
                print("Invalid fast cash option")
        else:
            print("wrong choice")
    else:
        print("wrong pin number")


f = jls_extract_def()

