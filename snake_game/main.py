from snake import SnakeGame

play = 'yes'
while play == 'yes':
    game = SnakeGame()
    play = game.play_again()
