from textwrap import dedent
from utils import get_random_word, get_unmasked_word, get_valid_guess


def start_game():
    while True:
        guessed_letters = []
        incorrect_guess_count = 6
        
        word = get_random_word()
        # word = 'blah'
        print(f"Okay, here we go: The secret word is {len(word)} characters long.\n")
        masked_word = '_' * len(word)
        
        while True:
            print("\n")
            print(f"Secret Word: {masked_word}")

            if masked_word == word:
                print(f"Congrats! You correctly guessed the word: {word}. GAME OVER!")
                break

            if incorrect_guess_count == 0:
                print(f"Uh oh!! GAME OVER! You have run out of guesses. The word is: {word}")
                break
            
            print(f"So far you have guessed: {sorted(guessed_letters) if guessed_letters else 'Nothing'}")
            guess = get_valid_guess(guessed_letters)
            guessed_letters.append(guess)

            if guess in word:
                print(f"\nYay! That was a good guess! The letter '{guess}' exists in the secret word.")

            else: 
                print(f"\nUh oh! That was NOT a great guess! The letter '{guess}' does NOT exist in the secret word.")
                incorrect_guess_count -= 1
                print(f"You have {incorrect_guess_count} incorrect guesses left.")

            masked_word = get_unmasked_word(word, masked_word, guess)

        play = input("\nWould you like to play again? (y/n): ")
        if play.lower() != 'y':
            print("Bye Bye! Hope you had fun!")
            break
        
        else:
            print("----------------------------------------------------------------------------------------------------\n")


if __name__ == '__main__':
    print("\n------------------------------------- Welcome to Hangman CLI game! ------------------------------------- ")
    
    intro = """
    - Application will randomly pick a word from the internet. 
    - You are expected to guess ONE letter in the word at each turn.
    - The objective is to correctly guess the word that the application has picked. 
    - You can have upto SIX incorrect guesses (i.e., guessed letter not in word) before it's game over.

    Good luck!
    """
    print(dedent(intro))
    
    start_game()