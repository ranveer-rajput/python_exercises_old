"""
Given a string of digits, output all the contiguous substrings of length `n` in
that string in the order that they appear.

For example, the string "49142" has the following 3-digit series:

- "491"
- "914"
- "142"

And the following 4-digit series:

- "4914"
- "9142"

And if you ask for a 6-digit series from a 5-digit string, you deserve
whatever you get.
"""

# def get_series(digits, length):
#     result = []
#     i = 0
#     while i <= len(digits) - length:
#         substring = ''
#         j = 0

#         while j < length:
#             substring =substring+ str(digits[i + j])
#             j += 1

#         result.append(substring)
#         i += 1
#     return result


# def get_series(digits,length):
#     result=[]
#     i=0
#     while i<=len(digits)-length:
#
#         substring=digits[i:i+length]
#         result.append(substring)

#         i=i+1
#     return result


def get_series(digits, length):
    result = []
    for i in range(len(digits) - length + 1):
        substr = digits[i : i + length]
        result.append(substr)
    return result


# digits = [1, 2, 3, 4]
# print(get_series(digits, 2))


def run_test(digits, length, expected, weight, title, hint):
    series = get_series(digits, length)

    if expected == series:
        print(f"Passed: {weight}: {title}")
    else:
        print(f"Failed: {title}: Expected -> {expected}, but got -> {series}")
        print(hint)


expected_length_2 = ["92", "20", "01", "17"]
run_test(
    "92017",
    2,
    expected_length_2,
    5,
    "test_with_length_2",
    "Hint: The function should return all possible substrings of length 2 from the given digits.",
)

expected_zero_length = ["", "", "", "", "", ""]
run_test(
    "92017",
    0,
    expected_zero_length,
    10,
    "test_with_zero_length",
    "Hint: Set len to 0 should return an array of empty strings with a length equal to digits.length() + 1.",
)

expected_numbers_length = ["92017"]
run_test(
    "92017",
    5,
    expected_numbers_length,
    5,
    "test_with_numbers_length",
    "Hint: When len is equal to the length of digits, the function should return the original digits as a single substring.",
)

expected_too_long = []
run_test(
    "92017",
    6,
    expected_too_long,
    10,
    "test_too_long",
    "Hint: When len is greater than the length of digits, the function should return an empty array.",
)
