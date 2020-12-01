digits = str(input("Please enter the 12 digit IBSN No: "))
adddigits = []


def totaldigits():

            digitslist = [int(integer) for integer in digits]
            print(digitslist ,"digitslist is <-")

            for digitsindex, item in enumerate(digitslist):
                if digitsindex / 2 and digitsindex % 2 == 0 or digitsindex == 0:
                    print("index [", digitsindex,"]", "value : ", item, "index can be divided by 2")
                    adddigits.append(item)
                else:
                    print("index [",digitsindex,"]", "value : ",item, "cant be divided by 2")
                    newval = int(item * 3)
                    adddigits.append(newval)
                    print( "newval is :" ,newval)
            
            checksum = sum(adddigits)
            print(checksum % 10 , "modulus")
            finalsum = (checksum % 10)
            final_final = 10 - finalsum
            print(final_final , "final checksum")
            print(adddigits, "adddigits is")


def validate():

    digitlen = len(digits)
    print(digitlen)
    if digitlen == 12:
        totaldigits()
    else:
        print("Please enter a valid number next time!")
        return

validate()
