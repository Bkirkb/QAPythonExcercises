def isnear(s1,s2):

    s1 = s1.casefold()
    s2 = s2.casefold()

    w1 = list(s1)
    w2 = list(s2)
    w1l = len(w1)
    w2l = len(w2)


    if w1l > w2l or w1l == w2l:
    
        for i in range(0,w1l):
            w1t = list(s1)
            w1t.pop(i)
            if w1t == w2:
                w1tj = ''.join(w1t)
                print(f"{s1} is close to {w1tj} ")
                return True
            else:
                waiting = True
        else:
            print(f"{s1} is not close to {s2}")
    else:
        return False
                
       
        
    


isnear("shed", "bed")
isnear("bread","read")
isnear("leaf","lef")
isnear("grief","fire")
isnear("Dragoon","Dragon")
isnear("Life","Like")
isnear("sHank", "Hank")
