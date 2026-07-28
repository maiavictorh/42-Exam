

def bracket_validator(s: str) -> bool:
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}

    for c in s:
        if c in brackets:
            stack.append(c)
        elif c in brackets.values():
            if not stack:
                return False
            if brackets[stack[-1]] != c:
                return False
            stack.pop()

    return len(stack) == 0


def main1():
    print("\nInput: bracket_validator('()')")
    print("Output:", bracket_validator('()'))

    print("\nInput: bracket_validator('()[]{}')")
    print("Output:", bracket_validator('()[]{}'))

    print("\nInput: bracket_validator('(]')")
    print("Output:", bracket_validator('(]'))

    print("\nInput: bracket_validator('([)]')")
    print("Output:", bracket_validator('([)]'))

    print("\nInput: bracket_validator('{[]}')")
    print("Output:", bracket_validator('{[]}'))

    print("\nInput: bracket_validator('hello(world)')")
    print("Output:", bracket_validator('hello(world)'))

    print("\nInput: bracket_validator('((())')")
    print("Output:", bracket_validator('((())'))

    print("\nInput: bracket_validator('')")
    print("Output:", bracket_validator(''))


def main2():
    from sys import argv

    if len(argv) < 2:
        print("Don't forget the second argument!")
        return

    s = argv[1]
    print(f"\nInput: bracket_validator('{s}')")
    print("Output:", bracket_validator(s))


main1()
