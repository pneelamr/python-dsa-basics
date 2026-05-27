# Aho-Corasick: Multi-pattern string matching automaton that finds all occurrences of multiple patterns simultaneously.
# Build a trie from all patterns; add failure links (like KMP's failure function) for O(1) mismatch transitions.
# After O(sum of pattern lengths) preprocessing, searches text in O(n + total matches) time.

import collections

# Time: O(sum of pattern lengths) — trie insertion plus one BFS pass to set failure links
# Space: O(sum of pattern lengths * alphabet_size) — trie nodes with children dicts
def build_automaton(patterns):
    automaton = [{'children': {}, 'fail': 0, 'output': []}]

    for pattern in patterns:
        cur = 0
        for ch in pattern:
            if ch not in automaton[cur]['children']:
                automaton[cur]['children'][ch] = len(automaton)
                automaton.append({'children': {}, 'fail': 0, 'output': []})
            cur = automaton[cur]['children'][ch]
        automaton[cur]['output'].append(pattern)

    queue = collections.deque()
    for ch, child in automaton[0]['children'].items():
        automaton[child]['fail'] = 0
        queue.append(child)

    while queue:
        u = queue.popleft()
        for ch, v in automaton[u]['children'].items():
            fail = automaton[u]['fail']
            while fail != 0 and ch not in automaton[fail]['children']:
                fail = automaton[fail]['fail']
            automaton[v]['fail'] = automaton[fail]['children'].get(ch, 0)
            if automaton[v]['fail'] == v:
                automaton[v]['fail'] = 0
            automaton[v]['output'] = automaton[v]['output'] + automaton[automaton[v]['fail']]['output']
            queue.append(v)

    return automaton

# Time: O(n + total matches) — each character advances the automaton in O(1); output collection is O(matches)
# Space: O(n + total matches) — result list storing all match positions
def search(text, automaton):
    cur = 0
    results = []
    for i, ch in enumerate(text):
        while cur != 0 and ch not in automaton[cur]['children']:
            cur = automaton[cur]['fail']
        cur = automaton[cur]['children'].get(ch, 0)
        for pattern in automaton[cur]['output']:
            results.append((i, pattern))
    return results
