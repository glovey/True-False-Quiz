class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.questions = questions

    def next_question(self):
        current_q = self.questions[self.question_number]
        self.question_number += 1

        answer = input (f"Q{self.question_number}. {current_q.text} (True / False) ?")

        if answer == current_q.answer:
            print ("Correct! Next question..")
            return True
        else:
            print ("Wrong! Are you dumb?")
            return False