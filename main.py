import tkinter as tk


root = tk.Tk()
root.title("Photocopier")
root.geometry("300x200")

label = tk.Label(root, text="Welcome to the Photocopier!")
label.pack(pady=20)


print("Welcome to the Photocopier!")
root.mainloop()


