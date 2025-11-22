import random
from .global_urls import dictionary

total_char = "qwertyuiopasdfghjkl;zxcvbnm,123456y7u890"

def generateKey(n = 4):
    a = 0 
    return_str = ""
    while a < n:
        b = random.choice(total_char)
        return_str += b
        a += 1
    return return_str if return_str  not in dictionary else  generateKey() 






