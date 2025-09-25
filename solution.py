#!/usr/bin/env python3
import sys

def palindrome_by_appending_reverse(num_str: str) -> str:
    """
    Create a palindrome by appending the reverse of the numeric digits.
    Example: '1223' -> '12233221'
    Non-digit characters are ignored.
    """
    digits = ''.join(ch for ch in num_str if ch.isdigit())
    if not digits:
        return ''
    return digits + digits[::-1]

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    results = [palindrome_by_appending_reverse(token) for token in data]
    sys.stdout.write('\n'.join(results))

if __name__ == "__main__":
    main()