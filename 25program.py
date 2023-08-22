import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def factorize_n(n, common_factor):
    p = gcd(n, common_factor)
    q = n // p
    return p, q

# Given public key parameters
n = 157723
e = 65537

# Suppose we are told that one plaintext block has a common factor with n
common_factor = 12345

# Attempt to factorize n based on the given information
p, q = factorize_n(n, common_factor)

print("n:", n)
print("Common Factor:", common_factor)
print("Potential p:", p)
print("Potential q:", q)

# Verify if n is correctly factored
if p * q == n:
    print("Successfully factored n!")
else:
    print("Failed to factorize n.")
