
import random

test_seed = int(input("create a seed number: "))

random.seed(test_seed)

namesAsCSV = input("give everybody's names, seperated by a comma\n")

names = namesAsCSV.split(",")

num_items = len(names)
print(names)

randnom_str = random.randint(0, num_items - 1)
# print(randnom_str)

person_to_pay = names[randnom_str]
print(person_to_pay  +  " is going to pay for today's bill")