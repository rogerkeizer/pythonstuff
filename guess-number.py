# quick and dirty expiriment without much validation
# TODO: check if first number is smaller than second

import random

print "Hallo, hoe heet jij?"

speler = raw_input(" > ")

print "Hoi ", speler , ", vertel mij het eerste getal"

getal1 = int(raw_input(" > "))

print "en het tweede getal?"

getal2 = int(raw_input(" > "))

print "Ik neem een getal in mijn hoofd."

getal = random.randint(getal1, getal2)

#print getal

antwoord = -1

while antwoord != getal:
    print speler, " welke getal heb ik in mijn hoofd?"

    antwoord = int(raw_input(" > "))

    if antwoord == getal:
        print "Goed zo!! Dat was het"
        break
    else:
        print "Helaas, fout!"
        print "Probeer het nog eens?"


print "GAME OVER!"

