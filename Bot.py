import random
class Bot:
    def __init__(self,color = 'black',active = True) :
        self.color = color
        self.active = True
    
    def get_bot_moves(self,possible_moves):
        return possible_moves[random.randrange(len(possible_moves))]


