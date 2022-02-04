from game_elements import Game_element
from word_generator import Word_Generator


class Director:
    def __init__(self):
        # self.draw_image = draw
        self.game_elements = Game_element()
        self.word_generator = Word_Generator()
        # self.terminal_services = terminal_services()
        self.is_playing = True

    def start_game(self):
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            
    def get_inputs(self):
        pass

    def do_updates(self):
        pass

    def do_outputs(self):
        pass

#     def run_game_element(): = Game_element()
# run_game_element.get_game_elements()