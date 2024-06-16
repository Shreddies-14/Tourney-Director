#Cameron Whyte
#League Builder
#This program will take various details about a desired layout of a league and create an Excel spreadsheet displaying the stats/details of the league. 
#29/05/2024

import logging
import datetime
import Classes.league as league


logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='League Builder/Logs/logs.log', level=logging.DEBUG)
    logger.debug("------------------------------------------------------------------------------------------------")
    logger.debug('Program Started at {}'.format(datetime.datetime.now(datetime.timezone.utc).strftime('%a, %d %b %Y %H:%M:%S GMT')))

#Define values
    userInput = 0
    validUserInput = False

#Welcome user
    print("Welcome to Cameron Whyte's League Builder!")
    print("Please enter the number of the action you want to perform.")
    print("1.Create a league")
    
    logger.info("Welcome complete waiting on user input")

#Get user input for what they want to do
    while not validUserInput: #Loop until valid input entered
        userInput = get_Valid_Integer("Enter the number!")

        if userInput > 0 and userInput < 2: #Check value is an enterable integer
            logger.info("User entered {}".format(userInput))
            validUserInput = True
            continue #Go back to start of loop

        logger.error("User entered {}, this was not an option".format(userInput))

    match int(userInput): #Matches the input to the correct function call
        case 1: #Create new league
            logger.info("Starting Creating a new League")
            newCreatedLeague = league.leagueClass() #This will create a new league table and write it to a CSV file
            newCreatedLeague.new_league()
    

    logger.debug('Program Finished at {}'.format(datetime.datetime.now(datetime.timezone.utc).strftime('%a, %d %b %Y %H:%M:%S GMT')) )

def get_Valid_Integer(outputString):
    validUserInput = False
    while not validUserInput: #Loop until valid input entered
        userInput = input(outputString)

        try: #Check value is a integer
            val = int(userInput)

        except ValueError: #If error
            logger.error("User entered {}, this threw an error".format(userInput))
            print("Invalid value entered please try again!")
            continue #Go back to start of loop
        
        return int(userInput)

if __name__ == '__main__':
    main()