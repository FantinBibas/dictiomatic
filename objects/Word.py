#!/usr/bin/env python3

from modules.leetomatic import leetomatic
from .Transformable import Transformable


class Word(Transformable):

    def __init__(self, word):
        if not isinstance(word, str):
            raise TypeError
        self.word = word
        self.dictionary = leetomatic.characters_transformations

    def set_dictionary(self, dictionary):
        self.dictionary = dictionary

    def get_transformations(self):
        yield from leetomatic.leetomatic(word=self.word, dictionary=self.dictionary)

    def get_word(self):
        return self.word
