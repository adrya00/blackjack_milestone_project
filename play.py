import string

abc = string.ascii_lowercase


def encrypt(msg, n):

    return ''.join(map(lambda x:abc [(abc.index(x)+n)%26] if x in abc else x, msg))

print (encrypt('how are you?',2))