
print("well come to treasure map")

row1 = [":)", ":)", ":)"]
row2 = [":)", ":)", ":)"]
row3 = [":)", ":)", ":)"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("where do you want to put the treasure?\n")


# print(f"{row1}\n{row2}\n{row3}")

horizonatal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizonatal - 1] = "XX"



print(f"{row1}\n{row2}\n{row3}")



