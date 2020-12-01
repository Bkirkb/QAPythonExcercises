def askname():
    names = 0
    while names < 5:
        name = str(input("What is Your name?"))
        print(name," Is Awesome ")
        names += 1

askname()

print("I hope you all have a great day!")


for i in range (10,21,2):
    print("This will print 6 times, because there are 6 steps of two between 10 and 21. 10, 12, 14, 16, 18 and 20")