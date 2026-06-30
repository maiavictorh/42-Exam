from sys import argv


def bracket_validator(s: str) -> bool:
    stack = []
    flag = True

    if len(s) == 0:
        return True

    if "(" in s:
        stack.append("(")
    if "[" in s:
        stack.append("[")
    if "{" in s:
        stack.append("{")

    if ")" in s:
        print(stack)
        if not stack or stack[-1] != "(":
            return False
        elif stack[-1] == "(":
            stack.pop(-1)

    if "]" in s:
        print(stack)
        if not stack or stack[-1] != "[":
            return False
        elif stack[-1] == "[":
            stack.pop(-1)

    if "}" in s:
        if not stack or stack[-1] != "{":
            return False

    print(stack)
    return flag


if __name__ == "__main__":
    s = argv[1]

    print(f"Input: bracket_validator(\"{s}\")")
    print("Output:", bracket_validator(s))
