def find_word_count(matrix: list[list[str]], word: str) -> int:
    if not matrix or not word:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    # All eight directions: right, right-down, down, left-down, left, left-up, up, right-up
    directions = [
        (0, 1), (1, 1), (1, 0), (1, -1),
        (0, -1), (-1, -1), (-1, 0), (-1, 1)
    ]

    def search_direction(row: int, col: int, dx: int, dy: int) -> bool:
        # Check if the word can be formed starting at (row, col) going in direction (dx, dy)
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False

        for i in range(len(word)):
            curr_row = row + i * dx
            curr_col = col + i * dy

            if (curr_row < 0 or curr_row >= rows or
                curr_col < 0 or curr_col >= cols or
                matrix[curr_row][curr_col] != word[i]):
                return False
        return True

    # Check each starting position
    for i in range(rows):
        for j in range(cols):
            # Try all eight directions from this position
            for dx, dy in directions:
                if search_direction(i, j, dx, dy):
                    count += 1

    return count

def find_only_crosses(matrix: list[list[str]], word: str) -> int:
    if not matrix or not word:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    reversed_word = word[::-1]

    def search_right_down(row: int, col: int, search_word: str) -> bool:
        # Check if the word can be formed starting at (row, col) going right-down
        for i in range(len(search_word)):
            curr_row = row + i
            curr_col = col + i

            if (curr_row >= rows or curr_col >= cols or
                matrix[curr_row][curr_col] != search_word[i]):
                return False
        return True

    def search_left_down(row: int, col: int, search_word: str) -> bool:
        # Check if the word can be formed starting at (row, col) going left-down
        for i in range(len(search_word)):
            curr_row = row + i
            curr_col = col - i

            if (curr_row >= rows or curr_col < 0 or
                matrix[curr_row][curr_col] != search_word[i]):
                return False
        return True

    # Check each starting position
    for i in range(rows):
        for j in range(cols):
            # Skip if we can't form an X pattern (need 2 more columns to the right)
            if j + 2 >= cols:
                continue

            # Try to find first diagonal (right-down)
            first_diagonal = (search_right_down(i, j, word) or
                            search_right_down(i, j, reversed_word))

            if first_diagonal:
                # If found, try to find second diagonal from 2 cells to the right
                second_diagonal = (search_left_down(i, j + 2, word) or
                                 search_left_down(i, j + 2, reversed_word))

                if second_diagonal:
                    count += 1

    return count

def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        matrix = [list(line.strip()) for line in lines]
    print("Part 1:")
    print(find_word_count(matrix, "XMAS"))
    print("Part 2:")
    print(find_only_crosses(matrix, "MAS"))
if __name__ == "__main__":
    main()