# function that takes two numbers and checks is the first is divisible by the second

def divisible(a,b):
    if a % b == 0:
        return int(a/b)
    else:
        return f"{a} is not divisible by {b}"


