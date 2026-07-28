

def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    new_list = []
    new_matrix = []

    for list in matrix:
        new_list = list[::-1]
        new_matrix.append(new_list)

    return new_matrix


def main() -> None:

    test1 = [[1, 2, 3], [4, 5, 6]]
    test2 = [[1, 2], [3, 4], [5, 6]]
    test3 = [[1, 2, 3, 4]]
    test4 = [[-1, -2], [-3, -4]]

    print(f"\nInput: mirror_matrix({test1})")
    print("Ouput:", mirror_matrix(test1))

    print(f"\nInput: mirror_matrix({test2})")
    print("Ouput:", mirror_matrix(test2))

    print("\nInput: mirror_matrix([[7]])")
    print("Ouput:", mirror_matrix([[7]]))

    print(f"\nInput: mirror_matrix({test3})")
    print("Ouput:", mirror_matrix(test3))

    print(f"\nInput: mirror_matrix({test4})")
    print("Ouput:", mirror_matrix(test4))


main()
