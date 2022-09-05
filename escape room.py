
print("welcome to escape room")
print("Your mission is to escape from the building")

choice01 = input('which door will your enter type "yellow door" or "blue door".\n').lower()

if choice01 == "blue door":
    choice02 = input('you\'ve come to the window. type "jumb" to jumb from the window. type "next" to look for another door.\n').lower()

    if choice02 == "next":
        choice03 = input('which door will you enter. type "green door" or "white door".\n')
        if choice03 == "green door":
            print("Congratulation you escaped. Enjoy the freedom :)")
        else:
            print("wrong door, you've eaten by beasts.Game over.")    
    else:
        print("your neck have been broken and you're dead, Game over.")

else:
    print("Wrong door, burned by fire, game over.")    