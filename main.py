from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_object = []
for question in question_data:
    new_question = question["text"]
    new_answer = question["answer"]
    new_object = Question(new_question,new_answer)
    question_object.append(new_object)
quiz = QuizBrain(question_object)
while quiz.still_has_question():
    quiz.next_question()

print("\nYou just completed the quiz")
print(f"You get {quiz.score}/{len(question_object)}")