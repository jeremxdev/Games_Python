from pytube import YouTube

def Download(link):
    YouTubeObject = YouTube(link)
    YouTubeObject = YouTubeObject.streams.get_highest_resolution()
    try:
        YouTubeObject.download()
    except:
        print("There has been an error in downloading your youtube video")
    print("This download has completed Yes !!")

link = input("Put your youtube link here!! URL: ")
Download(link)