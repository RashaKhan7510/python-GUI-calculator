import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("Python Calculator")
root.geometry("320x400")
root.resizable(False,False)

entry= tk.Entry(root,width=16,
font=('Arial',24),borderwidth=2,
relief="solid", justify='right')
entry.grid(row=0, column=0,
columnspan=4, padx=10, pady=20)

def click(button_text):
    if button_text == "=":
        try:
            result =str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END,
result)
        except Exception as e:
             messagebox.showerror("Error","Invalid Expression")
    elif button_text =="C":
        entry.delete(0,tk.END)
    else:
        entry.insert(tk.END, button_text)

buttons=[
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3), ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3), ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3), ("0",4,0), (".",4,1), ("C",4,2), ("+",4,3), ("=",5,0,4)
    ]
for b in buttons:
   text=b[0]
   row=b[1]
   col=b[2]
   if len(b) ==4:
      colspan=b[3]
      btn=tk.Button(root,text=text, width=34,height=2, command=lambda x=text: click(x))
      btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)
   else:
     btn= tk.Button(root, text=text, width=8, height=2, command=lambda x=text: click(x))
     btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
                
