def is_safe(report_str):
    # Convert string of numbers to list of integers
    numbers = [int(num) for num in report_str.split()]

    if len(numbers) < 2:
        return True

    # Check if sequence is ascending or descending
    is_ascending = all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
    is_descending = all(numbers[i] >= numbers[i+1] for i in range(len(numbers)-1))

    if not (is_ascending or is_descending):
        return False

    # Check for minimum difference of 1 and maximum difference of 3 between consecutive numbers
    for i in range(len(numbers)-1):
        diff = abs(numbers[i] - numbers[i+1])
        if diff < 1 or diff > 3:
            return False

    return True

def can_be_safe(report_str):
    # If it's already safe, no need to remove anything
    if is_safe(report_str):
        return True

    numbers = [int(num) for num in report_str.split()]

    # Try removing each number one at a time
    for i in range(len(numbers)):
        # Create new list without the current number
        test_numbers = numbers[:i] + numbers[i+1:]
        # Convert back to string format that is_safe expects
        test_report = ' '.join(map(str, test_numbers))

        if is_safe(test_report):
            return True

    return False

def main():
    with open("input.txt", "r") as file:
        reports = file.read().splitlines()

    print("Part 1:")
    # Process each report
    report_statuses = []
    for report in reports:
        report_statuses.append(is_safe(report))

    safe_count = sum(report_statuses)
    unsafe_count = len(report_statuses) - safe_count
    print(f"Safe reports: {safe_count}")
    print(f"Unsafe reports: {unsafe_count}")

    print("\nPart 2:")
    # Process each report for part 2
    fixable_count = 0
    unfixable_count = 0

    for report in reports:
        if can_be_safe(report):
            fixable_count += 1
        else:
            unfixable_count += 1

    print(f"Reports that are safe or can be made safe: {fixable_count}")
    print(f"Reports that cannot be made safe: {unfixable_count}")

if __name__ == "__main__":
    main()
