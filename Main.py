# A Columbia College CS work-study quiz

import os, sys
from flask import Flask, request, session, redirect, url_for
sys.path.append("/home/cccsquiz/mysite/classes/")
from AItem import *
from AItemGen import *
from AItemList import *

app = Flask(__name__)


@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>A simple quiz website</title>
        </head>
            <body>
            Are you an instructor click <a href="/instructor">here</a>.
            <br>
            Are you a student click <a href="/inputquiz">here</a>.
        </body>
    </html>
    """

@app.route('/instructor')
def instructor():
    return """
    <html>
        <body>
            To create an AssessmentItem click <a href="/create_aitem">here</a>.
        </body>
    </html>
    """

@app.route('/create_aitem')
def create_aitem():
    return """
    <html>
        <body>
            <form action= 'create_params' method='post'>
                AItemGen Id <input type='text' name= 'aigen_id'>
                <br>
                <input type='submit'>
            </form>
        </body>
    </html>
    """

@app.route('/create_params', methods = ['POST'])
def create_params():
    aigen_id = request.form['aigen_id']
    f = open("/home/cccsquiz/mysite/models/AssessmentItemGenerator/%s.py" % aigen_id, "r")
    s = f.read()
    f.close()
    return """
    <html>
        <head>
        AItemGen Id: %s
        </head>
        <body>
            <br>
            <pre style='background-color: #D6EAF8;border:1px solid Black; padding:0.5em'>%s</pre>
            <br>
            parameters (example x=1, y=2)
            <br>
            <form action= 'create_dict' method='post'>
                <input type='text' name= 'params'>
                <br>
                Number of questions to generate (default is 1)
                <br>
                <input type='text' name= 'num_questions' value ='1'>
                <br>
                Points the question is worth (default is 1)
                <br>
                <input type='text' name='points' value='1'>
                <input type='hidden' name='aigen_id' value ='%s'>
                <br>
                <input type='submit'>
            </form>
        </body>
    </html>
    """ % (aigen_id, s, aigen_id)

@app.route('/create_dict', methods=['POST'])
def enter_params():
    aigen_id = request.form.get('aigen_id', None)
    params = request.form['params']
    num_questions = int(request.form['num_questions'])
    points = int(request.form['points'])
    # regex that gets rid of all spaces in p
    import re
    p = re.sub(r"\s+", "", params, flags=re.UNICODE)

    ai_ids = []
    for i in range(0, num_questions):
        items = p.split(',')
        varnames = []
        for x in items:
            varnames.append(x.split('=')[0])
        valuestrings = []
        for x in items:
            valuestrings.append(x.split('=')[1])
        strlist = ','.join(valuestrings)
        ###################
        # The next step allows us to use pyhon to get the correct representation for values.
        # For example lets say our values our parameters come in as:
        # "x=1, y=2, z=3.4, w=complex(1,1)"
        # When these get split into valuestring they look like:
        # "1, 2, 3.4, complex(1,1)"
        # We cannont use this yet because the values are strings and not actually what they represent;
        # by storing the values in a file, we can then import the values as they actually represent and
        # store them in a dictionary with their corresponding keys.
        ###################
        f = open ("tmp.py", "w")
        f.write("values= [%s]" %strlist)
        f.close()
        sys.path.append("/home/cccsquiz/")
        import importlib
        import tmp
        importlib.reload(tmp)
        tuples = zip(varnames, tmp.values)
        d = dict(tuples)
        os.system('rm tmp.py')

        ai_gen = AItemGen(aigen_id)
        ai_id = ai_gen.create(d)
        ai_ids.append(ai_id)

    f = open("/home/cccsquiz/mysite/models/AssessmentItemGenerator/%s.py" % aigen_id, "r")
    aigen_file = f.read(); f.close()
    f = open("/home/cccsquiz/mysite/models/AssessmentItem/%s.py" % ai_id, "r")
    ai_file = f.read(); f.close()

    quiz = AItem()
    quiz.restore(ai_id)
    question = quiz.get_question()

    return """
    <html>
        <body>
            AItemGen Id: %s
            <br>
            <pre style='background-color: #D6EAF8;border:1px solid Black; padding:0.5em'>%s</pre>
            <br>
            parameters entered: %s
            <br>
            <br>
            AItem Ids: %s
            <br>
            <pre style='background-color: #D6EAF8;border:1px solid Black; padding:0.5em'>%s</pre>
        </body>
    </html>
    """ % (aigen_id, aigen_file, params, ','.join(ai_ids), ai_file)


@app.route('/inputquiz')
def inputquiz():
    return """
    <html>
        <body>
        Welcome to the Quiz Website
        <br>
        Please type in the Assessment Item ID provided to you by your instructor.
        <br>
            <form action='takequiz', method='post'>
                AssessmentItemID: <input type='text' name='ai_id'>
                <input type='submit'>
            </form>
        </body>
    </html>
    """

@app.route('/takequiz', methods=['POST'])
def takequiz():
    ai_id = request.form['ai_id']
    if ai_id == '':
        return redirect("/inputquiz")
    else:
        ai_id = ai_id.replace(' ', '')
        q1 = AItem()
        q1.restore(ai_id)
        student_answer = q1.get_student_answer()
        if student_answer == None:
            question = q1.get_question()
            return """
            <html>
                <body>
                    AssessmentItemId: %s
                    <form action='grade_quiz', method='post'>
                        %s
                        <input type='hidden' name='ai_id' value='%s'>
                        <input type='submit'>
                    </form>
                </body>
            </html>
            """ % (ai_id, question, ai_id)
        else:
            return """
            <html>
                <body>
                    You have already taken Assessment Item: %s
                    <br>
                    Click <a href="/inputquiz">here</a> to input another Assessment Item.
                </body>
            </html>
            """ %(ai_id)

@app.route('/grade_quiz', methods=['POST'])
def grade_quiz():
    ai_id = request.form['ai_id']
    student_answer = request.form['student_answer']

    current_question = AItem()
    current_question.restore(ai_id)
    current_question.set_score(student_answer)

    question = current_question.get_readable_question()
    score = current_question.get_score()
    answer = current_question.get_answer()

    current_question.save()

    return '''
    <html>
        <body>
            AssessmentItem: %s
            <br>
            <br>
            The Question was: %s
            <br>
            %s.
            <br>
            You answered: %s
            <br>
            Your score is: %s
            <br>
        </body>
    </html>
    ''' %(ai_id, question, answer, student_answer, score)
