class OppositionTeam:
    def __init__(self,name, OppOptionsBank, description = None, objectives = None):
        self.name = name
        self.OppOptionsBank = OppOptionsBank
        self.description = description
        self.objectives = objectives

    def get_description(self):
        return self.description
 
    def choose_option(self):
        options = self.OppOptionsBank.get_options()
        print(f'{self.name}, your options are:  {options}')
        print(f'{self.name}, choose your option')

        while True:
            selected_option = input('Enter the option number: ')

            try:
                selected_index = int(selected_option)
                if 1 <= selected_index <= len(options):
                    print(f"{self.name}, your choise is option {selected_index}")
                    return selected_index
                else:
                    print("Invalid option. Chose one of the available options")

            except ValueError:
                print("Invalid option. Chose one of the available options")
            