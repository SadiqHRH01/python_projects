
# student_heights = input("input the list of the students height: ").split()

# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# # print(student_heights)


# total_height = 0

# for height in student_heights:
#     total_height += height
# # print(total_height)


# number_students = 0
# for student in student_heights:
#     number_students += 1
# # print(number_students)

# average_height = round(total_height / number_students)
# print(average_height)




# student_heights = input("input the list of the students height: ").split()

# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)


# total_height = 0

# for height in student_heights:
#     total_height += height
# print(total_height)


# number_students = 0

# for student in student_heights:
#     number_students += 1
# print(number_students)

# average_height = round(total_height / number_students)
# print(average_height)




student_heights = input("input the list of the students height: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)


total_height = 0
for student in student_heights:
    total_height += student
print(total_height)

number_students = 0
for height in student_heights:
    number_students += 1
print(number_students)


average_height = round(total_height / number_students)
print(average_height)

num_number = 0
for number in range(1, 101):
    num_number += number
print(num_number)


even_num = 0
for number in range(2, 101, 2):
    # even_num += number
    print(number)



for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")    
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)



