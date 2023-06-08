# YouTube video downloader and converter
Hello! This is a program made in Python for downloading YouTube videos or converting it.


## Modules
- ___Tkinter:___ for the GUI; <br>
- ___Ttkbootstrap___: for styling the GUI; <br>
- ___Pytube:___ for getting the YouTube link and downloading the video; <br>
- ___Moviepy:___ for converting the video to mp3; <br>
- ___Os:___ for removing the mp4 file after converting it; <br>
- ___Pyinstaller:___ for converting the code to a executable file; 


## Observations
- I couldn't find a way to bypass the age restriction, so some videos can't be downloaded because of the YouTube age restriction; <br>
- For the version that converts to mp3 files, you can't deactivate the ``--noconsole`` command in Pyinstaller, or it'll become a mp4 downloader only;
- The function that downloads the videos as mp4 files is at the end of the Python file;
