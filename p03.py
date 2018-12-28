code_segment = %(x)s
output = %(y)s
correct_input = %(z)s

data = {"code_segment" : code_segment,
        "output" : output,
        "correct_input" : correct_input,
        "student_answer" : None,
        "score": None,
        "feedback" : None}

question = """Read this program carefully: \n %(code_segment)s \n\n
Is the following output correct? \n %(output)s \n\n
<input type="radio" name="student_answer" value="True">True<br>
<input type="radio" name="student_answer" value="False">False<br>
<input type="submit">"""

answer = "The correct answer is " + str(data["correct_input"])

def grading_func(data):
    if int(data["student_answer"]) == data["correct_input"]:
        return 1000000.0
    else:
        return -1000000.0
