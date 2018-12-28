x = %(x)s
y = %(y)s
z = %(z)s
correct_input = x + y - z

data = {"x" : x,
        "y" : y,
        "z" : z,
        "correct_input" : correct_input,
        "student_answer" : None,
        "score": None,
        "feedback" : None}

question = "What is %(x)s + %(y)s - %(z)s? <input type='text' name='student_answer'>"

answer = "The correct answer is " + str(data["correct_input"])

def grading_func(data):
    if int(data["student_answer"]) == data["correct_input"]:
        return 3.0
    else:
        return -3.0
