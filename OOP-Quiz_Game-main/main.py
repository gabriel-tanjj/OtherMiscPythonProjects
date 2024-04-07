from question_structure import Question
from data import question_data
from asking_questions import QuizBrain

question_bank = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(text=text, answer=answer)
    question_bank.append(new_question)

# We initlized the question class above and stored 2 attributes - text and answer inside it
# the quiz variable below is an object made from the QuizBrain function inside the asking_questions class
# and the question is an object made from the Question function in the question_structure class
# so the quiz variable/object will have access to the attributes in the question_structure class

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

while not quiz.still_has_question():
    print("You've completed the quiz!")
    print(f"Your final score is {quiz.user_score} / {quiz.question_number}")
    break