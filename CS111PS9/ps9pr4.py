#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """“intelligent” computer player 
    """
    
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.checker = checker
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """returns a string representing an AIPlayer object. This method 
        will override/replace the __repr__ method that is inherited from 
        Player. In addition to indicating which checker the AIPlayer object 
        is using, the returned string should also indicate the player’s 
        tiebreaking strategy and lookahead
        """
        
        return "Player " + self.checker + " (" +self.tiebreak+', '+ str(self.lookahead) +')'
    
    def max_score_column(self, scores):
        """takes a list scores containing a score for each column of the board,
        and that returns the index of the column with the maximum score. 
        If one or more columns are tied for the maximum score, the method 
        should apply the called AIPlayer‘s tiebreaking strategy to break the tie
        """   
        x = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                x += [i]
        if self.tiebreak == 'LEFT':
            return x[0]
        elif self.tiebreak == 'RIGHT':
            return x[-1]
        else:
            return random.choice(x)
    def scores_for(self, b):
        """takes a Board object b and determines the called AIPlayer‘s scores 
        for the columns in b. Each column should be assigned one of the four
        possible scores discussed in the Overview at the start of this problem, 
        based on the called AIPlayer‘s lookahead value. The method should return 
        a list containing one score for each column
        """
        scores = [50] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker,col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                opp_scores = opponent.scores_for(b)
                if max(opp_scores) == 100:
                    scores[col] = 0
                if max(opp_scores) == 50:
                    scores[col] = 50
                if max(opp_scores) == 0:
                    scores[col] = 100
                b.remove_checker(col)
        
        return scores
                
        """if col is full:
            use -1 for scores[col]
        elif already win/loss:
            use appropriate score (100 or 0)
        elif lookahead is 0:
            use 50 
        else:
            try col – adding a checker to it
            create an opponent with self.lookahead – 1 
            opp_scores = opponent.scores_for(...) 
            scores[col] = ???
            remove checker
     return scores"""
    def next_move(self, b):
        """overrides (i.e., replaces) the next_move method that is inherited 
        from Player. Rather than asking the user for the next move, this 
        version of next_move should return the called AIPlayer‘s judgment 
        of its best possible move. This method won’t need to do much work,
        because it should use your scores_for and max_score_column methods 
        to determine the column number that should be returned
         """
        self.num_moves += 1
        x = self.scores_for(b)
        return self.max_score_column(x)

        





















