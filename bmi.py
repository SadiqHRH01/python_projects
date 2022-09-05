weight = input("enter your weight in KG:")
height = input("enter your height in M: ")



# heightt = height[1]
# weightt = weight[0]

total_weight = int(weight) / float(height) ** 2
# fat = round(total_weight, 2)
# print int(fat)
if total_weight < 18.5:
    round(total_weight, 2)
    print(f"your bmi is {total_weight}, you are  underweight")
elif total_weight < 25:
    print(f"your bmi is {total_weight}, you have a normal weight")
elif total_weight <= 35:
    print(f"your bmi is {total_weight}, you are obese")
else:
    print(f"your bmi is {total_weight}, you are clinically obese")


total = int(total_weight)
print(total)