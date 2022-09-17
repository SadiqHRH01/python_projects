

# word_list = ["ardvart", "baboon", "camel"]
# import word_list in hangman wordlist


import random

from hangmanword import word_list

chosen_word = random.choice(word_list)
print(chosen_word)

lives = 6

from hangmanart import logo, stages
print(logo)
display = []
word_len = len(chosen_word)
for _ in range(word_len):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:

    guess = input("guess a letter: ").lower()

    if guess in display:
        print(f"you have already guessed {guess}")
    for position in range(word_len):
        letter = chosen_word[position]
     
        if letter == guess:
            display[position] = letter
       
    if guess not in chosen_word:
        print(f"you guessed {guess}, that's not in the word. you lose live.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose")

    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("you win.") 
        
# from hangman_art import stages
    print(stages[lives])
# if chosen_word == guess:
#     print(correct)


