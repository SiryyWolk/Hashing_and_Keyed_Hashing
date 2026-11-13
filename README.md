# Hashing and Keyed Hashing

This repository contains small Python experiments demonstrating core hash-function behavior, collision concepts, proof-of-work, and keyed password hashing.

## Overview

The project explores several practical cryptographic ideas:

- Computing digests with common algorithms such as MD5, SHA-1, SHA-256, SHA-384, SHA-512, and SHA-3 family hashes.
- Demonstrating a classic MD5 collision example using two different byte sequences that hash to the same digest.
- Showing a proof-of-work example based on finding a SHA-256 hash beginning with four zero bits.
- Measuring how Scrypt runtime changes when the cost parameter `N` and parallelism parameter `p` vary.

## Files

### `hashing_collision_proof-of-work.py`

This script contains three related sections:

1. Hashing a message with multiple algorithms and printing their outputs.
2. Comparing two different inputs that collide under MD5.
3. Mining a nonce for a SHA-256 proof-of-work challenge based on a student ID.

Example output includes:

- The digest of `Hello, World!` under several algorithms.
- A confirmation that the two payloads differ but produce the same MD5 hash.
- A nonce value that makes the SHA-256 hash of `C00305748!{nonce}` begin with `0000`.

### `hash_passphrase.py`

This script benchmarks Scrypt key derivation for password-like inputs using a random 16-byte salt.

It measures how runtime changes when:

- `N` varies from `2^10` to `2^18` with fixed `r=8` and `p=1`.
- `p` varies as `(1, 2, 4, 8)` while `N=2^14` and `r=8`.

This helps illustrate why memory- and CPU-hard KDFs are used for password hashing instead of plain hashing.

## Requirements

The scripts use the Python cryptography library.

Install dependencies:

```bash
pip install cryptography
```

## Run the examples

```bash
python hashing_collision_proof-of-work.py
python hash_passphrase.py
```

## Notes

- MD5 is intentionally used here only for demonstration of historical weaknesses and collision behavior.
- Real-world password storage should use a modern password hashing function such as Argon2, bcrypt, or scrypt.
- For security-sensitive systems, avoid using fast, unsalted hashes for passwords or integrity checks.

## Learning goals

This project introduces the following concepts:

- Hash function output and digest formatting.
- Collision resistance and why weak hash functions are dangerous.
- Proof-of-work workloads and brute-force search.
- Keyed derivation functions and parameter tuning.
- Why password hashing must be intentionally expensive and adaptive.
