digits = str(input("Please enter the 12 digit IBSN No: "))
adddigits = []

def validate():

    digitlen = len(digits)
    print(digitlen)
    if digitlen == 12:
        return digits
    else:
        print("Please enter a valid number next time!")

def checkdigit(digit):
    if digit / 2 and digit % 2 == 0:
        digit = digit
        print("even digit is" , digit)
        adddigits.append(digit)
        print(adddigits, "Even entry")
        return digit, adddigits
    else:
        newdigit = digit + (digit * 3)
        print("odd result is", newdigit)
        adddigits.append(newdigit)
        print(adddigits, "Odd entry")
        return newdigit, adddigits

def totaldigits():
    digits.split()
    digit1 = int(digits[0])
    checkdigit(digit1)
    digit2 = int(digits[1])
    checkdigit(digit2)
    digit3 = int(digits[2])
    checkdigit(digit3)
    digit4 = int(digits[3])
    checkdigit(digit4)
    digit5 = int(digits[4])
    checkdigit(digit5)
    digit6 = int(digits[5])
    checkdigit(digit6)
    digit7 = int(digits[6])
    checkdigit(digit7)
    digit8 = int(digits[7])
    checkdigit(digit8)
    digit9 = int(digits[8])
    checkdigit(digit9)
    digit10 = int(digits[9])
    checkdigit(digit10)
    digit11 = int(digits[10])
    checkdigit(digit11)
    digit12 = int(digits[11])
    checkdigit(digit12)

    digit13 = sum(adddigits)

    print("digit 13 modulus 10 is" , (digit13 % 10) - 10)

    finaldigit13a = digit13 % 10
    finaldigit13b = int(finaldigit13a - 10)



    first = (digit1,digit2,digit3)
    firstaltered = ''.join(str(x) for x in first)
    altered1 = int(firstaltered)
    second = (digit4)
    third = (digit5, digit6, digit7)
    thirdaltered = ''.join(str(y) for y in third)
    altered3 = int(thirdaltered)
    fourth = (digit8, digit9, digit10, digit11, digit12)
    fourthaltered = ''.join(str(j) for j in fourth)
    altered4 = int(fourthaltered)
    fifth = (finaldigit13b)
    print("IBSN IS " ,altered1,"-",second,"-",altered3,"-",altered4,"-",fifth)
    print("digit 13 has a remainder of", digit13 % 10 )


totaldigits()