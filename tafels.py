#!/usr/bin/env python3

import random
import sys

max = 10

number = 0
part1 = 0

question = "Welke tafels gaan we oefenen? : "
tafels = []

for tafel in input(question).split():
    tafels.append(int(tafel))

while True:
    multiplyordivision = random.randint(0, 1)
    tafel = tafels[random.randint(0, len(tafels)-1)]

    if multiplyordivision == 1:  # multiply
        part1 = random.randint(1, max)
        result = part1 * tafel
    else:  # division
        part1 = random.randint(1, max) * tafel
        result = part1 / tafel

    if multiplyordivision == 1:
        question = '%s x %s = ' % (str(part1), str(tafel))
    else:
        question = '%s : %s = ' % (str(part1), str(tafel))

    givenread = input(question)

    if givenread == '':
        sys.exit(0)

    given = int(givenread)

    if given == result:
        print('OK! super')
    else:
        print('WOEPS! het antwoord was %s' % str(result))
