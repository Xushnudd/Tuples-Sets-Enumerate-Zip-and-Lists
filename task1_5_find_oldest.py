def find_oldest(people: list) -> tuple:
    """
    Find the oldest person from a list of tuples (name, age).
    Args:
        people (list): List of tuples containing (name, age) pairs
    Returns:
        tuple: A tuple containing (name, age) of the oldest person
    """
    k = 0
    n = ""
    for i, y in people:
        if y>k:
            k = y
            n = i
    return n, k
print(find_oldest([("Ali", 20), ("Sara", 25), ("John", 22)]))