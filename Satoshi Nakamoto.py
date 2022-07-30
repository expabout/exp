import random
a=110001010000010011000101111010010100000011000101100101010100000011010101010001010001110110010101100110011010010011001001000100010011010101000001010100011001100101010001001100001101010101001101001100
def Extended_Eulid(a: int, m: int) -> int:
    def extended_eulid(a: int, m: int):
        if a == 0: 
            return 1, 0, m
        else:
            x, y, gcd = extended_eulid(m % a, a)
            x, y = y, (x - (m // a) * y) 
            return x, y, gcd 
    n = extended_eulid(a, m)
    if n[1] < 0:
        return n[1] + m
    else:
        return n[1]
def power(a, b, c):
    ans = 1
    while b != 0:
        if b & 1:
            ans = (ans * a) % c
        b >>= 1
        a = (a * a) % c
    return ans
def quick_power(a: int, b: int) -> int:
    ans = 1
    while b != 0:
        if b & 1:
            ans = ans * a
        b >>= 1
        a = a * a
    return ans
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)
def Miller_Rabin(n):
    a = random.randint(2, n - 2)
    s = 0 
    d = n - 1
    while (d & 1) == 0: 
        s += 1
        d >>= 1
    x = power(a, d, n)
    for i in range(s): 
        newX = power(x, 2, n)
        if newX == 1 and x != 1 and x != n - 1:
            return False
        x = newX
    if x != 1:
        return False
    return True
def Generate_prime(key_size: int) -> int:
    while True:
        num = random.randrange(quick_power(2, key_size - 1), quick_power(2, key_size))
        if Miller_Rabin(num):
            return num
def KeyGen(p: int, q: int):
    n = p * q
    e = a
    d = Extended_Eulid(e, (p - 1) * (q - 1))
    return n, e, d
def Sign(x: int, d: int, n: int) -> int:
    s = power(x, d, n)
    return s
if __name__ == '__main__':
    key_size = 136
    p = Generate_prime(key_size)
    q = Generate_prime(key_size)
    n, e, d = KeyGen(p, q)
    x = int(input("Message: "))
    if type(x) != int:
        raise ValueError("Must be an integer!")
    s = Sign(x, d, n)
    print("N: ", n)
    print("d: ", d)
    print("N: ", n)
    print("e: ", e)
    print("sig: ", s)