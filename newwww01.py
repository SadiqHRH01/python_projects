
print("Welcome to love calculator :)")

name01 = input("what is your name? \n")
name02 = input("what is their name? \n")

combined_all = name01 + name02

lower_case_all = combined_all.lower()

#print(lower_case_all)

t = lower_case_all.count("t")
r = lower_case_all.count("r")
u = lower_case_all.count("u")
e = lower_case_all.count("e")

truee = t + r + u + e

l = lower_case_all.count("l")
o = lower_case_all.count("o")
v = lower_case_all.count("v")
e = lower_case_all.count("e")

love = l + o + v + e

love_score = int(str(truee) + str(love))

if love_score  < 10 or love_score > 90:
    print(f"your score is {love_score}, you go together like coke and mentos :).")
elif love_score >= 40 and love_score >= 50:
    print(f"your score is {love_score}, you are alright together :).")
else:
    print(f"your score is {love_score}")    


