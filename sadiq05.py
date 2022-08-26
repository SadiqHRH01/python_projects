
print("DID YOU CHOP FOOD")

food = input("Did you chop food today? ")

if food == "yes":
    yes = input("which type of food? ")
    if yes >= "garri":
        print("its your turn to chop, keep enjoying the good life. :)")
    else:
        print("shame on you:)") 
if  food == "no":
    no = input("are you broke? ")
    if no == "yes":
        print("sorry boss go and hutsle")