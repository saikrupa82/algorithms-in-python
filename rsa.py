import random


def generate_key(k, seed=None):
    """
    the RSA key generating algorithm
    k is the number of bits in n
    """

    def modinv(a, m):
        """calculate the inverse of a mod m
        that is, find b such that (a * b) % m == 1"""
        b = 1
        while not (a * b) % m == 1:
            b += 1
        return b

    def gen_prime(k, seed=None):
        """generate a prime with k bits"""

        def is_prime(num):
            if num == 2:
                return True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        random.seed(seed)
        while True:
            key = random.randrange(int(2 ** (k - 1)), int(2 ** k))
            if is_prime(key):
                return key

    # size in bits of p and q need to add up to the size of n
    p_size = k / 2
    q_size = k - p_size

    e = gen_prime(k, seed)  # in many cases, e is also chosen to be a small constant

    while True:
        p = gen_prime(p_size, seed)
        if p % e != 1:
            break

    while True:
        q = gen_prime(q_size, seed)
        if q % e != 1:
            break

    n = p * q
    l = (p - 1) * (q - 1)  # calculate totient function
    d = modinv(e, l)

    return int(n), int(e), int(d)


def encrypt(data, e, n):
    return pow(int(data), int(e), int(n))


def decrypt(data, d, n):
    return pow(int(data), int(d), int(n))
    