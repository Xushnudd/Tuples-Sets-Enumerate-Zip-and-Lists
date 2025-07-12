def count_threes(numbers: tuple) -> int:
    """
    Count how many times 3 appears in the tuple.
    Args:
        numbers (tuple): A tuple of integers
    Returns:
        int: The count of number 3 in the tuple
    """
    s = 0
    for i in numbers:
        if i == 3:
            s+=1
    return s;
print(count_threes((1, 3, 3, 7, 3, 3)))
