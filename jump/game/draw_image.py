from game.game_elements import Game_element


class Jumper:
    def __init__(self):
        """This is the constructor method and we are building the image here and set it as a list"""

        self._game_elements = Game_element()
        self.chances = self._game_elements.chances

    def _display_image(self, chances):
        """ This is the list where we are taking the chances from the Game_element class
        as an index, so we can take the correct picture"""

        self.jumper_image = [
        """         
                  
                  
                   
                 x     
                /|\    
                / \    
                       
            ^^^^^^^^^^^ """,
        """         
                  
                  
                   
                 o     
                /|\    
                / \    
                       
            ^^^^^^^^^^^ """,
        """         
                  
                  
                \ /    
                 o     
                /|\    
                / \    
                       
            ^^^^^^^^^^^ """,
        """         
                 
               \   /   
                \ /    
                 o     
                /|\    
                / \    
                       
            ^^^^^^^^^^^ """,
        """         
               /___\   
               \   /   
                \ /    
                 o     
                /|\    
                / \    
                       
            ^^^^^^^^^^^ """,
        """ 
                ___    
               /___\   
               \   /   
                \ /    
                 o     
                /|\    
                / \    
                       
            ^^^^^^^^^^^ """,
            ]
        return self.jumper_image[chances]
