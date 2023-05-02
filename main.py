'''Importing the required modules'''
from dataclasses import dataclass, field
from typing import List, Optional
from random import shuffle
from time import sleep
from colorama import init, Fore
init()


@dataclass
class Card:
    '''Playing card.
    Suits: 0 = ♠, 1 = ♥, 2 = ♣, 3 = ♦.
    Values: 2...10 = 2...10, 11 = J, 12 = Q, 13 = K, 14 = A.'''
    suit: int
    value: int
    def __str__(self) -> str:
        value: str = str(self.value)
        match self.value:
            case 11:
                value = 'J'
            case 12:
                value = 'Q'
            case 13:
                value = 'K'
            case 14:
                value = 'A'
        suit: chr
        match self.suit:
            case 0:
                suit = '♠'
            case 1:
                suit = '♥'
            case 2:
                suit = '♣'
            case 3:
                suit = '♦'
        return value + ' ' + suit
    def __int__(self) -> int:
        match self.value:
            case 11:
                return 2
            case 12:
                return 3
            case 13:
                return 4
            case 14:
                return 11
        return self.value
    def show(self) -> None:
        '''Displays a card.'''
        if self.suit in (0, 2):
            print(Fore.BLACK, str(self), end='')
        else:
            print(Fore.RED, str(self), end='')


class Deck:
    '''Deck of playing cards.'''
    deck: List[Optional[Card]] = [Card(0, 0) for i in range(52)]
    def __init__(self) -> None:
        for _i_ in range(4):
            for _j_ in range(2, 15):
                self.deck[_i_ * 13 + _j_ - 2] = Card(_i_, _j_)
        shuffle(self.deck)
    def reshuffle(self) -> None:
        '''Shuffles the deck again.'''
        shuffle(self.deck)
    def get_card(self) -> Card:
        '''Get first card and pop it from deck.'''
        return self.deck.pop(0)


@dataclass
class Player:
    '''Player.'''
    number: int
    hand: List[Optional[Card]] = field(default_factory=list)
    def get_sum(self) -> int:
        '''Returns the value of cards in hand.'''
        value: int = 0
        for card in self.hand:
            value += int(card)
        return value
    def take_card(self, _deck_: Deck) -> None:
        '''Takes a new card from a deck.'''
        self.hand.append(_deck_.get_card())
    def show(self) -> None:
        '''Displays a hand and sum.'''
        print(Fore.GREEN, 'Your current hand:')
        for index in range(len(self.hand) - 1):
            self.hand[index].show()
            print(',', end='')
        if len(self.hand) > 0:
            self.hand[len(self.hand) - 1].show()
        print(Fore.GREEN, '\n Your current sum:')
        print(Fore.BLUE, self.get_sum())
    def move(self) -> int:
        '''Move actions'''
        print(Fore.GREEN, 'Move of player ' + str(self.number + 1))
        sleep(1)
        self.show()
        print(Fore.CYAN, '"t" (take) or "e" (end) ?')
        cmd: str = input(' ')
        while cmd != 'e':
            if cmd == 't':
                self.take_card(deck)
                self.show()
                if self.get_sum() > 21:
                    print(Fore.GREEN, 'You lose! Good Luck next time!')
                    sleep(2)
                    print('\n\n\n\n\n')
                    return -1
            cmd = input(' ')
        print(Fore.GREEN, 'You have finished your turn!')
        sleep(2)
        print("\n\n\n\n\n")
        return self.get_sum()


number_of_players = int(input('Enter number of players.'))
deck: Deck = Deck()
winner_num: int = -1
winner_result: int = -1
for player_number in range(number_of_players):
    player: Player = Player(player_number)
    player_result: int = player.move()
    if player_result > winner_result:
        winner_num = player_number
        winner_result = player_result
if winner_num == -1:
    print(Fore.GREEN, ' IT WAS AN EQUAL GAME, DRAW!')
else:
    print(Fore.GREEN, ' PLAYER ' + str(winner_num + 1) +
          ' WON WITH A SCORE OF ' + str(winner_result) + '!')
