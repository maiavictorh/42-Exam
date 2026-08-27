

def string_permutation_checker(s1: str, s2: str) -> bool:

    return sorted(s1) == sorted(s2)


def main():
    print('\nInput: string_permutation_checker("abc", "bca")')
    print(f'Output: {string_permutation_checker("abc", "bca")}')

    print('\nInput: string_permutation_checker("abc", "def")')
    print(f'Output: {string_permutation_checker("abc", "def")}')

    print('\nInput: string_permutation_checker("listen", "silent")')
    print(f'Output: {string_permutation_checker("listen", "silent")}')

    print('\nInput: string_permutation_checker("hello", "bello")')
    print(f'Output: {string_permutation_checker("hello", "bello")}')

    print('\nInput: string_permutation_checker("", "")')
    print(f'Output: {string_permutation_checker("", "")}')

    print('\nInput: string_permutation_checker("a", "")')
    print(f'Output: {string_permutation_checker("a", "")}')

    print('\nInput: string_permutation_checker("Abc", "abc")')
    print(f'Output: {string_permutation_checker("Abc", "abc")}')

    print('\nInput: string_permutation_checker("a gentleman", "elegant man")')
    print('Output:', string_permutation_checker("a gentleman", "elegant man"))


main()
