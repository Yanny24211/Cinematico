from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Separator

from API.query_1 import query_1
from API.query_2 import query_2
from API.query_3 import query_3
from API.query_4 import query_4
from API.query_5 import query_5
from API.view1 import view1
from API.view2 import view2
from API.view3 import view3

class query_menu_frame(Frame):

    def make_table(self, data, container):
        print("container: ",  container, "data: ", data)
        for widget in container.winfo_children():
            widget.destroy()

        for i in range(len(data[0])):
            e = Entry(container,fg='black', bg='#A4161A', bd = 2,font=('Bebas Neue',16,'bold'))
            e.grid(row=0, column=i)
            e.insert(END, data[0][i])
            e.config(state='disabled', disabledbackground='#A4161A', disabledforeground='black')

        for i in range(len(data[1])):
            for j in range(len(data[1][0])):
                e = Entry(container,fg='black',bg='#D3D3D3', bd = 2, width=20, font=('Bebas Neue',16))
                e.grid(row=(i+1), column=j)
                e.insert(END, data[1][i][j])
                e.config(state='disabled', disabledbackground='#D3D3D3', disabledforeground='black')
        
        container.pack(anchor='n',side=TOP, pady=50)

    def query_one(self, parent):
        ret = query_1().run()
        if isinstance(ret, str):
            messagebox.showerror("American Directors", ret)
            return
        self.make_table(ret, parent)
    
    def query_two(self, parent):
        ret = query_2().run()
        if isinstance(ret, str):
            messagebox.showerror("Movies Ordered by Release Date", ret)
            return
        self.make_table(ret, parent)

    def query_three(self, parent):
        ret = query_3().run()
        if isinstance(ret, str):
            messagebox.showerror("Average Rating of Each Genre", ret)
            return
        self.make_table(ret, parent)

    def query_four(self, parent):
        ret = query_4().run()
        if isinstance(ret, str):
            messagebox.showerror("Movies Bought By Customers", ret)
            return
        self.make_table(ret, parent)

    def query_five(self, parent):
        ret = query_5().run()
        if isinstance(ret, str):
            messagebox.showerror("Total Spent By Customers", ret)
            return
        self.make_table(ret, parent)

    def view_one(self, parent):
        ret = view1().run()
        if isinstance(ret, str):
            messagebox.showerror("Total Spent By Customers", ret)
            return
        self.make_table(ret, parent)
    
    def view_two(self, parent):
        ret = view2().run()
        if isinstance(ret, str):
            messagebox.showerror("Total Spent By Customers", ret)
            return
        self.make_table(ret, parent)

    def view_three(self, parent):
        ret = view3().run()
        if isinstance(ret, str):
            messagebox.showerror("Total Spent By Customers", ret)
            return
        self.make_table(ret, parent)



    def __init__(self, parent):
        button_style = {
            'bg': '#A4161A',  # Background color
            'fg': '#D3D3D3',    # Foreground color (text color)
            'font': ("Bebas Neue", 10, "bold"),  # Font style and size
            'padx': 7,       # Horizontal padding
            'pady': 5         # Vertical padding
        }
        Frame.__init__(self, parent.main, name="query_menu")
        self.config(width=1280, height=720)
        self.parent = parent
        self.pack_propagate(False)

        logout = Button(self, text="Main Menu", command=lambda: parent.switchFrame("main_menu"), **button_style)
        logout.pack(anchor='ne',side=TOP)

        heading = Label(self, text="Query Menu\n\n", font=("Bebas Neue", 40, "bold"), pady=10, bg="#292b2b", fg="#D3D3D3")
        heading.pack(anchor='n',side=TOP)

        tableContainer = Frame(self)

        nav = Frame(self)

        q1 = Button(nav, text="American Directors", command=lambda: self.query_one(tableContainer), **button_style)
        q1.grid(column=0,row=0,sticky="ew")

        q2 = Button(nav, text="Movies Ordered by Release Date", command=lambda: self.query_two(tableContainer), **button_style)
        q2.grid(column=1,row=0,sticky="ew")

        q3 = Button(nav, text="Average Rating of Each Genre", command=lambda: self.query_three(tableContainer), **button_style)
        q3.grid(column=2,row=0,sticky="ew")

        q4 = Button(nav, text="Movies Bought By Customers", command=lambda: self.query_four(tableContainer), **button_style)
        q4.grid(column=3,row=0,sticky="ew")

        q5 = Button(nav, text="Total Spent By Customers", command=lambda: self.query_five(tableContainer), **button_style)
        q5.grid(column=0,row=1,sticky="ew")

        v1 = Button(nav, text="General Movie Data", command=lambda: self.view_one(tableContainer), **button_style)
        v1.grid(column=1,row=1,sticky="ew")

        v2 = Button(nav, text="Best Rated Movies", command=lambda: self.view_two(tableContainer), **button_style)
        v2.grid(column=2,row=1,sticky="ew")

        v3 = Button(nav, text="User Status", command=lambda: self.view_three(tableContainer), **button_style)
        v3.grid(column=3,row=1,sticky="ew")

        nav.pack(anchor='n',side=TOP)

        customContainer = Frame(self)

        customContainer.pack(anchor='n',side=TOP)