

def store_values(s: str) -> tuple[int, str, int]:
    return (len(s), s.lower(), sum(1 for c in s if c in "aeiouAEIOU"))


def cryptic_sorter(strings: list[str]) -> list[str]:

    strs_len = len(strings)

    for i in range(strs_len):
        for j in range(strs_len - 1):
            if store_values(strings[j]) > store_values(strings[j + 1]):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]

    return strings


def main() -> None:
    test1 = ["apple", "cat", "banana", "dog", "elephant"]
    test2 = ["aaa", "bbb", "AAA", "BBB"]
    test3 = ["hello", "world", "hi", "test"]

    print(f"\nInput: cryptic_sorter({test1})")
    print("Output:", cryptic_sorter(test1))

    print(f"\nInput: cryptic_sorter({test2})")
    print("Output:", cryptic_sorter(test2))

    print(f"\nInput: cryptic_sorter({test3})")
    print("Output:", cryptic_sorter(test3))

    print("\nInput: cryptic_sorter([])")
    print("Output:", cryptic_sorter([]))

    print("\nInput: cryptic_sorter([""])")
    print("Output:", cryptic_sorter([""]))


main()
