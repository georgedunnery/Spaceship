"""
George Dunnery
CS 5001
Homework 5 - Programming #2 - DRIVER
11/2/2018
"""

# Import the required module
import spaceship

# Define the source of the words chosen for the game
WORDS = 'wordlist.txt'
SCORES = 'scores.txt'

def main():

    # Welcome the user to the game, intitialize variables to run while loops
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("Welcome to Spaceship, a peaceful take on the classic Hangman!\n")
    playing = True
    instance = True

    # Keeps track of the user's score (number of games won)
    wins = 0

    # Use while loop to conintue playing until the user decides to quit
    while playing:

        # List of wrong guesses, secret word, list that will reveal the word
        # as the user makes correct guesses: must be reset after each match
        wrong = []
        guess_me = spaceship.choose_word(spaceship.extract(WORDS))
        correct = spaceship.populate_correct(guess_me)

        # Display the initial blank spaces
        spaceship.letter_lines(guess_me)

        # Nested while loop contains each individual match
        while instance:

            # Get valid input from the user
            user_guess = input("Guess a letter:\n")
            while len(user_guess) != 1:
                user_guess = input("Your guess must be a single character:\n")
            
            if user_guess.lower() in guess_me.lower():
                positions = spaceship.validate_guess(user_guess, guess_me)

                # Find the positions where the letter exists and reveal them!
                for location in positions:
                    correct[location] = guess_me[location]
                spaceship.reveal_correct(correct)

            # If they guessed wrong, add it to the list of bad guesses and
            # draw the next piece of the spaceship
            else:
                wrong.append(user_guess)
                spaceship.show_wrong(wrong)
                spaceship.artist(len(wrong))

            # Check if the user has guessed the word yet
            if spaceship.victory(correct, guess_me) == True:
                print("\nHurray, you won!")
                instance = False
                wins += 1
            # Check if the user has exceeded their 5 wrong guesses
            if spaceship.defeat(wrong) == True:
                print("\nOh no, you lost! The correct word was: " + guess_me)
                instance = False

        # Allow the player to quit or play again
        choice = input("\nWould you like to play again? Enter y/n:\n")
        while choice != 'y' and choice != 'n':
            choice = input("Please enter 'y' or 'n':\n")
        choice = choice.lower()

        # If the user decides to quit, break out of the while loops here
        if choice == 'n':
            playing = False
            cool_name = input("Enter your name for posterity:\n")
        elif choice == 'y':
            instance = True

    # Tell the player how many games they won before they leave
    print("You have won", wins, "game(s) in total!")
    
    # Check if the scores.txt file exists. If it doesn't, create it.
    if spaceship.verify_existence(SCORES) == False:
        spaceship.create(cool_name, wins, SCORES)

    # If it does exist, determine whether scores is appended or written
    else:
        leaderboard = spaceship.extract(SCORES)
        high_score = spaceship.compare_scores(leaderboard)
        if high_score < wins:
            spaceship.insert(cool_name, wins, leaderboard, SCORES)
        else:
            spaceship.pin_tail(cool_name, wins, SCORES)

    # Close the turtle screen and thank the player for participating
    spaceship.bye()  
    print("\nThanks for playing!")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    
main()
