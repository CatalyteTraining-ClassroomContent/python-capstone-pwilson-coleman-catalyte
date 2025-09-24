submissions = {
"quiz_name": "string",
"quiz_module": "string",
"quiz_score": int,
"student_id": int,
"student_name": "string",
"submission_date": "string"
}

def filter_by_date(due_date, submissions):
    if not submissions:
        return []
    matching_submissions = [
        submission for submission in submissions if submission.get("submission_date") == due_date
    ]

    return matching_submissions

def filter_by_student_id(student_id, submissions):
    if not submissions:
        return []
    return [submission for submission in submissions if submission.get("student_id") == student_id]


def find_unsubmitted(due_date:str, student_names: list[str], submissions: list[dict]):
    if not student_names:
        return []
    filtered_submissions = filter_by_date(due_date, submissions)
    unsubmitted_students = student_names

    for submission in filtered_submissions:
        student_name = submission.get("student_name")
        if student_name in student_names:
            unsubmitted_students.remove(student_name)
    return unsubmitted_students

def get_average_score(submissions:list[dict]):
    total = 0
    for submission in submissions:
        total += submission.get("quiz_score")
    return total / len(submissions)