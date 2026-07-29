

def hidenp(small: str, big: str) -> bool:
    comp = ""

    for c in big:
        if c in small:
            comp += c

    return small in comp


def main() -> None:
    print('\nInput: hidenp("abc", "a1b2c3")')
    print("Output:", hidenp("abc", "a1b2c3"))

    print('\nInput: hidenp("ace", "abcde")')
    print("Output:", hidenp("ace", "abcde"))

    print('\nInput: hidenp("aec", "abcde")')
    print("Output:", hidenp("aec", "abcde"))

    print('\nInput: hidenp("", "abc")')
    print("Output:", hidenp("", "abc"))

    print('\nInput: hidenp("abc", "ab")')
    print("Output:", hidenp("abc", "ab"))

    print('\nInput: hidenp("aaaa", "aaa")')
    print("Output:", hidenp("aaaa", "aaa"))

    print('\nInput: hidenp("sing", "subsequence testing")')
    print("Output:", hidenp("sing", "subsequence testing"))


main()
