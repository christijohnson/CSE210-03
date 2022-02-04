class Jumper:

    def __init__(self):
        """This is the constructor method and we are building the image here and set it as a list"""
        self.jumper_image = [
            "    ___    ",
            "   /___\   ",
            "   \   /   ",
            "    \ /    ",
            "     o     ",
            "    /|\    ",
            "    / \    ",
            "           ",
            "^^^^^^^^^^^",
            ]  
    def display_image(self):
        """This is how the user will see the image correctly through the loop"""
        for image in self.jumper_image:
            print(image) 

    def delete_line(self):
        """ This function is supposed to delete the first line of the jumper_image"""
        self.jumper_image.pop(0)
        
    def jumper_is_dead(self):
        """This is only used when the player has not guessed the word for 5 attempts"""
        self.jumper_image = [
            "     x     ",
            "    /|\    ",
            "    / \    ",
            "           ",
            "^^^^^^^^^^^",
            ] 
        for image in self.jumper_image:
            print(image) 