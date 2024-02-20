import random

def run_game():
    guesses, word, used_letters = initialize_game()  # Initialize the game
    attempts = 7 # assign amount of attempts
    while attempts > 0 and '_' in guesses:  # Continue the game until the player runs out of attempts or guesses the word
        display_state(guesses, attempts)  # Display the current game state
        letter = get_player_input(used_letters)  # obtain letter guess from the player
        if not update_state(guesses, word, letter, used_letters):  # update the game state with the guessed letter
            attempts -= 1 # If the guessed letter is not in the word, decrease the number of attempts
        display_state(guesses, attempts) # Display the final game state
    if '_' in guesses:
        print(f"You lost! The word was '{''.join(word)}'.")# If the word has not been guessed, the player lost
    else:
        print("Congratulations, you won!")# If the word has been guessed, the player won


def initialize_game():
    print("\033[95m❤\033[0m\033[92mWelcome to Python Hangman!\033[0m\033[95m❤\033[0m")  # Print a welcome message
    #function is a 1D list of strings 
    words = ['python', 'programming', 'code', 'game', 'word', 'variable', 'strings', 'list', 'conditional', 'loops', 'function', 'class', 'object', 'inheritance', 'polymorphism', 'encapsulation', 'abstraction', 'exception', 'try', 'except', 'finally', 'raise', 'assert', 'import', 'from', 'as', 'with', 'pass', 'global', 'nonlocal', 'return', 'yield', 'del', 'def', 'if', 'else', 'elif', 'while', 'for', 'not', 'break', 'continue', 'True', 'False', 'None', 'print', 'input', 'integer', 'float', 'boolean', 'dictionary', 'set', 'tuple', 'range', 'len', 'sum', 'max', 'min', 'abs', 'ord', 'chr', 'zip', 'sorted', 'reversed', 'map', 'exec', 'open', 'read', 'write', 'close', 'append', 'remove', 'pop', 'insert', 'clear', 'copy', 'count', 'extend', 'index', 'reverse', 'sort', 'split', 'join', 'strip', 'replace', 'lower', 'upper', 'index', 'tuple', 'isinstance', 'locals', 'globals', 'random', 'csv', 'pygame', 'pyinstaller']
    word = random.choice(words)  # Select a random word from the list
    return ['_']*len(word), list(word), []  # Return the initail game state

def display_state(guesses, attempts):
    print('Word: ', ' '.join(guesses))  #Display the current word state
    print('Attempts left: ', attempts)  # display the remaining attempts

def get_player_input(used_letters):
    while True:
        letter = input("Enter a letter: ").lower()  #get a letter guess from the player
        if letter in used_letters:
            print("You've already guessed that letter. Try again.")  # Check if the letter has already been guessed
        elif not letter.isalpha() or len(letter) != 1:
            print("Please enter a single letter.")  # Check if the input is a single letter
        else:
            return letter  # Return the guessed letter

def update_state(guesses, word, letter, used_letters):
    used_letters.append(letter)  # Add the guessed letter to the list of used letters
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guesses[i] = letter  #Update the word state with the guesed letter
    else:
        return False  #if the guessed letter is not in the word, return False
    return True  #if the guessed letter is in the word, return True


run_game()  # Start the game