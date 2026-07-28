

def echo_validator(text: str) -> bool:

    if not text or len(text) == 0:
        return False
    return text.replace(" ", "").lower() == text[::-1].replace(" ", "").lower()


def main() -> None:
    print("\nInput: echo_validator('racecar')")
    print("Output:", echo_validator("racecar"))

    print("\nInput: echo_validator('A man a plan a canal Panama')")
    print("Output:", echo_validator("A man a plan a canal Panama"))

    print("\nInput: echo_validator('race a car')")
    print("Output:", echo_validator("race a car"))

    print("\nInput: echo_validator('Was it a car or a cat I saw')")
    print("Output:", echo_validator("Was it a car or a cat I saw"))

    print("\nInput: echo_validator('hello')")
    print("Output:", echo_validator("hello"))

    print("\nInput: echo_validator('Madam Im Adam')")
    print("Output:", echo_validator("Madam Im Adam"))

    print("\nInput: echo_validator('')")
    print("Output:", echo_validator(""))


main()
