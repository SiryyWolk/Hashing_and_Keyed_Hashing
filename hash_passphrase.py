import os
import time

from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

salt = os.urandom(16)
passphrase = b"correct horse battery staple"


def time_scrypt(n, r=8, p=1):
    start = time.perf_counter()
    Scrypt(salt=salt, length=32, n=n, r=r, p=p).derive(passphrase)
    return time.perf_counter() - start


# Part 1: r = 8, p = 1, N = 2^10 ... 2^18
for exp in range(10, 19):
    n = 2**exp
    print(f"N = 2^{exp:<2} ({n:>6}): {time_scrypt(n) * 1000:8.1f} ms")

# Part 2: N = 2^14, r = 8, double p each time
for p in (1, 2, 4, 8):
    print(f"p = {p}: {time_scrypt(2**14, 8, p) * 1000:8.1f} ms")