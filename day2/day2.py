import numpy as np
f = open("input.txt", "r")
d = f.read().split("\n")
sum_ids = 0
total = {'red': 12, 'green': 13, 'blue': 14}
for game in d:
    impossible = False
    game = game.replace(':', ';').replace(',', '').split(';')
    id = int(game[0].split()[-1])
    for take in game[1:]:
        el = take.split()
        for i in range(0,len(el), 2):
            num, col = int(el[i]), el[i+1]
            if total[col] < num:
                impossible = True
                break
        if impossible:
            break
    if not impossible:
        sum_ids +=id

print('Part 1: Sum ids', sum_ids)


#--------
import math
total = 0
f = open("input.txt", "r")
d = f.read().split("\n")
for game in d:
    game_set = {'green': 0, 'blue': 0, 'red':0}
    game = game.replace(':', ';').replace(',', '').split(';')
    for take in game[1:]:
        el = take.split()
        for i in range(0,len(el), 2):
            num, col = int(el[i]), el[i+1]
            game_set[col] = np.maximum(num, game_set[col])
    powerset = math.prod(game_set.values())
    total += powerset
print(total)