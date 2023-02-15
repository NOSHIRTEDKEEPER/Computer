from classes.YT import YoutubeDownloader

from classes.File_system import *

class Terminal:
    def __init__(self):
        self.folder = root
        self.commands = ["ls", "pwd", "cd", "yt"]
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
                self.cmd = input(self.pre_cmdl)
                self.check_command()

            index = index + 1

        else:
            if self.cmd == "":
                self.cmd = input(self.pre_cmdl)
                self.check_command()

            else:
                print(str(self.cmd) + " is not a valid command.")
                self.cmd = input(self.pre_cmdl)
                self.check_command()


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

        elif str(self.cmd) == "yt":
            video_url = input("What is the url?")
            video_path = input("What is the Path?")
            if video_path == "" or " ":
                video_path = "Windows/Users/Public/Public Downloads"

            YoutubeDownloader.download_video(video_url = video_url, video_path= video_path)

        elif "cd" in str(self.cmd):
            safe = self.folder
            self.folder = input("what folder was that?")
            if self.folder != safe.children:
                self.folder = safe

