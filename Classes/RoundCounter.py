class RoundCounter:
    def init(self, currentRound):
        self.currentRound = currentRound

    def getNextRound(self):
        self.currentRound += 1
        return self.currentRound

    def setRound(self, round):
        self.currentRound = round