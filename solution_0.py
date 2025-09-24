#!/usr/bin/env python3

def contains_permutation(s1: str, s2: str) -> bool:
    n = len(s1)
    m = len(s2)
    if n == 0:
        return True
    if m < n:
        return False

    # Build target counts
    target = {}
    for ch in s1:
        target[ch] = target.get(ch, 0) + 1

    # Initialize window counts for first n characters of s2
    window = {}
    for ch in s2[:n]:
        window[ch] = window.get(ch, 0) + 1

    if window == target:
        return True

    for i in range(n, m):
        left = s2[i - n]
        window[left] -= 1
        if window[left] == 0:
            del window[left]
        right = s2[i]
        window[right] = window.get(right, 0) + 1

        if window == target:
            return True

    return False

def main():
    s1 = 'ab'
    s2 = 'bddwasabsw'
    result = contains_permutation(s1, s2)
    print(result)

if __name__ == "__main__":
    main()