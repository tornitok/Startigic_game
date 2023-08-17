from Classes import PropositionTeam
from Classes import OptionsBank
from Classes import OppositionTeam


PropOptionBank = OptionsBank.OptionsBank()
PropOptionBank.add_option("Option 1: Turn the drills into a blockade of the island and its airspace. (4US,6China)")
PropOptionBank.add_option("Option 2: Take no direct military action but start sanctions demand explanation and an international committee. (5,5)")
PropOptionBank.add_option("Option 3: Respond by a swift missile attach on Taiwanese military bases. (3,7)")
PropOptionBank.add_option("Option 4: Go Eat Some Horse Meat! (5,5)")


ChinaTeam = PropositionTeam.PropositionTeam(name = 'ChinaTeam', PropOptionBank = PropOptionBank) 

ChinaTeam.choose_option()


OppOptionsBank = OptionsBank.OptionsBank()
OppOptionsBank.add_option("Option 1: Break the blocade with force. 60% success (6,3) or 0.")
OppOptionsBank.add_option("Option 2: Send in the military but do not try to brake the blockade. (5,5) 60% another incident.")

UsaTeam = OppositionTeam.OppositionTeam(name='UsaTeam', OppOptionsBank = OppOptionsBank)
# UsaTeam.choose_option()