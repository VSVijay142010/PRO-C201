from tkinter import *
window=Tk()

# add widgets here


window.title('Simple interest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

def calculate_prt():
  p=float(principal_entry.get())
  r=float(rate_entry.get())
  t=float(time_entry.get())
  prt=(p*r*t)/100
  prt=round(prt,1)
  result_label.destroy()
 
  output_message=Label(result_frame,"interest is "+str(prt), fg = "black", bg = "lightcyan", font=("Calibri", 12),width=42 )
  output_message.place(x=20,y=40)
  output_message.pack()

app_label=Label(window, text="SIMPLE INTEREST CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

principal_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
principal_label.place(x=20, y=90)

principal_entry=Entry(window, text="", bd=2, width=22)
principal_entry.place(x=150, y=187)

rate_label=Label(window, text="Rate", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
rate_label.place(x=20, y=140)

rate_entry=Entry(window, text="", bd=2, width=22)
rate_entry.place(x=150, y=187)

time_label=Label(window, text="Time", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
time_label.place(x=20, y=185)

time_entry=Entry(window, text="", bd=2, width=22)
time_entry.place(x=150, y=187)

calculate_button=Button(window,text='calculate',bg='cyan',font=('Calibri',14),bd=4,command=calculate_prt)
result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

