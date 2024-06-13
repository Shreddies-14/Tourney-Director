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

class leagueClass:

    id_iter = itertools.count() #Creates a counter 
    leagueOutput = []

    def __init__(self):
        self.id = next(self.id_iter) #Creates unique ID
        logger.info('Created Class with unique ID {}'.format(self.id))

    def new_league(self):
        #This will create a brand new league from scratch asking questions about it
        print("Welcome to the new league builder!\n")
        logger.info("New league builder started!")

        #Get values
        playerCount = main.get_Valid_Integer("How many players do you have?\n")
        divisionCount = main.get_Valid_Integer("How many divisions do you want?\n")
        logger.info("User entered {} for playerCount and {} for divisionCount!".format(playerCount, divisionCount))


        #Init values
        divisionPlayerSplit = [divisionCount]
        playersLeft = playerCount
        validTotalDivisionPlayerSplit = False
        validDivisionPlayerSplit = True

        if playerCount/divisionCount >= 2: #Check there is more than 2 per division
            while(not validTotalDivisionPlayerSplit): #Loop until a valid splits is entered
                x = 0

                while (x < divisionCount and validDivisionPlayerSplit): #Loop until all divisions are valid 
                    validUserInput = False

                    if (playersLeft < 2): #If there is less than 2 players then a valid division cannot be created
                        validDivisionPlayerSplit = False
                        print("Invalid split has been entered, please retry!\n")

                    while (not validUserInput): #Loop until valid split is entered
                        userDivisionSplitInput = main.get_Valid_Integer("How many people do you want in division {}? (Players left:{})\n".format(x + 1, playersLeft))

                        if userDivisionSplitInput <= playersLeft: #If input is a valid number
                            
                            divisionPlayerSplit[x] = userDivisionSplitInput
                            playersLeft = playersLeft - userDivisionSplitInput

                            validUserInput = True
                            x = x + 1

                        else:
                            print("Invalid Input please try again\n")

                for x,i in enumerate(divisionPlayerSplit): #Loop through all splits to confirm inputs to user
                    print("Division {} has {} players in it!\n".format(i + 1,x))
                
                validConfirmation = False

                while (not validConfirmation): #Loop until valid confirmation
                    userComfirmationInput = input("If this is correct type 'YES' else type 'NO'!\n")

                    if userComfirmationInput == "YES": 
                        validConfirmation = True
                        validTotalDivisionPlayerSplit = True

                    elif userComfirmationInput == "NO":
                        validConfirmation = True

                    else:
                        print("Invalid input please try again\n")




