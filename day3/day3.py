with open('input.txt') as f:
  lines = [l+'.' for l in f.read().split('\n') if l]

part_numbers = []
signs = []
number = []
num_idxs = []
gears = []
for row, l in enumerate(lines):

  last_is_digit = False
  for col, n in enumerate(l):
    if n.isdigit():
      number.append(int(n))
      num_idxs.append((row, col))
      last_is_digit = True
    else:
        if last_is_digit:
            sum_number = sum([val * 10**i for i, val in enumerate(reversed(number))]) # convert list of integers to number [3,4,7] --> 347
            part_numbers.append([sum_number, num_idxs]) # [467, (0, 3)], [114, (0, 8)], [...]], contains number and list of tuples with row,cols where the number is
            number = []
            num_idxs = []
            last_is_digit = False
        if n != '.':
           signs.append([n, (row, col)])
           gears.append([])

sol1 = 0

for value, idxs in part_numbers:
    for i, sign in enumerate(signs):
        sign_type, sign_loc = sign
        # print([max(abs(sign[0] - idx[0]), abs(sign[1] - idx[1])) for idx in idxs])
        if any([max(abs(sign_loc[0] - idx[0]), abs(sign_loc[1] - idx[1])) < 2 for idx in idxs]) :
            sol1 += value
            if sign_type == '*':
               gears[i].append(value)

sol2 = sum([g[0] * g[1] for g in gears if len(g)==2])

print(sol1)   
print(sol2)
        
        
