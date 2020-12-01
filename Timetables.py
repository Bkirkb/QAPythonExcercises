a = int(input("Please enter first number"))
b = int(input("Please enter second number"))


def checkinputs(a,b):
    
    while a % b != 0:
        a = int("Please enter first number")
        b = int("Please enter first number")

        if a % b == 0:
            divisible(a,b)


def divisible(a,b):

    if a / b and a % b == 0:
        print("Number is divisible with a remainder of 0") 
    else:
        print("can't divide")
        return(a,b)
        
divisible(a,b)
checkinputs(a,b)