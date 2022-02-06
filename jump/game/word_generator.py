#Generator
import random
# from game import director (is this needed?)

class Word_Generator:
    # add the variable and store in a list
    def __init__(self):
        self.word = ''

    def get_word(self):  
        # random word from candidates  
        candidates = [
            'cloud', 'hydrogen', 'laugh', 'smile', 'toothbrush', 'class', 'game', 'sunshine', 'galaxy', 'telephone'
            'puzzle', 'assignment', 'vacation', 'awkward', 'blizzard', 'fuchsia', 'jovial', 'mnemonic', 'transplant',
            'waltz', 'stretch', 'zombie', 'pineapple', 'beach', 'cello', 'ticket', 'spinkler', 'lighthouse',
            'suitcase', 'coconut', 'shark', 'sunflower', 'password', 'landscape', 'drawback', 'gasoline',
            'shampoo', 'chess', 'picnic', 'applause', 'nightmare', 'loveseat', 'charger', 'cabin'
        ]
        self.word = random.choice(candidates)
        return self.word



   