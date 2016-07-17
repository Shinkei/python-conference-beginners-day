# coding=utf8

"""
Challenge:  the Pythonic card deck class

The class CardDeck below represents a pack
of cards.

Find out how to use magic methods so that the
following three standard functions work:

    >>> import random
    >>> deck = CardDeck()
    >>> len(deck)
    52
    >>> print(deck[0])
    2♠
    >>> print(deck[-1])
    A♣
    >>> random.choice(deck) in list(deck)
    True
    >>> random.shuffle(deck)

Tip:
If you have lines in the docstring (this string) that look like interactive
Python sessions, you can use the doctest module to run and test this code.

Try: python -m doctest -v magic_methods.py

See: https://docs.python.org/3/library/doctest.html


Credit to Luciano Ramalho and his excellent book Fluent Python, from which
I stole this example.
"""



class CardDeck:
    ranks = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']
    suits = '♠♡♢♣'

    def __init__(self):
        self._cards = [
            rank + suit
            for suit in self.suits
            for rank in self.ranks
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, key):
        return(self._cards[key])

    def __setitem__(self, key, value):
        self._cards[key] = value;

import random
deck = CardDeck()
print(len(deck))
print(deck[0])
print(deck[-1])
print(random.choice(deck) in list(deck))
print(random.shuffle(deck)) # reordena la lista de forma aleatoria
print(deck[0])
print(deck[-1])


"""
Bonus exercise: Polynomial class

Create a class that represents polynomials.  You may need to stretch your memory back to high school maths!

A polynomial looks like

    2(xx) - x + 7

And its essential features are the coefficients of each power of x

in this example, power-2=2, power-1=-1, power-0=7

Credit to Moshe Goldstein
"""

class Polynomial:
    def __init__(self, coefficients):
        pass

    def __str__(self):
        pass  # TODO

    def __add__(self, poly):
        '''returns the result of adding poly from self'''
        pass  # TODO

    def __sub__(self, poly):
        '''returns the result of subtracting poly from self'''
        pass  # TODO

    def __mul__(self, poly):
        '''multiply two polynomials'''
        pass  # TODO

    def value(self, x):
        '''returns the value of the polynomial at point x'''
        pass  # TODO

    def derivative(self):
        '''returns the derivate of the polynomial'''
        pass  # TODO

