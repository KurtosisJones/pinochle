import random
import logging
import json
import os

with open("cards.json", "r") as af:
    deck = json.load(af)
with open("meld.json", "r") as af:
    meld = json.load(af)
with open("card_map.json", "r") as af:
    card_map = json.load(af)

random.shuffle(deck["4-Hand"])

new_shuffle = deck["4-Hand"]

# A relative in my family used to deal from the bottom, so we always had
# the player to the left of the dealer split the deck to ensure they didn't cheat
# so I did this here
len_deck = len(new_shuffle)

deck_split_index = random.randint(0,len_deck)
# split the deck on the random index
new_shuffle[deck_split_index:len_deck].extend(new_shuffle[0:deck_split_index])

player = 4
cards_dealt = 4
players = 4

total_cards = len(new_shuffle)
rounds = int(total_cards / (players * cards_dealt))

card_init_indices = [(round * players * cards_dealt) + (player - 1) * cards_dealt for round in range(rounds)]
card_indices = [index for i in card_init_indices for index in (i, i+1, i+2, i+3)]

player_list = [
    {"player":1,"team":1},
    {"player":2,"team":1},
    {"player":3,"team":2},
    {"player":4,"team":2}
]

[{card:card_map[card]} for card in deck["4-Hand"]]

# What I should impoliment is the shared chache so when the process checks the player's hand, it won't double count the 
# dependent tricks
[i for i in meld]