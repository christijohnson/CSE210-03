from game import word_generator
import time
from time import sleep
name = input("Enter Your Name: ")
print(f"Hello {name.title()}")
print("Get ready!!") 
print ("")
time.sleep(0)
print ("Let's play Jumpman!")
time.sleep(0.0)

class Game_element:

    def __init__(self):
        self.word = word_generator.Word_Generator()
        self.player_guess = ""
        self.chances = 6 #let's update the real number
        self.guessed = False
      
    def jumpman_word(self, letter):
        word_to_guess = '_' * len(self.word)
        return word_to_guess
        

    def check_guess(self):       #  jumpman_word, letter   .get_word(self)
        if self.guess_letter not in self.word:  
            self.chances -= 1 
            self.guess_letter.append(self.guess_letter)
            # wrong_message = "Wrong guess! Try again"
            # return wrong_message 
        else:
            self.guess_letter in self.word
            self.guess_letter.append(self.guess_letter)
            # This to take the word that is to be guessed and to split it into single letters.
            word_as_list = list(self.word_to_guess)
            indices = [i for i, letter in enumerate(self.word) if letter == self.guess_letter]
            for index in indices:
                word_as_list[index] = self.guess_letter
            # This is to bring the single letters back into the word.
            self.word_to_guess = "".join(word_as_list)
            # When there is no more "_" in the word_to_guess variable, the word has been guessed correctly.
            if "_" not in self.word_to_guess:
                self.guessed = True
        return self.word_to_guess


            # return self.word_to_guess+self.letter

    def player_guess(self, guess_letter):
        guess_letter = []
        return guess_letter   