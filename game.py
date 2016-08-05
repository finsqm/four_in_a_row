import numpy as np
from easyAI import TwoPlayersGame

class FourInARowGame(TwoPlayersGame):
    """
    """

    # ---------------------------------------------
    # Easy AI Methods
    # ---------------------------------------------

    def __init__(self, board):

        if len(players) == 2:
            self.players = players
        else:
            raise Exception('Must initialise game with two players, instead recieved {} players'.format(len(players)))

        self.initialise_board(board)

    def possible_moves(self):
        pass

    def make_move(self, move):
        pass

    def is_over(self):
        pass

    def show(self):
        pass

    def unmake_move(self, move):
        pass

    def scoring(self):
        pass

    # ---------------------------------------------
    # ---------------------------------------------

    def initalise_board(self, board):
        pass

class FourInARowGame_AIGames(FourInARowGame):
    
    def __init__(   
            self,
            timebank,
            time_per_move,
            player_names,
            your_bot,
            your_botid,
            field_columns,
            field_rows):

        super(FourInARowGame_AIGames, self).__init__(board)

    