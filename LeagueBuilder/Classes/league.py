#Cameron Whyte
#League Builder
#This program will take various details about a desired layout of a league and create an Excel spreadsheet displaying the stats/details of the league. 
#29/05/2024

import itertools
import logging
import pandas
import main
import Classes.player as plyr


print(pandas.__file__)
pandas.__version__

logger = logging.getLogger(__name__)

class leagueClass:

    id_iter_league = itertools.count() #Creates a counter 
    leagueOutput = []

    def __init__(self):
        self.id = next(self.id_iter_league) #Creates unique ID
        logger.info('Created League Class with unique ID {}'.format(self.id))

    def new_league(self):
        #This will create a brand new league from scratch asking questions about it
        print("Welcome to the new league builder!\n")
        logger.info("New league builder started!")

        self._get_User_Division_Size()

        #Get all players
        self._get_Player_Details()

#Setting up players
    def _get_Player_Details(self):
        self.players = []
        for x in range(self.playerCount):
            self.players.append(plyr.playerClass())
        logger.info("All players objects created")
        
        self._get_Player_Names()
        self._get_Player_Division()
        self._create_player_list()

    def _get_Player_Names(self):
        valid = False
        playerNamesFilePath = "LeagueBuilder/ReadableFiles/playerNames.txt"
        playerNameFile = open(playerNamesFilePath, "r")
        """
        while (not valid):
            try:
                playerNamesFilePath = "LeagueBuilder/ReadableFiles/" + input("Please enter the name of the file that contains player names! (File in ReadableFiles)\n")
                playerNameFile = open(playerNamesFilePath, "r")
                valid = True
                logger.info("Getting names from {}".format(playerNamesFilePath))

            except:
                print("Invalid file please try again!\n")
                logger.info("Invalid path entered for player names file: {}".format(playerNamesFilePath))
                valid = False
        """
        for x in range(self.playerCount):
            self.players[x].set_name(playerNameFile.readline().rstrip("\n"))

    def _get_Player_Division(self):
        valid = False
        playerDivisionFilePath = "LeagueBuilder/ReadableFiles/playerDivisions.txt"
        playerDivisionFile = open(playerDivisionFilePath, "r")
        """
        while (not valid):
            try:
                playerDivisionFilePath = "LeagueBuilder/ReadableFiles/" + input("Please enter the name of the file that contains player division! (File in ReadableFiles)\n")
                playerDivisionFile = open(playerDivisionFilePath, "r")
                valid = True
                logger.info("Getting names from {}".format(playerDivisionFilePath))
                
            except:
                print("Invalid file please try again!\n")
                logger.info("Invalid path entered for player names file: {}".format(playerDivisionFilePath))
                valid = False
        """
        for x in range(self.playerCount):
            self.players[x].set_division(playerDivisionFile.readline())

    def _create_player_list(self):
        self.playerListDic = {
            "ID" : [],
            "Name" : [],
            "Paid" : []
            }
        
        for x in self.players:
            self.playerListDic["ID"].append(x.id)
            self.playerListDic["Name"].append(x.name)
            self.playerListDic["Paid"].append('N')
        
        playerDF = pandas.DataFrame(self.playerListDic)

        playerDF.to_excel("LeagueBuilder/Outputs/league.xlsx", index=False)

#Defining Divisions Size
    def _get_User_Division_Size(self):
        #Define Division sizing
        valid = False
        while (not valid):
            #Get values
            self.playerCount = main.get_Valid_Integer("How many players do you have?\n")
            self.divisionCount = main.get_Valid_Integer("How many divisions do you want?\n")
            logger.info("User entered {} for playerCount and {} for divisionCount!".format(self.playerCount, self.divisionCount))

            if self.playerCount/self.divisionCount >= 2: #Check if it is possible to have valid splits
                self._define_Divisions_Size() #Defines Division size and amount
                valid = True
            else:
                print("Invalid values entered! Please try again!")
                logger.info("The values entered are invalid numbers!")

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
            validDivisionPlayerSplit = self._check_PlayersLeft(playersLeft, count) #Confirms there is enough players left to create a division
            playersLeft, count = self._valid_Split(playersLeft, count) #Gets a valid split amount
            
    def _valid_Split(self, playersLeft, x):
        #Init Values
        valid = False

        while (not valid): #Loop until valid split is entered
            userDivisionSplitInput = main.get_Valid_Integer("How many people do you want in division {}? (Players left:{})\n".format(x + 1, playersLeft))

            if userDivisionSplitInput <= playersLeft and userDivisionSplitInput > 1: #If input is a valid number
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

    def _check_PlayersLeft(self, check, x):
        if (check < 2 * (self.divisionCount - x)): #If there is less than 2 players then a valid division cannot be created
                valid = False
                print("Invalid split has been entered, please retry!\n")

        else:
            valid = True

        return valid
#Defining Divisions Size