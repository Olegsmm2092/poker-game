import random

SUITS_STR = tuple('shdc'.upper())
SUITS = '♠ ♥ ♦ ♣'.split()
SUITS_MAP = m = {SUITS_STR[n]: SUITS[n] for n in range(len(SUITS_STR))}
# RANKS = tuple(range(2, 10 + 1)) + tuple('j q k a'.upper().split())
RANKS = tuple(range(2, 14 + 1))


class Card: # say to ai modifed n d usi- dataclass and enum instead;
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self._get_value(rank)


    def _get_value(self, rank):
        if str(rank).isdigit():
            return int(rank)
        if rank == '10':
            return 10
        if rank in 'J Q K A'.split():
            return {'J': 11, 'Q': 12, 'K': 13, 'A': 14}[rank]

    def __repr__(self):
        return f"{self.rank}{m[self.suit]}"

    def __str__(self):
        if self.rank == 14:
            rank = 'A'
        elif self.rank == 13:
            rank = 'K'
        elif self.rank == 12:
            rank = 'Q'
        elif self.rank == 11:
            rank = 'J'
        else:
            rank = self.rank # int 
                                # тонкости if in one place x2 types type - 1 more сразу converter to init;

        return str(rank) + self.suit

    # add compare for cards
    def __eq__(self, __o: object) -> bool:
        return self.value == __o.value

    def __ne__(self, __o: object) -> bool:
        return self.value != __o.value

    def __lt__(self, __o: object) -> bool:
        return self.value < __o.value

    def __le__(self, __o: object) -> bool:
        return self.value <= __o.value

    def __gt__(self, __o: object) -> bool:
        return self.value > __o.value

    def __ge__(self, __o: object) -> bool:
        return self.value >= __o.value
    

class FrenchDeck:
    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in SUITS_STR for rank in RANKS]

    def deal(self):
        if len(self._cards) == 0:
            return None
        
        return self._cards.pop(0)

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

    def shuffle(self):
        random.shuffle(self._cards)
    