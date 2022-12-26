import random #import random in order to use randomize function for words
words = ['sandwich', 'random', 'secret', 'formulate', 'vintage', 'python', 'implicate', 'congratulate']

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
#def hangman():
#name_request()
