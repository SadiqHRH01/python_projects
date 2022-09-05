
print("wellcome to rollercoster")

height = int(input("what is your height in cm? "))
if height >= 120:
    print("you can ride the rollercoster!")
    age = int(input("what is your age? "))
    if age <= 12:
        bill = 5
        print ("child ticket are $5")
    elif age > 18:
        bill = 7
        print("youth ticket are $7")
    else:
        bill = 12
        print("Adults ticket are $12")

    want_photo = input("Do you want a photo takeN? Y or N. ")    
    if want_photo == "Y":
        bill += 3
        print(f"your final bill is ${bill}")
else:
    print("sorry you have to grow taller :)")