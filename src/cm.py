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
            self.clients.drop(self.clients.columns[0],axis=1,inplace=True)
        else:
            self.clients = pd.DataFrame(columns=["First Name","Last Name","investment","percent"])
            if(os.path.isdir("./data/")):
                self.saveClients()
            else:
                os.mkdir("./data/")
                self.saveClients()

    def saveClients(self):
        self.clients.to_csv("./data/clients.csv")

    def addClient(self, first, last):
        try:
            self.clients.loc[len(self.clients.index)] = [first, last, 0,0]
            self.saveClients()
            return(True)
        except:
            return(False)

    def removeClient(self, key):
        try:
            self.clients.drop(key,inplace=True)
            self.saveClients()
            return(True)
        except:
            return(False)
    def findClientIndex(self, first, last):
        return(self.clients.index[(self.clients['First Name']==first)&(self.clients['Last Name']==last)].tolist()[0])

    def getClietName(self, index):
        try:
            return(self.clients.loc[index,'First Name'])
        except:
            return("No client found.")

    def listClients(self):
        return(self.clients)

    def getIndexRange(self):
        return(range(1,5))

    def addInvestmentToClient(self, index, amount):
        try:
            cI = int(self.clients.loc[index,'investment'])
            self.clients.at[index,"investment"] = cI+amount
            self.saveClients()
            return(True)
        except:
            return(False)

    def withdrawalFromClient(self, index, amount):
        try:
            cI = int(self.clients.loc[index,'investment'])
            self.clients.at[index,"investment"] = cI-amount
            self.saveClients()
            return(True)
        except:
            return(False)
    
    def getClientWorth(self, index,currentTotal):
        totalInvestemnt = self.clients["investment"].sum()
        clientInvestment = self.clients.loc[index,'investment']
        clientPercent = clientInvestment/totalInvestemnt
        return(currentTotal*clientPercent)
