from matplotlib.style import use
import functions as f
import numpy as np

file = "dictionaries/toydict.txt"
dict = f.open_dictionary(file)
user_input = "icagr"
# assert(f.is_user_input_in_dictionary(user_input,dict))
print(f.check_word("cigar",user_input))