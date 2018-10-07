#!/usr/bin/env python3

import sys
import itertools
from objects.Transformable import Transformable
from objects.Word import Word


def concatomatic(transformables):
    if not isinstance(transformables, list) or not all([isinstance(transformable, Transformable) for transformable in transformables]):
        raise TypeError
    if len(transformables) == 0:
        yield ''
    else:
        current_transformations = transformables[0].get_transformations()
        if len(transformables) == 1:
            yield from current_transformations
        else:
            for prefix, suffix in itertools.product(current_transformations, concatomatic(transformables[1:])):
                yield prefix + suffix


def permutomatic(transformables):
    for i in range(len(transformables)):
        for transformables_permutation in itertools.permutations(transformables, i + 1):
            yield from concatomatic(list(transformables_permutation))


def dictiomatic():
    yield ''


def main(argv):
    transformables = []
    for word in argv[1:]:
        transformables.append(Word(word))
    for word in permutomatic(transformables):
        print(word)
    return 0


if __name__ == '__main__':
    exit(main(sys.argv))
