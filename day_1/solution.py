def main():
    # Part 1
    with open("input.txt", "r") as file:
        lines = file.readlines()

    left_list: list[int] = []
    right_list: list[int] = []

    for line in lines:
        left, right = line.strip().split()
        left_list.append(int(left))
        right_list.append(int(right))

    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)

    distance = 0
    for i in range(len(sorted_left)):
        distance += abs(sorted_left[i] - sorted_right[i])

    print(f"Part 1: Total sum: {distance}")

    # Part 2

    # Count occurrences of left numbers in right list
    similarity_score = 0
    for left_num in left_list:
        count = right_list.count(left_num)
        similarity_score += left_num * count

    print(f"Part 2: Similarity score: {similarity_score}")

if __name__ == "__main__":
    main()

