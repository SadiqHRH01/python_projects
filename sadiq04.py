# print("heloo"[2])
# print("123 + 345")
# print("3_3333")
# num_char = len(input("what is your name"))
print ("welcome to sadiq world")
bill = float(input("how much is the bills? $"))
tip = int(input("how many percentage would you like to give? 10, 12, or 15? "))
people = int(input("how many people would you to split the bill?"))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people   

final_amount = round(bill_per_person, 2)
print (f"each should person pay , ${final_amount}")