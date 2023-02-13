
class Main:
    def __init__(self):
        self.user = "user"
        self.comp = "my_comp"
        self.BASHsymb = "$"
        self.pre_cmdl = str(self.user) + "@" + str(self.comp) + str(self.BASHsymb)
        self.cmd = self.terminal_start()

    def terminal_start(self):
        cmd = input(str(self.pre_cmdl))
        return cmd

