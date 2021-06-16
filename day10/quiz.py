from data import question_data
class QuizQuestion:
    def __init__(self, text='Default Text', answer='Default Answer'):
        self.text = text
        self.answer = answer

    def __str__(self):
        '''Provides a formatted printing for QuizQuestions'''
        return 'Question(Text: ' + self.text + ' Answer: ' + self.answer +')' 

class QuizGame:
    def __init__(self, data):
        self.score = 0
        self.question_number = 0
        self.question_bank = []
        for question in data:
            self.question_bank.append(QuizQuestion(question['text'], question['answer']))

    def print_questions(self):
        '''Prints all QuizQuestions in the question_bank'''
        for question in self.question_bank:
            print(question)

    def next_question(self):
        '''loads next question in list, prompts user for answer'''
        question = self.question_bank[self.question_number]
        self.question_number += 1
        user_guess = input(f'Q.{self.question_number}. {question.text} (True/False)?: ').lower()
        if user_guess == question.answer.lower():
            print("That's correct!")
            self.score+=1
        else:
            print("Sorry, that was incorrect.")
        print(f"Your current score is {self.score}/{self.question_number}\n")    
        
        if self.question_number >= len(self.question_bank):
                return False
        return True

    def end_message(self):
        if self.score == len(self.question_bank):
            print(f"Congratulations, you got all {self.score} questions right!")
        else:
            print(f"Game Over. Your final score was {self.score}.")
