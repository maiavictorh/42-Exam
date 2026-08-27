

def string_sculptor(text: str) -> str:
    i = 0
    res = []

    for c in text:
        if c.isalpha():
            res.append(c.lower() if i % 2 == 0 else c.upper())
            i += 1
        else:
            res.append(c)

    return "".join(res)


def main():
    print('\nInput: string_sculptor("hello")')
    print(f'Output: "{string_sculptor("hello")}"')

    print('\nInput: string_sculptor("Hello World")')
    print(f'Output: "{string_sculptor("Hello World")}"')

    print('\nInput: string_sculptor("aBc123def")')
    print(f'Output: "{string_sculptor("aBc123def")}"')

    print('\nInput: string_sculptor("Python3.9!")')
    print(f'Output: "{string_sculptor("Python3.9!")}"')

    print('\nInput: string_sculptor("")')
    print(f'Output: "{string_sculptor("")}"')


main()
