from matplotlib.style import use
import functions as f
import numpy as np

word_of_the_day = f.generate_word_of_the_day()

file = "dictionaries/dictionary_full.txt"
full_dict = f.open_dictionary(file)

guesses = 0
while guesses < 6:
    user_input = input("Enter guess: ")
    assert(f.is_user_input_in_dictionary(user_input))
    result = f.check_word(word_of_the_day,user_input)
    print(list(user_input))
    print(result)
    if result == list("22222"):
        guesses = 6
        print("You guessed the right word!")
    guesses = guesses + 1 