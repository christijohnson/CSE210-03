from game import word_generator
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

    def __init__(self):
        self.word = word_generator.Word_Generator()
        self.player_guess = ""
        self.chances = 6 #let's update the real number
      
    def jumpman_word(self, letter):
        for letter in self.word:      
                if letter in self.word:    
                    return letter  
                else:
                    return("_")  

    def player_guess(self, jumpman_word, letter):          
        if letter not in self.word.get_word(self):  
            self.chances -= 1 
            wrong_message = "Wrong guess! Try again"
            return wrong_message 
        elif letter in self.word.get_word(self):
            return jumpman_word+letter
                