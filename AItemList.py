import os, sys

class AItemList:
    def __init__(self, ailist_id):
        if str(ailist_id).isalnum():
            self.ailist_id = ailist_id
            f = open('/home/cccsquiz/mysite/models/AssessmentItemList/tmp.py', 'w');
            f.write('from %s import ai_ids' % ailist_id);
            f.close()
            sys.path.append("/home/cccsquiz/mysite/models/AssessmentItemList/")
            from tmp import ai_ids
            self.ai_ids = ai_ids
            #os.system('rm /home/cccsquiz/mysite/models/AssessmentItemList/tmp.py')

    def get_ai_ids(self):
        return self.ai_ids
