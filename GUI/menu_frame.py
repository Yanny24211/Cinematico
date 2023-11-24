from tkinter import *
from tkinter import messagebox

from API.create_tables import create_tables
from API.create_views import create_views
from API.drop_tables import drop_tables
from API.drop_views import drop_views
from API.populate_tables import populate_tables

class main_menu_frame(Frame):

    def create_tables(self):
        ret = create_tables().run()
        if not ret.startswith('Error'):
            messagebox.showinfo("Create Tables", ret)
        else:
            messagebox.showerror("Create Tables", ret)

    def create_views(self):
        ret = create_views().run()
        if not ret.startswith('Error'):
            messagebox.showinfo("Create Views", ret)
        else:
            messagebox.showerror("Create Views", ret)

    def drop_tables(self):
        ret = drop_tables().run()
        if not ret.startswith('Error'):
            messagebox.showinfo("Drop Tables", ret)
        else:
            messagebox.showerror("Drop Tables", ret)

    def drop_views(self):
        ret = drop_views().run()
        if not ret.startswith('Error'):
            messagebox.showinfo("Drop Views", ret)
        else:
            messagebox.showerror("Drop Views", ret)

    def populate_tables(self):
        ret = populate_tables().run()
        if not ret.startswith('Error'):
            messagebox.showinfo("Populate Tables", ret)
        else:
            messagebox.showerror("Populate Tables", ret)

    def __init__(self, parent):
        Frame.__init__(self, parent.main, name="main_menu")
        self.config(width=1280, height=720)
        self.parent = parent

        button_style = {
            'bg': '#A4161A',  # Background color
            'fg': '#D3D3D3',    # Foreground color (text color)
            'font': ("Bebas Neue", 15, "bold"),  # Font style and size
            'padx': 10,       # Horizontal padding
            'pady': 5         # Vertical padding
        }

        choices = Frame(self)
        choices.configure(bg="#292b2b")
        choices.pack()

        heading = Label(choices, text="Cinematico Movie Store\n\n", font=("Bebas Neue", 40, "bold"), pady=10, bg="#292b2b", fg="#D3D3D3")
        heading.pack(side=TOP)

        # subheading = Label(choices, text="Actions\n", font=("Bebas Neue", 15, "bold"), bg="#292b2b", fg="#D3D3D3")
        # subheading.pack(side=TOP)

        ct = Button(choices, text="Create Tables", command=lambda: self.create_tables(), **button_style)
        ct.pack(side=LEFT)

        cv = Button(choices, text="Create Views", command=lambda: self.create_views(), **button_style)
        cv.pack(side=LEFT)

        dt = Button(choices, text="Drop Tables", command=lambda: self.drop_tables(), **button_style)
        dt.pack(side=LEFT)

        dv = Button(choices, text="Drop Views", command=lambda: self.drop_views(), **button_style)
        dv.pack(side=LEFT)

        pt = Button(choices, text="Populate Tables", command=lambda: self.populate_tables(), **button_style)
        pt.pack(side=LEFT)

        buttonQ = Button(choices, text="Queries", command=lambda: parent.switchFrame("query_menu"), **button_style)
        buttonQ.pack(side=LEFT)

        choices.place(relx=0.5, rely=0.33, anchor="center")