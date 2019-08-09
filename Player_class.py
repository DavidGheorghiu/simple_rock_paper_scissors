class Player:
    #TODO: fix id
    id = 0
    def __init__(self):
        self.id = id
        id += 1
        self.health = 100

    def getId(self):
        return self.id

    def getHealth(self):
        return self.health

    def damageHealth(self, damage):
        self.health -= damage

    #future use (idea)
    def restoreHealth(self, heal):
        self.health -= heal
    
    #player's choice (r, p, s)
    #TODO: make sure the user does r,p, or s
    def setChoice(choice):
        self.choice = choice
