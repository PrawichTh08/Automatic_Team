playersal = []
import random

# t# is place holder for unknown player (Not-Regitesd)
# 19 Players In System

def checkplayer(): 
    playerinput = input("Player Code : ")
    if playerinput not in playersal:
        playersal.append(playerinput)
        playernow = playerinput
        print("Loading...")
        #Tier4 vvv
        #t4 for Devlopers
        if playerinput == ("t4"):
            playerinput = int(4)
        #-----t4for Devlopers-----end
        if playerinput == ("tlk"):
            playerinput = int(4)
        if playerinput == ("lvi"):
            playerinput = int(4)
        if playerinput == ("kin"):
            playerinput = int(4)
            #Tier3 vvv
        if playerinput == ("tcn"):
            playerinput = int(3)
        if playerinput == ("t3"):
            playerinput = int(3)
        if playerinput == ("ryu"):
            playerinput = int(3)
        if playerinput == ("ran"):
            playerinput = int(3)
        if playerinput == ("vor"):
            playerinput = int(3)
        if playerinput == ("por"):
            playerinput = int(3)
        if playerinput == ("hro"):
            playerinput = int(3)
        if playerinput == ("ntb"):
            playerinput = int(2)
        if playerinput == ("nle"):
            playerinput = int(2)
        if playerinput == ("ska"):
            playerinput = int(3)
            #Tier2 vvv
        if playerinput == ("nle"):
            playerinput = int(2)
        if playerinput == ("t2"):
            playerinput = int(2)
        if playerinput == ("pan"):
            playerinput = int(2)
        if playerinput == ("sen"):
            playerinput = int(2)
        if playerinput == ("nut"):
            playerinput = int(2)
        if playerinput == ("zch"):
            playerinput = int(2)
        if playerinput == ("shm"):
            playerinput = int(2)
        if playerinput == ("bry"):
            playerinput = int(2)            
            #Tier1 vvv
        if playerinput == ("t1"):
            playerinput = int(1)
        if playerinput == ("neo"):
            playerinput = int(1)

        print("Players Currently in this Match ", playersal)
        print("Success!")
        print("----")
        return (playerinput), (playernow)
    else:
        playerinput = 0
        print("Player not found / Already in lists")
        print("----")
        return (playerinput)
