import tkinter
import tkinter.font
win=tkinter.Tk()
win.title("Admin Portal")
win.geometry("918x450")
win['bg']='black'
Headin_text=tkinter.Label(text="Admin Login Portal",
fg="green",bg="black")
Headin_text.pack()
Custom_Font=tkinter.font.Font( family = "Ancient Modern tales", 
                                 size = 25, 
                                 )
Headin_text.configure(font=Custom_Font)
text1=tkinter.Label(win,text="Admin Username:",fg="green",bg="black")
Custom_Font1=tkinter.font.Font(family="Consolas",size=15)
text1.configure(font=Custom_Font1)
text1.pack(pady=20,side=tkinter.TOP,anchor="w")
entry1 = tkinter.Entry(fg="black", bg="#64f586", width=50)
entry1.place(x=172,y=68)

text2=tkinter.Label(win,text="Admin Password:",fg="green",bg="black")
text2.pack(pady=20,side=tkinter.TOP,anchor="w")
text2.configure(font=Custom_Font1)
entry2=tkinter.Entry(fg="black", bg="#64f586", width=50)
entry2.place(x=172,y=134)
Username=entry1.get()
Password=entry2.get()
Login_button= tkinter.Button(
    text="Login",
    width=10,
    height=2,
    bg="#61ff96",
    fg="black",
)

label = tkinter.Label(win)



win.mainloop()



