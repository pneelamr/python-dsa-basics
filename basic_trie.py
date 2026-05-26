def create_trie():
    return {}


def insert(trie, word):
    node = trie
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]
    node['*'] = True  # marks end of word


def search(trie, word):
    node = trie
    for char in word:
        if char not in node:
            return False
        node = node[char]
    return '*' in node


def starts_with(trie, prefix):
    node = trie
    for char in prefix:
        if char not in node:
            return False
        node = node[char]
    return True


def delete(trie, word):
    def _delete(node, word, depth):
        if depth == len(word):
            if '*' not in node:
                return False
            del node['*']
            return len(node) == 0
        char = word[depth]
        if char not in node:
            return False
        if _delete(node[char], word, depth + 1):
            del node[char]
            return len(node) == 0
        return False
    _delete(trie, word, 0)


def display(trie):
    print(trie)
