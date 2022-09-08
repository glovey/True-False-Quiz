class QuizBrain:
  def __init__(self, questions):
    self.question_number = 0
    self.questions = questions
    self.score = 0

  def check_answer(self, user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
        print ("Correct!")
        self.score+=1
    
    else:
          print ("Wrong! Are you dumb?")
          
    print (f"The correct answer was {correct_answer}")
    print (f"Your score is {self.score}/{self.question_number}")
    print("\n")     
  
  def next_question(self):
    current_q = self.questions[self.question_number]
    self.question_number += 1

    user_answer = input (f"Q{self.question_number}. {current_q.text} (True / False) ?")
    self.check_answer(user_answer,current_q.answer)

  def hello():
    print ("hello")



  def still_questions(self):
    return self.question_number < len(self.questions)


 
      

