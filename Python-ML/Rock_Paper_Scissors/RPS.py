# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], pattern={}):
    
    guess = "R"
    op_length = 4
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    if prev_play != '':
        opponent_history.append(prev_play)
        
    

    
    if len(opponent_history) > op_length + 1:
        opponent_history.pop(0)
        moves = ''.join(opponent_history[-op_length:])
        potential_plays = [
            moves + "R",
            moves + "P",
            moves + "S",
        ]
    
        if ''.join(opponent_history[-(op_length+1):]) in pattern.keys():
            pattern[''.join(opponent_history[-(op_length+1):])] += 1
        else:
            pattern[''.join(opponent_history[-(op_length+1):])] = 1

        for i in potential_plays:
            if not i in pattern.keys():
                pattern[i] = 0

        
        
        
        prediction = max(potential_plays, key=lambda key:pattern[key])
        # print(prediction)
        
        
        guess = ideal_response[prediction[-1]]
        return guess
    return guess   
