# Huffman Coding: Greedy algorithm building optimal variable-length prefix-free codes for data compression.
# Build a min-heap of (frequency, char) nodes; repeatedly merge the two lowest-frequency nodes until one tree remains.
# Characters with higher frequency get shorter codes; no code is a prefix of another (prefix-free property).

import heapq

# Time: O(n log n) — each of n merge steps does a heap push/pop in O(log n)
# Space: O(n) — heap and tree together hold O(n) nodes
def build_huffman_tree(freq_map):
    counter = [0]
    heap = []
    for char, freq in freq_map.items():
        node = [freq, char, None, None]
        heapq.heappush(heap, (freq, counter[0], node))
        counter[0] += 1
    if len(heap) == 1:
        freq, _, node = heapq.heappop(heap)
        root = [freq, None, node, None]
        return root
    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)
        merged = [f1 + f2, None, left, right]
        heapq.heappush(heap, (f1 + f2, counter[0], merged))
        counter[0] += 1
    _, _, root = heapq.heappop(heap)
    return root

# Time: O(n) — visits each node exactly once; n is number of nodes in the tree
# Space: O(n) — output codes dict plus recursion stack depth O(n) worst case
def get_codes(node, prefix='', codes=None):
    if codes is None:
        codes = {}
    if node is None:
        return codes
    freq, char, left, right = node
    if char is not None:
        codes[char] = prefix if prefix else '0'
        return codes
    get_codes(left, prefix + '0', codes)
    get_codes(right, prefix + '1', codes)
    return codes

# Time: O(n * L) — n characters each looked up in codes dict, L is average code length
# Space: O(n) — encoded string and tree storage
def encode(text):
    freq_map = {}
    for ch in text:
        freq_map[ch] = freq_map.get(ch, 0) + 1
    root = build_huffman_tree(freq_map)
    codes = get_codes(root)
    encoded = ''.join(codes[ch] for ch in text)
    return encoded, root

# Time: O(m) — m is the length of the encoded bit string; each bit traverses one tree edge
# Space: O(1) — only pointers and the output string
def decode(encoded, root):
    result = []
    node = root
    for bit in encoded:
        freq, char, left, right = node
        if bit == '0':
            node = left
        else:
            node = right
        if node is None:
            break
        freq2, char2, l2, r2 = node
        if char2 is not None:
            result.append(char2)
            node = root
    return ''.join(result)
