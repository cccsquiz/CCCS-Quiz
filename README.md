# CCCS-Quiz

General comment: All objects must have an id that uniquely identifies the object in the system (or at least within its class). The id must be randomly generated, with a fixed length of 32, using characters in 0-9A-Za-z. 

# AssessmentItemGenerator (shorthand AItemGen)
- Comment: An AItemGen poduces AItem objects. This allows AItem objects to be created quickly. For instance an AItemGen object represents the question “What is x + y?” and answer x + y. This object can produce the AItem object that has the question “What is 1 + 2” with answer 3.

# AssessmentItem (shorthand AItem)
- Comment: This is the base class of all assessment item classes. The following are classes for assessment items. An assessment item represents a single student assessment such as a question in a quiz or an assignment.
- Fields:
id: string, question: HTML string, student_answer: string. Submitted by the string. (WARNING: Handle the case where there are multiple text boxes, answer, score: float in [0.0, 1.0], feedback: HTML string. Explanation of answer. This also allows instructor to manually add comments which are not auto-generated.
- TODO: Need start time, end time (if assessment item has time range), time when student submits, etc.
- Methods:  grade: computes the score and possibly the feedback

# AssessmentItemList (shorthand AItemList)
- A list of specific AItems i.e. the quiz itself. Has a unique ID that must be entered in order for a student to access the questions/AItems and submit their answers. 

