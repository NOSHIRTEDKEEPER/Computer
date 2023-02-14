class Terminal:
    def __init__(self):
        self.user = "user"
        self.comp = "my_comp"
        self.BASHsymb = "$"
        self.pre_cmdl = self.user + "@" + self.comp + self.BASHsymb
        cmd = input(self.pre_cmdl)
        self.process_command(cmd)
    def process_command(cmd,self):
        print(str(cmd))
