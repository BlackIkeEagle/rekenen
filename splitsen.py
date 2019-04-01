#!/usr/bin/env python3

import random
import sys

min = 1
max = 20

number = 0
part1 = 0
part2 = 0

while True:
    number = random.randint(1,max)
    part1 = random.randint(1,number)
    part2 = number - part1

    print('splits %s in ____ %s' % (str(number), str(part1)))
    givenread = input('          en ____ ')
    if givenread == '':
        sys.exit(0)

    given = int(givenread)

    if given == part2:
        print('OK! super!')
    else:
        print('WOEPS! het antwoord was %s' % str(part2))
