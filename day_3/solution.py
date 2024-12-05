import re

def find_mul_numbers(text: str) -> list[tuple[int, int]]:
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.finditer(pattern, text)
    return [(int(match.group(1)), int(match.group(2))) for match in matches]

def find_enabled_mul_numbers(text: str) -> list[tuple[int, int]]:
    pattern = r'(mul\((\d+),(\d+)\)|don\'t\(\)|do\(\))'
    matches = re.finditer(pattern, text)
    result: list[tuple[int, int]] = []
    enabled = True

    for match in matches:
        full_match = match.group(1)
        if full_match == "don't()":
            enabled = False
        elif full_match == "do()":
            enabled = True
        elif enabled:  # Only add mul numbers if enabled
            nums = re.match(r'mul\((\d+),(\d+)\)', full_match)
            if nums:
                result.append((int(nums.group(1)), int(nums.group(2))))

    return result

def main():
    with open("input.txt", "r") as file:
        text = file.read()

    # Part 1
    print("Part 1:")
    factor_pairs = find_mul_numbers(text)
    sum_of_products = 0
    for pair in factor_pairs:
        sum_of_products += pair[0] * pair[1]
    print(f"Sum of products: {sum_of_products}")

    # Part 2
    print("\nPart 2:")
    enabled_pairs = find_enabled_mul_numbers(text)
    sum_of_enabled_products = 0
    for pair in enabled_pairs:
        sum_of_enabled_products += pair[0] * pair[1]
    print(f"Sum of enabled products: {sum_of_enabled_products}")

if __name__ == "__main__":
    main()