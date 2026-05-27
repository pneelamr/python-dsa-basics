# Bloom Filter: Probabilistic set-membership structure using multiple hash functions and a bit array.
# Guarantees no false negatives but allows false positives with tunable probability.
# Space-efficient alternative to a hash set when exact membership is not required.

import hashlib


def create(size=1000):
    return {'bits': [0] * size, 'size': size}


def _hashes(value, size):
    seeds = [17, 31, 37]
    indices = []
    for seed in seeds:
        h = int(hashlib.md5(f"{seed}{value}".encode()).hexdigest(), 16)
        indices.append(h % size)
    return indices


# Time: O(k) where k=number of hash functions — computes k hashes per operation
# Space: O(m) where m=bit array size — fixed-size bit array
def add(bf, value):
    for i in _hashes(value, bf['size']):
        bf['bits'][i] = 1


def contains(bf, value):
    return all(bf['bits'][i] for i in _hashes(value, bf['size']))


def display(bf):
    set_bits = sum(bf['bits'])
    print(f"bits set: {set_bits}/{bf['size']} ({100 * set_bits // bf['size']}% full)")
