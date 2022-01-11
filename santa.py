import random
from peoples import peoples


def gift_random():
    santas = list(peoples.keys())
    kids = santas.copy()
    gifts = []

    for santa in santas:
        gift = kids.copy()
        if santa in gift:
            gift.remove(santa)
        exc = peoples[santa].get('exc')
        if exc and exc in gift:
            gift.remove(exc)
        random.shuffle(gift)
        kid = random.choice(gift)
        gifts.append({
            'name': santa,
            'gift': kid
        })
        kids.remove(kid)

    return gifts


def get_santas():
    not_found = True
    while not_found:
        try:
            gifts = gift_random()
            not_found = False
        except:
            pass
    return gifts