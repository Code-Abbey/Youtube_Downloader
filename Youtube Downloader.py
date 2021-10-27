# Install the required modules
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

#                   Backend
Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")

#download video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link again!!",fg="red")


    #download function
    select.download(Folder_Name)
    ytdError.config(text="Download Completed!!")

#Frontend

root = Tk()
root.title("Youtube Downloader")
#set window
root.geometry("350x400")
#set all content in center
root.columnconfigure(0,weight=1)

#YTD Link label
ytdLabel = Label(root,text="Enter the URL of the Video",font=("jost",15))
ytdLabel.grid()

#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

#Error MSG
ytdError = Label(root,text="Error Msg",fg="red",font=("jost",10))
ytdError.grid()

#Asking save file Label
saveLabel = Label(root,text="Save the Video File",font=("jost",15,"bold"))
saveLabel.grid()

#btn of save file
saveEntry = Button(root,width=10,bg="red",fg="white",text="choose Path",command=openLocation)
saveEntry.grid()

#Error Message Location
locationError = Label(root,text="Error Msg of Path",fg="red",font=("jost",10))
locationError.grid()

#Download Quality
ytdQuality = Label(root,text="Select Quality",font=("jost",15))
ytdQuality.grid()

#combobx
choices = ("720p","144p","Only Audio")
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

#Download button
downloadbtn = Button(root,text="Download",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()

#Developer Laber
devloperlabel = Label(root,text="Code Abbeycity",font=("jost",15))
devloperlabel.grid()
root.mainloop()