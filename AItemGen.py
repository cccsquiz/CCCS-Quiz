from CreateId import *

class AItemGen:
    def __init__(self, aigen_id):
        if str(aigen_id).isalnum():
            self.aigen_id = aigen_id

    def create(self, data_dict):
        f = open("/home/cccsquiz/mysite/models/AssessmentItemGenerator/%s.py" % self.aigen_id, "r")
        s = f.read();f.close()
        s = s %data_dict
        aitem_id = create_id()
        f = open("/home/cccsquiz/mysite/models/AssessmentItem/%s.py" % aitem_id, "w")
        f.write(s)
        f.write("aigen_id = \"%s\"\n" %self.aigen_id)
        f.close()
        return aitem_id

    def get_question(self):
        return self.question

    def get_answer(self):
        return self.answer
