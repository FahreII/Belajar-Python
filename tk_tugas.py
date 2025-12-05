import tkinter as tk

master =tk.Tk()
tk.Label(master,text="Masukan Panjang").grid(row=0)
tk.Label(master,text="Masukan Lebar").grid(row=1)

e1= tk.Entry(master)
e2= tk.Entry(master)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

def show_data():
    panjang = float(e1.get())
    lebar = float(e2.get())
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)

    txt_luas = "Luas : %s"%(luas)
    txt_keliling = "Keliling : %s"%(keliling)
    tk.Label(master, text=txt_luas).grid(row=4, columnspan=2)
    tk.Label(master, text=txt_keliling).grid(row=5, columnspan=2)
bt_show = tk.Button(master,text="Hitung",command=show_data)
bt_show.grid(row=3,column=0,sticky=tk.W,pady=4)

tk.mainloop()