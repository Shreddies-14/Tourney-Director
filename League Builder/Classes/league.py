#Cameron Whyte
#League Builder
#This program will take various details about a desired layout of a league and create an Excel spreadsheet displaying the stats/details of the league. 
#29/05/2024

import itertools
import logging

logger = logging.getLogger(__name__)

class leagueClass:

    id_iter = itertools.count() #Creates a counter 

    def __init__(self):
        self.id = next(self.id_iter) #Creates unique ID
        logger.info('Created Class with unique ID {}'.format(self.id))

