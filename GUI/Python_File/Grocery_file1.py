#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.editabletreeview import EditableTreeview
from tkcalendar.dateentry import DateEntry


class GroceryApp:

    #BUYING_FRAME
    def buying_frame_function(self) :
        self.BUYING_FRAME = tk.Frame(self.GROCERY_FRAME, name="buying_frame")
        self.BUYING_FRAME.configure(height=200, width=200)

        #BUY_ITEM_FRAME
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

        #NEW_ITEM_FRAME
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
        self.add_button = tk.Button(self.NEW_ITEM_FRAME, name="add_button")
        self.add_button.configure(
            background="#515DEF",
            borderwidth=0,
            compound="top",
            cursor="hand2",
            default="active",
            font="{Calibri} 16 {bold}",
            foreground="#ffffff",
            text='Add')
        self.add_button.place(anchor="nw", height=30, width=300, x=100, y=270)
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

    #INVENTORY_FRAME
    def inventory_frame_function(self):
        self.INVENTORY_FRAME = tk.Frame(
            self.GROCERY_FRAME, name="inventory_frame")
        self.INVENTORY_FRAME.configure(height=200, width=200)
        self.search_filter = tk.Entry(
            self.INVENTORY_FRAME, name="search_filter")
        self.search_filter.configure(font="{Calibri} 12 {}")
        self.search_filter.place(
            anchor="nw", height=30, width=140, x=30, y=100)
        self.category_filter = ttk.Combobox(
            self.INVENTORY_FRAME, name="category_filter")
        self.category_filter.configure(state="readonly")
        self.category_filter.place(
            anchor="nw", height=30, width=140, x=190, y=100)
        self.member_filter = ttk.Combobox(
            self.INVENTORY_FRAME, name="member_filter")
        self.member_filter.configure(state="readonly")
        self.member_filter.place(
            anchor="nw", height=30, width=140, x=350, y=100)
        self.quantity_filter = tk.Scale(
            self.INVENTORY_FRAME, name="quantity_filter")
        self.quantity_filter.configure(
            font="{Calibri} 12 {bold}",
            label='Quantity Used (%) :',
            orient="horizontal")
        self.quantity_filter.place(
            anchor="nw", height=70, width=140, x=510, y=68)
        self.date_filter = DateEntry(self.INVENTORY_FRAME, name="date_filter")
        self.date_filter.place(anchor="nw", height=30, width=140, x=670, y=100)
        self.exp_filter = DateEntry(self.INVENTORY_FRAME, name="exp_filter")
        self.exp_filter.place(anchor="nw", height=30, width=140, x=830, y=100)
        self.month_filter = ttk.Combobox(
            self.INVENTORY_FRAME, name="month_filter")
        self.month_filter.configure(state="readonly")
        self.month_filter.place(
            anchor="nw",
            height=30,
            width=120,
            x=990,
            y=100)
        label_33 = tk.Label(self.INVENTORY_FRAME)
        label_33.configure(font="{Calibri} 11 {bold}", text='Purchase Date :')
        label_33.place(height=20, width=100, x=670, y=78)
        label_34 = tk.Label(self.INVENTORY_FRAME)
        label_34.configure(font="{Calibri} 11 {bold}", text='Exp. Date :')
        label_34.place(height=20, width=100, x=830, y=78)
        self.table = EditableTreeview(self.INVENTORY_FRAME, name="table")
        self.table.configure(selectmode="extended")
        self.table.place(anchor="nw", height=450, width=1080, x=30, y=150)
        self.scrollbar = tk.Scrollbar(self.INVENTORY_FRAME, name="scrollbar")
        self.scrollbar.configure(orient="vertical")
        self.scrollbar.place(anchor="nw", height=450, x=1110, y=150)
        self.update_button = tk.Button(
            self.INVENTORY_FRAME, name="update_button")
        self.update_button.configure(
            background="#515DEF",
            borderwidth=0,
            compound="top",
            cursor="hand2",
            default="active",
            font="{Calibri} 16 {bold}",
            foreground="#ffffff",
            text='update',
            command=self.update_frame_function)
        self.update_button.place(
            anchor="nw", height=30, width=300, x=400, y=620)
        self.INVENTORY_FRAME.place(
            anchor="nw", height=670, width=1140, x=0, y=40)

        
    #UPDATE_FRAME
    def update_frame_function(self):
        self.UPDATE_FRAME = tk.Frame(self.GROCERY_FRAME, name="update_frame")
        self.UPDATE_FRAME.configure(height=200, width=200)
        self.UPDATE_ITEM_FRAME = tk.Frame(
            self.UPDATE_FRAME, name="update_item_frame")
        self.UPDATE_ITEM_FRAME.configure(
            background="#ffffff", height=550, width=550)
        self.update_name = ttk.Combobox(
            self.UPDATE_ITEM_FRAME, name="update_name")
        self.update_name.configure(state="readonly")
        self.update_name.place(anchor="nw", height=30, width=150, x=50, y=170)
        self.update_category = ttk.Combobox(
            self.UPDATE_ITEM_FRAME, name="update_category")
        self.update_category.configure(state="readonly")
        self.update_category.place(
            anchor="nw", height=30, width=150, x=50, y=100)
        self.update_member = ttk.Combobox(
            self.UPDATE_ITEM_FRAME, name="update_member")
        self.update_member.configure(state="readonly")
        self.update_member.place(
            anchor="nw", height=30, width=150, x=300, y=100)
        label_51 = tk.Label(self.UPDATE_ITEM_FRAME)
        label_51.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Product Name *')
        label_51.place(height=20, width=100, x=50, y=150)
        label_52 = tk.Label(self.UPDATE_ITEM_FRAME)
        label_52.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Brand')
        label_52.place(height=20, width=40, x=300, y=150)
        self.update_brand = tk.Entry(
            self.UPDATE_ITEM_FRAME, name="update_brand")
        self.update_brand.configure(font="{Calibri} 12 {}")
        self.update_brand.place(
            anchor="nw",
            height=30,
            width=150,
            x=300,
            y=170)
        label_53 = tk.Label(self.UPDATE_ITEM_FRAME)
        label_53.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Description')
        label_53.place(height=20, width=75, x=50, y=220)
        self.update_description = tk.Text(
            self.UPDATE_ITEM_FRAME, name="update_description")
        self.update_description.configure(font="{Calibri} 12 {}")
        self.update_description.place(
            anchor="nw", height=75, width=400, x=50, y=240)
        label_54 = tk.Label(self.UPDATE_ITEM_FRAME)
        label_54.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Category *')
        label_54.place(height=20, width=70, x=50, y=80)
        label_55 = tk.Label(self.UPDATE_ITEM_FRAME)
        label_55.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Member *')
        label_55.place(height=20, width=65, x=300, y=80)
        label_56 = tk.Label(self.UPDATE_ITEM_FRAME)
        label_56.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Quantity *')
        label_56.place(height=20, width=65, x=50, y=335)
        label_57 = tk.Label(self.UPDATE_ITEM_FRAME)
        label_57.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Price *')
        label_57.place(height=20, width=40, x=390, y=335)
        self.update_quantity = tk.Spinbox(
            self.UPDATE_ITEM_FRAME, name="update_quantity")
        self.update_quantity.configure(font="{Calibri} 12 {}")
        self.update_quantity.place(
            anchor="nw", height=30, width=70, x=50, y=355)
        self.update_unit = ttk.Combobox(
            self.UPDATE_ITEM_FRAME, name="update_unit")
        self.update_unit.configure(state="readonly")
        self.update_unit.place(anchor="nw", height=30, width=80, x=300, y=355)
        self.update_price = tk.Entry(
            self.UPDATE_ITEM_FRAME, name="update_price")
        self.update_price.configure(font="{Calibri} 12 {}")
        self.update_price.place(anchor="nw", height=30, width=70, x=380, y=355)
        label_58 = tk.Label(self.UPDATE_ITEM_FRAME)
        label_58.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Purches Date *')
        label_58.place(height=20, width=90, x=50, y=405)
        label_59 = tk.Label(self.UPDATE_ITEM_FRAME)
        label_59.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Exp. Date')
        label_59.place(height=20, width=60, x=300, y=405)
        self.label_60 = tk.Label(self.UPDATE_ITEM_FRAME, name="label_60")
        self.label_60.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Shop Name')
        self.label_60.place(height=20, width=75, x=50, y=475)
        self.label_61 = tk.Label(self.UPDATE_ITEM_FRAME, name="label_61")
        self.label_61.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Discount')
        self.label_61.place(height=20, width=60, x=300, y=475)
        self.update_shop = tk.Entry(self.UPDATE_ITEM_FRAME, name="update_shop")
        self.update_shop.configure(font="{Calibri} 12 {}")
        self.update_shop.place(anchor="nw", height=30, width=150, x=50, y=495)
        self.update_discount = tk.Entry(
            self.UPDATE_ITEM_FRAME, name="update_discount")
        self.update_discount.configure(font="{Calibri} 12 {}")
        self.update_discount.place(
            anchor="nw", height=30, width=150, x=300, y=495)
        self.update_update_button = tk.Button(
            self.UPDATE_ITEM_FRAME, name="update_update_button")
        self.update_update_button.configure(
            background="#515DEF",
            borderwidth=0,
            compound="top",
            cursor="hand2",
            default="active",
            font="{Calibri} 16 {bold}",
            foreground="#ffffff",
            text='Update')
        self.update_update_button.place(
            anchor="nw", height=40, width=400, x=50, y=565)
        label_62 = tk.Label(self.UPDATE_ITEM_FRAME)
        label_62.configure(
            background="#ffffff",
            font="{Calibri} 12 {bold underline}",
            text='Update Item')
        label_62.place(height=20, width=90, x=216, y=5)
        self.update_purchse = DateEntry(
            self.UPDATE_ITEM_FRAME, name="update_purchse")
        self.update_purchse.configure(
            date_pattern="yyyy/mm/dd",
            font="{Calibri} 12 {}")
        self.update_purchse.place(
            anchor="nw", height=30, width=150, x=50, y=425)
        self.update_exp = DateEntry(self.UPDATE_ITEM_FRAME, name="update_exp")
        self.update_exp.configure(
            date_pattern="yyyy/mm/dd",
            font="{Calibri} 12 {}")
        self.update_exp.place(anchor="nw", height=30, width=150, x=300, y=425)
        label_67 = tk.Label(self.UPDATE_ITEM_FRAME)
        label_67.configure(
            background="#ffffff",
            font="{Calibri} 11 {bold}",
            text='Quantity Left *')
        label_67.place(height=20, width=90, x=125, y=335)
        self.update_quantity_left = tk.update_quantity_left(self.UPDATE_ITEM_FRAME, name="spinbox_4")
        self.update_quantity_left.configure(font="{Calibri} 12 {}")
        self.update_quantity_left.place(anchor="nw", height=30, width=70, x=125, y=355)
        self.UPDATE_ITEM_FRAME.place(
            anchor="nw", height=630, width=500, x=35, y=20)
        self.UPDATE_FRAME.place(anchor="nw", height=670, width=1140, x=0, y=40)
        
        
    def __init__(self, master=None):
        # build ui
        self.GROCERY_FRAME = tk.Frame(master, name="grocery_frame")
        self.GROCERY_FRAME.configure(
            background="#515DEF", height=710, width=1140)
        
        #Button
        self.buy_button = tk.Button(self.GROCERY_FRAME, name="buy_button")
        self.buy_button.configure(
            background="#515DEF",
            borderwidth=0,
            compound="top",
            cursor="hand2",
            font="{Cambria} 16 {bold}",
            foreground="#ffffff",
            relief="flat",
            text='Buy',
            command=self.buying_frame_function)
        self.buy_button.place(
            anchor="nw",
            bordermode="ignore",
            height=30,
            width=60,
            x=100,
            y=5)

        #Button
        self.inventory_button = tk.Button(
            self.GROCERY_FRAME, name="inventory_button")
        self.inventory_button.configure(
            background="#515DEF",
            borderwidth=0,
            compound="top",
            cursor="hand2",
            font="{Cambria} 16 {bold}",
            foreground="#ffffff",
            relief="flat",
            text='Inventory',
            command=self.inventory_frame_function)
        self.inventory_button.place(
            anchor="nw",
            bordermode="ignore",
            height=30,
            width=100,
            x=250,
            y=5)
        
        #Button
        self.shopping_button = tk.Button(
            self.GROCERY_FRAME, name="shopping_button")
        self.shopping_button.configure(
            background="#515DEF",
            borderwidth=0,
            compound="top",
            cursor="hand2",
            font="{Cambria} 16 {bold}",
            foreground="#ffffff",
            relief="flat",
            text='Shopping')
        self.shopping_button.place(
            anchor="nw",
            bordermode="ignore",
            height=30,
            width=100,
            x=440,
            y=5)

        #Button
        self.expense_button = tk.Button(
            self.GROCERY_FRAME, name="expense_button")
        self.expense_button.configure(
            background="#515DEF",
            borderwidth=0,
            compound="top",
            cursor="hand2",
            font="{Cambria} 16 {bold}",
            foreground="#ffffff",
            relief="flat",
            text='Expense')
        self.expense_button.place(
            anchor="nw",
            bordermode="ignore",
            height=30,
            width=100,
            x=630,
            y=5)


        self.buying_frame_function()
        self.GROCERY_FRAME.place(anchor="nw", height=710, width=1140, x=230, y=40)

        # Main widget
        self.mainwindow = self.GROCERY_FRAME

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryApp(root)
    app.run()
