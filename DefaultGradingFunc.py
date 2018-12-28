def default_grading_func(data):
    if int(data["student_answer"]) == data["correct_input"]:
        return 1.0
    else:
        return 0.0
