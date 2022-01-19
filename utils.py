import requests


def get_random_word():
    URL = 'https://random-word-api.herokuapp.com/word'
    word = requests.get(URL).json()[0]
    
    if not word.isalpha():
        word = get_random_word()
    
    return word.lower()


def get_unmasked_word(word, masked_word, guess):
    '''
    This function takes the parameters "secret word", "masked word" as it is present now, and letter to use for unmasking.
    If the letter is present in the word, the function would return a new masked word with only that letter unmasked at all applicable positions.
    '''
    masked_word = list(masked_word)
    if guess in word:
        positions = [pos for pos, char in enumerate(word) if char == guess]
        for pos in positions:
            masked_word[pos] = guess
    
    return ''.join(masked_word)


def get_valid_guess(guessed_letters):
    '''
    This function returns a valid user input. User input is valid if it does not already exist in the input list and is an alphabet.
    '''
    guess = input("Enter your guess: ")
    
    if len(guess) != 1:
        print(f"WARNING: Guess one character at a time.")
        guess = get_valid_guess(guessed_letters)
    
    elif guess in guessed_letters:
        print(f"WARNING: The character '{guess}' has already been guessed. Please make a new guess.")
        guess = get_valid_guess(guessed_letters)
    
    elif not guess.isalpha():
        print(f"WARNING: Guess can only be an alphabet.")
        guess = get_valid_guess(guessed_letters)

    return guess.lower()