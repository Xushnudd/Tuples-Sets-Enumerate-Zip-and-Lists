def add_element(lst: list, element: any) -> list:
    """
    Add an element to the end of a list.
    Args:
        lst (list): The input list
        element (any): Element to add to the list
    Returns:
        list: List with the new element added
    """
    return lst+[element]
print(add_element([1, 2, 3], 4))
