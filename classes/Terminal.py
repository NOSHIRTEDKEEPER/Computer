from classes.File_system import *

class Terminal:
    def __init__(self):
        self.folder = root
        self.commands = ["ls", "pwd", "cd", "sudo su", "exit", "clear"]
        self.user = "user"
        self.comp = "my_comp"
        self.BASHsymb = "$"
        self.pre_cmdl = self.user + "@" + self.comp + self.BASHsymb
        self.cmd = input(self.pre_cmdl)

        self.check_command()

    def check_command(self):
        index = 0
        while index < len(self.commands):
            if self.commands[index] in str(self.cmd):
                self.process_command()

            index = index + 1


        if self.cmd == "":
            self.cmd = input(self.pre_cmdl)
            self.check_command()

################ below statement ###################################

        elif self.cmd != "clear" or "cd":
            print(str(self.cmd) + " is not a valid command.")
            self.cmd = input(self.pre_cmdl)
            self.check_command()

################# end problem #########################

    def process_command(self):
        if str(self.cmd) == "ls":
            if self.folder == root:
                root.ls()
                self.cmd = input(self.pre_cmdl)
                self.check_command()
            elif self.folder == e:
                e.ls()
                self.cmd = input(self.pre_cmdl)
                self.check_command()
        elif str(self.cmd) == "pwd":
            val = self.folder
            print(self.folder.value)
            while val != root:
                to_pr = val.parent()
                print(str(to_pr))

                val = val.parent()

            self.cmd = input(self.pre_cmdl)
            self.check_command()

        elif "cd" in str(self.cmd):
            safe = self.folder
            self.folder = input("what folder was that?")
            if self.folder != safe.children:
                self.folder = safe

        elif str(self.cmd) == "sudo su":
            self.user = "Root"
            self.BASHsymb = "#"
            self.pre_cmdl = self.user + "@" + self.comp + self.BASHsymb
            self.cmd = input(self.pre_cmdl)
            self.check_command()

        elif str(self.cmd) == "exit":
            self.user = "user"
            self.BASHsymb = "$"
            self.pre_cmdl = self.user + "@" + self.comp + self.BASHsymb
            self.cmd = input(self.pre_cmdl)
            self.check_command()

        elif str(self.cmd) == "clear":
            print("\t")
            print("\t")
            print("\t")
            print("\t")
            print("\t")
            print("\t")
            print("\t")
            print("\t")
            print("\t")
            print("\t")
