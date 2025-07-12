def check_common_elements(set1: set, set2: set) -> bool:
    """
    Check if two sets have any common elements.
    Args:
        set1 (set): First set of numbers
        set2 (set): Second set of numbers
    Returns:
        bool: True if sets have common elements, False otherwise
    """
    b = False
    for i in set1:
        for a in set2:
            if i == a:
                b = True
    return b
print(check_common_elements(set1 = {1, 2, 3}, set2 = {4, 5, 3}))