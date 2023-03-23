from tkinter import *
import string
#RANDOM PASSWORD GENERATOR MANISH
def generator():
    s_alpha=string.ascii_lowercase
    c_alpha=string.ascii_uppercase
    digit=string.digits
    sp_char=string.punctuation

    all=s_alpha+c_alpha+digit+sp_char
    print(all)




window=Tk()
window.title("Password generator")
window.config(bg='light blue')
window.geometry('400x450')
choice=IntVar
Font=('aril',15,'bold')
pslable=Label(window,text='Password Generator',font=('times new roman',25,'bold'),bg='black',fg='white')
pslable.grid(pady=10,column=0,row=1)
wrdbutton=Radiobutton(window,text='Weak',value=1,variable=choice,font=Font)
wrdbutton.grid(pady=5)
# wrdbutton.pack(side=TOP,pady=5)
nrdbutton=Radiobutton(window,text='Normal',value=2,variable=choice,font=Font)
nrdbutton.grid(pady=5)
srdbutton=Radiobutton(window,text='Strong',value=3,variable=choice,font=Font)
srdbutton.grid(pady=5)

pslen=Label(window,text='Password lenght',font=Font,bg='black',fg='white')
pslen.grid(pady=10,column=0,row=6)
lbox=Spinbox(window,text='',from_=5,to=20,width=5,font=Font)
lbox.grid()
gbutton=Button(window,text='Generate',font=Font,)
gbutton.grid(pady=5)
psfield=Entry(window,bd=2,width=25)
psfield.grid(pady=5)
cpbutton=Button(window,font=Font,text='Copy')
cpbutton.grid()


window.mainloop()