#GUI FOR CSC PROJECT by Bharghav
#If your datbase file is empty run the databse_creation.py file
import tkinter
import tkinter.font
from tkinter import messagebox
import sqlite3
from hashing import make_pw_hash, check_pw_hash
from subprocess import call
from hashing import make_pw_hash, check_pw_hash
from Homepage_gui import homePage
M_password=None
m_username=None
if __name__ == "__main__":
    def login(username,password):
        conn = sqlite3.connect('pass_manager.db')
            
        c = conn.cursor()
        
        if not username:
            messagebox.error("ERROR","Please enter a valid username in the username box.")
            return
        else:
            pass
        
        if not password:
            messagebox.error("ERROR","Please enter a valid password in the password box.")
            return
        else:
            pass
            
            
        c.execute("INSERT INTO user_data VALUES(:M_username, :master_pwd)",
                {
                    'M_username': username,
                    'master_pwd': password,
                })

        conn.commit() 
        conn.close()
        
        

    def signUp_Command():
        def signUp():
            global M_username
            global M_password
            M_username=user_name_entry.get()
            M_password=pass_word_entry.get()
            M_password=make_pw_hash(M_password)
            login(M_username,M_password)
            en=tkinter.Label(root,text="*Account Created Successfully",fg="red",bg="black")
            en.pack()
            return None
        root=tkinter.Tk()
        root.title("The Bois Password Manager - SignUp")
        root['bg']='black'
        Headin_text=tkinter.Label(root,text="SignUp",
        fg="green",bg="black")
        Font23=Custom_Font1=tkinter.font.Font(family="Ancient Modern Tales",size=25)
        Headin_text.configure(font=Font23)
        Headin_text.pack()
        Custom_Font=tkinter.font.Font( family = "Pixeboy", 
                                    size = 25, 
                                    )
        Headin_text.configure(font=Custom_Font)
        user_name=tkinter.Label(root,text="Username:",fg="green",bg="black")
        Custom_Font1=tkinter.font.Font(family="Consolas",size=15)
        user_name.configure(font=Custom_Font1)
        user_name.pack()
        user_name_entry = tkinter.Entry(root,fg="black", bg="#64f586", width=50)
        user_name_entry.pack()

        pass_word=tkinter.Label(root,text="Master Password:",fg="green",bg="black")
        pass_word.pack()
        pass_word.configure(font=Custom_Font1)
        pass_word_entry=tkinter.Entry(root,show="*",fg="black", bg="#64f586", width=50)
        pass_word_entry.pack()
        signUp_button= tkinter.Button(root,text="SignUp",width=10,height=2,bg="#61ff96",fg="black",command = signUp)
        signUp_button.pack(pady=5)
        root.mainloop()
    def Login():
        global username
        global password
        global m_username
        username=entry1.get()
        password=entry2.get()
        password=make_pw_hash(password)
        conn = sqlite3.connect('pass_manager.db')
        c = conn.cursor()
        c.execute("SELECT M_username from user_data WHERE M_username=? AND master_pwd=?", (username,password,))
        rows=c.fetchall()
        if rows==[]:
            wrg=tkinter.Label(win,text="*Wrong Username/Password",fg="red",bg="black")
            wrg.place(x=500,y=120)
            entry1.delete(0, 'end')
            entry2.delete(0, 'end')
        else:
            username=rows[0][0]
            homePage(username)
            m_username=username

        conn.close()

    win=tkinter.Tk()
    win.title("The Bois Password Manager - Login")
    win.geometry("920x640")
    win['bg']='black'
    Headin_text=tkinter.Label(text="The Bois password manager Login Portal",
    fg="green",bg="black")
    Headin_text.pack()
    Custom_Font=tkinter.font.Font( family = "Pixeboy", 
                                    size = 25, 
                                    )
    Headin_text.configure(font=Custom_Font)
    text1=tkinter.Label(win,text="Username:",fg="green",bg="black")
    Custom_Font1=tkinter.font.Font(family="Consolas",size=15)
    text1.configure(font=Custom_Font1)
    text1.pack(pady=20,side=tkinter.TOP,anchor="w")
    entry1 = tkinter.Entry(fg="black", bg="#64f586", width=50)
    entry1.place(x=100,y=50)

    text2=tkinter.Label(win,text="Master Password:",fg="green",bg="black")
    text2.pack(pady=20,side=tkinter.TOP,anchor="w")
    text2.configure(font=Custom_Font1)
    entry2=tkinter.Entry(show="*",fg="black", bg="#64f586", width=50)
    entry2.place(x=180,y=120)
    username=None
    password=None
    #Login button
    Login_button= tkinter.Button(
        text="Login",
        width=10,
        height=2,
        bg="#61ff96",
        fg="black",
        command=Login
    )
    signUp_button= tkinter.Button(
        text="SignUp",
        width=10,
        height=2,
        bg="#61ff96",
        fg="black",
        command = signUp_Command
    )
    signUp_button.pack()
    Login_button.pack()
    direc="images\matrix.gif"
    frameCnt = 20
    frames = [tkinter.PhotoImage(file=direc,format = 'gif -index %i' %(i)) for i in range(frameCnt)]
    def update(ind):

        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image=frame)
        win.after(100, update, ind)
    label = tkinter.Label(win)
    label.pack()
    win.after(0, update, 0)

    win.mainloop()

    
