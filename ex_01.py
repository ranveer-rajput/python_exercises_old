# NOTE: Do not modify function name, if you do, tests will not pass!
# Modify the return value to pass the test
def hello():
    return "Hello, World!"


def run_test(expected, weight, title, error_message):
    message = hello()
    if message == expected:
        print(f"Passed:{weight}:{title}")
    else:
        print(f"Failed:{title}:{error_message}")


run_test(
    expected="Hello, World!",
    weight=10,
    title="HelloWorldTest",
    error_message="Edit the return text according to the required value",
)
