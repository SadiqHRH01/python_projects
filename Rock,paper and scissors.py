import random


print("Wellcome to Rock,Paper and Scissors GAME")

user_choice = int(input("what do you choose? type 0 for rock, 1 for paper and 2 for scissors.\n"))

robot_choice = random.randint(0, 2)
print(robot_choice)






if user_choice >= 3 or robot_choice > 3:
    print("you type invalid number")
elif user_choice > robot_choice:
    print("you wins!")
elif robot_choice > user_choice:
    print("you lose!")
elif user_choice == robot_choice:
    print("it's draws")
elif user_choice == 0 and  robot_choice == 1:
    print("you lose!")
elif robot_choice == 0 and user_choice == 1:
    print("you wins!")