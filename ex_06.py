class ListOperations:
    def __init__(self, x, y):
        """
        Initialize the SetOperations class with two lists.

        :param x: The first list
        :param y: The second list
        """
        pass

    def merge(self):
        """
        Merge the two lists and return the merged list, duplicates are allowed.

        Example 1:
        - Input: [a,b,c], [1,2,3]
        - Output: [a,b,c,1,2,3]
        - Explanation: Two lists are merged

        Example 2:
        - Input: [1,4,1,6], [2,3,5,2]
        - Output: [1,4,1,6,2,3,5,2]
        - Explanation: Duplicate items are not removed from the merged list
        """
        pass


# Test class
class Tests:
    @staticmethod
    def run_merge_test(expected, x, y, weight, title, error_message):
        set_ops = ListOperations(x, y)
        res = set_ops.merge()

        if len(expected) == len(res):
            print(f"Passed:{weight}:{title}")
        else:
            print(f"Failed:{title}:{error_message}")


# -----------------------------
# Test cases for merging
# -----------------------------

Tests.run_merge_test(
    ["a", "b", "c", 1, 2, 3],
    ["a", "b", "c"],
    [1, 2, 3],
    5,
    "MergeLists",
    "Please check your logic correctly",
)

Tests.run_merge_test(
    ["a", "b", "c", "a", 1, 2, 3, 2],
    ["a", "b", "c", "a"],
    [1, 2, 3, 2],
    10,
    "DuplicateItems",
    "Keep duplicates in resulting list",
)

Tests.run_merge_test(
    [],
    [],
    [],
    5,
    "EmptyLists",
    "The union of two empty lists should be an empty list",
)

Tests.run_merge_test(
    [[1, 2], [3, 4], 5, 6],
    [[1, 2], [3, 4]],
    [5, 6],
    15,
    "NestedLists",
    "The union should work with lists containing nested lists",
)

Tests.run_merge_test(
    [0, False, "", [], None, 1, True, "a", [1]],
    [0, False, "", []],
    [None, 1, True, "a", [1]],
    20,
    "FalsyValues",
    "The union should handle and distinguish between falsy values",
)
