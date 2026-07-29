

def pattern_tracker(text: str) -> int:
    count = 0

    for i in range(len(text) - 1):
        if (text[i].isdigit() and text[i + 1].isdigit()
           and int(text[i]) == int(text[i + 1]) - 1):
            count += 1

    return count


def main() -> None:
    print('\nInput: pattern_tracker("123")')
    print('Output:', pattern_tracker("123"))

    print('\nInput: pattern_tracker("12a34")')
    print('Output:', pattern_tracker("12a34"))

    print('\nInput: pattern_tracker("987654321")')
    print('Output:', pattern_tracker("987654321"))

    print('\nInput: pattern_tracker("01234567")')
    print('Output:', pattern_tracker("01234567"))

    print('\nInput: pattern_tracker("abc")')
    print('Output:', pattern_tracker("abc"))

    print('\nInput: pattern_tracker("1a2b3c4")')
    print('Output:', pattern_tracker("1a2b3c4"))

    print('\nInput: pattern_tracker("112233")')
    print('Output:', pattern_tracker("112233"))


main()
