class Terminal:
    def __init__(self):
        self.commands = ["ls", "pwd", "cd"]
        self.number_commands = 3
        self.user = "user"
        self.comp = "my_comp"
        self.BASHsymb = "$"
        self.pre_cmdl = self.user + "@" + self.comp + self.BASHsymb
        self.cmd = input(self.pre_cmdl)
        self.process_command()

    def process_command(self):
        index = 0
        while index < self.number_commands:
            if str(self.cmd) == self.commands[index]:
                print(str(self.cmd))
                self.cmd = input(self.pre_cmdl)
                self.process_command()

            index = index + 1
        else:
            print(str(self.cmd) + " is not a valid command.")
            self.cmd = input(self.pre_cmdl)
            self.process_command()
