# Problem Set 2, hangman.py
# Name: Artem Pulupchyk
# Collaborators:
# Time spent: 4 days

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
        lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
        assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
        False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word = set(secret_word)
    letters_guessed = set(letters_guessed)
    if letters_guessed >= secret_word:
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guesses_word += letter
        else:
            guesses_word += "_ "
    return guesses_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    for i in letters_guessed:
        if i in alphabet:
            alphabet = alphabet.replace(i, '')
    return alphabet


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
        letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
        s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
        sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
        about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
        partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    vowels = "aeiou"
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have 3 warnings left")
    while True:
        print("--------------------------------------")
        if guesses_remaining <= 0:
            print("Sorry, you ran out of guesses. The word was", secret_word)
            break
        print("You have", guesses_remaining, "guesses left")
        get_available_letters(letters_guessed)
        print("Available letters:", get_available_letters(letters_guessed))
        letter = input("Please guess a letter: ").lower()
        if not letter.isalpha() or len(letter) != 1:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left:")
                print(get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:")
                print(get_guessed_word(secret_word, letters_guessed))
                continue
        elif letter in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! You've already guessed that letter. You have", warnings_remaining, "warnings left:")
                print(get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:")
                print(get_guessed_word(secret_word, letters_guessed))
                continue
        else:
            letters_guessed.append(letter)
        if letter in secret_word:
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            if letter not in vowels:
                guesses_remaining -= 1
            else:
                guesses_remaining -= 2
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
        if is_word_guessed(secret_word, letters_guessed):
            total_score = guesses_remaining * len(set(secret_word))
            print("Congratulations, you won! Your total score for this game is:", total_score)
            break


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word = list(my_word)
    for i in word:
        if i == " ":
            word.remove(i)
    gap_word = []
    for g in word:
        if g == "_":
            continue
        else:
            gap_word.append(g)
    if len(word) == len(other_word):
        for i in range(0, len(word)):
            if word[i] == "_" or word[i] == other_word[i]:
                continue
            else:
                return False
    elif len(word) != len(other_word):
        return False
    for i in range(0, len(gap_word)):
        if gap_word.count(gap_word[i]) == other_word.count(gap_word[i]):
            continue
        else:
            return False
    else:
        return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
            Keep in mind that in hangman when a letter is guessed, all the positions
            at which that letter occurs in the secret word are revealed.
            Therefore, the hidden letter(_ ) cannot be one of the letters in the word
            that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    new_list = []
    for w in wordlist:
        if match_with_gaps(my_word, w):
            new_list.append(w)
    if len(new_list) == 0:
        print("No matches found")
    else:
        print("Possible word matches are:", ' '.join(new_list))



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
          letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
        s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
        about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
        partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
        matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    vowels = "aeiou"
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    print(secret_word)
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have 3 warnings left")

    while True:
        print("--------------------------------------")
        if guesses_remaining <= 0:
            print("Sorry, you ran out of guesses. The word was", secret_word)
            break
        print("You have", guesses_remaining, "guesses left")
        get_available_letters(letters_guessed)
        print("Available letters:", get_available_letters(letters_guessed))
        letter = input("Please guess a letter: ").lower()
        if letter == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue
        elif not letter.isalpha() or len(letter) != 1:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left:")
                print(get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:")
                print(get_guessed_word(secret_word, letters_guessed))
                continue
        elif letter in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! You've already guessed that letter. You have", warnings_remaining, "warnings left:")
                print(get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:")
                print(get_guessed_word(secret_word, letters_guessed))
                continue
        else:
            letters_guessed.append(letter)
        if letter in secret_word:
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            if letter not in vowels:
                guesses_remaining -= 1
            else:
                guesses_remaining -= 2
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
        if is_word_guessed(secret_word, letters_guessed):
            total_score = guesses_remaining * len(set(secret_word))
            print("Congratulations, you won! Your total score for this game is:", total_score)
            break

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
