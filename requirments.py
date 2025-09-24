def filter_by_date(due_date, submissions):
    """
    Filter submissions by a specific due date.
    
    Args:
        due_date: The target due date to filter by (expected to match submission_date format)
        submissions (list): List of submission dictionaries, each containing a 'submission_date' key
    
    Returns:
        list: List of submissions that match the specified due date. Returns empty list if no submissions provided.
    """
    if not submissions:
        return []
    
    matching_submissions = [
        submission for submission in submissions 
        if submission.get("submission_date") == due_date
    ]
    return matching_submissions


def filter_by_student_id(student_id, submissions):
    """
    Filter submissions by a specific student ID.
    
    Args:
        student_id: The target student ID to filter by
        submissions (list): List of submission dictionaries, each containing a 'student_id' key
    
    Returns:
        list: List of submissions that match the specified student ID. Returns empty list if no submissions provided.
    """
    if not submissions:
        return []
    
    return [submission for submission in submissions if submission.get("student_id") == student_id]


def find_unsubmitted(due_date, student_names, submissions):
    """
    Find students who have not submitted their assignment by a specific due date.
    
    Args:
        due_date (str): The due date to check submissions against
        student_names (list[str]): List of all student names to check
        submissions (list[dict]): List of submission dictionaries containing 'submission_date' and 'student_name' keys
    
    Returns:
        list[str]: List of student names who have not submitted by the due date
    """
    if not student_names:
        return []
    
    filtered_submissions = filter_by_date(due_date, submissions)
    unsubmitted_students = student_names.copy()
    
    for submission in filtered_submissions:
        student_name = submission.get("student_name")
        if student_name in unsubmitted_students:
            unsubmitted_students.remove(student_name)
    
    return unsubmitted_students


def get_average_score(submissions):
    """
    Calculate the average quiz score across all submissions.
    
    Args:
        submissions (list[dict]): List of submission dictionaries, each containing a 'quiz_score' key
    
    Returns:
        float: Average quiz score across all submissions
    """
    total = 0
    for submission in submissions:
        total += submission.get("quiz_score", 0)  
    
    return total / len(submissions)


def get_average_score_by_module(submissions):
    """
    Calculate average quiz scores grouped by module.
    
    Args:
        submissions (list[dict]): List of submission dictionaries containing 'quiz_module' and 'quiz_score' keys
    
    Returns:
        dict: Dictionary mapping module names to their average scores.
    """
    if not submissions:
        return {}

    scores_by_module = {}
    for submission in submissions:
        quiz_module = submission.get("quiz_module")
        quiz_score = submission.get("quiz_score", 0)
        
        if quiz_module in scores_by_module:
            scores_by_module[quiz_module].append(quiz_score)
        else:
            scores_by_module[quiz_module] = [quiz_score]
    
    averages_by_module = {}
    for module, scores in scores_by_module.items():
        averages_by_module[module] = sum(scores) / len(scores)
    
    return averages_by_module