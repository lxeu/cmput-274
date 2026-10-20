from cmput274 import *

def newDeck():
    return foldr(map(lambda suit: buildList(lambda rank: LL(suit, rank+2), 13), buildList(lambda x: x, 4)), lambda l1, l2: foldr(l1, cons, l2), empty())

def suitDisplay(suit):
    if suit == 0:
        return "◆"
    if suit == 1:
        return "♣"
    if suit == 2:
        return "♥"
    if suit == 3:
        return "♠"

def rankDisplay(rank):
    if rank <= 9:
        return chr(ord("0") + rank)
    if rank == 10:
        return "X"
    if rank == 11:
        return "J"
    if rank == 12:
        return "Q"
    if rank == 13:
        return "K"
    if rank == 14:
        return "A"

map(lambda card: rankDisplay(first(rest(card))) + suitDisplay(first(card)), deck)