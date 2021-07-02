import tkinter
from pytube import YouTube
import webbrowser

root = tkinter.Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Youtube Video Downloader")


tkinter.Label(root, text ='Youtube Video Downloader', font ='arial 20 bold').pack()




##enter link
link = tkinter.StringVar()

tkinter.Label(root, text ='Paste Link Here:', font ='arial 15 bold').place(x= 160, y = 60)
link_enter = tkinter.Entry(root, width = 70, textvariable = link).place(x = 32, y = 90)



#function to download video
def callback(url):
    webbrowser.open_new(url)

def Downloader():

    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    tkinter.Label(root, text ='DOWNLOADED', font ='arial 15').place(x= 180, y = 210)


tkinter.Button(root, text ='DOWNLOAD', font ='arial 15', bg ='blue', padx = 2, command = Downloader).place(x=180, y = 150)
link1 = tkinter.Label(root, text="Source Code Here", font = 'arial 15', fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("http://www.github.com/alexliao95311/Youtube-Video-Downloader"))

root.mainloop()
