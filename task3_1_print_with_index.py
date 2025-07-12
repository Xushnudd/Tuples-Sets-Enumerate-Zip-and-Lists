def print_with_index(items: list) -> None:
    """
    Use enumerate to print each item in a list with its index.
    Args:
        items (list): List of items to print with their indices
    Returns:
        None: Prints each item with its index
    """
    index = 0
    for i in items:
        print(index, i)
        index+=1
print(print_with_index(["apple", "banana", "cherry"]))
