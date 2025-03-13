def player(prev_play, opponent_history=[]):
    # If it's the first round, play Rock ('R')
    if prev_play == '':
        return 'R'
    
    # Counter strategy based on the opponent's last move
    if prev_play == 'R':
        return 'P'  # Paper beats Rock
    elif prev_play == 'P':
        return 'S'  # Scissors beats Paper
    elif prev_play == 'S':
        return 'R'  # Rock beats Scissors
