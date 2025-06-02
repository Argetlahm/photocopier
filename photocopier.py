import tkinter as tk
import datetime as datetime
from datetime import timedelta as dt # Importing the datetime module to work with dates and times
import os # Importing the os module to interact with the operating system
import shutil # Importing the shutil module to perform high-level file operations
import glob # Importing the glob module to find all the pathnames matching a specified pattern
from os import listdir
from os.path import isfile, join
import random # Importing the random module to generate random numbers


def checkFile(filePath):
    if os.path.exists(filePath):
        # copy file to the destination folder
        destination = "D:/gambar2/tempwallpaper/"
        # Check if the destination folder exists, if not create it
        if not os.path.exists(destination):
            os.makedirs(destination)
        # Copy the file to the destination folder
        # Use os.system to copy the file (this is a simple way to copy files in Python)
        # os.system(f'copy "{filePath}" "{destination}"')
        shutil.copyfile(filePath, destination+"wallpaper.jpg")
        print(filePath + " copied to " + destination)
        label2 = tk.Label(root, text="Your wallpaper image has been copied!")
        label2.config(font=("Arial", 10))
        label2.config(bg="lightgreen")
        label2.pack(pady=5)
    else:
        print("File does not exist")
        label2 = tk.Label(root, text="Your wallpaper image has not been copied!")
        label2.config(font=("Arial", 10))
        label2.config(bg="red")
        label2.pack(pady=5)
        return False
    return True

root = tk.Tk()
root.title("Photocopier")
root.geometry("600x250")
root.config(bg="gray")

label = tk.Label(root, text="Welcome to the Photocopier!\nThis will help you copy your wallpaper image to one dedicated folder.")
label.config(font=("Arial", 12))
label.config(bg="lightblue")
label.pack(pady=20)
currentDate = tk.StringVar()
currentDate.set((datetime.datetime.today() - dt(1)).strftime("%Y%m%d"))
print(currentDate.get())
dateLabel = tk.Label(root, text="Yesterday Date: "+ currentDate.get())
# checkFile("C:/Users/gunaw/AppData/Local/Packages/Microsoft.BingWallpaper_8wekyb3d8bbwe/LocalState/images/Bing/"+currentDate.get()+"_bing.jpg")
mypath = "C:/Users/gunaw/AppData/Local/Packages/Microsoft.BingWallpaper_8wekyb3d8bbwe/LocalState/images/Bing/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# print(onlyfiles)
fileChosen = False
while not fileChosen:
    randomFile = random.choice(onlyfiles)
    if randomFile.endswith(".jpg") or randomFile.endswith(".jpeg"):
        fileChosen = True
        print("Random file chosen: " + randomFile)
        checkFile(mypath + randomFile)

dateLabel.config(font=("Arial", 10))
dateLabel.config(bg="lightblue")
dateLabel.pack(pady=5)
button2 = tk.Button(root, text="Exit", command=root.quit)
button2.pack(pady=10)
versionLabel = tk.Label(root, text="Version 1.1")
versionLabel.config(font=("Arial", 8))
versionLabel.config(bg="lightblue")
versionLabel.pack(pady=5)





print("Welcome to the Photocopier!")
root.mainloop()



