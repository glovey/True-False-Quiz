from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_bank.append(Question(item["text"],item["answer"]))

brain = QuizBrain(question_bank)



while brain.still_questions():
    brain.next_question()
    
                      
print (f"That's the end of the quiz. Your score was {brain.score} / {brain.question_number}")




