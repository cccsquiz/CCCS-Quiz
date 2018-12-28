x = %(x)s
y = %(y)s
correct_input = x // y

data = {"x" : x,
        "y" : y,
        "correct_input" : correct_input,
        "student_answer" : None,
        "score": None,
        "feedback" : None}

question = "What is %(x)s / %(y)s in C++? <input type='text' name='student_answer'>"
readable_question = "What is %(x)s / %(y)s in C++?"

answer = "The correct answer is " + str(data["correct_input"])

def grading_func(data):
    if int(data["student_answer"]) == data["correct_input"]:
        return 1.0
    else:
        return 0.0
