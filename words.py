import string
import random

def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    word_list = ["navgurukul", "learning", "kindness","laptop","anything",]
    return word_list

def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word


# import string
# import random

# def load_words():
    
#     my_file = open("words.txt")# i open words.txt file in my_file variable
#     my_data = my_file.read()# my_file read and i store in my_data file.
#     word_list = my_data.split(" ")# i split my_data file and i stor in word_list file.
#     return(word_list) # then i will return word_list 

# def choose_word():
#     """
#     word_list (list): list of words (strings)
#     ye function ek word randomly return karega
#     """
#     word_list = load_words()
#     secret_word = random.choice(word_list)
#     secret_word = secret_word.lower()

#     return secret_word