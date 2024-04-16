# coding=utf-8

import random
import time
"""
"When two dice are thrown randomly, at what time does the number 6 6 appear?"
"""
i = 1
while True:
    zar_1 = random.randint(1, 6)
    zar_2 = random.randint(1, 6)

    if zar_1 == 6 and zar_2 == 6:
        print("""Deneme {}:\t({},{}) *** """.format(i, zar_1, zar_2))
        time.sleep(2)
        break

    print("""Deneme {}:\t({},{}) """.format(i, zar_1, zar_2))
    i += 1
    time.sleep(0.5)
print("""\n*** {}. denemede (6,6) geldi ***""".format(i))

