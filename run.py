import random #import random in order to use randomize function for words
words = ['sandwich', 'random', 'secret', 'formulate', 'vintage', 'python', 'implicate', 'congratulate']
random.shuffle(words)
print(words)
def nameRequest():
    name = input("Hi, please enter your name:")
    print(f"Hi {name}, time to save a life !")
#def hangman():
nameRequest()
