f = open('input.txt', 'r')
chunks = f.read().split("\n\n")

maps, initial_seeds = chunks[1:], list(map(int, chunks[0].split('seeds: ')[1:][0].split()))
final_map = [[i, i] for i in initial_seeds ]

for _map in maps: # this iterates over block maps
    temp_seeds = list(map(lambda l: l[1], final_map)) # set the destination to temporal seed
    _mapp = _map.strip().split('\n')[1:]
    for line in _mapp: # this goes through lines of a map
      dest, source, _range = map(int, line.split())
      for i, seed in enumerate(temp_seeds):
        if source <=seed <= source + _range-1: # inside interval
          final_map[i][1] = seed - source + dest


print(min(list(map(lambda l: l[1], final_map))))
        

    


# seed_ranges = [[(start, end), (start, end)], [], []]
# d1 = {'seed00': soil00, #start range
      
#       }

# d2 = {'soil00': fetilizer00}

def find_sol(seeds):
  new_seeds = [s for s in seeds]
  for l in lines[2:]:
    if l.endswith('map:'):
      seeds = [ns for ns in new_seeds]
      temp_seeds = []
      continue
    if l == '':
      new_seeds += temp_seeds
      continue
    d_start, s_start, _range = map(int, tuple(l.split(' ')))
    left_over = []  # hate this, is there a cleaner way?
    for (ns, nr) in new_seeds:
      if s_start+nr <= ns+nr <= s_start+_range:  # contains interval
        temp_seeds.append((d_start+ns-s_start, nr))
      elif s_start <= ns < s_start+_range:  # precedes and intersects
        temp_seeds.extend([(d_start+ns-s_start, s_start+_range-ns), (s_start+_range, nr-s_start-_range+ns)])
      elif ns <= s_start < ns+nr:  # follows and intercepts
        temp_seeds.extend([(ns, s_start-ns), (d_start, nr-s_start+ns)])
      else:  # no intersection
        left_over.append((ns, nr))
    new_seeds = left_over  # hate this pt.2
  print(min([ns for ns, _ in new_seeds+temp_seeds]))

lines = [l.strip('\n') for l in open('input.txt').readlines()]
seed_in = [int(s) for s in lines[0].split(' ')[1:]]
find_sol([(s,1) for s in seed_in])
find_sol([(s, r) for s, r in zip(seed_in[::2], seed_in[1::2])])