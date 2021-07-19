import random
import sys
from manyfunctions import *
global line

players = []
vmap = ["Haven", "Split", "Breeze", "Bind", "Ascent", "Icebox"]

#Welcome Screen
print("-------------")
print("Welcome to SS X VR Technical Department")
print("-Fairness System-")
print("-------------")

#get playername
playercheckreturn = checkplayer()
p1d = playercheckreturn[1]
p1ds = playercheckreturn[0]
print(p1d, "//", p1ds)

playercheckreturn = checkplayer()
p2d = playercheckreturn[1]
p2ds = playercheckreturn[0]
print(p2d, "//", p2ds)

playercheckreturn = checkplayer()
p3d = playercheckreturn[1]
p3ds = playercheckreturn[0]
print(p3d, "//", p3ds)

playercheckreturn = checkplayer()
p4d = playercheckreturn[1]
p4ds = playercheckreturn[0]
print(p4d, "//", p4ds)

playercheckreturn = checkplayer()
p5d = playercheckreturn[1]
p5ds = playercheckreturn[0]
print(p5d, "//", p5ds)

playercheckreturn = checkplayer()
p1a = playercheckreturn[1]
p1as = playercheckreturn[0]
print(p1a, "//", p1as)

playercheckreturn = checkplayer()
p2a = playercheckreturn[1]
p2as = playercheckreturn[0]
print(p2a, "//", p2as)

playercheckreturn = checkplayer()
p3a = playercheckreturn[1]
p3as = playercheckreturn[0]
print(p3a, "//", p3as)

playercheckreturn = checkplayer()
p4a = playercheckreturn[1]
p4as = playercheckreturn[0]
print(p4a, "//", p4as)

playercheckreturn = checkplayer()
p5a = playercheckreturn[1]
p5as = playercheckreturn[0]
print(p5a, "//", p5as)

#calculate Summary of each
playersmatch = [p1a, p2a, p3a, p4a, p5a, p1d, p2d, p3d, p4d, p5d]
matchscore = p1ds + p2ds + p3ds + p4ds + p5ds + p1as + p2as + p3as + p4as + p5as
fr = [
    p1a, p1as, p2a, p2as, p3a, p3as, p4a, p4as, p5a, p5as, p1d, p1ds, p2d,
    p2ds, p3d, p3ds, p4d, p4ds, p5d, p5ds
]

print("Players In This Match : ")
print(playersmatch)
print("Processing....")

willfair = matchscore / 2

atk = playersmatch[0], playersmatch[1], playersmatch[2], playersmatch[
    3], playersmatch[4]
dfd = playersmatch[5], playersmatch[6], playersmatch[7], playersmatch[
    8], playersmatch[9]

if matchscore % 2 == 0:
    eoro = 0
if matchscore % 2 != 0:
    eoro = 1

#value of players
player1r = [fr[0], fr[1]]
player2r = [fr[2], fr[3]]
player3r = [fr[4], fr[5]]
player4r = [fr[6], fr[7]]
player5r = [fr[8], fr[9]]
player6r = [fr[10], fr[11]]
player7r = [fr[12], fr[13]]
player8r = [fr[14], fr[15]]
player9r = [fr[16], fr[17]]
player10r = [fr[18], fr[19]]

plfr = [
    player1r, player2r, player3r, player4r, player5r, player6r, player7r,
    player8r, player9r, player10r
]

dfdsrn = []
atksrn = []
count = 0

count = 0
#Find possible combinations
while True:
    random.shuffle(plfr)
    atksrn = plfr[0][1] + plfr[1][1] + plfr[2][1] + plfr[3][1] + plfr[4][1]
    dfdsrn = plfr[5][1] + plfr[6][1] + plfr[7][1] + plfr[8][1] + plfr[9][1]
    print(plfr[0][0], plfr[1][0], plfr[2][0], plfr[3][0], plfr[4][0],
          plfr[5][0], plfr[6][0], plfr[7][0], plfr[8][0], plfr[9][0])
    count += 1
    if atksrn == dfdsrn:
        break
    if count == 200:
        print(
            "We had Aleady tried 200 combinations we had Cancelled the randomization"
        )
        sys.exit()

# Annouce Combinations
print("---------------")
print("Today Teams")
print("---------------")
random.choice(vmap)
print("Attackers Team : ", plfr[0][0], plfr[1][0], plfr[2][0], plfr[3][0],
      plfr[4][0])
print("Defenders Team : ", plfr[5][0], plfr[6][0], plfr[7][0], plfr[8][0],
      plfr[9][0])
print("Score Is", atksrn, "each")
print("---------------")
print("Today Map is : ", vmap)
print("---------------")
print("Combinations Report : Tried ", count,
      " combinations to find perfect ones")
print("type M for maore information")
more = input("input here : ")

if more == ("M") or ("m") :
    print("Allplayer in this match :", playersmatch)
    print("---- Player Score ----")
    print(player1r)
    print(player2r)
    print(player3r)
    print(player4r)
    print(player5r)
    print(player6r)
    print(player7r)
    print(player8r)
    print(player9r)
    print(player10r)
    print()
    print("This Match have : ", matchscore, "Score in total")
else :
    sys.exit()

#['nly', 'ryu', 'hro', 't2', 'zch', 'neo', 'ska', 'bry', 'shm', 'sen']
