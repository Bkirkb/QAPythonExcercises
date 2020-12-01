newlist1 = []
newlist2 = []


def checkchars():
    word1 = str(input("Please enter the first word: "))
    word2 = str(input("Please enter the second word: "))

    w1list = [str(c) for c in word1]
    w2list = [str(c) for c in word2]

    print("Word1 list is: " , w1list)
    print("Word2 list is: ", w2list)

    for c in w1list:
        print(c)
    
    for c in w2list:
        newlist2.append(c)
        swordletters = len(newlist2)
        print(newlist2)
        print(int(swordletters))


checkchars()


