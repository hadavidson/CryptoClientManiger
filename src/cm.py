#system imports
import os
#other imports
import pandas as pd
#my imports

class cm:
    def __init__(self):
        super().__init__()
        if(os.path.exists("./data/clients.csv")):
            self.clients = pd.read_csv("./data/clients.csv")
        else:
            self.clients = pd.DataFrame(columns=["First Name","Last Name","investment"])
            if(os.path.isdir("./data/")):
                self.clients.to_csv("./data/clients.csv")
            else:
                os.mkdir("./data/")
                self.clients.to_csv("./data/clients.csv")

    def addClient(self, first, last, initAmount):
        self.clients.loc[len(self.clients.index)] = [first, last, initAmount]
        self.clients.to_csv("./data/clients.csv")
        return(True)

    def removeClient(self, key):

        return(True)
    def findClientIndex(self, first, last):

        return(1)

    def getClietName(self, index):

        return("Harrison Davidson")

    def listClients(self):

        return("names lol")

    def getIndexRange(self):
        return(range(1,5))

    def addInvestmentToClient(self, key, amount):

        return(True)

    def withdrawalFromClient(self, key, amount):

        return(True)
    
    def getClientWorth(self, key):

        return(0)
