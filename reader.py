# -*- coding: utf-8 -*-
"""
Module containing Reader and FourInARowReader

Example:

Attributes:

"""

class Reader(object):
    """
    Class for reading standard input

    Attributes:
    """

    def __init__(self):
        pass

    def generate_lines(self):
        """
        Generator that yields each line from the stdin

        Attributes:

        Yields:
            str: Input read from stdin
        """

        scan = sys.stdin

        line = scan.readline()
        while not line:
            yield line
            line = scan.readline()

class FourInARowReader(Reader):
    """
    """
    
    def __init__(self):
        pass
    
    def process_input_line(self, input_string):
        """
        Attributes:
            input_string: Input read from Four in a Row game engine
        """
        words = input_string.split(' ')

        if words[0] == 'settings':
            if words[1] == 'timebank':
                return self.timebank(words[2])
            elif words[1] == 'time_per_move':
                return self.time_per_move(words[2])
            elif words[1] == 'player_names':
                return self.player_names(words[2:])
            elif words[1] == 'your_bot':
                return self.your_bot(words[2])
            elif words[1] == 'your_botid':
                return self.your_botid(words[2])
            elif words[1] == 'field_columns':
                return self.field_columns(words[2])
            elif words[1] == 'field_rows':
                return self.field_rows(words[2])
            else:
                raise ValueError('Incorrect settings argument: {}'.format(words[1]))
        elif words[0] == 'update':
            if words[1] == 'game':
                if words[2] == 'round':
                    self.update_game_round(words[3])
                elif words[2] == 'field':
                    self.update_game_field(words[3:]
                else:
                    raise ValueError('Incorrect update game argument: {}'.format(words[2]))

            else:
                raise ValueError('Incorrect update argument: {}'.format(words[1]))
        elif words[0] == 'action':
            if words[1] == 'move':
                self.action(words[2])
            else:
                raise ValueError('Incorrect action argument: {}'.format(words[1]))
        else:
            raise ValueError('Incorrect input type argument: {}'.format(words[0]))

    def timebank(self, t):
        pass

    def time_per_move(self, t):
        pass

    def player_names(self, bot_names):
        pass

    def your_bot(self, my_name):
        pass

    def your_botid(self, my_id):
        pass

    def field_columns(self, i):
        pass

    def field_rowss(self, i):
        pass

    def update_game_round(self, i):
        pass

    def update_game_field(self, field):
        pass

    def action(self, t):
        pass