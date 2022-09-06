from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_bank.append(Question(item["text"],item["answer"]))

brain = QuizBrain(question_bank)

play = True

while play:
    play = brain.next_question()

print (f"\nGAME OVER! you made it to question {brain.question_number}, are you happy with yourself?")


