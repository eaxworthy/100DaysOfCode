from snake import SnakeGame

play = 'y'
while play == 'y':
    game = SnakeGame()
    play = game.play_again()
