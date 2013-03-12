#!/usr/bin/env python
from random import choice, random, paretovariate

VOWELS = 'aeiou'


def misspell_letter(letter):
    if letter in VOWELS and random() < 0.5:
        letter = choice(VOWELS)
    if random() < 0.5:
        letter = letter.upper()
    return letter * int(round(paretovariate(3)))


def misspell_word(word):
    word = list(word)
    for i, letter in enumerate(word):
        if random() < 0.3:
            word[i] = misspell_letter(letter)
    return ''.join(word)


if __name__ == '__main__':
    words_file = "/usr/share/dict/words"
    words = [line.strip().lower() for line in open(words_file)]
    for i in xrange(10000):
        word = choice(words)
        print misspell_word(word)
