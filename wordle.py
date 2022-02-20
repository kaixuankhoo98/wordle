from matplotlib.style import use
import functions as f
import numpy as np

word_of_the_day = f.generate_word_of_the_day()

file = "dictionaries/dictionary_full.txt"
full_dict = f.open_dictionary(file)

guesses = 0
correct = False
while guesses < 6:
    user_input = input("Enter guess: ")
    if f.is_user_input_in_dictionary(user_input):
        result = f.check_word(word_of_the_day,user_input)
        print(list(user_input))
        print(result)
        if result == list("22222"):
            if guesses == 0:
                print(f"You guessed the right word in 1 guess!")
            else:
                print(f"You guessed the right word in {guesses+1} guesses!")
            guesses = 6
            correct = True
        guesses = guesses + 1
    else:
        print("Error: not a valid 5 letter word in the dictionary")

if correct == False:
    print(f"Sorry, try again tomorrow! The correct word was {word_of_the_day}.")