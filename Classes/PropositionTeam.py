# Proposition team: has name and description; has its pool of options which is refreshed at each cycle; acts by choosing one option per cycle.

class PropositionTeam:
    def __init__(self,PropOptionBank, description = None, objectives = None):
        self.PropOptionBank = PropOptionBank
        self.description = description
        self.objectives = objectives


    def get_description(self):
        return self.description


    def get_options(self, PropOptionBank): #This seems to be redundant, as we can get options through PropTeamInstance.PropOptionBank.get_options()
        print(self.options)
        return self.options
    
    def choose_option(self, PropOptions): #PropOptions will be an instance of OptionsBank which is passed to the Proposition Team class method of chosing option
        print(PropOptionBank)
        print('Team {self.name}, choose your option')
        selected_option = input('Enter the option number: ')
        selected_index = PropOptions[int(selected_option)-1]  #selected_index is the selection of an option by Proposition team

        if selected_option != 0 or selected_option <= len(self.options):
            print('Team {self.name} chose option {selected_option}')
        else:
            print("Invalid option. Chose one of the available options") # needs redirection
            return None
        

