def get_coursework_score(test_one, test_two, test_three):
    total_score = test_one + test_two + test_three
    return total_score


def get_exam_score_70(exam_score_100):
    return (exam_score_100 / 100) * 70

def get_final_score(test_scores, exam_score_100):
    course_work_score = get_coursework_score(*test_scores)
    exam_score_70 = get_exam_score_70(exam_score_100)
    return course_work_score + exam_score_70

def get_grade(score):
    raise NotImplementedError(f"Implement {get_grade} function")


final_score = get_final_score([10, 8, 9], 90)

print(final_score)
