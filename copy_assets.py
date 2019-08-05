from tkinter import *
import shutil as sh
from time import sleep
from os.path import exists
import os, sys, stat
#from win32 import win32con, win32api


fields = ('Source Path', 'Target Path')

def remove_readonly(fn, path, excinfo):
    try:
        os.chmod(path, stat.S_IWRITE)
        fn(path)
    except Exception as exc:
        print ("Skipped:", path, "because:\n", exc)

def copy_assets(entries):

  #local_path = "D:\\ADAM\\ws"
  src_raw = (entries['Source Path'].get())
  dst_raw = (entries['Target Path'].get()) 

  #src = local_path + src_raw
  #dst = local_path + dst_raw

  src = src_raw.split(':')[0].upper() +":"+ src_raw.split(':')[1]
  dst = dst_raw.split(':')[0].upper() +":"+ dst_raw.split(':')[1]

  if os.path.isdir(src) == True:
    if src.split('\\')[-1] == dst.split('\\')[-1]:
      print ("Copying folder contents...")
      if exists( dst ):
        sh.rmtree(dst, onerror=remove_readonly)
        sh.copytree( src, dst )
      else:
          sh.copytree( src, dst ) 
    else:
      raise Exception( "  //Error: Please check source and target paths.//")
  else:
        print ("Copying single file...")
        sh.copyfile( src, dst )

  print ("Process finished......")


def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"<Workspace Path>")
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
   return entries

if __name__ == '__main__':
   root = Tk()
   root.title(" ===// Copy Asset 1.0  //=== ")
   root.geometry("1000x100")
   root.configure(background='#151630')
   root.resizable(1,0)
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = Button(root, text='Copy Asset',
          command=(lambda e=ents: copy_assets(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   print ("Launch tool ......")

   b3 = Button(root, text='Quit', command=root.quit)
   b3.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
