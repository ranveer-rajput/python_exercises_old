# NOTE: Do not modify function name, if you do, tests will not pass!
# Modify the function to check if x exists in `numbers` list
def search_number(x, numbers):
    if len(numbers) == 0:
        return False

    for i in numbers:
        if i == x:
            return True

    return False


def run_test(ans, expected, numbers, weight, title, error_message):
    res = search_number(expected, numbers)
    if ans == res:
        print(f"Passed:{weight}:{title}")
    else:
        print(f"Failed:{title}:{error_message}")


run_test(True, 9, [4, 1, 9, 8], 5, "FoundTest", "Please check your logic correctly")

run_test(
    False,
    100,
    [12, 45, 7, 23, 56, 89, 34],
    5,
    "NotFoundTest",
    "Please check your logic correctly",
)

run_test(
    False,
    -1,
    [],
    10,
    "EmptyListTest",
    "When numbers is an empty list the output should be `False`",
)
