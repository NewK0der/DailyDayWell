#!/usr/bin/python3
import tkinter as tk
import Grocery_file1


class MainFrameApp:
    def call_grocery_page(self):
        Grocery_file1.GroceryApp()
        
    def __init__(self, user, master=None):
        # build ui
        self.user = user

        Main = tk.Tk() if master is None else tk.Toplevel(master)
        Main.configure(background="#ffff80", height=750, width=1370)
        Main.overrideredirect("false")
        Main.title("DailyDayWell")
        #side bar
        self.SIDE_BAR_FRAME = tk.Frame(Main, name="side_bar_frame")
        self.SIDE_BAR_FRAME.configure(
            background="#ffffff", height=200, width=200)
        label_1 = tk.Label(self.SIDE_BAR_FRAME)
        self.img_logo = tk.PhotoImage(file=r"C:\Users\Binit Shaw\Desktop\Project\GUI\Icon\logo.png", master = Main)
        label_1.configure(
            image=self.img_logo,
            justify="center",
            state="normal")
        label_1.place(anchor="nw", height=20, width=217, x=10, y=10)
        label_4 = tk.Label(self.SIDE_BAR_FRAME)
        self.img_grocery_logo1 = tk.PhotoImage(file=r"C:\Users\Binit Shaw\Desktop\Project\GUI\Icon\grocery_logo1.png", master = Main)
        
        label_4.configure(
            font="TkDefaultFont",
            image=self.img_grocery_logo1,
            justify="center",
            state="normal")
        label_4.place(anchor="nw", height=36, width=40, x=10, y=200)
        label_5 = tk.Label(self.SIDE_BAR_FRAME)
        self.img_medicine_logo = tk.PhotoImage(file=r"C:\Users\Binit Shaw\Desktop\Project\GUI\Icon\medicine_logo.png", master = Main)
        label_5.configure(
            font="TkDefaultFont",
            image=self.img_medicine_logo,
            justify="center",
            state="normal")
        label_5.place(anchor="nw", height=40, width=40, x=10, y=300)
        label_6 = tk.Label(self.SIDE_BAR_FRAME)
        self.img_bill_logo = tk.PhotoImage(file=r"C:\Users\Binit Shaw\Desktop\Project\GUI\Icon\bill_logo.png", master = Main)
        label_6.configure(
            font="TkDefaultFont",
            image=self.img_bill_logo,
            justify="left",
            state="normal")
        label_6.place(anchor="nw", height=40, width=40, x=10, y=400)
        label_7 = tk.Label(self.SIDE_BAR_FRAME)
        self.img_schedule_logo = tk.PhotoImage(file=r"C:\Users\Binit Shaw\Desktop\Project\GUI\Icon\schedule_logo.png", master = Main)
        label_7.configure(
            font="TkTextFont",
            image=self.img_schedule_logo,
            justify="center",
            state="normal")
        label_7.place(anchor="nw", height=40, width=40, x=10, y=500)
        label_8 = tk.Label(self.SIDE_BAR_FRAME)
        self.img_setting_logo = tk.PhotoImage(file=r"C:\Users\Binit Shaw\Desktop\Project\GUI\Icon\setting_logo.png", master = Main)
        label_8.configure(
            cursor="arrow",
            font="TkDefaultFont",
            image=self.img_setting_logo,
            justify="center",
            state="normal")
        label_8.place(anchor="nw", height=40, width=40, x=10, y=600)
        #grocery button
        self.grocery_button = tk.Button(
            self.SIDE_BAR_FRAME, name="grocery_button")
        self.grocery_button.configure(
            background="#ffffff",
            default="normal",
            font="{Calibri} 12 {bold}",
            justify="left",
            overrelief="flat",
            relief="flat",
            text='Grocery Manage',
            command = self.call_grocery_page)
        self.grocery_button.place(
            anchor="nw", height=30, width=120, x=55, y=200)
        
        self.medicine_button = tk.Button(
            self.SIDE_BAR_FRAME, name="medicine_button")
        self.medicine_button.configure(
            background="#ffffff",
            compound="top",
            default="normal",
            font="{Calibri} 12 {bold}",
            justify="center",
            overrelief="flat",
            relief="flat",
            text='Medicine Manage')
        self.medicine_button.place(
            anchor="nw", height=30, width=120, x=55, y=300)
        self.bill_button = tk.Button(self.SIDE_BAR_FRAME, name="bill_button")
        self.bill_button.configure(
            background="#ffffff",
            cursor="arrow",
            default="normal",
            font="{Calibri} 12 {bold}",
            justify="left",
            overrelief="flat",
            relief="flat",
            text='Bill Manage')
        self.bill_button.place(anchor="nw", height=30, width=90, x=55, y=400)
        self.schedule_button = tk.Button(
            self.SIDE_BAR_FRAME, name="schedule_button")
        self.schedule_button.configure(
            background="#ffffff",
            default="normal",
            font="{Calibri} 12 {bold}",
            justify="left",
            overrelief="flat",
            relief="flat",
            text='Schedule Manage')
        self.schedule_button.place(
            anchor="nw", height=30, width=125, x=55, y=500)
        self.setting_button = tk.Button(
            self.SIDE_BAR_FRAME, name="setting_button")
        self.setting_button.configure(
            background="#ffffff",
            default="normal",
            font="{Calibri} 14 {bold}",
            justify="left",
            overrelief="flat",
            relief="flat",
            takefocus=False,
            text='Setting')
        self.setting_button.place(
            anchor="nw", height=30, width=70, x=55, y=600)
        
        self.dashboard_button = tk.Button(self.SIDE_BAR_FRAME, name="button_1")
        self.dashboard_button.configure(
            background="#ffffff",
            default="normal",
            font="{Calibri} 12 {bold}",
            justify="center",
            overrelief="flat",
            relief="flat",
            text='Dashboard')
        self.dashboard_button.place(anchor="nw", height=30, width=80, x=55, y=100)
        label_9 = tk.Label(self.SIDE_BAR_FRAME)
        self.img_dashboard_logo = tk.PhotoImage(file=r"C:\Users\Binit Shaw\Desktop\Project\GUI\Icon\dashboard_logo.png", master = Main)
        label_9.configure(
            compound="top",
            font="TkDefaultFont",
            image=self.img_dashboard_logo,
            justify="center",
            state="normal",
            takefocus=False)
        label_9.place(anchor="nw", height=36, width=40, x=10, y=100)
        self.SIDE_BAR_FRAME.place(anchor="nw", height=750, width=230, x=0, y=0)
        #Top Bar
        self.TOP_BAR_FRAME = tk.Frame(Main, name="top_bar_frame")
        self.TOP_BAR_FRAME.configure(
            background="#ffffff", height=200, width=200)
        label_15 = tk.Label(self.TOP_BAR_FRAME)
        label_15.configure(
            background="#ffffff",
            font="{Calibri} 25 {}",
            justify="center",
            state="normal",
            text='👋🏼')
        label_15.place(anchor="nw", height=35, width=40, x=10, y=0)
        self.user_name_label = tk.Label(
            self.TOP_BAR_FRAME, name="user_name_label")
        self.user_name_label.configure(
            background="#ffffff",
            font="{Calibri} 12 {bold}",
            foreground="#000000",
            text="Hello, "+user,
            anchor="nw"
            )
        self.user_name_label.place(
            anchor="nw", height=35, width=250, x=55, y=0)
        self.TOP_BAR_FRAME.place(
            anchor="nw", height=40, width=1140, x=230, y=0)

        # Main widget
        self.mainwindow = Main

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = MainFrameApp("")
    app.run()
