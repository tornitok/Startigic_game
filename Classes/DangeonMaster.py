import PropositionTeam
import EventBank
import OppositionTeam
import RoundCounter
import OptionsBank

class DangeonMaster:
    def __init__(self):
        self.proposition_team = PropositionTeam
        self.opposition_team = OppositionTeam
        self.event_bank = EventBank
        self.round_counter = RoundCounter
        self.options_bank = OptionsBank


    def add_event(self, event):
         self.event_bank.append(event)

    def add_team(self,team_op,team_prop):
        self.proposition_team.append(team_op)
        self.opposition_team.append(team_prop)

        return f'В игру добавлены {team_op} и {team_prop}'

    def round_counter(self):
        print(f"Начинается {self.round_counter} раунд")
        self.round_counter += 1

    def