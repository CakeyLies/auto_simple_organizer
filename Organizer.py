import os
import os.path
import shutil
import glob
from pathlib import Path

cwd = os.getcwd()
#Make folders for sorting
if not os.path.isdir("Executables"):
    exe = os.mkdir("Executables")
else:
    exe = os.path.abspath("Executables")

if not os.path.isdir("Videos"):
    videos = os.mkdir("Videos")
else:
    videos = os.path.abspath("Videos")

if not os.path.isdir("Photos"):
    photos = os.mkdir("Photos")
else:
    photos = os.path.abspath("Photos")


#Check files for file type

exeLocation = list(glob.glob("./*.exe"))
for exeFiles in exeLocation:
    exeFiles = str(exeFiles)[2:]
    exePath = os.path.abspath(str(exeFiles))
    shutil.move(exePath , exe)

videoLocation = list(glob.glob("./*.mp4"))
for videoFiles in videoLocation:
    videoFiles = str(videoFiles)[2:]
    videoPath = os.path.abspath(str(videoFiles))
    shutil.move(videoPath , videos)

videoLocation = list(glob.glob("./*.mov"))
for videoFiles in videoLocation:
    videoFiles = str(videoFiles)[2:]
    videoPath = os.path.abspath(str(videoFiles))
    shutil.move(videoPath , videos)

photoLocation = list(glob.glob("./*.png"))
for photoFiles in photoLocation: 
    photoFiles = str(photoFiles)[2:]
    photoPath = os.path.abspath(str(photoFiles))
    shutil.move(photoPath , photos)


photoLocation = list(glob.glob("./*.jpg"))
for photoFiles in photoLocation: 
    photoFiles = str(photoFiles)[2:]
    photoPath = os.path.abspath(str(photoFiles))
    shutil.move(photoPath , photos)


#os.mkdir("test")
#path = os.getcwd()
# myFile = open("test.txt", "w+")
# shutil.move('C:/Users/There/Documents/Python 3/test.txt','C:/Users/There/Documents/Python 3/Learning python/test.txt' )
# myFile.close()
