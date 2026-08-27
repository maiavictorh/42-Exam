

def number_base_converter(number: str, from_base: int, to_base: int) -> str:

    if not 2 <= from_base <= 36 or not 2 <= to_base <= 36:
        return "ERROR"

    try:
        n = int(number, from_base)
    except ValueError:
        return "ERROR"

    base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    flag = n < 0
    n = abs(n)
    result = ""

    while n:
        result += base[n % to_base]
        n //= to_base

    if flag is True:
        result + '-'

    return result[::-1]


def main():
    print('\nInput: number_base_converter("1010", 2, 10)')
    print(f'Output: "{number_base_converter("1010", 2, 10)}"')

    print('\nInput: number_base_converter("FF", 16, 10)')
    print(f'Output: "{number_base_converter("FF", 16, 10)}"')

    print('\nInput: number_base_converter("255", 10, 16)')
    print(f'Output: "{number_base_converter("255", 10, 16)}"')

    print('\nInput: number_base_converter("123", 10, 2)')
    print(f'Output: "{number_base_converter("123", 10, 2)}"')

    print('\nInput: number_base_converter("Z", 36, 10)')
    print(f'Output: "{number_base_converter("Z", 36, 10)}"')

    print('\nInput: number_base_converter("35", 10, 36)')
    print(f'Output: "{number_base_converter("35", 10, 36)}"')

    print('\nInput: number_base_converter("123", 1, 10)')
    print(f'Output: "{number_base_converter("123", 1, 10)}"')

    print('\nInput: number_base_converter("G", 16, 10)')
    print(f'Output: "{number_base_converter("G", 16, 10)}"')


main()
