class Submission:

    def __init__(self, quizName, quizModule, quizScore, studentId, studentName, submissionDate):
        self.quizName = quizName
        self.quizModule = quizModule
        self.quizScore = quizScore
        self.studentId = studentId
        self.studentName = studentName
        self.submissionDate = submissionDate

def filter_by_date(due_date, list_of_submissions):
    if not list_of_submissions:
        return []
    matching_submissions = [
        submission for submission in list_of_submissions if submission.get("submissionDate") == due_date
    ]

    return matching_submissions

def filter_by_student_id(studentId, list_of_submissions):
    if not list_of_submissions:
        return []
    return [ submission for submission in list_of_submissions if submission.get("studentId") == studentId]

def find_unsubmitted(due_date, student_names, list_of_submissions):
    if not student_names:
        return []
    submitted_today = {submission.get("studentName") for submission in(list_of_submissions or []) if submission.get("submissionDate") == due_date}

    return [name for name in student_names if name not in submitted_today]