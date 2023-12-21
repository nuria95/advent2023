import numpy as np
import math
race_times, records = [list(map(int, n.split()[1:])) for n in open('input.txt', 'r').readlines()]
total_ways = 1
def num_ways(t, dist_rec):
    # dist = v * t = time_pressed * (race_time - time_pressed)  > DIST_REC; time_pressed --> x
    # dist = -x**2 + race_time * x - dist_rec  > 0; 
    # dist = x**2 - race_time * x + dist_rec < 0 # quadratic eq, 2 solutions, since parabola, all values in between solutions are below zero :)
    # ways =  (-B +/- sqrt(B**2 - 4AC))/ 2A
    way_max = (t + math.sqrt(t**2 - 4*dist_rec))/2
    way_min = (t - math.sqrt(t**2 - 4*dist_rec))/2
    if way_max == math.floor(way_max) and way_min == math.ceil(way_min):
        return way_max - way_min -1 # if way_max and way_min are ints (ex 5,2) then you have 2 options {3,4} --> (5-2)
    return math.floor(way_max) - math.ceil(way_min) + 1 #if not ints ex. 5.4 and 1.8 then you have 4 options --> (5-2 +1) {2,3,4,5} 

for race_time, record in zip(race_times, records):
    # Brute force
    dist = np.array([v*(race_time-v) for v in range(1, race_time)]) # dist = v * t, where t = race_time - vel
    ways_ = len(dist[dist>record])
    
    # Efficient:
    ways = int(num_ways(race_time, record))
    total_ways *=ways

print('Sol1: ', total_ways)
print('Sol 2', num_ways(*[int(''.join(n.split()[1:])) for n in open('input.txt', 'r').readlines()]))



