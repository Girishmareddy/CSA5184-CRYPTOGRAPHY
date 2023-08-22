def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return (x % m + m) % m

# Given public key
e = 31
n = 3599

# Find p and q using trial-and-error
for p in range(2, n):
    if n % p == 0:
        q = n // p
        break

# Calculate totient (phi) of n
phi = (p - 1) * (q - 1)

# Calculate private key using modular inverse
d = mod_inverse(e, phi)

print("p:", p)
print("q:", q)
print("Private key (d):", d)
