
#OptionsBank: is a storage of all the options for each team in the game. Each option will have a unique set of counter-options. 

class  BankOfOptions:

    def __init__(self, options = None):
        self.options = options or []

    def get_options(self):
        print("Options are", self.options)
        return self.options
    
    def add_option(self, option):
        self.options.append(option)

    def remove_option(self, option):
        self.options.remove(option)

