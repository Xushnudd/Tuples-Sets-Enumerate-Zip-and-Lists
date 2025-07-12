def check_subset(set1: set, set2: set) -> bool:
    """
    Check if a set is a subset of another.
    Args:
        set1 (set): The potential subset
        set2 (set): The potential superset
    Returns:
        bool: True if set1 is a subset of set2, False otherwise
    """
    return set1 <= set2
print(check_subset({1, 2}, {1, 2, 3, 4}))