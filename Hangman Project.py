"""
Purpose: To practice using loops, string accumulators, functions, and recursion.
Program Information: This recursive program allows the user to play the game Hangman. The user is allowed to keep guessing letters, untill they guess the word or run out of guesses.
Authors: Phan Anh Le
Date: April 7, 2023
CS111
"""

import string                                                               #Importing the string package -- because it will be needed later on in the program

def hangman(word, filled_word, guess, letters):                             #Defining our function, with its parameters
    '''
    Purpose: To allow the user to play Hangman game, prompting them to guess letters and reveal correct guesses while deducting guesses for incorrect ones.
    
    Parameters:
    word: The word to be guessed. (string)
    filled_word: A string that represents the word to be guessed with underscores in place of the letters. (string)
    guess: The number of guesses the user has. (integer)
    letters: A string of available letters to guess. (string)

    Return Value: None
    '''
    if not isinstance(word,str):
        return False
    if not isinstance(filled_word,str): 
        return False 
    if not isinstance(guess, int) or guess < 0: 
        return False
    if not isinstance (letters, str): 
        return False
    
    letters_list = list(letters)
    

    if guess == 0:                                                          #Setting our base case, so that our function will end once the user reaches zero guesses -- keeping the function from continous infinite recursion
        print("You lose. The correct word is " + word)                      #Telling the user that they had ran out of guesses and the correct word before we return and end the program
        return
    
    if filled_word == word:                                                 #When the filled word (what the user is guessing) is equal to the word, we are printing a message telling the user that they have guesses the whole word correctly
        print ("Congratulations, you won!")
        return


    if letters == string.ascii_lowercase:                                   #Setting letters equal to the built in alphabet function -- allowing us to not have to type all of them in manually
        filled_word = len(word) * "-"                                       #To print the empty letters as dashes, first take the length of our word, and making the empty filled_word spring to have that number of dashes


    print ("You have " + str(guess) + " guesses left")                      #Updating the user on how many guesses they have left
    print ("Available letters: " + letters)                                 #Printing the letters that the user has availble to choose from

    guess_letter = input("Please guess a letter: ").lower()                 #Getting user input for which letter they will be guessing each time

    
    if guess_letter not in letters_list:                                    #Checking to see if the users guess is a letter using the in function, if it is not the correct type input (not a letter), the program will print invalid input to the screen
        print ("The letter is invalid")                     
        print ("Please try again!")
        print ("-" * 12 )                                                   #Creating a boarder of dashes to seperate each round of the game
        hangman(word, filled_word, guess, letters)                          #Using recursion to call the function again, allowing the user to enter the next round of guesses. We are not removing a guess when they dont guess a valid letter

        
    elif guess_letter in word:                                              #Checking to see if the users guess is in the word using the in function
        for n in range (len(word)):                                         #Creating a loop to run through each letter in the word
            if guess_letter == word[n]:                                     #If the letters match up, we are updating our filled word (the empty dashes) to portray the letter in the correct place
                filled_word = filled_word[:n] + guess_letter + filled_word[n+1:]        #The process/code we are using to do what is mentioned above
        print ("Good guess: " + filled_word )                                           #Telling the user that their letter was in the word, and printing the filled word to the screen, so they are able to see where the letter they guesses is in the word
        new_letters = letters.replace(guess_letter, "")                     #Updating the users available letters to guess from, by replacing the guessed letter with "" (nothing)
        print ("-" * 12)                                                    #Creating the boarder before sending the user to the next round of guesses
        hangman(word, filled_word, guess, new_letters)                      #Using recursion to call the game again, allowing the user to make their next guess

    else:                                                                   #Using an else for when the user made a guess with the correct input (a letter that is available still), but it is not in the word
        print("Oops! That letter is not in my word: " + filled_word)        #Telling the user that the letter is not in the word, and reprinting their filled_word to the screen
        new_letters = letters.replace(guess_letter, "")                     #Updating our new_letters variable to take out their incorrect guess from their choices of available letters
        print ("-" * 12)                                                    #Creating the boarder to signify a new round
        hangman(word, filled_word, guess-1, new_letters)                    #Calling our function again using recursion, but this time we are removing a guess from the users available guesses




def main():                                                                 #Defining our main function
    '''
    Purpose: Calls main function to run the code
    Parameters: 
    word: the word to be guessed. (string)
    Return Value: None
    '''
    word = "tact"                                                           #Defining what the word will be in the game
    print ("Welcome to the game, Hangman!")                                 #Here we are introducing the game do that it only displays to the screen once
    print ("I am thinking of a word that is " + str(len(word)) + " letters long.")
    letters = string.ascii_lowercase                                        #Defining letters to be the built-in string function of the alphabet, before we call it in our function
    hangman(word, "", 8, letters)                                           #Calling our recursive function

if __name__ == "__main__":
    main()                                                                  #Calling our main function









