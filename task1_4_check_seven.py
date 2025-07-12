def check_seven(numbers: tuple) -> bool:
    """
    Check if the number 7 exists in a tuple.
    Args:
        numbers (tuple): A tuple of integers
    Returns:
        bool: True if 7 is in the tuple, False otherwise
    """
    a = False
    for i in numbers:
        if i == 7:
            a = True
    return a
print(check_seven((1, 2, 3, 4)))
