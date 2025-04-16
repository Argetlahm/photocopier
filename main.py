import tkinter as tk
import datetime as datetime

root = tk.Tk()
root.title("Photocopier")
root.geometry("600x250")
root.config(bg="gray")

label = tk.Label(root, text="Welcome to the Photocopier!\nThis will help you copy your wallpaper image to one dedicated folder.")
label.config(font=("Arial", 12))
label.config(bg="lightblue")
label.pack(pady=20)
currentDate = tk.IntVar()
currentDate.set(datetime.datetime.today().strftime("%Y-%m-%d"))
print(currentDate)
dateLabel = tk.Label(root, text="Current Date: 2023-10-01")
dateLabel.config(font=("Arial", 10))
dateLabel.config(bg="lightblue")
dateLabel.pack(pady=5)
button = tk.Button(root, text="Start", command=lambda: print("Starting Photocopier..."))
button.pack(pady=10)
button2 = tk.Button(root, text="Exit", command=root.quit)
button2.pack(pady=10)



print("Welcome to the Photocopier!")
root.mainloop()


