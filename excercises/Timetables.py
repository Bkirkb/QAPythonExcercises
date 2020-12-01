def checknum():

    n = int(input("Please enter a number between 1-20 for times tables: "))
    i = 1

    if n <= 20 and n > 1:
        
        while i < n + 1:
            j = 1
            while j < n + 1:
                if j * i < 10:
                    print(j * i, end="    ")
                    j += 1
                elif j * i >= 100:
                    print(j * i, end="  ")
                    j += 1
                else:
                    print(j * i, end="   ")
                    j += 1
            i += 1
            print()

    elif n > 20 or n < 1:
            print("try again")
            checknum()
    else:
        print("Hidden Error")
            

checknum()
