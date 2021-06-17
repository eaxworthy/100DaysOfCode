from quiz import QuizGame
#from data import question_data
import json
from urllib.request import urlopen

url = 'https://opentdb.com/api.php?amount=15&difficulty=easy&type=boolean&encode=url3986'
response = urlopen(url)
question_data = json.loads(response.read())['results']

quiz_game = QuizGame(question_data)
questions_left = True

while questions_left:
    questions_left = quiz_game.next_question()

quiz_game.end_message()
