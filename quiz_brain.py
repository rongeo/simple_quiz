#class to act as the brain of the quiz
class QuizBrain:
    def __init__(self,question_bank):
        self.question_number = 0
        self.question_list=question_bank
        self.score=0

    def still_has_questions(self):
        if self.question_number>=len(self.question_list):
            return False
        else:
            return True
        # or we can write..... return self.question_number<len(self.question_list)
    def check_Score(self,user_ans,correct_answer):
        if correct_answer.lower()==user_ans.lower():
            self.score += 1
            print(f"You got it correct")
        else:
            print(f"You got it wrong")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is {self.score}/ {self.question_number}\n")

    def next_question(self):
        ques=self.question_list[self.question_number]
        self.question_number+=1
        user_ans=input(f"Q No {self.question_number}: {ques.text} (True\False)\n")
        self.check_Score(user_ans,ques.answer)



