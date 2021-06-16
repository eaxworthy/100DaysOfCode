from quiz import QuizGame
from data import question_data

quiz_game = QuizGame(question_data)

questions_left = True

while questions_left:
    questions_left = quiz_game.next_question()

quiz_game.end_message()
