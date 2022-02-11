import numpy as np

def open_dictionary(filename):
    with open(filename, "r") as dict:
        content = dict.read()
    content = content.replace('"',"") # strips dict of quotation marks
    return content.split(",") # splits by comma

def is_user_input_in_dictionary(user_input, dictionary):
    if user_input not in dictionary:
        return False
    return True

def check_word(word_of_the_day, user_input):
    '''
    Returns a list of numbers:
        0 means letter is not in the word of the day
        1 means wrong spot
        2 means correct spot
    '''
    word_of_the_day = list(word_of_the_day)
    user_input = list(user_input)
    return_val = list("00000")

    # Check if any are in the right spot.
    for i in range(5):
        if user_input[i] == word_of_the_day[i]:
            return_val[i] = '2'
            user_input[i] = '0' # sets value to 0 so no duplicates
            word_of_the_day[i] = '1' # sets value to 1

    # Check for wrong spots.
    for i in range(5):
        for j in range(5):
            if user_input[i] == word_of_the_day[j]:
                return_val[i] = '1'
                user_input[i] = '0'
                word_of_the_day[j] = '1'
    
    return (return_val)