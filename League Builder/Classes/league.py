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
        self.playerCount = main.get_Valid_Integer("How many players do you have?\n")
        self.divisionCount = main.get_Valid_Integer("How many divisions do you want?\n")
        logger.info("User entered {} for playerCount and {} for divisionCount!".format(self.playerCount, self.divisionCount))

        if self.playerCount/self.divisionCount >= 2:
            self._define_Divisions_Size() #Defines Division size and amount

                     
#Defining Divisions Size
    def _define_Divisions_Size(self):
        #Init value
        self.divisionPlayerSplit = [0] * self.divisionCount #Create array

        if self.playerCount/self.divisionCount >= 2: #Check there is more than 2 per division
            validTotalDivisionPlayerSplit = False

            while(not validTotalDivisionPlayerSplit): #Loop until a user is happy with entered values
                self._valid_Division_Splits()
                validTotalDivisionPlayerSplit = self._confirm_Choice() #Check they are happy with entered values

    def _valid_Division_Splits(self):
        #Init Values
        count = 0
        validDivisionPlayerSplit = True
        playersLeft = self.playerCount

        while (count < self.divisionCount and validDivisionPlayerSplit): #Loop until all divisions are valid 
            validDivisionPlayerSplit = self._check_PlayersLeft(playersLeft) #Confirms there is enough players left to create a division
            playersLeft, count = self._valid_Split(playersLeft, count) #Gets a valid split amount
            
    def _valid_Split(self, playersLeft, valid, x):
        #Init Values
        valid = False

        while (not valid): #Loop until valid split is entered
            userDivisionSplitInput = main.get_Valid_Integer("How many people do you want in division {}? (Players left:{})\n".format(x + 1, playersLeft))

            if userDivisionSplitInput <= playersLeft: #If input is a valid number
                self.divisionPlayerSplit[x] = userDivisionSplitInput #Update split array
                playersLeft = playersLeft - userDivisionSplitInput #Update players left

                valid = True
                x = x + 1

            else:
                print("Invalid Input please try again\n")
            
            return playersLeft, x

    def _confirm_Choice(self):
        #Init Values
        validConfirmation = False

        for i,x in enumerate(self.divisionPlayerSplit): #Loop through all splits to confirm inputs to user
            print("Division {} has {} players in it!\n".format(i + 1,x))

        while (not validConfirmation): #Loop until valid confirmation
            userComfirmationInput = input("If this is correct type 'YES' else type 'NO'!\n")

            if userComfirmationInput == "YES": 
                validConfirmation = True
                return True

            elif userComfirmationInput == "NO":
                validConfirmation = True

            else:
                print("Invalid input please try again\n")

    def _check_PlayersLeft(self, check):
        if (check < 2): #If there is less than 2 players then a valid division cannot be created
                valid = False
                print("Invalid split has been entered, please retry!\n")

        else:
            valid = True

        return valid
#Defining Divisions Size