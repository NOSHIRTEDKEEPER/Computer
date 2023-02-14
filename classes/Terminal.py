class Terminal:
    def __init__(self):
        self.user = "user"
        self.comp = "my_comp"
        self.BASHsymb = "$"
        self.pre_cmdl = self.user + "@" + self.comp + self.BASHsymb
        self.cmd = input(self.pre_cmdl)
        self.process_command()
    def process_command(self):
        print(str(self.cmd))
