
f = open('input.txt', 'r')
d = f.read().split("\n")

sol1, num_cards = 0, [1] * len(d)
for card_id, game in enumerate(d):
    win, have = game.split(': ')[1:][0].split('|')
    win_set = set(list(map(lambda x: int(x), win.split())))
    have_set = set(list(map(lambda x: int(x), have.split())))
    matches = len(have_set.intersection(win_set))
    sol1 += int(2**(matches-1))
    for i in range(card_id+1, card_id+1+matches):
        num_cards[i]+= num_cards[card_id]

sol2 = sum(num_cards)
print(sol1)
print(sol2)