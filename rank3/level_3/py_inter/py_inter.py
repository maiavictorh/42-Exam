

def inter(s1: str, s2: str) -> str:
    res = ""

    for c in s1:
        if c in res:
            continue
        if c in s2:
            res += c

    return res


def main() -> None:
    print('\nInput: inter("hello", "world")')
    print(f'Output: "{inter("hello", "world")}"')

    print('\nInput: inter("banana", "band")')
    print(f'Output: "{inter("banana", "band")}"')

    print('\nInput: inter("abcabc", "bc")')
    print(f'Output: "{inter("abcabc", "bc")}"')

    print('\nInput: inter("abc", "xyz")')
    print(f'Output: "{inter("abc", "xyz")}"')

    print('\nInput: inter("", "abc")')
    print(f'Output: "{inter("", "abc")}"')


main()
