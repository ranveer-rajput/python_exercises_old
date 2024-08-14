"""
## Instructions

Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
A factor is a number that evenly divides into another number, leaving no remainder.
The simplest way to test if a one number is a factor of another is to use the [modulo operation](https://en.wikipedia.org/wiki/Modulo_operation).

The rules of `raindrops` are that if a given number:

- has 3 as a factor, add 'Pling' to the result.
- has 5 as a factor, add 'Plang' to the result.
- has 7 as a factor, add 'Plong' to the result.
- _does not_ have any of 3, 5, or 7 as a factor, the result should be the digits of the number.

## Examples

- 28 has 7 as a factor, but not 3 or 5, so the result would be "Plong".
- 30 has both 3 and 5 as factors, but not 7, so the result would be "PlingPlang".
- 34 is not factored by 3, 5, or 7, so the result would be "34".

"""


def raindrops(n):
    rain_str = ""

    # Implement your logic here

    return rain_str


def run_test(number, expected, weight, title, error_message, hint):
    message = raindrops(number)
    if message == expected:
        print(f"Passed:{weight}:{title}")
    else:
        print(f"Failed:{title}:{error_message}{message}")
        print(hint)


run_test(
    1,
    "1",
    5,
    "test_1",
    "Expected '1' but got -> ",
    "Hint 👉: Check the handling of numbers not divisible by 3, 5, or 7",
)
run_test(
    3,
    "Pling",
    2,
    "test_3",
    "Expected 'Pling' but got -> ",
    "Hint 👉: Check the handling of numbers divisible by 3",
)
run_test(
    5,
    "Plang",
    2,
    "test_5",
    "Expected 'Plang' but got -> ",
    "Hint 👉: Check the handling of numbers divisible by 5",
)
run_test(
    7,
    "Plong",
    2,
    "test_7",
    "Expected 'Plong' but got -> ",
    "Hint 👉: Check the handling of numbers divisible by 7",
)
run_test(
    6,
    "Pling",
    2,
    "test_6",
    "Expected 'Pling' but got -> ",
    "Hint 👉: Check the handling of numbers divisible by both 3 and 2",
)
run_test(
    8,
    "8",
    5,
    "test_8",
    "Expected '8' but got -> ",
    "Hint 👉: Check the handling of numbers not divisible by 3, 5, or 7",
)
run_test(
    9,
    "Pling",
    2,
    "test_9",
    "Expected 'Pling' but got -> ",
    "Hint 👉: Check the handling of numbers divisible by 3",
)
run_test(
    10,
    "Plang",
    2,
    "test_10",
    "Expected 'Plang' but got -> ",
    "Hint 👉: Check the handling of numbers divisible by 5",
)
run_test(
    14,
    "Plong",
    2,
    "test_14",
    "Expected 'Plong' but got -> ",
    "Hint 👉: Check the handling of numbers divisible by 7",
)
run_test(
    15,
    "PlingPlang",
    2,
    "test_15",
    "Expected 'PlingPlang' but got -> ",
    "Hint 👉: Check the handling of numbers divisible by both 3 and 5",
)
run_test(
    21,
    "PlingPlong",
    2,
    "test_21",
    "Expected 'PlingPlong' but got -> ",
    "Hint 👉: Check the handling of numbers divisible by both 3 and 7",
)
run_test(
    25,
    "Plang",
    2,
    "test_25",
    "Expected 'Plang' but got -> ",
    "Hint 👉: Check the handling of numbers divisible by 5",
)
run_test(
    27,
    "Pling",
    2,
    "test_27",
    "Expected 'Pling' but got -> ",
    "Hint 👉: Check the handling of numbers divisible by 3",
)
run_test(
    35,
    "PlangPlong",
    2,
    "test_35",
    "Expected 'PlangPlong' but got -> ",
    "Hint 👉: Check the handling of numbers divisible by both 5 and 7",
)
run_test(
    49,
    "Plong",
    2,
    "test_49",
    "Expected 'Plong' but got -> ",
    "Hint 👉: Check the handling of numbers divisible by 7",
)
run_test(
    52,
    "52",
    5,
    "test_52",
    "Expected '52' but got -> ",
    "Hint 👉: Check the handling of numbers not divisible by 3, 5, or 7",
)
run_test(
    105,
    "PlingPlangPlong",
    2,
    "test_105",
    "Expected 'PlingPlangPlong' but got -> ",
    "Hint 👉: Check the handling of numbers divisible by 3, 5, and 7",
)
run_test(
    3125,
    "Plang",
    2,
    "test_3125",
    "Expected 'Plang' but got -> ",
    "Hint 👉: Check the handling of numbers divisible by 5",
)
run_test(
    12121,
    "12121",
    5,
    "test_12121",
    "Expected '12121' but got -> ",
    "Hint 👉: Check the handling of numbers not divisible by 3, 5, or 7",
)
