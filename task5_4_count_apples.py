def count_apples(items: list) -> int:
    """
    Count how many times "apple" appears in a list.
    Args:
        items (list): List of strings
    Returns:
        int: Number of times "apple" appears in the list
    """
    a = 0
    for i in items:
        if i == "apple":
            a+=1
    return a
print(count_apples(["apple", "banana", "apple"]))
