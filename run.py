import random #import random in order to use randomize function for words
import time #import to add time function to introduction
#all words using uppercase to match expected input below
import string #imported to verify letters against the alphabet
words = ['SANDWICH', 'RANDOM', 'SECRET', 'FORMULATE', 'VINTAGE', 'PYTHON', 'IMPLICATE', 'CONGRATULATE']
print("Hi, welcome to hangman!")
time.sleep(2)
print("you must try and guess the random word")
time.sleep(2)
print("you only have 7 lives so be careful!!\n")
time.sleep(2)
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
        name = input("Please enter your name:")
        if not name.isalpha():
            print("please enter a name with letters only!")
            continue
        else:
            print(f"\n{name}! It's time to save a life!\n")
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
        print(f'you have {lives} lives left\n')
        print('letters used so far: \n', ' '.join(used_letters)) #gives string of used letters
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
                print(f"\nhard luck, you have lost a life, {lives} left")
            
        elif guess in used_letters:
            print('you have already guessed this letter, try again')
        else:
            print('the character you have entered has not been recognized, please try again')
    
    if lives == 0:
        time.sleep(2)
        print(f'Hard luck, you have ran out of lives, better luck next time !\n\nThe word was {word}')
    else:
        time.sleep(2)
        print(f'congratulations, you won, thank you for playing \n you successfully guessed {word}')
#functionality to allow the user to try again, code block from python-forum.io utilised, will be linked in readMe
def playAgain():
    while True:
        print('press 1 if you would like to play again')
        print('press Q if you would like to quit')
        choice = input('Enter your choice: ').lower()
        if choice == '1':
            hangman()
        elif choice == 'q':
            return False
        else:
            print('you have not picked a viable choice, please try again')

#compiles and runs all functions
def hangman():
    get_word(words)
    name_request()
    guess_letter()
hangman()
playAgain()
