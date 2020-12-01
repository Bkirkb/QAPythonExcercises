digits = str(input("Please enter the 12 digit IBSN No: "))
adddigits = []




def convert(list):
    s = [str(i) for i in list]
    con = int("".join(s))

    return(con)



def totaldigits():

            digitslist = [int(integer) for integer in digits]
         #   print(digitslist ,"digitslist is <-")

            for digitsindex, item in enumerate(digitslist):
                if digitsindex / 2 and digitsindex % 2 == 0 or digitsindex == 0:
                #    print("index [", digitsindex,"]", "value : ", item, "index can be divided by 2")
                    adddigits.append(item)
                else:
                #    print("index [",digitsindex,"]", "value : ",item, "cant be divided by 2")
                    newval = int(item * 3)
                    adddigits.append(newval)
                #    print( "newval is :" ,newval)
            
            checksum = sum(adddigits)
            # print(checksum % 10 , "modulus")
            finalsum = (checksum % 10)
            final_final = 10 - finalsum
           # print(final_final , "final checksum")
           # print(adddigits, "adddigits is")
            

            first3 = [digitslist[0], digitslist[1], digitslist[2]]
            second3 = digitslist[3]
            third3 = [digitslist[4], digitslist[5], digitslist[6]]
            fourth3 = [digitslist[7], digitslist[8], digitslist[9], digitslist[10], digitslist[11]]
            final3 = final_final

            isbnfinal = print("Your ISBN Number is: ", convert(first3),"-",second3,"-",convert(third3),"-",convert(fourth3),"-",final3)
            return isbnfinal


def validate():

    digitlen = len(digits)
   # print(digitlen)
    if digitlen == 12:
        totaldigits()
    else:
        print("Please enter a valid number next time!")
        return

validate()
