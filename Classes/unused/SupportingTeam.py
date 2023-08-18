class SupportingTeam:
    def init(self, name, options, description):
        self.name = name
        self.options = options
        self.description = description

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def set_options(self, options):
        self.options = options

    def get_options(self):
        return self.options
