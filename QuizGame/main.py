from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#creating the question bank
question_bank = []
for q in question_data:
    question_text = q["text"]
    question_answer = q["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print(f"You have completed all the questions!! "
      f"\nYour final score is: {quiz.score}/{quiz.question_number}")



