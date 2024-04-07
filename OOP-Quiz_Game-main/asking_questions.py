class QuizBrain():

    def __init__(self, question_list):
        self.user_score = 0
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.question} (True/False): ").lower()
        self.check_answer(user_answer, current_question.question_answer)


    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got the question right!")
            self.user_score += 1
        else:
            print("You got it wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"You current score is {self.user_score} / {self.question_number}")



