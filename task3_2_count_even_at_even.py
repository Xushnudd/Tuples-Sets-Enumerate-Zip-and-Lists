def count_even_at_even(numbers: list) -> int:
    """
    Count how many even numbers are at even indexes.
    Args:
        numbers (list): List of integers
    Returns:
        int: Count of even numbers at even indexes
    """
    a = numbers[2::2]
    b = 0
    for i in a:
        if i%2 == 0:
            b += 1
    return b
print(count_even_at_even([2, 4, 6, 3, 8]))
