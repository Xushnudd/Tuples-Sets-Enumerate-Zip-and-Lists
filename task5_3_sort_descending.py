def sort_descending(numbers: list) -> list:
    """
    Sort a list in descending order.
    Args:
        numbers (list): List of numbers to sort
    Returns:
        list: List sorted in descending order
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers
print(sort_descending([5, 2, 9, 1]))
