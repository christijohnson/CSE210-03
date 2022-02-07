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
        self._game_elements.jumpman_word()
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            
    def _get_inputs(self):
        """Gets the guesses from the player
        
        Args:
            self (Director): an instance of Director."""
        
        guess = self._terminal_services.read_letters('Guess a letter [a-z]: ')
        self._game_elements.get_guess(guess)
        

    def _do_updates(self):
        """Checks if letters guessed are in the hidden word.

        Args:
            self (Director): an instance of Director."""
        
        self._game_elements.check_guess()
        self._game_elements.word_complete()
        
        

    def _do_outputs(self):
        """Displays jumper image and any correctly guessed letters in the hidden word.

        Args:
            self (Director): an instance of Director."""
        word_to_guess = self._game_elements.word
        chances = self._game_elements.chances
        self._terminal_services.write_text(f'Number of chances left: {chances}')

        display_word = self._game_elements.word_to_guess
        self._terminal_services.write_text(display_word)

        display_jumper = self._draw_image.display_image(chances)
        self._terminal_services.write_draw(display_jumper)

        if self._game_elements.word_complete() == True:
            self._terminal_services.write_text('Congrats, you won!')
            self._is_playing = False
        elif chances == 0:
            self._terminal_services.write_text(f'Sorry, you did not make it! The word was {word_to_guess}.')
            self._is_playing = False
