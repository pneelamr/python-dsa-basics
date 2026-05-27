# Run-Length Encoding (RLE): Lossless compression that collapses runs of repeated characters.
# encode replaces each run with (character)(count), e.g. "aaabbc" → "a3b2c1".
# decode reverses this by parsing each (character, digits) pair and repeating the character.

# Time: O(n) — single pass over the string counting consecutive characters
# Space: O(n) — output list grows proportional to encoded string length
def encode(s):
    if not s:
        return ''
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return ''.join(result)


# Time: O(n) — single pass over the encoded string parsing chars and counts
# Space: O(n) — output list accumulates decoded characters
def decode(s):
    result = []
    i = 0
    while i < len(s):
        ch = s[i]
        i += 1
        num = ''
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
        result.append(ch * int(num))
    return ''.join(result)
