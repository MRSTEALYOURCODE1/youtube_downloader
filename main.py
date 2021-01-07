from tkinter import *
import pytube

def download():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()
        video.download("/users/gr8amu/documents")
        notif.config(fg="Green", text="Download Complete")
    except Exception as e:
        print(e)
        notif.config(fg="red", text="Video Couldn't Be Downloaded")

main = Tk()
main.title("YouTube Video Downloader")


Label(main, text="YouTube Videos Downloader", fg="Green", font=("Arial",15)).grid(sticky=N,padx=100,row=0)
Label(main, text="Enter YouTube Link Below:", font=("Arial",12)).grid(sticky=N,row=1,pady=15)

notif = Label(main, font=("Arial", 12))
notif.grid(sticky=N, pady=1, row=4)

url = StringVar()

Entry(main, width=50, textvariable=url).grid(sticky=N , row=2)
Button(main, width=20, text="Download", font=("Arial", 12),command=download).grid(sticky=N, row=3,pady=15)

main.mainloop()
