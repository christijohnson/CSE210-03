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

    def get_game_elements(self):
        jumpman_word = ''
        chance = 10
        while chance > 0:         
            failed = 0            
            for letter in self.word.get_word(self):      
                if letter in jumpman_word:    
                    return letter  
                else:
                    print( "_")    
                    failed += 1   
            if failed == 0:        
                winning_message = (f"You Won, Congratulations, {name.title()}!" ) 
                return winning_message
                           
            guess = input("Guess a letter:").strip().lower()
            jumpman_word = jumpman_word+guess                    
            if guess not in self.word.get_word(self):  
                chance -= 1 
                wrong_message = "Wrong guess! Try again"
                chances_reminding = (f"You have {chance} chances reminding.")
                return wrong_message,chances_reminding
            elif chance == 0:           
                game_over = "You Lose! Better Luck Next Time"
                return game_over
                