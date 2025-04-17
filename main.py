import tkinter as tk
import datetime as datetime
from datetime import timedelta as dt # Importing the datetime module to work with dates and times
import os # Importing the os module to interact with the operating system



def checkFile(filePath):
    if os.path.exists(filePath):
        print("File exists")
    else:
        print("File does not exist")
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
checkFile("C:/Users/gunaw/AppData/Local/Packages/Microsoft.BingWallpaper_8wekyb3d8bbwe/LocalState/images/Bing/20250417_bing.jpg")
dateLabel.config(font=("Arial", 10))
dateLabel.config(bg="lightblue")
dateLabel.pack(pady=5)
button = tk.Button(root, text="Start", command=lambda: print("Starting Photocopier..."))
button.pack(pady=10)
button2 = tk.Button(root, text="Exit", command=root.quit)
button2.pack(pady=10)



print("Welcome to the Photocopier!")
root.mainloop()



