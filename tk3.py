import tkinter as tk

master =tk.Tk()
tk.Label(master,text="Nama").grid(row=0)
tk.Label(master,text="Alamat").grid(row=1)

e1= tk.Entry(master)
e2= tk.Entry(master)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

def show_data():
    txt_nama = "Nama Saya : %s"%(e1.get())
    txt_alamat = "Alamat Saya : %s"%(e2.get())
    tk.Label(master, text=txt_nama).grid(row=4, columnspan=2)
    tk.Label(master, text=txt_alamat).grid(row=5, columnspan=2)
bt_show = tk.Button(master,text="Show",command=show_data)
bt_show.grid(row=3,column=0,sticky=tk.W,pady=4)

tk.mainloop()