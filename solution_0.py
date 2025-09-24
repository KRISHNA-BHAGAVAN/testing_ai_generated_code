from collections import Counter

def check_inclusion(s1, s2):
    len1, len2 = len(s1), len(s2)
    if len1 == 0:
        return True
    if len1 > len2:
        return False

    target = Counter(s1)
    window = Counter(s2[:len1])
    if window == target:
        return True

    for i in range(len1, len2):
        out_char = s2[i - len1]
        in_char = s2[i]

        window[out_char] -= 1
        if window[out_char] == 0:
            del window[out_char]

        window[in_char] += 1

        if window == target:
            return True

    return False

def main():
    s1 = 'ab'
    s2 = 'bddwasabsw'
    result = check_inclusion(s1, s2)
    print(result)

if __name__ == "__main__":
    main()