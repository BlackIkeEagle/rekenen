#!/usr/bin/env python3

import random
import sys

min = 1
max = 20

number = 0
part1 = 0
part2 = 0

while True:
    upordown = random.randint(0,1)

    if upordown == 1:
        result = random.randint(1,max)
        part1 = random.randint(1,result)
        part2 = result - part1
    else:
        part1 = random.randint(1,max)
        part2 = random.randint(1,part1)
        result = part1 - part2

    if upordown == 1:
        question = '%s + %s = ' % (str(part1), str(part2))
    else:
        question = '%s - %s = ' % (str(part1), str(part2))

    givenread = input(question)

    if givenread == '':
        sys.exit(0)

    given = int(givenread)

    if given == result:
        print('OK! super')
    else:
        print('WOEPS! het antwoord was %s' % str(result))
