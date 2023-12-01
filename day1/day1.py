f = open("input.txt", "r")
d = f.read().split("\n")
total = 0


for l in d:
    s = ''.join(x for x in l if x.isdigit())
    s = s[0]+s[-1]
    total += int(s)

print('Result Day 1.1',total)


# Part 2:
matches = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',  'nine', 1,2,3,4,5,6,7,8,9]
text2num = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven': 7, 'eight':8, 'nine':9, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6,7:7,8:8,9:9}
total = 0
for l in d:
    first = (10000, '')
    last = (0, '')
    for m in matches:
        first_ = l.find(str(m))
        last_ = l.rfind(str(m))
        if first_ != -1 and first_ < first[0]:
            first = (first_, m)
        if last_ != -1 and last_ > last[0]:
            last = (last_,m) 
    if last[1] == '':
        last = first
    s = text2num[first[1]]*10 + text2num[last[1]] #here the numbers are already integers so summing them doesn't append
    total+=s

print('Restult Day 1.2',total)
