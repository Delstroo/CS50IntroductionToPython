import random
# You can also import it like this `from random import choice`

coin = random.choice(["heads", "tails"])

number = random.randint(1, 20)

cards = ["Jack", "Queen", "King"]
random.shuffle(cards)

for card in cards:
    print(card)