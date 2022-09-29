import copy
import random 

class Hat():
    def __init__(self, **hat):
        self.dict = {}
        for a,b in hat.items():
            self.dict[a] = b 
        self.contents = []
        for key,value in self.dict.items():
            for i in range(value):
                self.contents.append(key)
        
    
    def draw(self, draw):
        self.ball_drawn = []
        if draw >= len(self.contents):
            self.ball_drawn = self.contents
            return self.ball_drawn
        else:
            for i in range(draw):
                x = random.choice(self.contents)
                self.ball_drawn.append(x)
                self.contents.remove(x)
            return self.ball_drawn

def experiment(hat,
            expected_balls,
            num_balls_drawn,
            num_experiments):
    
    count = 0    


    for x in range(num_experiments):
        sample = copy.deepcopy(hat)
        sample_balls = sample.draw(num_balls_drawn)
        match = []
        for key,value in expected_balls.items():
            for e in range(value):
                match.append(key)
        for i in sample_balls:
            if i in match:
                match.remove(i)
        if len(match) == 0:
            count +=1
    return count / num_experiments
    

 