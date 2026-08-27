

def anagram(s1: str, s2: str) -> bool:

    return sorted(s1.lower().replace(" ", "")) \
            == sorted(s2.lower().replace(" ", ""))


def main():
    print('\nInput: anagram("listen", "silent")')
    print(f'Output: {anagram("listen", "silent")}')

    print('\nInput: anagram("Triangle", "Integral")')
    print(f'Output: {anagram("Triangle", "Integral")}')

    print('\nInput: anagram("Dormitory", "Dirty Room")')
    print(f'Output: {anagram("Dormitory", "Dirty Room")}')

    print('\nInput: anagram("hello", "world")')
    print(f'Output: {anagram("hello", "world")}')

    print('\nInput: anagram("", "")')
    print(f'Output: {anagram("", "")}')

    print('\nInput: anagram("abc", "abcc")')
    print(f'Output: {anagram("abc", "abcc")}')


main()
