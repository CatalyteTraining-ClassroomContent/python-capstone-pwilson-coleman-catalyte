submissions = {
"quiz_name": "string",
"quiz_module": "string",
"quiz_score": int,
"student_id": int,
"student_name": "string",
"submission_date": "string"
}

submissions = [
    {
        "quiz_name": "Functions Quiz",
        "quiz_module": "Python Functions",
        "quiz_score": 85,
        "student_id": 1,
        "student_name": "Alice Johnson",
        "submission_date": "2025-09-20"
    },
    {
        "quiz_name": "Functions Quiz",
        "quiz_module": "Python Functions",
        "quiz_score": 92,
        "student_id": 2,
        "student_name": "Brian Davis",
        "submission_date": "2025-09-20"
    },
    {
        "quiz_name": "Functions Quiz",
        "quiz_module": "Python Functions",
        "quiz_score": 77,
        "student_id": 3,
        "student_name": "Catherine Green",
        "submission_date": "2025-09-21"
    },
    {
        "quiz_name": "Loops Quiz",
        "quiz_module": "Python Loops",
        "quiz_score": 88,
        "student_id": 1,
        "student_name": "Alice Johnson",
        "submission_date": "2025-09-21"
    },
    {
        "quiz_name": "Loops Quiz",
        "quiz_module": "Python Loops",
        "quiz_score": 79,
        "student_id": 2,
        "student_name": "Brian Davis",
        "submission_date": "2025-09-21"
    },
    {
        "quiz_name": "Loops Quiz",
        "quiz_module": "Python Loops",
        "quiz_score": 95,
        "student_id": 3,
        "student_name": "Catherine Green",
        "submission_date": "2025-09-22"
    },
    {
        "quiz_name": "Data Types Quiz",
        "quiz_module": "Python Basics",
        "quiz_score": 82,
        "student_id": 1,
        "student_name": "Alice Johnson",
        "submission_date": "2025-09-19"
    },
    {
        "quiz_name": "Data Types Quiz",
        "quiz_module": "Python Basics",
        "quiz_score": 74,
        "student_id": 2,
        "student_name": "Brian Davis",
        "submission_date": "2025-09-19"
    },
    {
        "quiz_name": "Data Types Quiz",
        "quiz_module": "Python Basics",
        "quiz_score": 90,
        "student_id": 3,
        "student_name": "Catherine Green",
        "submission_date": "2025-09-19"
    },
    {
        "quiz_name": "Variables Quiz",
        "quiz_module": "Python Basics",
        "quiz_score": 87,
        "student_id": 1,
        "student_name": "Alice Johnson",
        "submission_date": "2025-09-18"
    }
]




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

def get_average_score_by_module(submissions: list[dict]):
    if not submissions:
        return {}
    
    scores_by_module = {}
    for submission in submissions:
        quiz_module = submission.get("quiz_module") # Python Loops
        quiz_score = submission.get("quiz_score")

        if quiz_module in scores_by_module:
            scores_by_module[quiz_module].append(quiz_score)
        else:
            scores_by_module[quiz_module] = [quiz_score]
    total = 0
    for submission in scores_by_module:
        total += scores_by_module.get(quiz_score)
        return total / len(submissions)