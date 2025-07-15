def find_passing_students(names: list, scores: list, passing_score: int = 60) -> list:
    """
    Find which students passed using names and scores.
    Args:
        names (list): List of student names
        scores (list): List of corresponding scores
        passing_score (int): Minimum score to pass, defaults to 60
    Returns:
        list: List of names of students who passed
    """
    p = []
    for i in range(len(names)):
        if scores[i] >= passing_score:
            p.append(names[i])
    return p
print(find_passing_students(["Ali", "Sara"], [45, 85]))
