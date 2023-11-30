#Zadanie
# - Stworzyć klasę `Card` która ma dwa pola - `suit` (wartości np. `club`, `diamond`, `heart`, `spade`), `value` (wartości np. `9`, `10`, `J`, `Q`, `K`, `A`) przeciążyć metodę od obsługi `<` i `>` które oznacza "bicie karty"
#   - Karta bije kartę jeśli ma ten sam kolor i mocniejszą wartość
#   - Pik (`spade`) jest atutem - bije inne kolory. Pozostałe kolory nie biją się nawzajem

class Card:
    VALUES = ('9', '10', 'J', 'Q', 'K', 'A')
    SUITS = ('clubs', 'diamonds', 'hearts', 'spades')

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def czy_bije(self, karta2):
        return self.SUITS.index(self.suit) > self.SUITS.index(karta2.suit) or (
                self.SUITS.index(self.suit) == self.SUITS.index(karta2.suit) and
                self.VALUES.index(self.value) > self.VALUES.index(karta2.value)
        )

    def __repr__(self):
        return f'Card("{self.suit}", "{self.value}")'

    def __str__(self):
        return f'Card("{self.suit}", "{self.value}")'

    def __gt__(self, other):
        return self.czy_bije(other)

    def __lt__(self, other):
        return other.czy_bije(self)

    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value

    def __ge__(self, other):
        return self.czy_bije(other) or self == other



trefl9 = Card("clubs", "9")
spades_ace = Card("spades", "A")
heart_king = Card("hearts", "K")

spades_ace > trefl9
spades_ace.__gt__(trefl9)


spades_ace < trefl9


spades_ace.czy_bije(trefl9)
trefl9.czy_bije(spades_ace)

reka = [ spades_ace, heart_king, trefl9]
reka
reka.sort()
reka

str(spades_ace)