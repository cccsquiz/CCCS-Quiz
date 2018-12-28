from DefaultGradingFunc import *
import sys, os

class AItem:
    def __init__(self, question=None, answer=None, aitem_id=None,
    grading_func=None, data=None, readable_question=None, aigen_id=None):
        self.question = question
        self.answer = answer
        self.aitem_id = aitem_id
        self.data = data
        self.readable_question = readable_question
        self.aigen_id = aigen_id
        if grading_func == None:
            self.grading_func = default_grading_func
        else:
            self.grading_func = grading_func

    def save(self):
        f = open('/home/cccsquiz/mysite/models/AssessmentItemGenerator/tmp.py', 'w'); f.write('from %s import *' % self.aigen_id); f.close()
        sys.path.append("/home/cccsquiz/mysite/models/AssessmentItemGenerator/")
        from tmp import grading_func
        self.grading_func = grading_func
        f = open("/home/cccsquiz/mysite/models/AssessmentItem/%s.py" % str(self.aitem_id).zfill(2), "w")
        f.write("question = \"%s\"\n" %self.question)
        f.write("answer = \"%s\"\n" %self.answer)
        f.write("grading_func = %s\n" %self.grading_func)
        f.write("data = %s\n" %self.data)
        f.write("readable_question = %s\n" %self.readable_question)
        f.write("aigen_id = %s\n" %self.aigen_id)

        f.close()

    def restore(self, aitem_id):
        if str(aitem_id).isalnum():
            self.aitem_id = aitem_id
            f = open('/home/cccsquiz/mysite/models/AssessmentItem/tmp1.py', 'w'); f.write('from %s import *' % self.aitem_id); f.close()
            sys.path.append("/home/cccsquiz/mysite/models/AssessmentItem/")
            from tmp1 import question, answer, data, readable_question, grading_func, aigen_id
            self.question = str(question)
            self.readable_question = str(readable_question)
            self.answer = str(answer)
            self.data = data
            self.aigen_id = aigen_id
            self.grading_func = grading_func
            os.system('rm /home/cccsquiz/mysite/models/AssessmentItem/tmp1.py')

    def set_score(self, student_answer):
        self.data["student_answer"] = student_answer
        self.data["score"] = self.grading_func(self.data)

    def get_id(self):
        return self.aitem_id

    def get_question(self):
        return self.question

    def get_readable_question(self):
        return self.readable_question

    def get_answer(self):
        return self.answer

    def get_student_answer(self):
        return data["student_answer"]

    def get_score(self):
        return self.data["score"]

    def get_correct_input(self):
        return self.data["correct_input"]

    def get_student_answer(self):
        return self. data["student_answer"]
