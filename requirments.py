{
"quizName": "string",
"quizModule": "string",
"quizScore": int,
"studentId": int,
"studentName": "string",
"submissionDate": "string"
}

def filter_by_date(due_date, list_of_submissions):
    if not list_of_submissions:
        return []