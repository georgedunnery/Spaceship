"""
George Dunnery
CS 5001
Homework 5 - Programming #2 - TEST SUITE
11/2/2018



                      --- Test Suite Description ---
   Functions tested followed by an explanation of the input passed to them:

1. verify_existence
  Good input: Files that exist should return True, capitalization does change
  the existence of a file
  Bad input: Files that don't exist return False

2. extract
  Good input: Correctly spelled filename produces the expected list of words
  Bad input: Misspelled/wrong filename returns an empty list

3. create
  Good input: Player name and filename as strings, wins as an integer.
  Bad input: Player/filenames as unexpected data types

4. insert
  Good input: Player name and filename as strings, wins as an integer,
  leaderboard as a list (generated by extract)
  Bad input: Player/filenames as unexpected data types, non-existent file

5. pin_tail
  Good input: Player name and filename as strings, wins as an integer,
  leaderboard as a list (generated by extract)
  Bad input: Player/filenames as unexpected data types, non-existent file

6. choose_word
  Good input: List of words produces one of the words at random
  Bad input: List of integers, floats, etc., still returns one of the list
  values at random, Empty list should return ''

7. validate_guess
  Good input: A letter that exists in the word should return the right positions
  of the string where the letter is located, including apostrophes. If a user
  has guessed the letter 'a', all positions for both 'a' and 'A' should be
  returned
  Bad input: There should not be an error where the position is off by one
  
8. populate_correct
  Good input: Length of the list 'correct' should be the same as the length of
  the secret word 'guess_me
  Bad input: There should not be an error where the position is off by one,
  the word '' should return a list of length 0

9. victory
  Good input: The order of the letters in the list 'correct' should match the
  order and case of the letters in the string 'guess_me' (the user is shown
  all cases of a guessed letter, however, the 'correct' list remembers the
  capitalizations, which is seen on the letter lines during gameplay)
  Bad input: Any variation between the list and the string, including spaces,
  should return False

10. defeat
  Good input: Lists of length 4 or less should return False, lists with length
  equal to or greater than 5 should return Tryue
  Bad input: Lists of things other than letters should still produce the same
  result - boolean based on length

11. top_dog
  Good input: Lists of numbers should return the largest number, works with
  both integers and floats (but all scores should be an integer)
  Bad input: Empty list should just return zero

12. compare_scores
  Good input: List of strings: name + ' ' + integer, should produce a list of
  integers. Empty list just returns 0
  Bad input: Lists without a space return 0

STATEMENT:
I am confident that I have tested every eventuality for the spaceship game. The
user only has a very shallow ability to cause an error through their inputs,
which have all been accounted for. Functions that should always be passed
good input by other functions in the logic of the game have also been made
robust enough to deal with bad input without encountering an error. The player
shouldn't encounter any problems while playing the game, inputting anything they
can think of.

The test suite is quite long, so I have attempted to make it more readable
using comments and by separating out several sections containing similar types
of code (i.e. variables, printing functions, testing functions).
"""

# ------------------------------------------------------------------------------
# IMPORT MODULE containing the functions to be tested
import spaceship



# ------------------------------------------------------------------------------
# IMPORTANT INFORMATION ABOUT TEST SUITE FLAT FILES

# REQUIRED TO RUN SUITE: test_extract.txt
# DISPOSABLE: scores_test_1.txt, scores_test_2.txt, scores_test_3.txt, 55.txt

# The disposable files will be generated and modified to help with testing, but
# the underlying extract function MUST have test_extract.txt to verify itself!




# ------------------------------------------------------------------------------
# VARIABLES that will pass various inputs to the functions throughout testing

FUNCTIONS = ['verify_existence (1 of 12)', 'extract (2 of 12)',
             'create (3 of 12)', 'insert (4 of 12)', 'pin_tail (5 of 12)',
             'choose_word (6 of 12)', 'validate_guess (7 of 12)',
             'populate_correct (8 of 12)', 'victory (9 of 12)',
             'defeat (10 of 12)', 'top_dog (11 of 12)',
             'compare_scores (12 of 12)']

# Dictionary of filenames : expected output from extracting, list
EXTRACT = {'test_extract.txt':['sample', 'Extracted', 'far-out', "it's"],
           'non_existent_file.txt':[]}

# Lists of ordered information: Player's name as a string, wins as an int,
# the filename as a string. Expecting: boolean for success, list of contents
CREATE = [['Alice', 3, 'scores_test_1.txt', True,['Alice 3']],
          ['bob', 7.2, 'scores_test_2.txt', True, ['bob 7.2']],
          [16, '3', 'scores_test_3.txt', True,['16 3']],
          ['CAM@$!', 22, '55.txt', True,['CAM@$! 22']]]

# Lists of ordered information: Player's name as a string, wins as an int,
# the filename as a string. Expecting: boolean for success, list of contents 
INSERT = [['Drinkme', 5, 'scores_test_1.txt', True, ['Drinkme 5', 'Alice 3']],
          ['Ben', 7.3, 'scores_test_2.txt', True, ['Ben 7.3', 'bob 7.2']],
          [15, '5', 'scores_test_3.txt', True, ['15 5','16 3']],
          ['sam', 23, '55.txt', True, ['sam 23', 'CAM@$! 22']]]

# Lists of ordered information: Player's name as a string, wins as an int,
# the filename as a string. Expecting: boolean for success, list of contents 
TAIL = [['madqueen', 1, 'scores_test_1.txt', True, ['Drinkme 5', 'Alice 3',
                                                    'madqueen 1']],
          ['bert', 7.1, 'scores_test_2.txt', True, ['Ben 7.3', 'bob 7.2',
                                                    'bert 7.1']],
          [200, '1', 'scores_test_3.txt', True, ['15 5', '16 3', '200 1']],
          ['lamb', 23, '55.txt', True, ['sam 23', 'CAM@$! 22', 'lamb 23']]]

# Dictionary of filenames : whether they should exist or not
VERIFY = {'wordlist.txt':True, 'Wordlist.txt':True, 'WordList.txt':True,
          'wordlistt.txt':False, 'wordlist.py':False, 'dictionary.txt':False}

# List of lists
CHOOSE = [["run"], ["dog"], ["park"], ["Boston"], ["it's"], [""]]

# List of lists containing ordered information: user's guess, secret word,
# expected positions of the letters
VALIDATE = [['a', 'America', [0,6]],['', 'dog',[]],['T', 'Turtle',[0,3]],
            ["'", "it's",[2]],['-', 'far-out', [3]],['!', 'Hurray!',[6]]]

# Lists of  ordered information: secret word, length of the
# expected list generated by the function
CORRECT = [['dog', 3], ['', 0], ["it's", 4], ['Boston', 6], ['CS5001', 6]]

# List of lists: letters of a secret word as individual strings in a list,
# secret word
VICTORY = [[['d','o','g'], 'dog', True],[["i","t","'","s"], "it's", True],
           [['T','u','r','t','l','e'], 'Turtle', True],
           [[' ','d','o','g'], 'dog', False], [['d','o','g',' '], 'dog', False],
           [['b','o','s','t','o','n'], 'Boston', False]]

# List of lists containing sample wrong guesses, and boolean - if the player
# has lost yet
DEFEAT = [[[], False], [['j'], False], [['a','b'], False],
          [['x','y','z'], False], [["'",'-','!','6'], False],
          [['t','h','e','n'], False], [['q','w','e','r','t'], True],
          [['n','o','h','a','p','p','y'], True],
          [['l','o','s','t','g','a','m','e'], True]]

# List of lists containing numbers representing the numerical scores
# extracted from the scores.txt file, and the expected largest number
TOP_DOG = [[[3, 2, 1, 2, 3, 0], 3], [[7, 3, 5, 2], 7], [[], 0],
           [[0, 1, 3, 7, 2, 21], 21]]

# List containing strings that represent the lines of a scores.txt, and
# the expected highest integer. \n would already be stripped by extract function
COMPARE = [[['person 5', 'dog 2', 'cat 3', 'car 0'], 5],
           [['park 3', 'wrong 7', 'other 10'], 10],
           [['okay 9', 'epic 21', 'test 0'], 21], [[], 0],
           [['okay9', 'epic21', 'test0'], 0]]



# ------------------------------------------------------------------------------
# SUITE FUNCTIONS that expedite repetitive printing tasks

def announce(function_name):
    """
    Parameter: Name of the function, string. List of functions
    Does: Announces that a new function is being tested, removes the first
    position in the list so the argument can always be FUNCTIONS[0]
    Returns: Nothing
    """
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("\tTESTING FUNCTION:", function_name)

def stats(passed, failed, total):
    """
    Parameters: Number of tests passed, failed, and in total, all integers
    Does: Prints the statistics
    Returns: Nothing
    """
    print("\tPassed:", passed, "-- Failed:", failed, "-- Total:", total,
          "-- Viability:", int((passed/total) * 100), "%")


# ------------------------------------------------------------------------------
# TESTING SECTION where the spaceship.py module functions are tested

def main():

    # Inform the user the test suite is starting, initialize a variable to
    # use with announce() to let the user know which function is being tested
    which_test = 0
    print("\n\tWelcome to the spaceship.py module Test Suite\n")

    # Initialize variables that will accumulate testing statistics
    passed = 0
    failed = 0
    total = 0

    # 12 TESTS WILL BE RUN IN TOTAL
    
    # TEST 1: verify_existence
    # Input: dictionary VERIFY
    announce(FUNCTIONS[which_test])
    for key in VERIFY:
        print("Testing", key, "expecting", VERIFY[key], end="")
        total += 1
        if spaceship.verify_existence(key) == VERIFY[key]:
            print("...Success!")
            passed += 1
        else:
            print("...Failed")
            failed += 1
    which_test += 1
    stats(passed, failed, total)

    # TEST 2: extract
    # Input: dictionary EXTRACT
    announce(FUNCTIONS[which_test])
    for key in EXTRACT:
        print("\nTesting", key, "expecting", EXTRACT[key], end="")
        total += 1
        if spaceship.extract(key) == EXTRACT[key]:
            print("...Success!")
            passed += 1
        else:
            print("...Failed")
            failed += 1
    which_test += 1
    stats(passed, failed, total)

    # TEST 3: create
    # Input: list of lists CREATE
    # PREREQUISITES: extract and verify_existence must work correctly for this
    # test to be valid
    announce(FUNCTIONS[which_test])
    for five in CREATE:
        print("Testing", five[:3], "expecting", five[3], "&", five[4], end="")
        total += 1
        spaceship.create(five[0], five[1], five[2])
        if spaceship.verify_existence(five[2]) == True \
        and spaceship.extract(five[2]) == five[4]:
            print("...Success")
            passed += 1
        else:
            print("...Failed")
            failed += 1
    which_test += 1
    stats(passed, failed, total)

    # TEST 4: insert
    # Input: list of lists INSERT
    # PREREQUISITES: extract, verify_existence, and create must work correctly
    # for this test to be valid
    announce(FUNCTIONS[which_test])
    for five in INSERT:
        print("Testing", five[:3], "expecting", five[3], "&", five[4], end="")
        total += 1
        spaceship.insert(five[0], five[1], spaceship.extract(five[2]), five[2])
        if spaceship.verify_existence(five[2]) == True \
        and spaceship.extract(five[2]) == five[4]:
            print("...Success!")
            passed += 1
        else:
            print("...Failed")
            failed += 1
    which_test += 1
    stats(passed, failed, total)

    # TEST 5: pin_tail
    # Input: list of lists TAIL
    # PREREQUISITES: extract, verify_existence, create and insert must work
    # correctly for this test to be valid
    announce(FUNCTIONS[which_test])
    for five in TAIL:
        print("Testing", five[:3], "expecting", five[3], "&", five[4], end="")
        total += 1
        spaceship.pin_tail(five[0], five[1], five[2])
        if spaceship.verify_existence(five[2]) == True \
        and spaceship.extract(five[2]) == five[4]:
            print("...Success!")
            passed += 1
        else:
            print("...Failed")
            failed += 1
    which_test += 1
    stats(passed, failed, total)

    # TEST 6: choose_word
    # Input: list CHOOSE
    announce(FUNCTIONS[which_test])
    for item in CHOOSE:
        print("Testing", item, "expecting", item[0], end="")
        total += 1
        if spaceship.choose_word(item) == item[0]:
            print("...Success!")
            passed += 1
        else:
            print("...Failed")
            failed += 1
    which_test += 1
    stats(passed, failed, total)

    # TEST 7: validate_guess
    # Input: list of lists VALIDATE
    announce(FUNCTIONS[which_test])
    for triple in VALIDATE:
        print("Testing", triple[0], "in", triple[1], "expecting", triple[2],
              end="")
        total += 1
        if spaceship.validate_guess(triple[0], triple[1]) == triple[2]:
            print("...Success!")
            passed += 1
        else:
            print("...Failed")
            failed += 1
    which_test += 1
    stats(passed, failed, total)

    # TEST 8: populate_correct
    # Input: list of lists CORRECT
    announce(FUNCTIONS[which_test])
    for pair in CORRECT:
        print("Testing", pair[0], "expecting", pair[1], end="")
        total += 1
        if len(spaceship.populate_correct(pair[0])) == pair[1]:
            print("...Success!")
            passed += 1
        else:
            print("...Failed")
            failed += 1
    which_test += 1
    stats(passed, failed, total)

    # TEST 9: victory
    # Input: list of lists VICTORY
    announce(FUNCTIONS[which_test])
    for triple in VICTORY:
        print("Testing", triple[0], "expecting", triple[2], end="")
        total += 1
        if spaceship.victory(triple[0], triple[1]) == triple[2]:
            print("...Success!")
            passed += 1
        else:
            print("...Failed")
            failed += 1
    which_test += 1
    stats(passed, failed, total)

    # TEST 10: defeat
    # Input: List of lists DEFEAT
    announce(FUNCTIONS[which_test])
    for pair in DEFEAT:
        print("Testing", pair[0], "expecting", pair[1], end="")
        total += 1
        if spaceship.defeat(pair[0]) == pair[1]:
            print("...Success!")
            passed += 1
        else:
            print("...Failed")
            failed += 1
    which_test += 1
    stats(passed, failed, total)

    # TEST 11: top_dog
    # Input: list of lists TOP_DOG
    announce(FUNCTIONS[which_test])
    for pair in TOP_DOG:
        print("Testing", pair[0], "expecting", pair[1], end="")
        total += 1
        if spaceship.top_dog(pair[0]) == pair[1]:
            print("...Success!")
            passed += 1
        else:
            print("...Failed")
            failed += 1
    which_test += 1
    stats(passed, failed, total)

    # TEST 12: compare_scores
    # Input: list of lists COMPARE
    announce(FUNCTIONS[which_test])
    for pair in COMPARE:
        print("Testing", pair[0], "expecting", pair[1], end="")
        total += 1
        if spaceship.compare_scores(pair[0]) == pair[1]:
            print("...Success!")
            passed += 1
        else:
            print("...Failed")
            failed += 1
    which_test += 1
    stats(passed, failed, total)

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("\tTEST SUITE COMPLETE")
    stats(passed, failed, total)
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    
main()
