def replace_even_numbers(numbers: list) -> list:
    """
    Replace all even numbers with 0.
    Args:
        numbers (list): List of integers
    Returns:
        list: List with even numbers replaced by 0
    """
    l = []
    for i in numbers:
        if i%2 == 0:
            l.append(0)
        else:
            l.append(i)
    return l
print(replace_even_numbers([1, 2, 3, 4]))
