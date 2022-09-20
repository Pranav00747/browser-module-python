import tkinter as ttm
from tkinter.ttk import *
from PIL import Image, ImageTk
class Browser_Module:
  def create_main_page():
     mt = ttm.Tk()
     mt.title("Browser Module")
     xw = mt.winfo_screenwidth()
     xh = mt.winfo_screenheight()
     mt.geometry("%dx%d"%(xw, xh))
     mt.overrideredirect(1)
     return mt

if __name__=="__main__":
 bm = Browser_Module
 bmm = bm.create_main_page()
 def about_page():
  abt = ttm.Tk()
  wx = (abt.winfo_screenwidth()-600)/2
  wy = (abt.winfo_screenheight()-400)/2
  abt.geometry("600x400+%d+%d"%(wx, wy))
  abt.title("About")
  abt.overrideredirect(1)
  def clk(e):
    abt.destroy()
  abt.bind('<Button-1>', clk)
  icc = ttm.Canvas(abt, width=600, height=400, bg='#003366')
  icc.place(x=0, y=0)
  icc.create_text(260, 20, fill='white', font=('MS Sans Serif', 10), text="This is sample module of Web Box developed by Mr. Pranav")
  icc.create_text(250, 40, fill='white', font=('MS Sans Serif', 10), text="Hi, this is Pranav founder/creator of this product, I am good")
  icc.create_text(256, 60, fill='white', font=('MS Sans Serif', 10), text="person always try to help others if they need help, if you want")
  icc.create_text(175, 80, fill='white', font=('MS Sans Serif', 10), text="to connect with me follow me on :")
  icc.create_text(256, 140, fill='white', font=('MS Sans Serif', 10), text="Instagram :- https://www.instagram.com/elcodificadorrr_._")
  icc.create_text(205, 160, fill='white', font=('MS Sans Serif', 10), text="GitHub :- https://github.com/Pranav00747")
  lab1 = ttm.Label(icc, text="Copyright of @Pranav (Web Box)", bg='#003366', fg='white', font=('Calibri', 10))
  lab1.place(x=200, y=360)
  def ll_e(e):
   lab1.config(font=('Calibri', 12), fg='yellow')
  def ll_l(e):
   lab1.config(font=('Calibri', 10), fg='white')
  lab1.bind('<Enter>', ll_e)
  lab1.bind('<Leave>', ll_l)
 mb = ttm.Menu(bmm)
 about = ttm.Menu(mb, tearoff=0)
 about.add_command(label='About', command=about_page)
 mb.add_cascade(label='File')
 mb.add_cascade(label='Help', menu=about)
 bmm.config(menu=mb)
 wd =bmm.winfo_screenwidth()
 ht  =bmm.winfo_screenheight()
 mainc = ttm.Canvas(bmm, bg='#2c4a7d', width=wd, height=40, highlightthickness=0)
 mainc.place(x=0, y=0)
 mainc.create_line(0, 38, wd, 39, fill='#071c40')
 ttext = ttm.Label(bmm, text='Browser Module', bg='#2c4a7d', fg='white', font=('Arial', 12))
 ttext.place(x=10, y=10)
 cctext = ttm.Label(bmm, text='x', bg='#2c4a7d', fg='white', font=('Arial', 10))
 cctext.place(x=wd-40, y=9)
 def c_e(e):
  cctext.config(font=('Arial', 12), fg='yellow')
 def c_l(e):
  cctext.config(font=('Arial', 10), fg='white')
 def c_c(e):
  bmm.destroy()
 cctext.bind('<Enter>', c_e)
 cctext.bind('<Leave>', c_l)
 cctext.bind('<Button-1>', c_c)
 toolc = ttm.Canvas(bmm, bg='#e0e0e0', width=wd, height=60, highlightthickness=0)
 toolc.place(x=0, y=40)
 img2 = Image.open('refresh.png')
 img2 = img2.resize((20, 20))
 global m_img2
 m_img2 = ImageTk.PhotoImage(img2)
 url_t = ttm.Entry(toolc, width=175, font=('Arial', 10))
 url_t.place(x=120, y=12)
 backl = ttm.Label(toolc, text='<-', fg='black', font=('Calibri', 16), bg='#e0e0e0')
 backl.place(x=5, y=12)
 def b_e(e):
  backl.config(font=('Calibri', 18))
 def b_c(e):
  backl.config(font=('Calibri', 16))
 backl.bind('<Enter>', b_e)
 backl.bind('<Leave>', b_c)
 refl = ttm.Label(toolc, width=20, height=20, bg='#e0e0e0',  image=m_img2)
 refl.place(x=35, y=16)
 def r_e(e):
  refl.config(width=22, height=22)
 def r_c(e):
  refl.config(width=20, height=20)
 refl.bind('<Enter>', r_e)
 refl.bind('<Leave>', r_c)
 forwl = ttm.Label(toolc, text='->', fg='black', font=('Calibri', 16), bg='#e0e0e0')
 forwl.place(x=65, y=12)
 def f_e(e):
  forwl.config( font=('Calibri', 18))
 def f_c(e):
  forwl.config( font=('Calibri', 16))
 forwl.bind('<Enter>', f_e)
 forwl.bind('<Leave>', f_c)
 bmm .mainloop()
