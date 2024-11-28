#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from tkcalendar.dateentry import DateEntry


class GroceryApp:
    def __init__(self, master=None):
        # build ui
        self.GROCERY_FRAME = tk.Frame(master, name="grocery_frame")
        self.GROCERY_FRAME.configure(
            background="#515DEF", height=710, width=1140)
        
        self.BUYING_FRAME = tk.Frame(self.GROCERY_FRAME, name="buying_frame")
        self.BUYING_FRAME.configure(height=200, width=200)
        self.BUY_ITEM_FRAME = tk.Frame(
            self.BUYING_FRAME, name="buy_item_frame")
        self.BUY_ITEM_FRAME.configure(
            background="#ffffff", height=550, width=550)
        
        self.name = ttk.Combobox(self.BUY_ITEM_FRAME, name="name")
        self.name.configure(state="readonly")
        self.name.place(anchor="nw", height=30, width=150, x=50, y=170)
        
        self.category = ttk.Combobox(self.BUY_ITEM_FRAME, name="category")
        self.category.configure(state="readonly")
        self.category.place(anchor="nw", height=30, width=150, x=50, y=100)
        
        self.member = ttk.Combobox(self.BUY_ITEM_FRAME, name="member")
        self.member.configure(state="readonly")
        self.member.place(anchor="nw", height=30, width=150, x=300, y=100)
        
        label_8 = tk.Label(self.BUY_ITEM_FRAME)
        label_8.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Product Name *')
        label_8.place(height=20, width=100, x=50, y=150)
        label_1 = tk.Label(self.BUY_ITEM_FRAME)
        label_1.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Brand')
        label_1.place(height=20, width=40, x=300, y=150)
        
        self.brand = tk.Entry(self.BUY_ITEM_FRAME, name="brand")
        self.brand.configure(font="{Calibri} 12 {}")
        self.brand.place(anchor="nw", height=30, width=150, x=300, y=170)
        
        label_2 = tk.Label(self.BUY_ITEM_FRAME)
        label_2.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Description')
        label_2.place(height=20, width=75, x=50, y=220)
        
        self.description = tk.Text(self.BUY_ITEM_FRAME, name="description")
        self.description.configure(font="{Calibri} 12 {}")
        self.description.place(anchor="nw", height=75, width=400, x=50, y=240)
        
        label_3 = tk.Label(self.BUY_ITEM_FRAME)
        label_3.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Category *')
        label_3.place(height=20, width=70, x=50, y=80)
        label_4 = tk.Label(self.BUY_ITEM_FRAME)
        label_4.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Member *')
        label_4.place(height=20, width=65, x=300, y=80)
        label_5 = tk.Label(self.BUY_ITEM_FRAME)
        label_5.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Quantity *')
        label_5.place(height=20, width=65, x=50, y=335)
        label_6 = tk.Label(self.BUY_ITEM_FRAME)
        label_6.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Price *')
        label_6.place(height=20, width=40, x=300, y=335)
        self.quantity = tk.Spinbox(self.BUY_ITEM_FRAME, name="quantity")
        self.quantity.configure(font="{Calibri} 12 {}")
        self.quantity.place(anchor="nw", height=30, width=70, x=50, y=355)
        self.unit = ttk.Combobox(self.BUY_ITEM_FRAME, name="unit")
        self.unit.configure(state="readonly")
        self.unit.place(anchor="nw", height=30, width=80, x=125, y=355)
        self.price = tk.Entry(self.BUY_ITEM_FRAME, name="price")
        self.price.configure(font="{Calibri} 12 {}")
        self.price.place(anchor="nw", height=30, width=150, x=300, y=355)
        label_7 = tk.Label(self.BUY_ITEM_FRAME)
        label_7.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Purches Date *')
        label_7.place(height=20, width=90, x=50, y=405)
        label_9 = tk.Label(self.BUY_ITEM_FRAME)
        label_9.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Exp. Date')
        label_9.place(height=20, width=60, x=300, y=405)
        self.label_ = tk.Label(self.BUY_ITEM_FRAME, name="label_")
        self.label_.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Shop Name')
        self.label_.place(height=20, width=75, x=50, y=475)
        self.label_10 = tk.Label(self.BUY_ITEM_FRAME, name="label_10")
        self.label_10.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Discount')
        self.label_10.place(height=20, width=60, x=300, y=475)
        self.shop = tk.Entry(self.BUY_ITEM_FRAME, name="shop")
        self.shop.configure(font="{Calibri} 12 {}")
        self.shop.place(anchor="nw", height=30, width=150, x=50, y=495)
        self.discount = tk.Entry(self.BUY_ITEM_FRAME, name="discount")
        self.discount.configure(font="{Calibri} 12 {}")
        self.discount.place(anchor="nw", height=30, width=150, x=300, y=495)
        self.login_button = tk.Button(self.BUY_ITEM_FRAME, name="login_button")
        self.login_button.configure(
            background="#515DEF",
            borderwidth=0,
            compound="top",
            cursor="hand2",
            default="active",
            font="{Calibri} 16 {bold}",
            foreground="#ffffff",
            text='Buy')
        self.login_button.place(anchor="nw", height=40, width=400, x=50, y=565)
        label_11 = tk.Label(self.BUY_ITEM_FRAME)
        label_11.configure(
            background="#ffffff",
            font="{Calibri} 12 {bold underline}",
            text='Buy Item')
        label_11.place(height=20, width=70, x=216, y=5)
        self.purchse_date = DateEntry(self.BUY_ITEM_FRAME, name="purchse_date")
        self.purchse_date.configure(
            date_pattern="yyyy/mm/dd",
            font="{Calibri} 12 {}")
        self.purchse_date.place(anchor="nw", height=30, width=150, x=50, y=425)
        self.exp_date = DateEntry(self.BUY_ITEM_FRAME, name="exp_date")
        self.exp_date.configure(
            date_pattern="yyyy/mm/dd",
            font="{Calibri} 12 {}")
        self.exp_date.place(anchor="nw", height=30, width=150, x=300, y=425)
        self.BUY_ITEM_FRAME.place(
            anchor="nw", height=630, width=500, x=35, y=20)
        self.NEW_ITEM_FRAME = tk.Frame(
            self.BUYING_FRAME, name="new_item_frame")
        self.NEW_ITEM_FRAME.configure(
            background="#ffffff", height=200, width=200)
        label_12 = tk.Label(self.NEW_ITEM_FRAME)
        label_12.configure(
            background="#ffffff",
            font="{Calibri} 12 {bold underline}",
            text='New Item')
        label_12.place(height=20, width=70, x=240, y=5)
        label_13 = tk.Label(self.NEW_ITEM_FRAME)
        label_13.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Product Name *')
        label_13.place(height=20, width=100, x=25, y=80)
        self.newproduct = tk.Entry(self.NEW_ITEM_FRAME, name="newproduct")
        self.newproduct.configure(font="{Calibri} 12 {}")
        self.newproduct.place(
            anchor="nw",
            bordermode="outside",
            height=30,
            width=150,
            x=25,
            y=100)
        self.button_1 = tk.Button(self.NEW_ITEM_FRAME, name="button_1")
        self.button_1.configure(
            background="#515DEF",
            borderwidth=0,
            compound="top",
            cursor="hand2",
            default="active",
            font="{Calibri} 16 {bold}",
            foreground="#ffffff",
            text='Add')
        self.button_1.place(anchor="nw", height=30, width=300, x=100, y=270)
        label_14 = tk.Label(self.NEW_ITEM_FRAME)
        label_14.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Category *')
        label_14.place(height=20, width=70, x=325, y=80)
        self.new_category = ttk.Combobox(
            self.NEW_ITEM_FRAME, name="new_category")
        self.new_category.configure(state="readonly")
        self.new_category.place(
            anchor="nw",
            height=30,
            width=150,
            x=325,
            y=100)
        label_15 = tk.Label(self.NEW_ITEM_FRAME)
        label_15.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Description  ')
        label_15.place(height=20, width=80, x=25, y=150)
        self.new_discription = tk.Text(
            self.NEW_ITEM_FRAME, name="new_discription")
        self.new_discription.configure(height=10, width=50)
        self.new_discription.place(
            anchor="nw", height=75, width=450, x=25, y=170)
        self.NEW_ITEM_FRAME.place(
            anchor="nw", height=350, width=500, x=605, y=20)
        self.BUYING_FRAME.place(anchor="nw", height=670, width=1140, x=0, y=40)
        self.GROCERY_FRAME.place(
            anchor="nw",
            height=710,
            width=1140,
            x=230,
            y=40)

        # Main widget
        self.mainwindow = self.GROCERY_FRAME

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryApp(root)
    app.run()
