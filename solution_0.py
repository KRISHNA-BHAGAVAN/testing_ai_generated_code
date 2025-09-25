import sys

def swap_no_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

def to_number(s):
    try:
        if any(ch in s for ch in ('.', 'e', 'E')):
            return float(s)
        return int(s)
    except Exception:
        raise ValueError(f"Invalid numeric input: {s}")

def read_two_numbers():
    data = []
    for line in sys.stdin:
        parts = line.strip().split()
        for p in parts:
            if p:
                data.append(p)
                if len(data) >= 2:
                    break
        if len(data) >= 2:
            break
    if len(data) >= 2:
        a = to_number(data[0])
        b = to_number(data[1])
        return a, b
    else:
        return 0, 0

def main():
    a, b = read_two_numbers()
    a, b = swap_no_temp(a, b)
    print(a, b)

if __name__ == "__main__":
    main()