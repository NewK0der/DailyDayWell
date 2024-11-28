#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector as ms
from tkinter import messagebox
import Login_file_design

class SignupApp:
    
    def open_login(self):
        Login_file_design.LoginApp()
        self.SIGN_UP_FRAME.destroy()
        
    #sign_up Function
    def Sign_up(self) :
        con = ms.connect(host="localhost",database="DailyDayWell",user="root",passwd="12345")
        cur = con.cursor()

        cur.execute('Create table if not exists User_Details(Name varchar(30) not null, Number varchar(10) unique not null, Email varchar(30) primary key, Password varchar(30) not null);')
        cur.execute('insert into User_Details values("{}","{}","{}","{}");'.format(self.name.get(), self.number.get(), self.email.get(), self.password.get()))            
        cur.execute('Create table if not exists {}( Product_Name varchar(30) not null, Category varchar(30) not null, Description varchar(200));'.format(self.name.get()+"_Product"))
        cur.execute('Create table if not exists {}( S_N int primary key auto_increment, Category varchar(30) not null, Member varchar(30) not null, Product_Name varchar(30), Brand varchar(30), Description varchar(200), Quantity_left integer not null, Quantity integer not null, Unit varchar(10) not null, Price integer not null, total integer not null, Purches_Date date not null, Exp_Date date, Shop varchar(30), Discount integer);'.format(self.name.get()+"_Stocks"))
        con.commit()
        messagebox.showinfo("Message","Successfully Sign.")
        self.open_login()
        
    def __init__(self, master=None):
        # build ui
        self.SIGN_UP_FRAME = tk.Frame(
            master, container=False, name="sign_up_frame")
        self.SIGN_UP_FRAME.configure(
            background="#ffffff",
            borderwidth=0,
            height=600,
            width=800)
        label_1 = tk.Label(self.SIGN_UP_FRAME)
        self.img_signin_image = tk.PhotoImage(file=r"C:\Users\Binit Shaw\Desktop\Project\GUI\Icon\signin_image.png")
        label_1.configure(
            anchor="n",
            background="#ffffff",
            compound="top",
            font="TkDefaultFont",
            image=self.img_signin_image)
        label_1.place(anchor="nw", height=500, width=300, x=50, y=50)
        label_2 = tk.Label(self.SIGN_UP_FRAME)
        label_2.configure(
            background="#ffffff",
            font="{Calibri} 36 {bold}",
            text='Sign up')
        label_2.place(anchor="nw", height=55, width=150, x=400, y=50)
        label_3 = tk.Label(self.SIGN_UP_FRAME)
        label_3.configure(
            background="#ffffff",
            font="{Calibri} 11 {}",
            text='Let’s get you all st up so you can access your personal account.')
        label_3.place(width=380, x=400, y=110)
        label_4 = tk.Label(self.SIGN_UP_FRAME)
        label_4.configure(
            background="#ffffff",
            font="{Calibri} 14 {bold}",
            relief="flat",
            takefocus=False,
            text='Full Name')
        label_4.place(height=30, width=100, x=540, y=150)
        separator_1 = ttk.Separator(self.SIGN_UP_FRAME)
        separator_1.configure(orient="horizontal")
        separator_1.place(anchor="nw", height=1, width=140, x=400, y=165)
        separator_2 = ttk.Separator(self.SIGN_UP_FRAME)
        separator_2.configure(orient="horizontal")
        separator_2.place(anchor="nw", height=1, width=150, x=640, y=165)
        separator_3 = ttk.Separator(self.SIGN_UP_FRAME)
        separator_3.configure(orient="vertical")
        separator_3.place(anchor="nw", height=50, width=1, x=400, y=165)
        separator_4 = ttk.Separator(self.SIGN_UP_FRAME)
        separator_4.configure(orient="vertical")
        separator_4.place(anchor="nw", height=50, width=1, x=790, y=165)
        separator_5 = ttk.Separator(self.SIGN_UP_FRAME)
        separator_5.configure(orient="horizontal")
        separator_5.place(anchor="nw", height=1, width=390, x=400, y=215)
        #Name Entry
        self.name = tk.Entry(self.SIGN_UP_FRAME, name="name")
        self.name.configure(borderwidth=0, font="{Calibri} 12 {}")
        self.name.place(
            anchor="nw",
            bordermode="ignore",
            height=35,
            width=370,
            x=410,
            y=175)
        label_5 = tk.Label(self.SIGN_UP_FRAME)
        label_5.configure(
            background="#ffffff",
            font="{Calibri} 16 {bold}",
            justify="left",
            relief="flat",
            takefocus=False,
            text='Phone Number')
        label_5.place(height=30, width=140, x=530, y=225)
        separator_6 = ttk.Separator(self.SIGN_UP_FRAME)
        separator_6.configure(orient="horizontal")
        separator_6.place(anchor="nw", height=1, width=130, x=400, y=240)
        separator_7 = ttk.Separator(self.SIGN_UP_FRAME)
        separator_7.configure(orient="horizontal")
        separator_7.place(anchor="nw", height=1, width=120, x=670, y=240)
        separator_8 = ttk.Separator(self.SIGN_UP_FRAME)
        separator_8.configure(orient="vertical")
        separator_8.place(anchor="nw", height=50, width=1, x=400, y=240)
        separator_9 = ttk.Separator(self.SIGN_UP_FRAME)
        separator_9.configure(orient="vertical")
        separator_9.place(anchor="nw", height=50, width=1, x=790, y=240)
        separator_10 = ttk.Separator(self.SIGN_UP_FRAME)
        separator_10.configure(orient="horizontal")
        separator_10.place(anchor="nw", height=1, width=390, x=400, y=290)
        #Number Entry
        self.number = tk.Entry(self.SIGN_UP_FRAME, name="number")
        self.number.configure(borderwidth=0, font="{Calibri} 12 {}")
        self.number.place(
            anchor="nw",
            bordermode="ignore",
            height=35,
            width=370,
            x=410,
            y=250)
        separator_11 = ttk.Separator(self.SIGN_UP_FRAME)
        separator_11.configure(orient="horizontal")
        separator_11.place(anchor="nw", height=1, width=165, x=400, y=315)
        separator_12 = ttk.Separator(self.SIGN_UP_FRAME)
        separator_12.configure(orient="horizontal")
        separator_12.place(anchor="nw", height=1, width=180, x=610, y=315)
        separator_13 = ttk.Separator(self.SIGN_UP_FRAME)
        separator_13.configure(orient="vertical")
        separator_13.place(anchor="nw", height=50, width=1, x=400, y=315)
        separator_14 = ttk.Separator(self.SIGN_UP_FRAME)
        separator_14.configure(orient="vertical")
        separator_14.place(anchor="nw", height=50, width=1, x=790, y=315)
        separator_15 = ttk.Separator(self.SIGN_UP_FRAME)
        separator_15.configure(orient="horizontal")
        separator_15.place(anchor="nw", height=1, width=390, x=400, y=365)
        #Email Entry
        self.email = tk.Entry(self.SIGN_UP_FRAME, name="email")
        self.email.configure(borderwidth=0, font="{Calibri} 12 {}")
        self.email.place(
            anchor="nw",
            bordermode="ignore",
            height=35,
            width=370,
            x=410,
            y=325)
        label_7 = tk.Label(self.SIGN_UP_FRAME)
        label_7.configure(
            background="#ffffff",
            font="{Calibri} 16 {bold}",
            justify="left",
            relief="flat",
            takefocus=False,
            text='Password')
        label_7.place(height=30, width=80, x=550, y=375)
        separator_16 = ttk.Separator(self.SIGN_UP_FRAME)
        separator_16.configure(orient="horizontal")
        separator_16.place(anchor="nw", height=1, width=140, x=400, y=390)
        separator_17 = ttk.Separator(self.SIGN_UP_FRAME)
        separator_17.configure(orient="horizontal")
        separator_17.place(anchor="nw", height=1, width=150, x=640, y=390)
        separator_18 = ttk.Separator(self.SIGN_UP_FRAME)
        separator_18.configure(orient="vertical")
        separator_18.place(anchor="nw", height=50, width=1, x=400, y=390)
        separator_19 = ttk.Separator(self.SIGN_UP_FRAME)
        separator_19.configure(orient="vertical")
        separator_19.place(anchor="nw", height=50, width=1, x=790, y=390)
        separator_20 = ttk.Separator(self.SIGN_UP_FRAME)
        separator_20.configure(orient="horizontal")
        separator_20.place(anchor="nw", height=1, width=390, x=400, y=440)
        #Password entry
        self.password = tk.Entry(
            self.SIGN_UP_FRAME, name="password",show="*")
        self.password.configure(borderwidth=0, font="{Calibri} 12 {}")
        self.password.place(
            anchor="nw",
            bordermode="ignore",
            height=35,
            width=370,
            x=410,
            y=400)
        label_8 = tk.Label(self.SIGN_UP_FRAME)
        label_8.configure(
            background="#ffffff",
            borderwidth=0,
            cursor="arrow",
            font="{Calibri} 14 {bold}",
            relief="raised",
            takefocus=False,
            text='Email')
        label_8.place(height=30, width=50, x=570, y=300)
        #button
        self.submit_button = tk.Button(
            self.SIGN_UP_FRAME, name="submit_button")
        self.submit_button.configure(
            background="#515DEF",
            borderwidth=0,
            compound="top",
            cursor="hand2",
            default="normal",
            font="{Bahnschrift SemiLight SemiConde} 16 {bold}",
            foreground="#ffffff",
            overrelief="flat",
            text='Create Account',
            command=self.Sign_up)
        self.submit_button.place(
            anchor="nw", height=40, width=390, x=400, y=460)
        label_9 = tk.Label(self.SIGN_UP_FRAME)
        label_9.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            relief="flat",
            takefocus=False,
            text='Already have an account ?')
        label_9.place(height=25, width=160, x=500, y=510)
        #Button
        self.login_button = tk.Button(self.SIGN_UP_FRAME, name="login_button")
        self.login_button.configure(
            background="#ffffff",
            borderwidth=0,
            cursor="hand2",
            font="{Calibri} 11 {bold}",
            foreground="#FB610A",
            overrelief="flat",
            text='Login',
            command=self.open_login)
        self.login_button.place(anchor="nw", height=25, width=35, x=665, y=510)
        
        label_6 = tk.Label(self.SIGN_UP_FRAME)
        self.img_logo = tk.PhotoImage(file=r"C:\Users\Binit Shaw\Desktop\Project\GUI\Icon\logo.png")
        label_6.configure(
            anchor="n",
            background="#ffffff",
            compound="top",
            cursor="arrow",
            font="TkDefaultFont",
            image=self.img_logo)
        label_6.place(anchor="nw", height=20, width=217, x=570, y=10)
        self.SIGN_UP_FRAME.place(
            anchor="nw",
            bordermode="ignore",
            height=600,
            width=800,
            y=0)
        self.SIGN_UP_FRAME.grid_anchor("n")

        # Main widget
        self.mainwindow = self.SIGN_UP_FRAME

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = SignupApp(root)
    app.run()
