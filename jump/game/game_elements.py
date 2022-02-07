from game.word_generator import Word_Generator
import time
from time import sleep

name = input("Enter Your Name: ")
print(f"Hello {name.title()}")
print("Get ready!!") 
print ("")
time.sleep(1)
print ("Let's play Jumpman!")
time.sleep(0.5)

class Game_element:
    """ Class controls the elements of the jumpman game
        Args - choose word, player guess, chances, guessed, word to guess, word
    """
    def __init__(self):
        self.chose_word = Word_Generator()
        self.player_guess = []
        self.chances = 5 
        self.guessed = False
        self.word_to_guess = ''
        self.word = ''


    def jumpman_word(self):
        """ Gets the random word and prints underscore for length of word
            Args - self
            Return - underscore for length of word to guess
            """
        word = self.chose_word.get_word()
        self.word = word
        self.word_to_guess = '_' * len(word)
        return self.word_to_guess


    def check_guess(self):
        """ Checks for correct letters, keeps track of number of guesses
            Args - self
            Return - the number of chances for the player, correct letters
            """
        while  not self.guessed and self.chances > 0:
            if self.player_guess not in self.word:  
                self.chances -= 1 
            else:
                self.player_guess in self.word
                # This to take the word that is to be guessed and to split it into single letters.
                word_as_list = list(self.word_to_guess)
                indices = [i for i, letter in enumerate(self.word) if letter == self.player_guess]
                for index in indices:
                    word_as_list[index] = self.player_guess
                # This is to bring the single letters back into the word.
                self.word_to_guess = "".join(word_as_list)               
            return self.word_to_guess


    def word_complete(self):
        """ Checks to see of the players guesses match the word
            Args - self
            Returns - true if matched
        """
        if self.word_to_guess == self.word:
            return True
    

    def get_guess(self, letter):
        """ Args - self and letter
        """
        self.player_guess = letter   