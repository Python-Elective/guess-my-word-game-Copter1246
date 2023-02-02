import random
import string

WORDLIST_FILENAME = "word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)
    Returns a word from word_list at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for c in secret_word:
        if c not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    output = ""
    for c in secret_word:
        if c in letters_guessed: 
            output += c
        else:
            output += "_ "
    return output
    
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''   
    output = string.ascii_lowercase
    for c in letters_guessed:
        output = output.replace(c, "")
    return output

def game_loop(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game.
    * At the start of the game, let the user know how many 
      letters the secret_word contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so

    '''
    # FILL IN YOUR CODE HERE...
    print ("Let the game begin!")
    print ("I am thinking of a word with", len(secret_word), "letters")
    guess_remain = 8
    letter_guessed = []
    while is_word_guessed(secret_word, letter_guessed) == False and guess_remain > 0:
        print("You have", guess_remain, "guesses remaining")
        remain_letter = get_available_letters(letter_guessed)
        print("Letters available to you:", remain_letter)

        c = input("Guess a letter:").lower()
        if c in remain_letter:
            letter_guessed.append(c)
            if c in secret_word:
                print("Correct:", get_guessed_word(secret_word, letter_guessed))
            else:
                print("Incorrect, this letter is not in my word:", get_guessed_word(secret_word, letter_guessed))
                guess_remain -= 1
        else:
            print("You fool", get_guessed_word(secret_word, letter_guessed))
    
    if (is_word_guessed(secret_word, letter_guessed)):
        print ("You WIN")
    else :
        print("GAME OVER")


def main():
    secret_word = choose_word(word_list)
    game_loop(secret_word)

# Testcases
# you might want to pick your own
# secret_word while you're testing


if __name__ == "__main__":
    main()