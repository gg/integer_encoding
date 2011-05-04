import integer_encoding
import string

def test_base62_encoding():
    alphabet = string.ascii_letters + string.digits
    encode = integer_encoding.encoder(alphabet)
    decode = integer_encoding.decoder(alphabet)
    assert(''.join(encode(decode('ZRq3lhPI'))) == 'ZRq3lhPI')

def test_object_encoding():
    alphabet = [('a', 'b', 'c'), ('d', 'e'), 7, 49, 8, 64]
    encode = integer_encoding.encoder(alphabet)
    decode = integer_encoding.decoder(alphabet)

    xs = [('d', 'e'), ('d', 'e'), ('a', 'b', 'c'), 7, 8, 8, 49, 64]
    assert(encode(decode(xs)) == xs)
