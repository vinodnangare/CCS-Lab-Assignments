p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))
e = int(input("Enter encryption key e: "))
M = int(input("Enter message M: "))  
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def mod_inverse(e, phi):
    a, b = e, phi
    x0, x1 = 0, 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    return x1 % phi if x1 > 0 else (x1 + phi) % phi  
if p == q:
    print("Error: p and q must be distinct prime numbers.")
    exit()
n = p * q
phi_n = (p - 1) * (q - 1)
if gcd(e, phi_n) != 1:
    print("Error: e must be coprime with φ(n). Choose a different e.")
    exit()
d = mod_inverse(e, phi_n)
C = pow(M, e, n)  
print(f"\nPublic Key (n, e): ({n}, {e})")
print(f"Private Key (d): {d}")
print(f"Cipher Text (C): {C}")
