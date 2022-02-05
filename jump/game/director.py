from game.game_elements import Game_element
from game.word_generator import Word_Generator
from game.terminal_service import TerminalService
from game.draw_image import Jumper


class Director:
    """A person who directs the games.
    
    The responsibility of a Director is to control the squence of play.
    
    Attributes:
        draw_image (Jumper): Display the jumper in the various stages of the game.
        game_elements (Game_elements): 
        word_generator (Word_Generator): Gets a random word.
        terminal_services (TerminalService): For getting and displaying information on the terminal.
        is_playing (boolen): Wheather or not to keep playing
    """
    

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        self._draw_image = Jumper()
        self._game_elements = Game_element()
        self._word_generator = Word_Generator()
        self._terminal_services = TerminalService()
        self._is_playing = True

    def start_game(self):
        """Starts the game.
        
        Args:
            self (Director): an instance of Director."""
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            
    def _get_inputs(self):
        """Gets the guesses from the player
        
        Args:
            self (Director): an instance of Director."""

        guess = self._terminal_services.read_letters('Guess a letter [a-z]: ')
        # self._game_elements.random_word(guess)
        self._game_elements.guessed_letter(guess)

    def _do_updates(self):
        """Checks if letters guessed are in the hidden word.

        Args:
            self (Director): an instance of Director."""

        self._game_elements._check_letters()

    def _do_outputs(self):
        """Displays jumper image and any correctly guessed letters in the hidden word.

        Args:
            self (Director): an instance of Director."""

        display_word = self._game_elements.random_word()
        self._terminal_services.write_text(display_word)

        display_jumper = self._draw_image.display_image()
        self._terminal_services.write_draw(display_jumper)

        if self._game_elements.word_complete():
            self._terminal_services.write_text('Congrats, you won!')
            self._is_playing = False
#     def run_game_element(): = Game_element()
# run_game_element.get_game_elements()