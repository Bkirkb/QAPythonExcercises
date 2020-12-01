redo ="Please enter a mark between 0 and 100"
tm = int
mvalid = bool
cvalid = bool
pvalid = bool

def inputs():
        mm = int(input("Please Enter Your Maths Mark: "))
        if mm > 100 or mm < 0:
            mvalid = False
            while mvalid == False:
                print("VALID NUMBER BETWEEN 0-100 PLEASE")
                mm = int(input("Please Enter Your Maths Mark: "))
                if mm < 101 and mm > 0:
                    mvalid = True
                    mm = mm

        elif mm < 101 and mm > 0:
            mm = mm
            mvalid = True

        cm = int(input("Please Enter Your Chemistry Mark: "))
        if cm > 100 or cm < 0:
            cvalid = False
            while cvalid == False:
                print("VALID NUMBER BETWEEN 0-100 PLEASE")
                cm = int(input("Please Enter Your Chemistry Mark: "))
                if cm < 101 and cm > 0:
                    cvalid = True
                    cm = cm

        elif cm < 101 and cm > 0:
            cm = cm
            cvalid = True

        pm = int(input("Please Enter Your Physics Mark: "))
        if pm > 100 or pm < 0:
            pvalid = False
            while pvalid == False:
                print("VALID NUMBER BETWEEN 0-100 PLEASE")
                pm = int(input("Please Enter Your Physics Mark: "))
                if pm < 101 and pm > 0:
                    pvalid = True
                    pm = pm

        elif pm < 101 and pm > 0:
            pm = pm
            pvalid = True


        tm = (mm + cm + pm) / 3

        if  tm >= 70:
            print("Your Percentage Score is 3" , tm , "%")
            print("You scored a grade of : A" )

        elif tm >= 60:
            print("Your Percentage Score is " , tm , "%")
            print("You scored a grade of : B" )

        elif tm >= 50:
            print("Your Percentage Score is " , tm , "%")
            print("You scored a grade of : C" )

        elif tm >= 40:
            print("Your Percentage Score is " , tm , "%")
            print("You scored a grade of : D" )

        elif tm < 40:
            print("Your Percentage Score is " , tm , "%")
            print("You Failed!" )

        print("Your Maths Mark is " , mm)
        print("Your Chemistry Mark is " , cm)
        print("Your Physics Mark is " , pm)


inputs()
