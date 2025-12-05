import tkinter as tk

master =tk.Tk()
tk.Label(master,text="Nama").grid(row=0)
tk.Label(master,text="Alamat").grid(row=1)

e1= tk.Entry(master)
e2= tk.Entry(master)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

tk.mainloop()