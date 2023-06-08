import tkinter as tk
import ttkbootstrap as ttk
from pytube import YouTube
from moviepy.editor import *
import os


# [DOWNLOAD FUNCTION]
def download_mp3():
    link = entry.get()

    video = YouTube(link)
    audio = video.streams.filter(only_audio=True).first()
    destination = ''
    audio_file = audio.download(output_path=destination)

    mp3 = AudioFileClip(audio_file)
    mp3.write_audiofile(audio_file[:-4] + ".mp3")

    os.remove(audio_file)


# [WINDOW]
window = ttk.Window(themename='yeti')
window.title('YTMP3')
window.geometry('600x200')


# [WIDGETS]
# title
title_label = ttk.Label(
    master=window,
    text='YTMP3',
    font='Georgia 24 bold' 
)
title_label.pack()

# input
input_frame = ttk.Frame(
    master=window
)

entry = ttk.Entry(
    master=input_frame,
    justify='center'
)
button = ttk.Button(
    master=input_frame,
    text='Download',
    command=download_mp3, 
)

window.bind('<Return>', lambda event:download_mp3())

input_frame.pack()
entry.pack(pady=5, ipady=4, ipadx=200)
button.pack(pady=5)


# [RUN WINDOW]
window.mainloop()



# [YTMP4 FUNCTION]
'''
def download_mp4():
    link = entry.get()

    video = YouTube(link)
    mp4 = video.streams.get_highest_resolution()
    destination = ''
    mp4.download(output_path=destination)
'''
