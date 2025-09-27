import pytest
from requirements import (
    filter_by_date,
    filter_by_student_id,
    find_unsubmitted,
    get_average_score,
    get_average_score_by_module,
)


@pytest.fixture
def submission_data():
    return [
        {
            "quiz_name": "Functions Quiz",
            "quiz_module": "Python Functions",
            "quiz_score": 92,
            "student_id": 2,
            "student_name": "Brian Davis",
            "submission_date": "2025-09-20",
        },
        {
            "quiz_name": "Functions Quiz",
            "quiz_module": "Python Functions",
            "quiz_score": 77,
            "student_id": 3,
            "student_name": "Catherine Green",
            "submission_date": "2025-09-21",
        },
        {
            "quiz_name": "Loops Quiz",
            "quiz_module": "Python Loops",
            "quiz_score": 88,
            "student_id": 1,
            "student_name": "Alice Johnson",
            "submission_date": "2025-09-21",
        },
        {
            "quiz_name": "Loops Quiz",
            "quiz_module": "Python Loops",
            "quiz_score": 79,
            "student_id": 2,
            "student_name": "Brian Davis",
            "submission_date": "2025-09-21",
        },
        {
            "quiz_name": "Loops Quiz",
            "quiz_module": "Python Loops",
            "quiz_score": 95,
            "student_id": 3,
            "student_name": "Catherine Green",
            "submission_date": "2025-09-22",
        },
        {
            "quiz_name": "Data Types Quiz",
            "quiz_module": "Python Basics",
            "quiz_score": 82,
            "student_id": 1,
            "student_name": "Alice Johnson",
            "submission_date": "2025-09-19",
        },
        {
            "quiz_name": "Data Types Quiz",
            "quiz_module": "Python Basics",
            "quiz_score": 74,
            "student_id": 2,
            "student_name": "Brian Davis",
            "submission_date": "2025-09-19",
        },
        {
            "quiz_name": "Data Types Quiz",
            "quiz_module": "Python Basics",
            "quiz_score": 90,
            "student_id": 3,
            "student_name": "Catherine Green",
            "submission_date": "2025-09-19",
        },
        {
            "quiz_name": "Variables Quiz",
            "quiz_module": "Python Basics",
            "quiz_score": 87,
            "student_id": 1,
            "student_name": "Alice Johnson",
            "submission_date": "2025-09-18",
        },
    ]


def test_filter_date_function_as_expected(submission_data):
    expected = [
        {
            "quiz_name": "Variables Quiz",
            "quiz_module": "Python Basics",
            "quiz_score": 87,
            "student_id": 1,
            "student_name": "Alice Johnson",
            "submission_date": "2025-09-18",
        }
    ]
    assert filter_by_date("2025-09-18", submission_data) == expected


def test_filter_date_empty_submissions_returns_empty_lists():
    assert filter_by_date("2025-09-18", []) == []


def test_filter_stduent_id_as_expected(submission_data):
    expected = [
        {
            "quiz_name": "Loops Quiz",
            "quiz_module": "Python Loops",
            "quiz_score": 88,
            "student_id": 1,
            "student_name": "Alice Johnson",
            "submission_date": "2025-09-21",
        },
        {
            "quiz_name": "Data Types Quiz",
            "quiz_module": "Python Basics",
            "quiz_score": 82,
            "student_id": 1,
            "student_name": "Alice Johnson",
            "submission_date": "2025-09-19",
        },
        {
            "quiz_name": "Variables Quiz",
            "quiz_module": "Python Basics",
            "quiz_score": 87,
            "student_id": 1,
            "student_name": "Alice Johnson",
            "submission_date": "2025-09-18",
        },
    ]
    assert filter_by_student_id(1, submission_data) == expected

def test_filter_student_id_empty_submission_empty_list():
    assert filter_by_student_id(2, []) == []

def test_find_unsubmitted_quizzes_as_expeceted(submission_data):
    expected = ["Paige Coleman", "Rachel Coleman"]
    assert find_unsubmitted("2025-09-21", ["Paige Coleman", "Rachel Coleman", "Alice Johnson"], submission_data) == expected

def test_find_unsubmitted_empty_student_names_empty_list(submission_data):
    assert find_unsubmitted("2025-08-09", [], submission_data) == []

def test_unsubmitted_empty_submissions_empty_list():
    assert find_unsubmitted("2025-09-17", ["Alice Johnson"], []) == []

def test_find_unsubmitted_all_submitted_returns_empty(submission_data):
    everyone = ["Alice Johnson", "Brian Davis", "Catherine Green"]
    assert find_unsubmitted("2025-09-19", everyone, submission_data) == []

def test_average_score_single_submission(submission_data):
    single = [submission_data[-1]]
    assert get_average_score(single) == 87

def test_get_average_score_by_module_empty_returns_empty_dict():
    assert get_average_score_by_module([]) == {}