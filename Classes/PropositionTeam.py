# Proposition team: has name and description; has its pool of options which is refreshed at each cycle; acts by choosing one option per cycle.
class PropositionTeam:
    def __init__(self,name, PropOptionBank, description = None, objectives = None):
        self.name = name
        self.PropOptionBank = PropOptionBank
        self.description = description
        self.objectives = objectives


    def get_description(self):
        return self.description
    
    def choose_option(self):
        options = self.PropOptionBank.get_options()
        print(f'{self.name}, your options are:  {options}')
        print(f'{self.name}, choose your option')
        selected_option = input('Enter the option number: ')
      

        while True:

            try:
                selected_index = int(selected_option)
                if 1 <= selected_index <= len(options):
                    print(f"{self.name}, your choise is option {selected_index}")
                    return selected_index
                else:
                    print("Invalid option. Chose one of the available options")

            except ValueError:
                print("Invalid option. Chose one of the available options")
            
            

        
            
        