
class BankOfOptions:
    def init(self, options):
        self.options = options

    def set_options(self, options):
        self.options = options

    def get_options(self):
        return self.options

    def __str__(self):
        sb = []
        sb.append("Bank of Options:\n")
        for option in self.options:
            sb.append(option + "\n")
        return ''.join(sb)
