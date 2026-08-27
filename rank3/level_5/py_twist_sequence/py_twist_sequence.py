

def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:
        return []

    n = len(arr)
    k = k % n

    if k == 0:
        return arr

    return arr[-k:] + arr[:-k]


def main():
    print('\nInput: twist_sequence([1, 2, 3, 4, 5], 2)')
    print(f'Output: {twist_sequence([1, 2, 3, 4, 5], 2)}')

    print('\nInput: twist_sequence([1, 2, 3], 1)')
    print(f'Output: {twist_sequence([1, 2, 3], 1)}')

    print('\nInput: twist_sequence([1, 2, 3, 4], 0)')
    print(f'Output: {twist_sequence([1, 2, 3, 4], 0)}')

    print('\nInput: twist_sequence([1, 2, 3], 5)')
    print(f'Output: {twist_sequence([1, 2, 3], 5)}')

    print('\nInput: twist_sequence([], 3)')
    print(f'Output: {twist_sequence([], 3)}')


main()
