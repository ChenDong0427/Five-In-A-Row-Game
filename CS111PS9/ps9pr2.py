#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.
class Player:
    """A Player
    """

    def __init__(self, checker):
        """constructs a new Player object by initializing the following two attributes:

an attribute checker – a one-character string that represents the gamepiece for the player, as specified by the parameter checker

an attribute num_moves – an integer that stores how many moves the player has made so far. This attribute should be initialized to zero to signify that the Player object has not yet made any Connect Four moves.
        """
        assert(checker == 'X' or checker == 'O')
        self.num_moves = 0
        self.checker = checker
    
    def __repr__(self):
        """returns a string representing a Player object. The string returned 
            should indicate which checker the Player object is using. For example
            """
        if self.checker == 'X':
            return 'Player X'
        else:
            return 'Player O'
    def opponent_checker(self):
        """returns a one-character string representing the checker of the 
        Player object’s opponent. The method may assume that the calling 
        Player object has a checker attribute that is either 'X' or 'O'
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
    def next_move(self, b):
        """accepts a Board object b as a parameter and returns the column 
        where the player wants to make the next move. To do this, the method 
        should ask the user to enter a column number that represents where 
        the user wants to place a checker on the board. The method should 
        repeatedly ask for a column number until a valid column number is given
        """
        while True:
            x = int(input('Enter a column: '))
            if b.can_add_to(x) == True:
                self.num_moves += 1
                return x
            else:
                print('Try again!')















