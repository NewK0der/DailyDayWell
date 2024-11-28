#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class BuyItemFrameApp:
    def __init__(self, master=None):
        # build ui
        self.BUY_ITEM_FRAME = tk.Frame(GROCERY_FRAME, name="buy_item_frame")
        self.BUY_ITEM_FRAME.configure(
            background="#ffffff", height=550, width=500)
        combobox_1 = ttk.Combobox(self.BUY_ITEM_FRAME)
        combobox_1.configure(state="readonly")
        combobox_1.place(anchor="nw", height=30, width=150, x=50, y=70)
        self.categoty = ttk.Combobox(self.BUY_ITEM_FRAME, name="categoty")
        self.categoty.configure(state="readonly")
        self.categoty.place(anchor="nw", height=30, width=150, x=50, y=255)
        self.member = ttk.Combobox(self.BUY_ITEM_FRAME, name="member")
        self.member.configure(state="readonly")
        self.member.place(anchor="nw", height=30, width=150, x=300, y=255)
        label_8 = tk.Label(self.BUY_ITEM_FRAME)
        label_8.configure(
            background="#ffffff",
            borderwidth=0,
            font="{Calibri} 11 {bold}",
            text='Product Name *')
        label_8.place(height=20, width=100, x=50, y=50)
        label_1 = tk.Label(self.BUY_ITEM_FRAME)
        label_1.configure(
            background="#ffffff",
            borderwidth=0,
            font="{Calibri} 11 {bold}",
            text='Brand')
        label_1.place(height=20, width=40, x=300, y=50)
        self.brand = tk.Entry(self.BUY_ITEM_FRAME, name="brand")
        self.brand.configure(font="{Calibri} 12 {}", selectborderwidth=5)
        self.brand.place(
            anchor="nw",
            bordermode="outside",
            height=30,
            width=150,
            x=300,
            y=70)
        label_2 = tk.Label(self.BUY_ITEM_FRAME)
        label_2.configure(
            background="#ffffff",
            borderwidth=0,
            font="{Calibri} 11 {bold}",
            text='Description')
        label_2.place(height=20, width=75, x=50, y=120)
        self.description = tk.Text(self.BUY_ITEM_FRAME, name="description")
        self.description.configure(height=10, width=50)
        self.description.place(anchor="nw", height=75, width=400, x=50, y=140)
        label_3 = tk.Label(self.BUY_ITEM_FRAME)
        label_3.configure(
            background="#ffffff",
            borderwidth=0,
            font="{Calibri} 11 {bold}",
            text='Category *')
        label_3.place(height=20, width=70, x=50, y=235)
        label_4 = tk.Label(self.BUY_ITEM_FRAME)
        label_4.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Member *')
        label_4.place(height=20, width=65, x=300, y=235)
        label_5 = tk.Label(self.BUY_ITEM_FRAME)
        label_5.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Quantity *')
        label_5.place(height=20, width=65, x=50, y=305)
        label_6 = tk.Label(self.BUY_ITEM_FRAME)
        label_6.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Price *')
        label_6.place(height=20, width=40, x=300, y=305)
        self.quantity = tk.Spinbox(self.BUY_ITEM_FRAME, name="quantity")
        self.quantity.configure(font="{Calibri} 12 {}")
        self.quantity.place(anchor="nw", height=30, width=70, x=50, y=325)
        self.unit = ttk.Combobox(self.BUY_ITEM_FRAME, name="unit")
        self.unit.configure(state="readonly")
        self.unit.place(anchor="nw", height=30, width=80, x=125, y=325)
        self.price = tk.Entry(self.BUY_ITEM_FRAME, name="price")
        self.price.configure(font="{Calibri} 12 {}")
        self.price.place(
            anchor="nw",
            bordermode="outside",
            height=30,
            width=150,
            x=300,
            y=325)
        label_7 = tk.Label(self.BUY_ITEM_FRAME)
        label_7.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Purches Date *')
        label_7.place(height=20, width=90, x=50, y=375)
        label_9 = tk.Label(self.BUY_ITEM_FRAME)
        label_9.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Exp. Date')
        label_9.place(height=20, width=60, x=300, y=375)
        self.exp = tk.Entry(self.BUY_ITEM_FRAME, name="exp")
        self.exp.configure(
            borderwidth=1,
            font="{Calibri} 12 {}",
            selectborderwidth=5)
        self.exp.place(
            anchor="nw",
            bordermode="outside",
            height=30,
            width=150,
            x=300,
            y=395)
        self.purchesdate = tk.Entry(self.BUY_ITEM_FRAME, name="purchesdate")
        self.purchesdate.configure(font="{Calibri} 12 {}")
        self.purchesdate.place(
            anchor="nw",
            bordermode="outside",
            height=30,
            width=150,
            x=50,
            y=395)
        self.label_ = tk.Label(self.BUY_ITEM_FRAME, name="label_")
        self.label_.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Shop Name')
        self.label_.place(height=20, width=75, x=50, y=445)
        self.label_10 = tk.Label(self.BUY_ITEM_FRAME, name="label_10")
        self.label_10.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Discount')
        self.label_10.place(height=20, width=60, x=300, y=445)
        self.shop = tk.Entry(self.BUY_ITEM_FRAME, name="shop")
        self.shop.configure(
            borderwidth=1,
            font="{Calibri} 12 {}",
            selectborderwidth=5)
        self.shop.place(
            anchor="nw",
            bordermode="outside",
            height=30,
            width=150,
            x=50,
            y=465)
        self.discount = tk.Entry(self.BUY_ITEM_FRAME, name="discount")
        self.discount.configure(font="{Calibri} 12 {}")
        self.discount.place(
            anchor="nw",
            bordermode="outside",
            height=30,
            width=150,
            x=300,
            y=465)
        self.BUY_ITEM_FRAME.place(
            anchor="nw", height=550, width=500, x=25, y=25)

        # Main widget
        self.mainwindow = self.BUY_ITEM_FRAME

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = BuyItemFrameApp(root)
    app.run()
