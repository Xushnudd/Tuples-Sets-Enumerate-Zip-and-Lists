def swap_values(a: int, b: int) -> tuple:
    """
    Swap the values of two variables using a tuple.
    Args:
        a (int): First number
        b (int): Second number
    Returns:
        tuple: A tuple containing the swapped values (b, a)
    """
    a, b = b, a
    return (a, b)
print(swap_values(12, 23))
