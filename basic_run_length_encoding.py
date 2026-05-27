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
