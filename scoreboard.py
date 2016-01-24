from render import set_game_info

class Scoreboard():

    def __init__(self,surface):
        self.surface = surface
        self.level = 1
        self.score = 0
        self.lines = 0

    def level_up(self):
        self.level += 1
        set_game_info(surface,level_val=self.level)

    def score_up(self,value):
        self.score += value
        set_game_info(surface,score_val=self.score)

    def lines_up(self,value):
        self.lines+= value
        set_game_info(self.surface,lines_val=self.lines)
