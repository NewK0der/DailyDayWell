#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import Login_file_design
import Signup_file_design
import mysql.connector as ms
from tkinter import messagebox
import DailyDayWell


class NewprojectApp:

    def open_signup(self):
        Signup_file_design.SignupApp()
        self.LOGIN_FRAME.destroy()

    def login(self) :
        con = ms.connect(host="localhost",database="DailyDayWell",user="root",passwd="12345")
        cur = con.cursor()
        cur.execute("Select * from User_Details;")
        details = cur.fetchall()
        email = self.email.get()
        password = self.password.get()
        for d in details:
            if d[-2] == email and d[-1] == password:
                self.mainwindow.destroy()
                DailyDayWell.MainFrameApp(d[0])
                break
        else :
            messagebox.showerror("Error","Invalid User or Password.")
        
    def __init__(self, master=None):
        # build ui
        self.Login = tk.Tk() if master is None else tk.Toplevel(master)
        self.Login.configure(height=600, width=800)
        self.Login.resizable(False, False)
        self.Login.title("DailyDayWell")

        self.LOGIN_FRAME = tk.Frame(self.Login, name="login_frame")
        self.LOGIN_FRAME.configure(
            background="#ffffff",
            borderwidth=0,
            height=600,
            relief="ridge",
            width=800)
        label_1 = tk.Label(self.LOGIN_FRAME)
        self.img_login_image = tk.PhotoImage(file=r"C:\Users\Binit Shaw\Desktop\Project\GUI\Icon\login_image.png")
        label_1.configure(
            anchor="n",
            background="#ffffff",
            compound="top",
            font="TkTextFont",
            image=self.img_login_image)
        label_1.place(anchor="nw", height=500, width=300, x=450, y=50)
        label_2 = tk.Label(self.LOGIN_FRAME)
        label_2.configure(
            background="#ffffff",
            font="{Calibri} 36 {bold}",
            text='Login')
        label_2.place(anchor="nw", height=55, width=110, x=50, y=100)
        label_3 = tk.Label(self.LOGIN_FRAME)
        label_3.configure(
            background="#ffffff",
            font="{Calibri} 11 {}",
            state="normal",
            text='Login to access your account.')
        label_3.place(width=180, x=50, y=160)
        separator_11 = ttk.Separator(self.LOGIN_FRAME)
        separator_11.configure(orient="horizontal")
        separator_11.place(anchor="nw", height=1, width=140, x=50, y=220)
        separator_12 = ttk.Separator(self.LOGIN_FRAME)
        separator_12.configure(orient="horizontal")
        separator_12.place(anchor="nw", height=1, width=180, x=240, y=220)
        separator_13 = ttk.Separator(self.LOGIN_FRAME)
        separator_13.configure(orient="vertical")
        separator_13.place(anchor="nw", height=50, width=1, x=50, y=220)
        separator_14 = ttk.Separator(self.LOGIN_FRAME)
        separator_14.configure(orient="vertical")
        separator_14.place(anchor="nw", height=50, width=1, x=420, y=220)
        separator_15 = ttk.Separator(self.LOGIN_FRAME)
        separator_15.configure(orient="horizontal")
        separator_15.place(anchor="nw", height=1, width=370, x=50, y=270)
        #Email entry
        self.email = tk.Entry(self.LOGIN_FRAME, name="email")
        self.email.configure(borderwidth=0, font="{Calibri} 12 {}")
        self.email.place(
            anchor="nw",
            bordermode="ignore",
            height=35,
            width=350,
            x=60,
            y=230)
        label_8 = tk.Label(self.LOGIN_FRAME)
        label_8.configure(
            background="#ffffff",
            borderwidth=0,
            cursor="arrow",
            font="{Calibri} 14 {bold}",
            relief="raised",
            takefocus=False,
            text='Email')
        label_8.place(height=30, width=50, x=190, y=205)
        #Button
        self.login_button = tk.Button(self.LOGIN_FRAME, name="login_button")
        self.login_button.configure(
            background="#515DEF",
            borderwidth=0,
            compound="top",
            cursor="hand2",
            default="active",
            font="{Calibri} 16 {bold}",
            foreground="#ffffff",
            overrelief="sunken",
            text='Login',
            command=self.login)
        self.login_button.place(anchor="nw", height=40, width=370, x=50, y=380)
        
        label_9 = tk.Label(self.LOGIN_FRAME)
        label_9.configure(
            background="#ffffff",
            font="{Calibri Light} 11 {bold}",
            relief="flat",
            state="normal",
            takefocus=False,
            text="Don't have an account ?")
        label_9.place(height=25, width=170, x=130, y=460)
        #Button
        self.sign_up_button = tk.Button(
            self.LOGIN_FRAME, name="sign_up_button")
        self.sign_up_button.configure(
            background="#ffffff",
            borderwidth=0,
            cursor="hand2",
            font="{Calibri} 11 {bold}",
            foreground="#FB610A",
            overrelief="raised",
            state="normal",
            text='Sign up',
            command=self.open_signup)
        self.sign_up_button.place(
            anchor="nw", height=25, width=50, x=305, y=460)
        separator_1 = ttk.Separator(self.LOGIN_FRAME)
        separator_1.configure(orient="horizontal")
        separator_1.place(anchor="nw", height=1, width=140, x=50, y=300)
        separator_2 = ttk.Separator(self.LOGIN_FRAME)
        separator_2.configure(orient="horizontal")
        separator_2.place(anchor="nw", height=1, width=180, x=240, y=300)
        separator_3 = ttk.Separator(self.LOGIN_FRAME)
        separator_3.configure(orient="vertical")
        separator_3.place(anchor="nw", height=50, width=1, x=50, y=300)
        separator_4 = ttk.Separator(self.LOGIN_FRAME)
        separator_4.configure(orient="vertical")
        separator_4.place(anchor="nw", height=50, width=1, x=420, y=300)
        separator_5 = ttk.Separator(self.LOGIN_FRAME)
        separator_5.configure(orient="horizontal")
        separator_5.place(anchor="nw", height=1, width=370, x=50, y=350)
        #Password entry
        self.password = tk.Entry(self.LOGIN_FRAME, name="password",show="*")
        self.password.configure(borderwidth=0, font="{Calibri} 12 {}")
        self.password.place(
            anchor="nw",
            bordermode="ignore",
            height=35,
            width=350,
            x=60,
            y=310)
        label_4 = tk.Label(self.LOGIN_FRAME)
        label_4.configure(
            background="#ffffff",
            borderwidth=0,
            cursor="arrow",
            font="{Calibri} 14 {bold}",
            justify="left",
            relief="raised",
            takefocus=False,
            text='Password')
        label_4.place(height=30, width=80, x=190, y=285)
        self.forget_password = tk.Button(
            self.LOGIN_FRAME, name="forget_password")
        self.forget_password.configure(
            background="#ffffff",
            borderwidth=0,
            cursor="hand2",
            font="{Calibri} 11 {bold}",
            foreground="#FB610A",
            justify="left",
            overrelief="raised",
            state="normal",
            text='Forget password ?')
        self.forget_password.place(
            anchor="nw", height=20, width=120, x=50, y=425)
        label_6 = tk.Label(self.LOGIN_FRAME)
        self.img_logo = tk.PhotoImage(file=r"C:\Users\Binit Shaw\Desktop\Project\GUI\Icon\logo.png")
        label_6.configure(
            anchor="n",
            background="#ffffff",
            compound="top",
            cursor="arrow",
            font="TkDefaultFont",
            image=self.img_logo)
        label_6.place(anchor="nw", height=20, width=217, x=10, y=10)
        self.LOGIN_FRAME.place(
            anchor="nw",
            bordermode="ignore",
            height=600,
            width=800,
            y=0)
        self.LOGIN_FRAME.grid_anchor("n")
        
        # Main widget
        self.mainwindow = self.Login

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = NewprojectApp()
    app.run()

