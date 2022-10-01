import math

def find_order(a, n):
    """
    Find order for positive integer n and given integer a that satisfies gcd(a, n) = 1.
    """
    if (a == 1) & (n == 1):
        # Exception Handeling : 1 is the order of of 1
        return 1
    if math.gcd(a, n) != 1:
        print ("a and n should be relative prime!")
        return -1
    for i in range(1, n):
        if pow(a, i) % n == 1:
            return i
    return -1