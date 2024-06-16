#Cameron Whyte
#League Builder
#This program will take various details about a desired layout of a league and create an Excel spreadsheet displaying the stats/details of the league. 
#29/05/2024

import itertools
import logging
import pandas
import main

pandas.__version__
logger = logging.getLogger(__name__)

class playerClass:
    id_iter_player = itertools.count() #Creates a counter 

    def __init__(self):
        self.id = next(self.id_iter_player) #Creates unique ID
        logger.info('Created Player Class with unique ID {}'.format(self.id))