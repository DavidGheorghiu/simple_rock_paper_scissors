class Player:
    #TODO: fix id
    id = 0
    def __init__(self):
        self.id = Player.id
        Player.id += 1
        self.health = 100

    def getId(self):
        return self.id

    def getHealth(self):
        return self.health

    def getChoice(self):
        return self.choice

    #player's choice (r, p, s)
    #TODO: make sure the user does r,p, or s
    def setChoice(self, choice):
        self.choice = choice

    def damageHealth(self, damage):
        self.health -= damage
