#Cameron Whyte
#League Builder
#This program will take various details about a desired layout of a league and create an Excel spreadsheet displaying the stats/details of the league. 
#29/05/2024

import logging
import Classes.league as league
import datetime

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='League Builder/Logs/logs.log', level=logging.INFO)
    logger.info('Program Started at {}'.format(datetime.datetime.now(datetime.timezone.utc).strftime('%a, %d %b %Y %H:%M:%S GMT')))
    logger.info('Program Finished at {}'.format(datetime.datetime.now(datetime.timezone.utc).strftime('%a, %d %b %Y %H:%M:%S GMT')) )

if __name__ == '__main__':
    main()