"""
George Dunnery
CS 5001
Homework 5 - Programming #2 - MODULE
11/2/2018
"""

# Turtle module is necessary for visualization
# Random module will help select a random word
import turtle
import random

# Define SHIP to be turtle, since a spaceship is being drawn
SHIP = turtle



# SECTION 1: Functions coordinate the gameplay logic - - - - - - - - - - - - -
def extract(filename):
    """
    Paramters: Filename, a .txt file
    Does: Reads the file into a list so the information can be accessed,
    strips away \n so strings are properly formatted for the game
    Returns: List, elements are strings composed of each line in the file.
    """
    try:
        infile = open(filename, 'r')
        raw_data = infile.readlines()
        infile.close()
        for i in range(len(raw_data)):
            raw_data[i] = raw_data[i].strip('\n')
        return raw_data
    except OSError:
        print("Error reading file.")
        return []

def choose_word(word_list):
    """
    Parameters: List of words to choose from
    Does: Chooses a word for the user to guess using a random integer
    Returns: String, a word from the wordlist file
    """
    try:
        return word_list[random.randint(0, len(word_list) - 1)]
    except ValueError:
        return ''
    
def validate_guess(user_guess, guess_me):
    """
    Parameters: The user's guess, the secret word, strings
    Does: Searches the word for the position(s) of the matching letter
    Returns: List of positions where the guessed letter is located in the
    secret word
    """
    positions = []
    for i in range(len(guess_me)):
        if user_guess.lower() == guess_me[i].lower():
            positions.append(i)
    return positions

def populate_correct(guess_me):
    """
    Parameter: The secret word
    Does: Creates a list with empty positions corresponding to the letters
    in the secret word. This list will later be updated as the user guesses
    correct letters.
    Returns: List
    """
    correct = []
    for i in range(len(guess_me)):
        correct.append(" ")
    return correct

def victory(correct, guess_me):
    """
    Parameters: Correct, list representing how much of the word has been
    guessed. Guess_me, string of the secret word iteself
    Does: Checks to see if the user has guessed the entire word yet
    Returns: Boolean
    """
    if len(correct) != len (guess_me):
        return False
    for letter in range(len(guess_me)):
        if guess_me[letter] != correct[letter]:
            return False
    return True

def defeat(wrong):
    """
    Parameter: Wrong, list of wrong guesses
    Does: Checks if the player has exceeded the maximum number of wrong guesses
    Returns: Boolean
    """
    if len(wrong) >= 5:
        return True
    else:
        return False

def compare_scores(leaderboard):
    """
    Parameters: List containing the strings of data read from the scores.txt
    file by the extract function
    Does: Processes the data in the scores file, removing the names to pass
    a list of integers to the top_dog function, which then responds with
    the highest score from the file
    Returns: The highest score from the file
    """
    try:
        score_list = []
        for prev_score in leaderboard:
            prev_score = prev_score.split(' ')
            score_list.append(int(prev_score[1]))
        return top_dog(score_list)
    except IndexError:
        return 0


def top_dog(score_list):
    """
    Parameter: List of scores from the scores file
    Does: Seeks the highest score
    Returns: Largest integer in the list, or zero if there's an IndexError
    """
    try:
        if len(score_list) == 1:
            return score_list[0]
        else:
            if score_list[0] > top_dog(score_list[1:]):
                return score_list[0]
            else:
                return top_dog(score_list[1:])
    except IndexError:
        return 0

def create(cool_name, wins, SCORES):
    """
    Parameters: The number of wins the player has, integer. The name of the
    scores file, string
    Does: Creates the file if it doesn't already exist
    Returns: Nothing
    """
    outfile = open(str(SCORES), 'w')
    outfile.write(str(cool_name) + ' ' + str(wins) + '\n')
    outfile.close()

def insert(cool_name, wins, leaderboard, SCORES):
    """
    Paremeters: The number of games the player won, integer. The list of
    previously saved scores, list. The name of the scores.txt file, string.
    Does: Writes the new top score to the beginning of the file, and then
    rewrites all of the old scores after the new entry
    Returns: Nothing
    """
    outfile = open(str(SCORES), 'w')
    outfile.write(str(cool_name) + ' ' + str(wins) + '\n')
    for prev_score in leaderboard:
        outfile.write(prev_score + '\n')
    outfile.close()

def pin_tail(cool_name, wins, SCORES):
    """
    Parameter: Number of wins the player achieved, integer
    Does: Appends the player's name and score to the end of the list, because
    if they weren't first, they are last
    Returns: Nothing
    """
    outfile = open(str(SCORES), 'a')
    outfile.write(str(cool_name) + ' ' + str(wins) + '\n')
    outfile.close()

def verify_existence(filename):
    """
    Parameter: Name of the file, string
    Does: Checks if the file exists by trying to open it. Needed to help
    determine when to write or append the scores file.
    Returns: Boolean
    """
    try:
        seekfile = open(filename)
        seekfile.close()
        return True
    except OSError:
        return False




    
# SECTION 2: Functions generate visualizations - - - - - - - - - - - -
def letter_lines(guess_me):
    """
    Parameter: The secret word, string.
    Does: Draws a line for each letter in the secret word. Since it is only
    called at the start of each round, it also clears the screen of any
    previous round
    Returns: Nothing
    """
    SHIP.clear()
    spaces = ""
    for i in range(len(guess_me)):
        spaces += '___  '
    SHIP.penup()
    SHIP.goto(200,0)
    SHIP.write(spaces, False, 'left')
    SHIP.penup()
    SHIP.goto(0,0)

def show_wrong(wrong):
    """
    Parameter: The list of incorrect guesses
    Does: Displays the incorrect guesses to help the player remember
    what they've already guessed
    Returns: Nothing
    """
    if len(wrong) >= 1:
        SHIP.penup()
        SHIP.goto((-200 + 15 * len(wrong)),0)
        SHIP.write(wrong[-1], False, 'center', ('Times', 12, 'bold'))
        SHIP.goto(0,0)

def reveal_correct(correct):
    """
    Parameter: List corresponding to the positions of the correctly guessed
    letters, with open spaces in unknown locations. Easily generated with the
    populate_correct function.
    Does: Writes the location(s) of a correct letter, which slowly reveals
    the word to the player
    Returns: Nothing
    """
    SHIP.penup()
    for position in range(len(correct)):
        SHIP.goto((200 + (25 * position), 5))
        SHIP.write(correct[position], False, 'left', ('Times', 12, 'bold'))
    SHIP.goto(0,0)

def artist(num_wrong):
    """
    Parameter: Number of wrong guesses, integer
    Does: Calls other functions to draw ceertain parts of the spaceship
    depending on the number of incorrect guesses
    Returns: Nothing
    """
    SHIP.update()
    if num_wrong == 1:
        draw_body()
    elif num_wrong == 2:
        draw_left_rocket()
    elif num_wrong == 3:
        draw_right_rocket()
    elif num_wrong == 4:
        draw_left_flame()
    else:
        draw_right_flame()

def draw_body():
    """
    Parameters: None
    Does: Draws the body for the first incorrect guess
    Returns: Nothing
    """
    SHIP.penup()
    SHIP.goto(0,175)
    SHIP.pendown()
    SHIP.goto(-50,100)
    SHIP.goto(-50,-100)
    SHIP.goto(50,-100)
    SHIP.goto(50,100)
    SHIP.goto(0,175)

def draw_left_rocket():
    """
    Parameters: None
    Does: Draws the left rocket for the second incorrect guess
    Returns: Nothing
    """
    SHIP.penup()
    SHIP.goto(-70,-50)
    SHIP.pendown()
    SHIP.goto(-40,-130)
    SHIP.goto(-100,-130)
    SHIP.goto(-70,-50)

def draw_right_rocket():
    """
    Parameters: None
    Does: Draws the right rocket for the second incorrect guess
    Returns: Nothing
    """
    SHIP.penup()
    SHIP.goto(70,-50)
    SHIP.pendown()
    SHIP.goto(40,-130)
    SHIP.goto(100,-130)
    SHIP.goto(70,-50)
    
def draw_left_flame():
    """
    Parameters: None
    Does: Draws the left flame for the second incorrect guess
    Returns: Nothing
    """
    SHIP.penup()
    SHIP.goto(-100,-130)
    SHIP.pendown()
    SHIP.goto(-90,-150)
    SHIP.goto(-80,-130)
    SHIP.goto(-70,-160)
    SHIP.goto(-60,-130)
    SHIP.goto(-50,-150)
    SHIP.goto(-40,-130)

def draw_right_flame():
    """
    Parameters: None
    Does: Draws the right flame for the second incorrect guess
    Returns: Nothing
    """
    SHIP.penup()
    SHIP.goto(100,-130)
    SHIP.pendown()
    SHIP.goto(90,-150)
    SHIP.goto(80,-130)
    SHIP.goto(70,-160)
    SHIP.goto(60,-130)
    SHIP.goto(50,-150)
    SHIP.goto(40,-130)

def bye():
    """
    Parameters: None
    Does: Gets rid of the turtle screen
    Returns: Nothing
    """
    SHIP.bye()
