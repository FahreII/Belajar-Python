import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="python.png")
logo_label = tk.Label(root, image=logo).pack(side="right")

expanation = "saya mahasiswa"
desc_label = tk.Label(root,
                justify=tk.LEFT,
                padx=10,
                text=expanation).pack(side="left")

root.mainloop()