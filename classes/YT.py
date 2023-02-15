
# ================= Importing Modules ===================

from pytube import YouTube

# ===========================================================

class YoutubeDownloader():

    # =======================  Downloading Video ====================
    def download_video(self, video_url, video_path):
        if str(video_url) == "":
            print("Error", "Please Paste Video URL")
        elif 'https://' not in str(video_url):
            print("Error", "Wrong Video Url")
        elif str(video_path) == "":
            print("Error", "Please provide Path")
        else:
            # try:
            # Just fix resolution video and add variabel in video downloader
            # And create messagebox show info download started.
            self.url = video_url
            self.path = video_path
            self.video = YouTube(self.url).streams
            self.stream = self.video.filter(
                file_extension="mp4", res="720p",
                only_audio=False
            ).first()
            print("Download Started")

        # except:
        # time.sleep(10)
        # messagebox.showerror("Error","Unable to Download Video | Something went wrong !!")

        # ========================= End ==============================

    # ==============================  Main Window ========================
    def __init__(self, video_url, video_path):
        self.download_video(video_url, video_path)
