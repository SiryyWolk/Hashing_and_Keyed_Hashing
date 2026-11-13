from cryptography.hazmat.primitives import hashes


def digest(algorithm, data: bytes) -> str:
    h = hashes.Hash(algorithm)
    h.update(data)
    return h.finalize().hex()


# Section 1
msg = "Hello, World!".encode("utf-8")
algos = {
    "MD5": hashes.MD5(), "SHA-1": hashes.SHA1(), "SHA-256": hashes.SHA256(),
    "SHA-384": hashes.SHA384(), "SHA-512": hashes.SHA512(),
    "SHA3-256": hashes.SHA3_256(), "SHA3-384": hashes.SHA3_384(),
    "SHA3-512": hashes.SHA3_512(),
}
for name, algo in algos.items():
    print(f"{name:9} {digest(algo, msg)}")

# Section 2: join the 4 lines, decode hex -> bytes, THEN hash
a = ("d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f89"
     "55ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5b"
     "d8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0"
     "e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70")
b = ("d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f89"
     "55ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5b"
     "d8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0"
     "e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70")
ma, mb = bytes.fromhex(a), bytes.fromhex(b)
print("different messages:", ma != mb)
print("MD5 a:", digest(hashes.MD5(), ma))
print("MD5 b:", digest(hashes.MD5(), mb))
print("collision:", digest(hashes.MD5(), ma) == digest(hashes.MD5(), mb))

# Section 4: proof-of-work 
student = "C00305748"
nonce = 0
while True:
    h = digest(hashes.SHA256(), f"{student}!{nonce}".encode("utf-8"))
    if h.startswith("0000"):
        print("nonce:", nonce, "hash:", h)
        break
    nonce += 1