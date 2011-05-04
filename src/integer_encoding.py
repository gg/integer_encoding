#!/usr/bin/env python
# coding: utf-8

from collections import deque

def encoder(alphabet):
    """
    Returns an encoder that encodes a positive integer into
    a base-`len(alphabet)` sequence of alphabet elements.

    `alphabet`: a list of hashable elements used to encode an integer; i.e.
    `'0123456789'` is an alphabet consisting of digit character elements.
    """
    base = len(alphabet)

    def encode(num):
        if num == 0:
            return [alphabet[0]]
        deq = deque()
        while num > 0:
            num, rem = divmod(num, base)
            deq.appendleft(alphabet[rem])
        return list(deq)

    return encode

def decoder(alphabet):
    """
    Returns a decoder that decodes a base-`len(alphabet)` encoded sequence of
    alphabet elements into a positive integer.

    `alphabet`: a list of hashable elements used to encode an integer; i.e.
    `'0123456789'` is an alphabet consisting of digit characters.
    """
    base = len(alphabet)
    index = dict((v, k) for k, v in enumerate(alphabet))

    def decode(xs):
        try:
            result = 0
            for i, x in enumerate(xs[::-1]):
                result += (base ** i) * index[x]
            return result
        except KeyError:
            raise ValueError("%r is not in the alphabet %r" % (x, alphabet))

    return decode
