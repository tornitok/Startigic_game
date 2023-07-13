class OppositionTeam:
    def init(self, name, description=None, objectives=None):
        self.name = name
        self.description = description
        self.objectives = objectives

    def get_options(self, OppBankOfOptions): # i need to fix this one
        return self.options
    
    def choose_option(self, OppOptions): #PropOptions will be an instance of OptionsBank which is passed to the Proposition Team class method of chosing option
        print(OppOptions)
        print('Team {self.name}, choose your option')
        selected_option = input('Enter the option number: ')
        selected_index = OppOptions[int(selected_option)-1]  #selected_index is the selection of an option by Proposition team

        if selected_option != 0 or selected_option <= len(self.options):
            print('Team {self.name} chose option {selected_option}')
        else:
            print("Invalid option. Chose one of the available options") # needs redirection
            return None

 
