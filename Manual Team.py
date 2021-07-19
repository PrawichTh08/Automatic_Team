import time
import random
from manyfunctions import *

vmap = ["Haven","Split","Breeze","Bind","Ascent","Icebox"]

print("Welcome to SS x VR Technological Department")
print("-------------------------------------------")
print("System13 fairness program")
print("")

#Input Process
while True:
    print("Currently Calulating Defenders' points")
    print("")

    cs = 0
    print("Player Number 1 Defenders")
    p1d = checkplayer()
    cs += p1d
    print("Current Score ", cs)
    print("Player Number 2 Defenders")
    p2d = checkplayer()
    cs += p2d
    print("Current Score ", cs)
    print("Player Number 3 Defenders")
    p3d = checkplayer()
    cs += p3d
    print("Current Score ", cs)
    print("Player Number 4 Defenders")
    p4d = checkplayer()
    cs += p4d
    print("Current Score ", cs)
    print("Player Number 5 Defenders")
    p5d = checkplayer()
    cs += p5d
    print("Current Score ", cs)

    print(playersal)

    dscore = cs
    print("Deffenders Currently have", dscore, "points")

    print("")
    print("Redo Deffenders' Points?")
    res = input("Y/N : ")
    if res == ("Y"):
        continue 

    print("")

    print("Currently Calulating Attackers' points")
    print("")

    csa = 0
    print("Player Number 1 Attackers")
    p1a = checkplayer()
    csa += p1a
    print("Current Score ", csa)
    print("Player Number 2 Attackers")
    p2a = checkplayer()
    csa += p2a
    print("Current Score ", csa)
    print("Player Number 3 Attakers")
    p3a = checkplayer()
    csa += p3a
    print("Current Score ", csa)
    print("Player Number 4 Attackers")
    p4a = checkplayer()
    csa += p4a
    print("Current Score ", csa)
    print("Player Number 5 Attackers")
    p5a = checkplayer()
    csa += p5a
    print("Current Score ", csa)

    print("-----------------")

    ascore = csa
    print("Attackers Currently have", ascore, "points")
    print("")

    scoredif = 0
    if ascore < dscore:
        scoredif = dscore - ascore
    else:
        scoredif = ascore - dscore

    # Annouce and Find Result
    print("Result :")
    if ascore == dscore:
        print("Fair! With the Score of ", ascore, " each!")
        pvmap = random.choice(vmap)
        print("Today map : ", pvmap)
    else:
        if ascore != dscore:
            print("Unfair! Defenders' have ", scoredif, " more point(s).")
        else:
            scoredif = ascore - dscore
            print("Unfair! Attackers' have ", scoredif, " more point(s).")

    print("")

    # Automatic Restart
    if scoredif > 0:
        i = 0
        print("team is not fair the system will auto restart")
        for i in range(0, 3):
            print(i)
            time.sleep(2)
        print("Restated do it carefully this time!")
        continue
    else:
        break
