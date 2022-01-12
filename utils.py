import requests

def get_random_word():
    URL = 'https://random-word-api.herokuapp.com/word'
    word = requests.get(URL).json()[0]
    
    if not word.isalpha():
        word = get_random_word()
    
    return word.lower()
    

def get_unmasked_word(word, masked_word, guessed_letters):
    masked_word = list(masked_word)
    for letter in guessed_letters:
        if letter in word:
            positions = [pos for pos, char in enumerate(word) if char == letter]
            for pos in positions:
                masked_word[pos] = letter
    
    return ''.join(masked_word)


def get_valid_guess(guessed_letters):
    guess = input("Enter your guess: ")
    
    if len(guess) != 1:
        print(f"WARNING: Guess only one character at a time.")
        guess = get_valid_guess(guessed_letters)
    
    elif guess in guessed_letters:
        print(f"WARNING: The character '{guess}' has already been guessed. Please make a new guess.")
        guess = get_valid_guess(guessed_letters)
    
    elif not guess.isalpha():
        print(f"WARNING: Guess can only be an alphabet.")
        guess = get_valid_guess(guessed_letters)

    return guess.lower()