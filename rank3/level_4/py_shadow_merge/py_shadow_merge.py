

def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:

    return sorted(list1 + list2)


def main():
    print('\nInput: shadow_merge([1, 3, 5], [2, 4, 6])')
    print(f'Output: {shadow_merge([1, 3, 5], [2, 4, 6])}')

    print('\nInput: shadow_merge([1, 2, 3], [4, 5, 6])')
    print(f'Output: {shadow_merge([1, 2, 3], [4, 5, 6])}')

    print('\nInput: shadow_merge([1], [2, 3, 4])')
    print(f'Output: {shadow_merge([1], [2, 3, 4])}')

    print('\nInput: shadow_merge([], [1, 2, 3])')
    print(f'Output: {shadow_merge([], [1, 2, 3])}')

    print('\nInput: shadow_merge([1, 1, 2], [1, 3, 3])')
    print(f'Output: {shadow_merge([1, 1, 2], [1, 3, 3])}')


main()
