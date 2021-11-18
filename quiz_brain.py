class QuizBrain:
    def __init__(self, quiz_list):
        self.question_no = 0
        self.question_list = quiz_list
        self.answer = ""
        self.score = 0

    def still_has_question(self):
        if self.question_no <= 11:
            return True
        else:
            return False

    def next_question(self):
        user_answer = input(f"{self.question_no + 1} {self.question_list[self.question_no].question}")
        self.check_answer(user_answer, self.question_list[self.question_no].answer)
        self.question_no += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got the right answer")
            self.score += 1
        else:
            print("You didn't get it")
        print(f"Correct answer is {correct_answer}")
        print(f"Your score is {self.score}")
