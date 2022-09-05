
print("Welcome To Shawarma Deliveries :)")

size = input("What size of shawarwa do you want? S, M, or L. ").lower()

bill = 0

if size == "S":
    bill += 15
elif size == "L":
    bill += 20 
else:
    bill += 25

add_ketchup = input("Do you want ketchup? Y OR N. ").lower()

if add_ketchup == "y":
    bill += 2 
add_coke = input("Do you want a drinks? Y OR N. ").lower()
if add_coke == "Y":
    bill += 1

print(f"your final bill is ${bill}")    

