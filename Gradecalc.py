redo ="Please enter a mark between 0 and 100"
total_mark = int
mvalid = bool
cvalid = bool
pvalid = bool

def inputs(m_mark, c_mark, p_mark, total_mark):

        m_mark = int(input("Please Enter Your Maths Mark: "))
        if m_mark > 100 or m_mark < 0:
            mvalid = False
            while mvalid == False:
                print("VALID NUMBER BETWEEN 0-100 PLEASE")
                m_mark = int(input("Please Enter Your Maths Mark: "))
                if m_mark < 101 and m_mark > 0:
                    mvalid = True
                    m_mark = m_mark

        elif m_mark < 101 and m_mark > 0:
            m_mark = m_mark
            mvalid = True
        
        c_mark = int(input("Please Enter Your Chemistry Mark: "))
        if c_mark > 100 or c_mark < 0:
            cvalid = False
            while cvalid == False:
                print("VALID NUMBER BETWEEN 0-100 PLEASE")
                c_mark = int(input("Please Enter Your Chemistry Mark: "))
                if c_mark < 101 and c_mark > 0:
                    cvalid = True
                    c_mark = c_mark

        elif c_mark < 101 and c_mark > 0:
            c_mark = c_mark
            cvalid = True
        
        p_mark = int(input("Please Enter Your Physics Mark: "))
        if p_mark > 100 or p_mark < 0:
            pvalid = False
            while pvalid == False:
                print("VALID NUMBER BETWEEN 0-100 PLEASE")
                p_mark = int(input("Please Enter Your Physics Mark: "))
                if p_mark < 101 and p_mark > 0:
                    pvalid = True
                    p_mark = p_mark

        elif p_mark < 101 and p_mark > 0:
            p_mark = p_mark
            pvalid = True
            checkmark(total_mark , m_mark , c_mark , p_mark)   
            return total_mark , m_mark , c_mark , p_mark
                 
        

def checkmark(m_mark, c_mark, p_mark, total_mark):

        if  total_mark >= 70:
            print("Your Percentage Score is 3" , total_mark , "%")
            print("You scored a grade of : A" )

        elif total_mark >= 60:
            print("Your Percentage Score is " , total_mark , "%")
            print("You scored a grade of : B" )

        elif total_mark >= 50:
            print("Your Percentage Score is " , total_mark , "%")
            print("You scored a grade of : C" )

        elif total_mark >= 40:
            print("Your Percentage Score is " , total_mark , "%")
            print("You scored a grade of : D" )

        elif total_mark < 40:
            print("Your Percentage Score is " , total_mark , "%")
            print("You Failed!" )

        print("Your Maths Mark is " , m_mark)
        print("Your Chemistry Mark is " , c_mark)
        print("Your Physics Mark is " , p_mark)

        return m_mark, c_mark, p_mark, total_mark


inputs(m_mark, c_mark, p_mark, total_mark)
