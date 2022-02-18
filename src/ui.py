#system imports
import os
#other imports

#my imports
import src.cm

class ui:
    ccm1 = src.cm.cm()

    def __init__(self):
        super().__init__()

    def clearScreen(self):
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        else:
            command = 'clear'
        os.system(command)

    def checkIfNumber(self, name:str):
        while(True):
            num = input(name+": ")
            try:
                num = float(num)
                return(num)
            except:
                print(name+" must be a number.")
        


    def getInput(self):
        userIn = self.checkIfNumber("Selection")
        if userIn in range(1,9):
            output = ""
            if(userIn==1):
                first = input("First Name: ")
                last = input("Last Name: ")
                if(self.ccm1.addClient(first, last)):
                    output = "Successfully added "+first+" "+last+" at index "+str(self.ccm1.findClientIndex(first,last))
                else:
                    output = "Failed to add client."
            elif(userIn == 2):
                clientIndex = self.checkIfNumber("Client Index Number")
                if(self.ccm1.removeClient(clientIndex)):
                    output = ("Successfully removed client")
                else:
                    output = ("Failed to removed client.")
            elif(userIn == 3):
                output = (self.ccm1.listClients())
            elif(userIn == 4):
                clientIndex = self.checkIfNumber("Client Index Number")
                addAmount = self.checkIfNumber("Deposit ammount")
                if(self.ccm1.addInvestmentToClient(clientIndex,addAmount)):
                    output = ("Successfully Deposited $"+str(addAmount)+" to "+self.ccm1.getClietName(clientIndex))
                else:
                    output = ("Failed to Deposit $"+str(addAmount)+" to client.")
            elif(userIn == 5):
                clientIndex = self.checkIfNumber("Client Index Number")
                withdrawalAmount = self.checkIfNumber("Ammount to withdrawal")
                if(self.ccm1.withdrawalFromClient(clientIndex,withdrawalAmount)):
                    output = ("Successfully withdrew $"+str(withdrawalAmount)+" from "+self.ccm1.getClietName(clientIndex))
                else:
                    output = ("Failed to withdrawal $"+str(withdrawalAmount)+" from client.")
            elif(userIn == 6):
                clientIndex = self.checkIfNumber("Client Index Number")
                currentWorth = self.checkIfNumber("Current Worth")
                output = (self.ccm1.getClietName(clientIndex)+" is worth: "+str(self.ccm1.getClientWorth(clientIndex,currentWorth)))
            elif(userIn == 7):
                output = "Welcome to the CRM"
            elif(userIn == 8):
                self.clearScreen()
                print("Good bye!")
                exit()

            self.clearScreen()
            # if(output!=""):
            print(output)
            self.drawUI(clear=False)
                
        else:
            self.drawUI(bad=True)

    def drawUI(self, bad=False, clear=True):
        if(clear):
            self.clearScreen()
            print("Welcome to the CRM")
        if(bad):
            print("Bad input try again.")
        print("1: Add Client          ||  4: Deposit To Client")
        print("2: Remove Client       ||  5: Withdrawal From Client")
        print("3: List All Clients    ||  6: Get Client Worth")
        print("7: Clear Screen        ||  8: Exit")
        self.getInput()