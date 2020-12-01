from first_module.divisible import divisible
from first_module.dice import dice

num_one = int(input("Please enter the first number: "))
num_two = int(input("Please enter the second number: "))

print("Answer: " + str(divisible(num_one, num_two)))
print(dice())
print(dice())

