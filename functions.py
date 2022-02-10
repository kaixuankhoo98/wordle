import numpy as np

def open_dictionary(filename):
    with open(filename, "r") as dict:
        content = dict.read()
    content = content.replace('"',"") # strips dict of quotation marks
    return content.split(",") # splits by comma