# NOTE: Do not modify function name, if you do, tests will not pass!
# Modify the function to return largest number from `numbers` list
def largest_number(numbers):
    if len(numbers) == 0:
        return -1

    max = 0

    for i in numbers:
        if i > max:
            max = i

    return max


def run_test(expected, numbers, weight, title, error_message):
    largest = largest_number(numbers)
    if largest == expected:
        print(f"Passed:{weight}:{title}")
    else:
        print(f"Failed:{title}:{error_message}")


run_test(
    9,
    [4, 1, 9, 8],
    10,
    "BigNumberTest",
    "Please check your logic to return the correct largest number",
)

run_test(
    -1,
    [],
    5,
    "EmptyListTest",
    "When `numbers` is an empty list, the largest number should be `-1`",
)
