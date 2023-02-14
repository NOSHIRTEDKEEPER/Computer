from classes.File_system import TreeNode

class Terminal:
    def __init__(self):
        self.commands = ["ls", "pwd", "cd"]
        self.number_commands = 3
        self.user = "user"
        self.comp = "my_comp"
        self.BASHsymb = "$"
        self.pre_cmdl = self.user + "@" + self.comp + self.BASHsymb
        self.cmd = input(self.pre_cmdl)
        self.check_command()

    def check_command(self):
        index = 0
        while index < self.number_commands:
            if str(self.cmd) == self.commands[index]:
                self.process_command()
                self.cmd = input(self.pre_cmdl)
                self.check_command()

            index = index + 1
        else:
            print(str(self.cmd) + " is not a valid command.")
            self.cmd = input(self.pre_cmdl)
            self.check_command()

    def process_command(self):
        print(str(self.cmd))
        TreeNode.