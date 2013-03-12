#!/usr/bin/env python
import re
from collections import defaultdict
from difflib import get_close_matches
from cmd import Cmd


VOWEL_RE = re.compile(r'[aeiou]')
REPEAT_RE = re.compile(r'(.)\1+')


def to_pattern(word):
    """
    Converts a word to a common pattern.
    """
    # Vowels are replaced with a *
    # this gives us more tolerance to vowels mispelling
    pattern = VOWEL_RE.sub('*', word)
    # Repeated symbols are replaced by just one of them
    pattern = REPEAT_RE.sub(r'\1', pattern)
    return pattern


class SpellCommand(Cmd):
    def __init__(self, words_file):
        Cmd.__init__(self)
        self.prompt = '> '
        self.no_suggestion = 'NO SUGGESTION'
        self.words = set(line.strip().lower() for line in open(words_file))

        self.approx = defaultdict(set)
        for word in self.words:
            pattern = to_pattern(word)
            self.approx[pattern].add(word)

    def default(self, line):
        if line == 'EOF':
            exit(0)

        word = line.lower().strip()
        pattern = to_pattern(word)

        if word in self.words:
            print word

        elif pattern in self.approx:
            words = self.approx[pattern]
            suggestion = get_close_matches(word, words, n=1, cutoff=0.3)
            print suggestion and suggestion[0] or self.no_suggestion

        else:
            print self.no_suggestion


if __name__ == '__main__':
    words_file = '/usr/share/dict/words'
    commmand = SpellCommand(words_file)
    commmand.cmdloop()
