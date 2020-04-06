# Author: Guðjón Ingi Valdimarsson
# Date: 06.04.2020
from os import system, name
from filefuncs import *
from random import Random
Random = Random()

# Constants for profile list
WINS = 0
LOSSES = 1
HISTORY = 2
SCORE = 3
NAME = 4

# File constants
WORDFILE = "words.txt"
PROFILEFILE = "profiles.txt"
FIGURESFILE = "sticks.txt"

# Menu ascii art
HANGMAN_STRING = """
 _   _
| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __
| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
|  _  | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/
"""

class Hangman():
    def __init__(self):
        self.wordlist = get_file_list(WORDFILE)             # Load words list
        self.sticklist = get_stickfigures(FIGURESFILE)      # Load stick figures list
        self.profiles = get_profiles(PROFILEFILE)           # Load saved profiles dict
        self.id = max(self.profiles) + 1                    # Get a new id based on older id's
        self.profiles[self.id] = [0, 0, [], 0, "Unsaved"]   # Add new empty profile to profiles dict
        self.profile_list = self.profiles[self.id]          # Profiles list to ease updating it
    
    def clear(self):
        """ A function that clears the terminal screen on either MAC, Linux or Windows """
        if name == "nt": # Windows clear
            system("cls")
        else:           # Linux and MAC clear
            system("clear")

# -------- Game functions --------
    def _check_word(self, word, guess):
        """ Checks if the word matches the guess or if a character in the word matches the guess """
        if word == guess:
            return word
        else:
            if guess in word:
                return True
        return False

    def _update_hidden(self, word, hidden, character):
        """ Updates hidden for every character that matches in word """
        hidden = list(hidden)
        for index in range(len(word)):
            if word[index] == character:
                hidden[index] = character
        return "".join(hidden)

    def _check_guess(self, guess, length):
        """ Checks if the guess is valid """
        if not guess.isalpha():
            print ("Only alphabetical letters allowed!")
            return False
        elif len(guess) > 1 and len(guess) != length:
            print ("Only guess one character or whole word!")
            return False
        else:
            return True

    def one_game(self, guesses):
        """ Takes in the ammount of allowed gusses and plays a game of hangman.
            Update profile at end with score """
        guessBool = False       # To print stick figures if 10 guesses are allowed
        if guesses == 10:      
            guessBool = True

        word = self.wordlist[Random.randint(0, len(self.wordlist) - 1)]
        hidden = "-" * len(word)

        while guesses != 0:
            print ("{}  You have {} guesses left".format(hidden, guesses))
            guess = input("Your guess (one character or whole word): ").lower()
            if self._check_guess(guess, len(hidden)):       # Check guess is valid i.e. 1 character or whole word
                check = self._check_word(word, guess)       # Check if word contains letter or if whole word == guess
                if check == word:
                    break
                elif check is True:
                    hidden = self._update_hidden(word, hidden, guess)
                    if hidden == word:
                        break
                    else:
                        print ("Great job that is a correct letter")
                else:
                    print ("That is not a letter in the word/that is not the word")
                    guesses -= 1
            self.clear()
            if guessBool:       # Prints stick figures if guesses allowed is 10
                print (self.sticklist[10 - guesses])

        if guesses == 0:        # If guesses run out you loose
            self.clear()
            print ("You ran out of guesses, you lost and the word was '{}'".format(word))
            print (self.sticklist[10])
            self._update_profile_score("Loss", -10)
        else:                   # If player wins
            print ("\nYou won, the word is '{}'".format(word))
            self._update_profile_score("Win", len(word) + guesses)
    
    def _update_profile_score(self, result_str, score):
        """ Takes in a result string and a score and updates the profile accordingly """
        if result_str == "Loss":
            self.profile_list[LOSSES] += 1
        else:
            self.profile_list[WINS] += 1
        self.profile_list[HISTORY].append(result_str)
        self.profile_list[SCORE] += score

    def play(self):
        """ Play games until user does not want to any more """
        while True:
            self.clear()
            guesses = int(input("How many guesses would you like to allow (10 for stick figures): "))
            self.one_game(guesses)
            play_another = input("Would you like to play another game? (y/n): ").lower()
            if play_another != "y":
                break

# -------- Add word to list and file --------
    def _add_word(self):
        """ Gets multiple inputs from user to add to the word list and if the
            user wishes it saves them to the words file """
        words_list = []
        while True:
            word = input("Type word to add (only alphabetical characters): ").lower()
            if word.isalpha():
                if word not in self.wordlist:
                    words_list.append(word)
                another = input("Do you want to add another word? (y/n): ").lower()
                if another != "y":
                    break
            else:
                print ("That is not a valid word, try again")
        self.wordlist.extend(words_list)
        savetofile = input("Save words to file? (y/n): ").lower()   # Check if word list should be saved to file
        if savetofile == "y":
            add_words_to_file(WORDFILE, words_list)

# -------- Menu functions --------
    def display_score(self):
        """ Displays score of current profile """
        self.clear()
        print ("Profile: {}\nWins: {}\nLosses: {}\nScore: {}\nHistory: {}".format(self.profile_list[NAME], self.profile_list[WINS], \
                self.profile_list[LOSSES], self.profile_list[SCORE], ", ".join(self.profile_list[HISTORY]).strip()))
        inp = input("Press enter to go back ")
    
    def _get_menu_key(self, num_options):
        """ Takes in an int of possible inputs, asks user to select and returns selection """
        while True:
                try:
                    user_input = input("\nSelect what you want to do (1-{}): ".format(num_options))
                    user_input = int(user_input)
                    if user_input < 1 or user_input > num_options:
                        raise ValueError()
                    break
                except ValueError:
                    print ("{} is not a valid option".format(user_input))
        return user_input
    
    def _profile_menu(self):
        """ Handles switching and saving of profiles """
        while True:
            self.clear()
            print ("1. Load profile\n2. Save current profile\n3. Back")
            key = self._get_menu_key(3)
            if key == 1:
                self.clear()
                print ("ID: Name")
                for pid, plist in self.profiles.items():
                    name = plist[NAME]
                    if pid == self.id:
                        print ("{}: {} (current)".format(pid, name))
                    else:
                        print ("{}: {}".format(pid, name))
                new_profile = self._get_menu_key(len(self.profiles))
                if not new_profile == self.id:
                    self.id = new_profile
                    self.profiles = get_profiles(PROFILEFILE)
                    self.profile_list = self.profiles[self.id]

            elif key == 2:
                if self.profile_list[NAME] == "Unsaved":
                    new_name = input("Set profile name: ")
                    self.profile_list[NAME] = new_name
                save_profiles(PROFILEFILE, self.profiles)

            else:
                break

    def menu(self):
        """ Main menu with options to play game, display score, view and change profiles and add words to word bank """
        while True:
            self.clear()
            print (HANGMAN_STRING)
            print ("1. Play game\n2. Display score and history\n3. Add word to word bank\n4. Profile menu\n5. Quit")
            key = self._get_menu_key(5)
            if key == 1:
                self.play()
            elif key == 2:
                self.display_score()
            elif key == 3:
                self._add_word()
            elif key == 4:
                self._profile_menu()
            else:
                sure_inp = input("Are you sure you want to quit? All unsaved progress will be lost (y/n): ").lower()
                if sure_inp == "y":
                    break

def main():
    game = Hangman()
    game.menu()

if __name__ == "__main__":
    main()