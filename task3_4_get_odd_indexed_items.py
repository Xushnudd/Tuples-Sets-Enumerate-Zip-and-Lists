def get_odd_indexed_items(items: list) -> list:
    """
    Print only items at odd indexes.
    Args:
        items (list): List of items
    Returns:
        list: Items at odd indexes
    """
    a = items[1::2]
    return a
print(get_odd_indexed_items([2, 4, 6, 3, 8]))
