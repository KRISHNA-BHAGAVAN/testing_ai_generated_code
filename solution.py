import sys

def main():
    data = sys.stdin.read().strip()
    if not data:
        return
    print(data)

if __name__ == "__main__":
    main()