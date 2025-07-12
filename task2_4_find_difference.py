def find_difference(set1: set, set2: set) -> set:
    """
    Find the difference between two sets.
    Args:
        set1 (set): First set of numbers
        set2 (set): Second set of numbers
    Returns:
        set: Elements in set1 that are not in set2
    """
    return set1.difference(set2)
print(find_difference({1, 2, 3}, {2, 3, 4}))