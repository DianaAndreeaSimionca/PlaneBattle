import tkinter as tk

root = tk.Tk()

receiveFrame = tk.Frame(root)
receiveFrame.pack(side=tk.LEFT)

attackFrame = tk.Frame(root)
attackFrame.pack(side=tk.RIGHT)

username = tk.Label(root, text="Username: ")
usernameEntry = tk.Entry(root)



root.mainloop()