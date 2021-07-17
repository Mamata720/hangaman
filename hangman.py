import string
from words import choose_word
from images import IMAGES # in this line meaning from images i am import IMAGES variable list.

# End of helper code
# -----------------------------------
def InValide(guess):# def is pree difine keyword  invalide is a variable i pass the guess argument inside the paremeter.
    if len(guess) > 1:#len of guess is less then 1(because i have to take only one letter input from user)
        return False # then i it will return False.
    if not guess.isalpha():#if guess is not in string (isalpha() function returning the value in bool if guess is in string then iw will give True or else it will return False.)
        return False# then return False.
        
    return True# then return True

def hint(secret_word, letters_guessed):
    import random#i import random libry 
    index = 0 #index is started from 0
    not_guessed_letters = []# not_guessed_letters in this variable i assign empty list.

    while index < len(secret_word):
        letter = secret_word[index]#i difine letter variable in that i assign secreat_word[index] value
        if letter not in letters_guessed:
            if letter not in not_guessed_letters:
                not_guessed_letters.append(letter)#append letter in not_guessed_letters empty list. 
        index = index + 1#increment
    # print(not_guessed_letters)
    return random.choice(not_guessed_letters)


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
      False otherwise
    '''
    if secret_word in get_guessed_word(secret_word, letters_guessed):# replac of == we can use in 
        return True# then print True .
    return False#or else return False.

# Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess kar raha hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
    eg agar secret_word = "kindness", letters_guessed = [k,n, s]
    to hum return karenge "k_n_n_ss"
    '''

    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''
    import string
    all_letters  = string.ascii_lowercase
    letters_left = " "
    i = 0 #  i difine one variable in that i assigen 0 variable
    while i < len(all_letters):# i less then len of all_letters 
        if all_letters[i] not in letters_guessed:# all_letters[i] value not in letters_guessed.
            letters_left += all_letters[i]# all_letters[i]value i add in leters_left sring variable.
        i = i + 1# increment of i .
    # for i in all_letters:
    #     if i not in letters_guessed:
    #         letters_left += i 

    return letters_left

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Hangman game yeh start karta hai:
    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secret_word mei kitne letters hai
    * Har round mei user se ek letter guess karne ko bolte hai
    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi
    * Har round ke baar, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai
    '''
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print( "")
    # print(secret_word)
    while True:
        lives = input("\n1)Easy\n2)Medium\n3)Hard\n Enter your level:-")
        if "Easy" in lives or "easy" in lives or "1" in lives:
            level = 8
            index = 0
            break
        elif "Medium" in lives or "medium" in lives or "2" in lives :
            level = 6
            index = 2
            break
        elif  "Hard" in lives or "hard" in lives or "3" in lives:
            level = 4
            index = 4
            break
        else:
            print("Wrong Input Enter Again :)")# if we are enter wrong answer then it will iterate again.

    letters_guessed = []
    remaining_lives = level # i assign level value in remainging lives.
    # remaining_lives = 8#i difine remaining_lives for giving 8 chance to user.
    guess_count = 1
    image_index= index # i am difining image_index variable for counting the index of IMAGE List in that i assign index value. .
    while  remaining_lives > 0:

        available_letters = get_available_letters(letters_guessed)
        print ("Available letters: " + available_letters)#, +
        print("Remember only ",4 - guess_count ," times you can use hint after thata it will not work")
        guess = input("Please guess a letter / use hint :- ")# guess is taking input from user .
        
        if guess == "hint" and guess_count < 4: # if guess is equal to equal to hint and guess_count less then 4 
            print("You use your",guess_count ,"chance .")
            letter = ( hint(secret_word, letters_guessed))# in letter variable i called hint function .
            # print(guess_count)
            guess_count = guess_count + 1 # increment of guess_count.
       

        else:
            letter = guess.lower()# it is converting guess. letter in lower case.

            if not InValide(letter):# call the InValide function 
                continue# if letter is not valide then continue taking input
        
        if letter in secret_word:# if letter in secret_word 
            letters_guessed.append(letter)# then letters_guessed.append letter.

        if letter in secret_word:
            letters_guessed.append(letter)
            print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print ("")

            if is_word_guessed(secret_word, letters_guessed) == True:
                print (" * * Congratulations, you won! * * ")
                print ("")
                break 

        else:
            print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            letters_guessed.append(letter)
            print ("")
            print(IMAGES[image_index])#IMAGES is list name image_index(value of image_index in IMAGES list)
            image_index+=1#increment of image_index
            remaining_lives -= 1# increment of remaining_lives 
            if remaining_lives == 0:# if my remaining lives is  0 
                print("Your secret word is :- " ,secret_word)# then this line will execute.
    # Load the list of words into the variable wordlist
    # So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)

