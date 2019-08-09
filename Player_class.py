class Player:
    def __init__(self):
        self.health = 100

    def getHealth(self):
        return self.health

    def damageHealth(self, damage):
        self.health -= damage

    def restoreHealth(self, heal):
        self.health -= heal
