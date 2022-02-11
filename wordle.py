from matplotlib.style import use
import functions as f
import numpy as np

word_of_the_day = f.generate_word_of_the_day()

file = "dictionaries/dictionary_full.txt"
full_dict = f.open_dictionary(file)

user_input = "abate"
# assert(f.is_user_input_in_dictionary(user_input,dict))
print(f.check_word(word_of_the_day,user_input))