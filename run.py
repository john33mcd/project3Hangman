import random #import random in order to use randomize function for words
#all words using uppercase to match expected input below
words = ['SANDWICH', 'RANDOM', 'SECRET', 'FORMULATE', 'VINTAGE', 'PYTHON', 'IMPLICATE', 'CONGRATULATE']
import string #imported to verify letters against the alphabet
lives = 5
def get_word(words):
    '''
    get random word from pre populated list and apply a random function on it, return 
    the random word from the list
    '''
    word = random.choice(words)
    return word

def name_request():
    '''
    requests the users name and starts the game once a name is provided,
     will only accept letters.
    '''
    name = ''
    while True:
        name = input("Hi, please enter your name:")
        if not name.isalpha():
            print("please enter a name with letters only!")
            continue
        else:
            print(f"Hi {name}, time to save a life !")
            break
def guess_letter():
    '''
    function to allow user to make a guess, converts any guess to uppercase and 
    only allows alphabet entry. the guess letter function also tracks lives
    and responds to each input by the user.
    the majority of the below code block has been taken from the youtube tutorial from Kylie Ying, 
    link and credits will be included in readMe file
    '''
    word = get_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)#checks predetermined alphabet
    used_letters = set() #what the user has input
    lives = 7
    while len(word_letters) > 0 and lives > 0: #while there is still letters to be filled
        #letters that have been used
        print('letters used so far: ', ' '.join(used_letters)) #gives string of used letters
        print(f'you have {lives} lives left')
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word:', ' '.join(word_list))
        
        guess = input('Guess a letter:').upper()
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                print('well done, that was a correct guess')

            else:
                lives = lives - 1
                print(f"hard luck, you have lost a life, only {lives} left")
            
        elif guess in used_letters:
            print('you have already guessed this letter, try again')
        else:
            print('the character you have entered has not been recognized, please try again')
    
    if lives == 0:
        print(f'oh no, you have ran out of lives, better luck next time !\n the word was {word}')
    else:
        print(f'congratulations, you won, thank you for playing \n you successfully guessed {word}')

def hangman():
    get_word(words)
    name_request()
    guess_letter()
hangman()
