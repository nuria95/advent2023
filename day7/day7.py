from collections import defaultdict
from functools import cmp_to_key

out = [f.split() for f in open('input.txt', 'r').readlines()]

cards, bids = list(map(lambda x: x[0], out)), list(map(lambda x: int(x[1]), out))

_types = {(5,): 7, (1,4):6, (2,3):5, (1,1,3):4, (1,2,2):3, (1,1,1,2):2, (1,1,1,1,1): 1}
strengths_1 = {'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}
strengths_2 = {'A':13, 'K':12, 'Q':11, 'J':0, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}

def get_types(cards, bids, _types, strengths, joker=False):
    cards_types = defaultdict(list)
    for card, bid in zip(cards, bids):
        d = defaultdict(int)
        val_card = []
        for k in card:
            d[k] +=1
            val_card.append(strengths[k])
        if joker and d['J']<5: #if all are jokers, don't need to add them in any other type
            d_ = d.copy()
            d_.pop('J')  # we need to omit key J when computing the max below
            d[max(d_, key=d.get)]+=d['J'] #max(d, key=d.get)  returns the key with max value, omit the key J
            d.pop('J')
        card_type = _types[tuple(sorted(d.values()))]
        cards_types[card_type].append([card, val_card, bid])
    return cards_types

def my_comparer(card1, card2):
    # print(f'comparing {card1} vs {card2}')
    _, val1, _ = card1
    _, val2, _ = card2
    for c1, c2 in zip(val1, val2):
        if c1 > c2: 
            return 1
        if c1 < c2:
            return -1   
    return 0 # if after iterating over ALL elements, they where all the same, return 0

i = 0 
for strength, joker in zip([strengths_1, strengths_2], [False, True]):
    cards_types = get_types(cards, bids, _types, strength, joker)
    my_types = sorted(cards_types.keys()) # iterate over types, from lower to higher rank
    all_sorted_bids = []
    for _type in my_types:
        cards_type = cards_types[_type]
        sorted_cards = sorted(cards_type, key = cmp_to_key(my_comparer)) # list of lists
        all_sorted_bids.extend(list(list(zip(*sorted_cards))[2]))
    i+=1
    print(f'Sol {i}', sum([ (rank+1)*bid  for rank, bid in enumerate(all_sorted_bids)]))


    










    
    

