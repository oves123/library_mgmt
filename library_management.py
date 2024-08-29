from tkinter import *
from tkinter import Menu
from tkinter import messagebox
from time import strftime
from tkcalendar import DateEntry
from tkinter import ttk
import datetime as dt
import mysql.connector


my_db = mysql.connector.connect(host="localhost", user="root", password="400102", database="library")
my_cursor = my_db.cursor()
class library_management:
    def login_page(self):
        self.l_title = Label(window, text=" LIBRARY MANAGEMENT", bg="#b09be8", padx=2, pady=6,
                             font=("arial black", 18, "italic"), relief=RIDGE, fg="#f21d0a")
        self.l_title.pack(side=TOP, fill=X)
        self.u_name = Label(window, text="Username", bg="#bcd2f5", font=("arial black", 12), fg="#ed0763")
        self.u_name.place(x=90, y=70)
        self.u_name_e = Entry(window, width=30)
        self.u_name_e.place(x=210, y=75)
        self.password = Label(window, text="Password", bg="#bcd2f5", font=("arial black", 12), fg="#ed0763")
        self.password.place(x=90, y=130)
        self.password_e = Entry(window, width=30, show="*")
        self.password_e.place(x=210, y=134)
        self.show_pass = Button(window, text="Show", command=self.show)
        self.show_pass.place(x=420, y=134)
        self.creat_ac_btn = Button(window, text="Create Account", bg="#e2f095", fg="#0505fa", command=self.create_account)
        self.creat_ac_btn.place(x=100, y=200)
        self.f_password_btn = Button(window, text="Forgot Password ?", bg="#e2f095", fg="#0505fa", command=self.forgot_password)
        self.f_password_btn.place(x=300, y=199)
        self.next_btn = Button(window, text="Login", bg="#f4c5fa", fg="#fc030f", command=self.library)
        self.next_btn.place(x=230, y=199)


    def library(self):
        c_username = self.u_name_e.get()
        c_password = self.password_e.get()
        sql = "select * from create_ac_data where c_username = %s and c_password = %s"
        my_cursor.execute(sql, [(c_username), (c_password)])
        result3 = my_cursor.fetchall()
        if self.u_name_e.get() == "" or self.password_e.get() == "":
            messagebox.showwarning("Login", "Please Enter Username And Password")
        elif result3:
            self.window3 = Toplevel()
            self.window3.title("Library Management")
            self.window3.geometry("1368x768+0+0")
            self.window3.config(bg="#f3ffbf")
            menubar = Menu(self.window3)
            self.window3.config(menu=menubar)
            file_menu = Menu(menubar, tearoff=0)
            file_menu.add_separator()
            sub_menu1 = Menu(file_menu, tearoff=0)
            sub_menu1.add_command(label='All Books', command=self.all_book)
            sub_menu1.add_command(label='Search Book', command=self.search_book)
            sub_menu1.add_command(label='Insert Book', command=self.insert_book)
            sub_menu1.add_command(label='Update Book', command=self.update_book)
            sub_menu1.add_command(label='Delete Book', command=self.delete_book)
            sub_menu = Menu(file_menu, tearoff=0)
            sub_menu.add_command(label='Search Student Detail', command=self.search_student)
            sub_menu.add_command(label='Update Student Record', command=self.update_student_record)
            sub_menu.add_command(label='Delete Student Record', command=self.delete_student_record)
            sub_menu.add_command(label='Show All Student Record', command=self.all_student)
            file_menu.add_cascade(label="Student", menu=sub_menu)
            file_menu.add_cascade(label="Book", menu=sub_menu1)
            file_menu.add_cascade(label="Add Book", command=self.i_b)
            file_menu.add_cascade(label="Book Issue", command=self.book_issue)
            file_menu.add_separator()
            file_menu.add_command(label='Exit', command=self.window3.destroy)
            file_menu.add_separator()
            menubar.add_cascade(label="View", menu=file_menu, underline=0)
            self.lib_title = Label(self.window3, text=" LIBRARY MANAGEMENT", bg="#df9eff", padx=2, pady=6,
                             font=("arial black", 18, "bold"), relief=RIDGE, fg="#ad2d45")

            self.t = Label(self.lib_title, font=('calibri', 20, 'bold'), background='#000000', foreground='#26ff00', height=1)
            string = strftime('%H:%M:%S %p')
            self.t.config(text=string)
            self.t.after(1000)
            self.t.place(x=10, y=3)

            date = dt.datetime.now()
            label = Label(self.lib_title, text=f"{date:%A, %B %d, %Y}", font=('calibri', 20, 'bold'), background='#000000', foreground='#26ff00', height=1)
            label.place(x=1000, y=3)
            self.lib_title.pack(side=TOP, fill=X)

            self.student1 = Label(self.window3, text="Student Detail", font=('calibri', 20, 'bold'), bg="#f3ffbf", fg="red")
            self.student1.place(x=600, y=55)
            self.student_dt = LabelFrame(self.window3, text="Student Detail", width=700, height=210, bg="#95c9c9", relief=RIDGE, bd=10)
            self.student_dt.place(x=350, y=100)
            self.student_f_name = Label(self.student_dt, text="First Name", bg="#5e8a5e")
            self.student_f_name.place(x=30, y=10)
            self.student_f_name_e = Entry(self.student_dt)
            self.student_f_name_e.place(x=140, y=10)
            self.student_l_n = Label(self.student_dt, text="Last Name", bg="#5e8a5e")
            self.student_l_n.place(x=410, y=10)
            self.student_l_n_e = Entry(self.student_dt)
            self.student_l_n_e.place(x=520, y=10)
            self.student_father_name = Label(self.student_dt, text="Father Name", bg="#5e8a5e")
            self.student_father_name.place(x=30, y=40)
            self.student_father_name_e = Entry(self.student_dt)
            self.student_father_name_e.place(x=140, y=40)
            self.student_mother_name = Label(self.student_dt, text="Mother Name", bg="#5e8a5e")
            self.student_mother_name.place(x=410, y=40)
            self.student_mother_name_e = Entry(self.student_dt)
            self.student_mother_name_e.place(x=520, y=40)
            self.student_name = Label(self.student_dt, text="Student Name", bg="#5e8a5e")
            self.student_name.place(x=30, y=70)
            self.student_name_e = Entry(self.student_dt)
            self.student_name_e.place(x=140, y=70)
            self.std = Label(self.student_dt, text="Standard", bg="#5e8a5e")
            self.std.place(x=410, y=70)
            self.std_e = Entry(self.student_dt)
            self.std_e.place(x=520, y=70)
            self.roll_no = Label(self.student_dt, text="Roll No", bg="#5e8a5e")
            self.roll_no.place(x=30, y=100)
            self.roll_no_e = Entry(self.student_dt)
            self.roll_no_e.place(x=140, y=100)
            self.teacher_name = Label(self.student_dt, text="Teacher Name", bg="#5e8a5e")
            self.teacher_name.place(x=410, y=100)
            self.teacher_name_e = Entry(self.student_dt)
            self.teacher_name_e.place(x=520, y=100)
            self.age = Label(self.student_dt, text="Age", bg="#5e8a5e")
            self.age.place(x=30, y=130)
            n = StringVar()
            self.agechoosen = ttk.Combobox(self.student_dt, width=10, textvariable=n)
            self.agechoosen['values'] = (' 7',
                                      ' 8',
                                      ' 9',
                                      ' 10',
                                      ' 11',
                                      ' 12',
                                      ' 13',
                                      ' 14',
                                      ' 15',
                                      ' 16',
                                      ' 17',
                                      ' 18')

            self.agechoosen.place(x=140, y=130)
            self.agechoosen.current(3)
            self.parents_no = Label(self.student_dt,  text="Parents Mobile No", bg="#5e8a5e")
            self.parents_no.place(x=410, y=135)
            self.parents_no_e = Entry(self.student_dt)
            self.parents_no_e.place(x=520, y=135)

            self.frame = Frame(self.window3, bd=10, bg="#ffebb5", width=1350, height=50, relief=SUNKEN)
            self.frame.place(x=0, y=330)
            self.submit_btn = Button(self.frame, text="Submit", bg="#fbff80", command=self.submit_btn1, relief=RIDGE, padx=3, bd=5)
            self.submit_btn.place(x=170, y=2)
            self.update_btn = Button(self.frame, text="Update", bg="#fbff80", command=self.update_student_record, relief=RIDGE, padx=3, bd=5)
            self.update_btn.place(x=500, y=2)
            self.delete_btn = Button(self.frame, text="Delete", bg="#fbff80", command=self.delete_student_record, relief=RIDGE, padx=3, bd=5)
            self.delete_btn.place(x=800, y=2)
            self.cabtn = Button(self.frame, text="Cancel", bg="#fbff80", command=self.canbtn, relief=RIDGE, padx=3, bd=5)
            self.cabtn.place(x=1100, y=2)
            self.refresh_btn = Button(self.window3, text="Refresh", bg="#fbff80", command=self.ref, relief=RIDGE, padx=3, bd=5)
            self.refresh_btn.place(x=1250, y=60)

        #
            self.student_details_label = Label(self.window3, text="Student Details", fg="red", font=('calibri', 20, 'bold'), bg="#f3ffbf")
            self.student_details_label.place(x=600, y=390)
            self.student_tabel = ttk.Treeview(self.window3)
            self.student_tabel['columns'] = (
                'fname', "lname", 'faname', 'moname', 'age', "panumber", "stuname", "rollno", "standard", "teachername")
            style = ttk.Style(self.window3)
            style.theme_use("clam")
            style.configure("Treeview.Heading", background="black", foreground="#22ff00")
            style.configure("Treeview", background="#bed1bf", foreground="#000000")
            #
            self.student_tabel.column("#0", width=0, stretch=NO)
            self.student_tabel.column("fname", anchor=CENTER, width=90)
            self.student_tabel.column("lname", anchor=CENTER, width=90)
            self.student_tabel.column("faname", anchor=CENTER, width=90)
            self.student_tabel.column("moname", anchor=CENTER, width=90)
            self.student_tabel.column("age", anchor=CENTER, width=90)
            self.student_tabel.column("panumber", anchor=CENTER, width=150)
            self.student_tabel.column("stuname", anchor=CENTER, width=90)
            self.student_tabel.column("rollno", anchor=CENTER, width=90)
            self.student_tabel.column("standard", anchor=CENTER, width=90)
            self.student_tabel.column("teachername", anchor=CENTER, width=120)
            #
            self.student_tabel.heading("#0", text="", anchor=CENTER)
            self.student_tabel.heading("fname", text="First Name", anchor=CENTER)
            self.student_tabel.heading("lname", text="Last Name", anchor=CENTER)
            self.student_tabel.heading("faname", text="Father Name", anchor=CENTER)
            self.student_tabel.heading("moname", text="Mother Name", anchor=CENTER)
            self.student_tabel.heading("age", text="Age", anchor=CENTER)
            self.student_tabel.heading("panumber", text="Parents Mobile No", anchor=CENTER)
            self.student_tabel.heading("stuname", text="Student Name", anchor=CENTER)
            self.student_tabel.heading("rollno", text="Roll No", anchor=CENTER)
            self.student_tabel.heading("standard", text="Standard", anchor=CENTER)
            self.student_tabel.heading("teachername", text="Teacher Name", anchor=CENTER)
            query = "select * from student_detail1"
            my_cursor.execute(query)
            data = my_cursor.fetchall()
            for i in data:
                self.student_tabel.insert("", 'end', iid=i[0], values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
            self.student_tabel.place(x=185, y=430)
            self.add_book_w = Button(self.window3, text="Add Book > ", bg="#fbff80", command=self.i_b, relief=RIDGE, padx=3, bd=5)
            self.add_book_w.place(x=1200, y=620)
            self.add_book_w = Button(self.window3, text="Book Issue >", bg="#fbff80", command=self.book_issue, relief=RIDGE,
                                     padx=3, bd=5)
            self.add_book_w.place(x=1200, y=580)
        else:
            messagebox.showerror("Something Went Wrong", "Please Enter Correct Username And Password")

        self.u_name_e.delete(0, "end")
        self.password_e.delete(0, "end")

        # window.destroy()
    def book_issue(self):
        self.book_i = Toplevel()
        self.book_i.title("Book Issue")
        self.book_i.geometry("1368x768+0+0")
        self.book_i.config(bg="#ffccc7")
        menubar = Menu(self.book_i)
        self.book_i.config(menu=menubar)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_separator()
        sub_menu1 = Menu(file_menu, tearoff=0)
        sub_menu1.add_command(label='All Books', command=self.all_book)
        sub_menu1.add_command(label='Search Book', command=self.search_book)
        sub_menu1.add_command(label='Insert Book', command=self.insert_book)
        sub_menu1.add_command(label='Update Book', command=self.update_book)
        sub_menu1.add_command(label='Delete Book', command=self.delete_book)
        sub_menu = Menu(file_menu, tearoff=0)
        sub_menu.add_command(label='Search Student Detail', command=self.search_student)
        sub_menu.add_command(label='Update Student Record', command=self.update_student_record)
        sub_menu.add_command(label='Delete Student Record', command=self.delete_student_record)
        sub_menu.add_command(label='Show All Student Record', command=self.all_student)
        file_menu.add_cascade(label="Student", menu=sub_menu)
        file_menu.add_cascade(label="Book", menu=sub_menu1)
        file_menu.add_cascade(label="Add Book", command=self.i_b)
        file_menu.add_cascade(label="Book Issue", command=self.book_issue)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.book_i.destroy)
        file_menu.add_separator()
        menubar.add_cascade(label="View", menu=file_menu, underline=0)
        self.book_give = Label(self.book_i, text="Student Book", fg="red", font=('calibri', 20, 'bold'),
                                           bg="#ffccc7")
        self.book_give.place(x=600, y=20)
        self.book_sel = LabelFrame(self.book_i, text="Student Book Info ", width=700, height=250, relief=RIDGE, bg="#fdffb0", bd=10, fg="black")
        self.book_sel.place(x=340, y=70)
        self.sel_book_student_name = Label(self.book_sel, text="Student Name", bg="#fdffb0", font=("arial", 13, "bold"), fg="#0008ff")
        self.sel_book_student_name.place(x=10, y=10)
        self.sel_book_student_name_e = Entry(self.book_sel)
        self.sel_book_student_name_e.place(x=140, y=12)
        self.sel_book_student_roll = Label(self.book_sel, text="Roll No", bg="#fdffb0", font=("arial", 13, "bold"), fg="#0008ff")
        self.sel_book_student_roll.place(x=380, y=10)
        self.sel_book_student_roll_e = Entry(self.book_sel)
        self.sel_book_student_roll_e.place(x=520, y=10)
        self.sel_book_student_std = Label(self.book_sel, text="Standard", bg="#fdffb0", font=("arial", 13, "bold"), fg="#0008ff")
        self.sel_book_student_std.place(x=10, y=45)
        self.sel_book_student_std_e = Entry(self.book_sel)
        self.sel_book_student_std_e.place(x=140, y=45)
        self.sel_book_student_parents = Label(self.book_sel, text="Parents Mob-No", bg="#fdffb0", font=("arial", 13, "bold"), fg="#0008ff")
        self.sel_book_student_parents.place(x=380, y=45)
        self.sel_book_student_parents_e = Entry(self.book_sel)
        self.sel_book_student_parents_e.place(x=520, y=45)
        self.sel_book_student_book_name = Label(self.book_sel, text="Book Name", bg="#fdffb0", font=("arial", 13, "bold"), fg="#0008ff")
        self.sel_book_student_book_name.place(x=10, y=80)
        self.sel_book_student_book_name_e = Entry(self.book_sel)
        self.sel_book_student_book_name_e.place(x=140, y=80)
        self.sel_book_student_author_name = Label(self.book_sel, text="Author Name", bg="#fdffb0", font=("arial", 13, "bold"), fg="#0008ff")
        self.sel_book_student_author_name.place(x=380, y=80)
        self.sel_book_student_author_name_e = Entry(self.book_sel)
        self.sel_book_student_author_name_e.place(x=520, y=80)
        self.sel_book_student_book_price = Label(self.book_sel, text="Price", bg="#fdffb0", font=("arial", 13, "bold"), fg="#0008ff")
        self.sel_book_student_book_price.place(x=10, y=115)
        self.sel_book_student_book_price_e = Entry(self.book_sel)
        self.sel_book_student_book_price_e.place(x=140, y=115)
        self.sel_book_student_book_qty = Label(self.book_sel, text="Quantity", bg="#fdffb0", font=("arial", 13, "bold"), fg="#0008ff")
        self.sel_book_student_book_qty.place(x=380, y=115)
        self.sel_book_student_book_qty_e = Entry(self.book_sel)
        self.sel_book_student_book_qty_e.place(x=520, y=115)
        self.sel_book_student_from_d = Label(self.book_sel, text="From", bg="#fdffb0", font=("arial", 13, "bold"), fg="#0008ff")
        self.sel_book_student_from_d.place(x=10, y=150)
        self.sel_book_student_book_from_date_e = DateEntry(self.book_sel, selectmode="day")
        self.sel_book_student_book_from_date_e.place(x=140, y=150)
        self.sel_book_student_to_d = Label(self.book_sel, text="To", bg="#fdffb0", font=("arial", 13, "bold"), fg="#0008ff")
        self.sel_book_student_to_d.place(x=380, y=150)
        self.sel_book_student_to_d_e = DateEntry(self.book_sel, selectmode="day")
        self.sel_book_student_to_d_e.place(x=520, y=150)

        self.frame_book = Frame(self.book_i, bd=10, bg="#658a8a", width=1350, height=50, relief=SUNKEN)
        self.frame_book.place(x=0, y=330)
        self.submit_btn = Button(self.frame_book, text="Submit", bg="#fbff80", command=self.submit_book_detail, relief=RIDGE,
                                 padx=3, bd=5)
        self.submit_btn.place(x=170, y=2)
        self.update_btn = Button(self.frame_book, text="Update", bg="#fbff80", command=self.update_book_detail,
                                 relief=RIDGE, padx=3, bd=5)
        self.update_btn.place(x=500, y=2)
        self.delete_btn = Button(self.frame_book, text="Delete", bg="#fbff80", command=self.delete_book_detail,
                                 relief=RIDGE, padx=3, bd=5)
        self.delete_btn.place(x=800, y=2)
        self.cabtn = Button(self.frame_book, text="Cancel", bg="#fbff80", command=self.cancel_book_window, relief=RIDGE, padx=3, bd=5)
        self.cabtn.place(x=1100, y=2)
        self.refresh_btn = Button(self.book_i, text="Refresh", bg="#fbff80", command=self.ref_student_book_window, relief=RIDGE, padx=3,
                                  bd=5)
        self.refresh_btn.place(x=1280, y=20)


        self.student_book = Label(self.book_i, text="Student Book Detail", fg="red", font=('calibri', 20, 'bold'),
                                           bg="#ffccc7")
        self.student_book.place(x=600, y=390)
        self.bo_tabel_info = ttk.Treeview(self.book_i)
        self.bo_tabel_info['columns'] = (
            'sname', "rollno", 'standard', 'pnumber', 'bookname', "author", "price", "qty", "from", "to")
        style = ttk.Style(self.book_i)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="black", foreground="#22ff00")
        style.configure("Treeview", background="#ffbaf0", foreground="#000000")
        #
        self.bo_tabel_info.column("#0", width=0, stretch=NO)
        self.bo_tabel_info.column("sname", anchor=CENTER, width=90)
        self.bo_tabel_info.column("rollno", anchor=CENTER, width=90)
        self.bo_tabel_info.column("standard", anchor=CENTER, width=90)
        self.bo_tabel_info.column("pnumber", anchor=CENTER, width=150)
        self.bo_tabel_info.column("bookname", anchor=CENTER, width=150)
        self.bo_tabel_info.column("author", anchor=CENTER, width=150)
        self.bo_tabel_info.column("price", anchor=CENTER, width=90)
        self.bo_tabel_info.column("qty", anchor=CENTER, width=90)
        self.bo_tabel_info.column("from", anchor=CENTER, width=90)
        self.bo_tabel_info.column("to", anchor=CENTER, width=90)
        #
        self.bo_tabel_info.heading("#0", text="", anchor=CENTER)
        self.bo_tabel_info.heading("sname", text="Student Name", anchor=CENTER)
        self.bo_tabel_info.heading("rollno", text="Roll No", anchor=CENTER)
        self.bo_tabel_info.heading("standard", text="Standard", anchor=CENTER)
        self.bo_tabel_info.heading("pnumber", text="Parents Mo-no", anchor=CENTER)
        self.bo_tabel_info.heading("bookname", text="Book Name", anchor=CENTER)
        self.bo_tabel_info.heading("author", text="Author Name", anchor=CENTER)
        self.bo_tabel_info.heading("price", text="Price", anchor=CENTER)
        self.bo_tabel_info.heading("qty", text="Quantity", anchor=CENTER)
        self.bo_tabel_info.heading("from", text="From", anchor=CENTER)
        self.bo_tabel_info.heading("to", text="To", anchor=CENTER)
        self.bo_tabel_info.place(x=140, y=430)
        query = "select * from student_book_detail"
        my_cursor.execute(query)
        data = my_cursor.fetchall()
        for i in data:
            self.bo_tabel_info.insert("", 'end', iid=i[0],
                                      values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))

        self.book_i.mainloop()
    def cancel_book_window(self):
        self.book_i.destroy()
    def ref_student_book_window(self):
        if self.sel_book_student_name_e.get() == "" or self.sel_book_student_roll_e.get() == "" or self.sel_book_student_std_e.get() == "" or self.sel_book_student_parents_e.get() == "" or self.sel_book_student_book_name_e.get() == "" or self.sel_book_student_author_name_e.get() == "" or self.sel_book_student_book_price_e.get() == "" or self.sel_book_student_book_qty_e.get() == "":
            messagebox.showwarning("Blank Warning", "First Enter Something")
        else:
            self.sel_book_student_name_e.delete(0, "end")
            self.sel_book_student_roll_e.delete(0, "end")
            self.sel_book_student_std_e.delete(0, "end")
            self.sel_book_student_parents_e.delete(0, "end")
            self.sel_book_student_book_name_e.delete(0, "end")
            self.sel_book_student_author_name_e.delete(0, "end")
            self.sel_book_student_book_price_e.delete(0, "end")
            self.sel_book_student_book_qty_e.delete(0, "end")

    def delete_book_detail(self):
        self.delete_sb_window = Toplevel()
        self.delete_sb_window.geometry("350x200")
        self.delete_sb_window.title("Delete Student Book Record")
        self.delete_sb_window.config(bg="#dcdea0")
        self.sel_book_student_name = Label(self.delete_sb_window, text="Student Name", bg="#dcdea0")
        self.sel_book_student_name.place(x=20, y=20)
        self.sel_book_student_name_e = Entry(self.delete_sb_window)
        self.sel_book_student_name_e.place(x=120, y=20)
        self.sel_book_student_parents = Label(self.delete_sb_window, text="Mobile Number", bg="#dcdea0")
        self.sel_book_student_parents.place(x=20, y=50)
        self.sel_book_student_parents_e = Entry(self.delete_sb_window)
        self.sel_book_student_parents_e.place(x=120, y=50)
        self.delete = Button(self.delete_sb_window, text="Delete", command=self.s_delete1)
        self.delete.place(x=20, y=80)
        self.delete_sb_window.mainloop()

    def s_delete1(self):
        if self.sel_book_student_name_e.get() == "" or self.sel_book_student_parents_e.get() == "":
            messagebox.showwarning("Blank", "Please Enter Detail")
        if len(self.sel_book_student_parents_e.get()) < 10 or len(self.sel_book_student_parents_e.get()) > 10:
            messagebox.showwarning("Phone Number", "Phone Number Must Be Enter 10 Digit")
        else:
            my_cursor.execute("delete from student_book_detail where parents_no = '" + self.sel_book_student_parents_e.get() + "'")
            my_cursor.execute("commit")
            messagebox.showinfo("Delete", "student Book Detail has Been Deleted")
        self.sel_book_student_name_e.delete(0, END)
        self.sel_book_student_parents_e.delete(0, E)

    def update_book_detail(self):
        self.update_book_d = Toplevel()
        self.update_book_d.title("Update Student Book Detail")
        self.update_book_d.config(bg="#c7c9ff")
        self.update_book_d.geometry("1200x350")
        self.update_book_d_l = Label(self.update_book_d, text="Update Student Book Detail", fg="red", font=('calibri', 20, 'bold'),
                                           bg="#c7c9ff")
        self.update_book_d_l.place(x=450, y=10)
        self.bo_tabel_info = ttk.Treeview(self.update_book_d)
        self.bo_tabel_info['columns'] = (
            'sname', "rollno", 'standard', 'pnumber', 'bookname', "author", "price", "qty", "from", "to")
        style = ttk.Style(self.update_book_d)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="black", foreground="#22ff00")
        style.configure("Treeview", background="#ffbaf0", foreground="#000000")
        #
        self.bo_tabel_info.column("#0", width=0, stretch=NO)
        self.bo_tabel_info.column("sname", anchor=CENTER, width=90)
        self.bo_tabel_info.column("rollno", anchor=CENTER, width=90)
        self.bo_tabel_info.column("standard", anchor=CENTER, width=90)
        self.bo_tabel_info.column("pnumber", anchor=CENTER, width=150)
        self.bo_tabel_info.column("bookname", anchor=CENTER, width=150)
        self.bo_tabel_info.column("author", anchor=CENTER, width=150)
        self.bo_tabel_info.column("price", anchor=CENTER, width=90)
        self.bo_tabel_info.column("qty", anchor=CENTER, width=90)
        self.bo_tabel_info.column("from", anchor=CENTER, width=90)
        self.bo_tabel_info.column("to", anchor=CENTER, width=90)
        #
        self.bo_tabel_info.heading("#0", text="", anchor=CENTER)
        self.bo_tabel_info.heading("sname", text="Student Name", anchor=CENTER)
        self.bo_tabel_info.heading("rollno", text="Roll No", anchor=CENTER)
        self.bo_tabel_info.heading("standard", text="Standard", anchor=CENTER)
        self.bo_tabel_info.heading("pnumber", text="Parents Mo-no", anchor=CENTER)
        self.bo_tabel_info.heading("bookname", text="Book Name", anchor=CENTER)
        self.bo_tabel_info.heading("author", text="Author Name", anchor=CENTER)
        self.bo_tabel_info.heading("price", text="Price", anchor=CENTER)
        self.bo_tabel_info.heading("qty", text="Quantity", anchor=CENTER)
        self.bo_tabel_info.heading("from", text="From", anchor=CENTER)
        self.bo_tabel_info.heading("to", text="To", anchor=CENTER)
        self.bo_tabel_info.place(x=50, y=60)
        query = "select * from student_book_detail"
        my_cursor.execute(query)
        data = my_cursor.fetchall()
        for i in data:
            self.bo_tabel_info.insert("", 'end', iid=i[0],
                                      values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))

        self.sel_book_student_name = Label(self.update_book_d, text="Student Name", bg="#c7c9ff", font=("arial", 13, "bold"),
                                           fg="#0008ff")
        self.sel_book_student_name.place(x=20, y=300)
        self.sel_book_student_name_e = Entry(self.update_book_d)
        self.sel_book_student_name_e.place(x=140, y=300)
        self.sel_book_student_roll = Label(self.update_book_d, text="Roll No", bg="#c7c9ff", font=("arial", 13, "bold"),
                                           fg="#0008ff")
        self.sel_book_student_roll.place(x=270, y=300)
        self.sel_book_student_roll_e = Entry(self.update_book_d)
        self.sel_book_student_roll_e.place(x=350, y=300)
        self.sel_book_student_std = Label(self.update_book_d, text="Standard", bg="#c7c9ff", font=("arial", 13, "bold"),
                                          fg="#0008ff")
        self.sel_book_student_std.place(x=470, y=300)
        self.sel_book_student_std_e = Entry(self.update_book_d)
        self.sel_book_student_std_e.place(x=550, y=300)
        self.sel_book_student_parents = Label(self.update_book_d, text="Parents Mob-No", bg="#c7c9ff",
                                              font=("arial", 13, "bold"), fg="#0008ff")
        self.sel_book_student_parents.place(x=690, y=300)
        self.sel_book_student_parents_e = Entry(self.update_book_d)
        self.sel_book_student_parents_e.place(x=840, y=300)
        self.update_btn_book = Button(self.update_book_d, text="Update", bg="#fbff80", relief=SUNKEN, bd=5, command=self.update_book_detail_btn)
        self.update_btn_book.place(x=1100, y=300)
        self.bo_tabel_info.bind("<ButtonRelease-1>", self.click)
        self.update_book_d.mainloop()

    def click(self, e):
        self.sel_book_student_name_e.delete(0, END)
        self.sel_book_student_roll_e.delete(0, END)
        self.sel_book_student_std_e.delete(0, END)
        self.sel_book_student_parents_e.delete(0, END)
        self.selected = self.bo_tabel_info.focus()
        self.values = self.bo_tabel_info.item(self.selected, 'values')
        self.sel_book_student_name_e.insert(0, self.values[0])
        self.sel_book_student_roll_e.insert(0, self.values[1])
        self.sel_book_student_std_e.insert(0, self.values[2])
        self.sel_book_student_parents_e.insert(0, self.values[3])

    def update_book_detail_btn(self):
        if self.sel_book_student_name_e.get() == "" or self.sel_book_student_roll_e.get() == "" or self.sel_book_student_std_e.get() == "" or self.sel_book_student_parents_e.get() == "":
            messagebox.showwarning("Update", "Please Select Entry In Tree View")
        if len(self.sel_book_student_parents_e.get()) < 10 or len(self.sel_book_student_parents_e.get()) > 10:
            messagebox.showwarning("Phone Number", "Phone Number Must Be Enter 10 Digit")
        else:
            my_cursor.execute(
                "update student_book_detail set sname = '" + self.sel_book_student_name_e.get() + "', rollno = '" + self.sel_book_student_roll_e.get() + "', standard = '" + self.sel_book_student_std_e.get() + "' where parents_no = '" + self.sel_book_student_parents_e.get() + "'")
            my_cursor.execute("commit")
            messagebox.showinfo("Updated", "Your Data is Updated")
            self.sel_book_student_name_e.delete(0, END)
            self.sel_book_student_roll_e.delete(0, END)
            self.sel_book_student_std_e.delete(0, END)
            self.sel_book_student_parents_e.delete(0, END)
    def submit_book_detail(self):
        if self.sel_book_student_name_e.get() == "" or self.sel_book_student_roll_e.get() == "" or self.sel_book_student_std_e.get() == "" or self.sel_book_student_parents_e.get() == "" or self.sel_book_student_book_name_e.get() == "" or self.sel_book_student_author_name_e.get() == "" or self.sel_book_student_book_price_e.get() == "" or self.sel_book_student_book_qty_e.get() == "":
            messagebox.showwarning("Required", "All Field Required")
        else:
            my_cursor.execute("insert into student_book_detail values('"+self.sel_book_student_name_e.get()+"', '"+self.sel_book_student_roll_e.get()+"', '"+self.sel_book_student_std_e.get()+"', '"+self.sel_book_student_parents_e.get()+"', '"+self.sel_book_student_book_name_e.get()+"', '"+self.sel_book_student_author_name_e.get()+"', '"+self.sel_book_student_book_price_e.get()+"', '"+self.sel_book_student_book_qty_e.get()+"', '"+self.sel_book_student_book_from_date_e.get()+"', '"+self.sel_book_student_to_d_e.get()+"')")
            my_cursor.execute("commit")
            messagebox.showinfo("Submit", "Data Successful Submitted")
            self.bo_tabel_info = ttk.Treeview(self.book_i)
            self.bo_tabel_info['columns'] = (
                'sname', "rollno", 'standard', 'pnumber', 'bookname', "author", "price", "qty", "from", "to")
            style = ttk.Style(self.book_i)
            style.theme_use("clam")
            style.configure("Treeview.Heading", background="black", foreground="#22ff00")
            style.configure("Treeview", background="#bed1bf", foreground="#000000")
            #
            self.bo_tabel_info.column("#0", width=0, stretch=NO)
            self.bo_tabel_info.column("sname", anchor=CENTER, width=90)
            self.bo_tabel_info.column("rollno", anchor=CENTER, width=90)
            self.bo_tabel_info.column("standard", anchor=CENTER, width=90)
            self.bo_tabel_info.column("pnumber", anchor=CENTER, width=150)
            self.bo_tabel_info.column("bookname", anchor=CENTER, width=150)
            self.bo_tabel_info.column("author", anchor=CENTER, width=150)
            self.bo_tabel_info.column("price", anchor=CENTER, width=90)
            self.bo_tabel_info.column("qty", anchor=CENTER, width=90)
            self.bo_tabel_info.column("from", anchor=CENTER, width=90)
            self.bo_tabel_info.column("to", anchor=CENTER, width=90)
            #
            self.bo_tabel_info.heading("#0", text="", anchor=CENTER)
            self.bo_tabel_info.heading("sname", text="Student Name", anchor=CENTER)
            self.bo_tabel_info.heading("rollno", text="Roll No", anchor=CENTER)
            self.bo_tabel_info.heading("standard", text="Standard", anchor=CENTER)
            self.bo_tabel_info.heading("pnumber", text="Parents Mo-no", anchor=CENTER)
            self.bo_tabel_info.heading("bookname", text="Book Name", anchor=CENTER)
            self.bo_tabel_info.heading("author", text="Author Name", anchor=CENTER)
            self.bo_tabel_info.heading("price", text="Price", anchor=CENTER)
            self.bo_tabel_info.heading("qty", text="Quantity", anchor=CENTER)
            self.bo_tabel_info.heading("from", text="From", anchor=CENTER)
            self.bo_tabel_info.heading("to", text="To", anchor=CENTER)
            self.bo_tabel_info.place(x=140, y=430)
            query = "select * from student_book_detail"
            my_cursor.execute(query)
            data = my_cursor.fetchall()
            for i in data:
                self.bo_tabel_info.insert("", 'end', iid=i[0],
                                          values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
            self.sel_book_student_name_e.delete(0, "end")
            self.sel_book_student_roll_e.delete(0, "end")
            self.sel_book_student_std_e.delete(0, "end")
            self.sel_book_student_parents_e.delete(0, "end")
            self.sel_book_student_book_name_e.delete(0, "end")
            self.sel_book_student_author_name_e.delete(0, "end")
            self.sel_book_student_book_price_e.delete(0, "end")
            self.sel_book_student_book_qty_e.delete(0, "end")

    def i_b(self):
        self.i_book = Toplevel()
        self.i_book.title("Book Detail")
        self.i_book.geometry("1368x768+0+0")
        self.i_book.config(bg="#f3ffbf")
        menubar = Menu(self.i_book)
        self.i_book.config(menu=menubar)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_separator()
        sub_menu1 = Menu(file_menu, tearoff=0)
        sub_menu1.add_command(label='All Books', command=self.all_book)
        sub_menu1.add_command(label='Search Book', command=self.search_book)
        sub_menu1.add_command(label='Insert Book', command=self.insert_book)
        sub_menu1.add_command(label='Update Book', command=self.update_book)
        sub_menu1.add_command(label='Delete Book', command=self.delete_book)
        sub_menu = Menu(file_menu, tearoff=0)
        sub_menu.add_command(label='Search Student Detail', command=self.search_student)
        sub_menu.add_command(label='Update Student Record', command=self.update_student_record)
        sub_menu.add_command(label='Delete Student Record', command=self.delete_student_record)
        sub_menu.add_command(label='Show All Student Record', command=self.all_student)
        file_menu.add_cascade(label="Student", menu=sub_menu)
        file_menu.add_cascade(label="Book", menu=sub_menu1)
        file_menu.add_cascade(label="Add Book", command=self.i_b)
        file_menu.add_cascade(label="Book Issue", command=self.book_issue)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.i_book.destroy)
        file_menu.add_separator()
        menubar.add_cascade(label="View", menu=file_menu, underline=0)
        self.lib_title = Label(self.i_book, text=" LIBRARY MANAGEMENT", bg="#df9eff", padx=2, pady=6,
                               font=("arial black", 18, "bold"), relief=RIDGE, fg="#ad2d45")

        self.t = Label(self.lib_title, font=('calibri', 20, 'bold'), background='#000000', foreground='#26ff00',
                       height=1)
        string = strftime('%H:%M:%S %p')
        self.t.config(text=string)
        self.t.after(1000)
        self.t.place(x=10, y=3)

        date = dt.datetime.now()
        label = Label(self.lib_title, text=f"{date:%A, %B %d, %Y}", font=('calibri', 20, 'bold'), background='#000000',
                      foreground='#26ff00', height=1)
        label.place(x=1000, y=3)
        self.lib_title.pack(side=TOP, fill=X)

        self.student1 = Label(self.i_book, text="Book Detail", font=('calibri', 20, 'bold'), bg="#f3ffbf", fg="red")
        self.student1.place(x=600, y=55)
        self.student_dt = LabelFrame(self.i_book, text="Book Detail", width=700, height=210, bg="#95c9c9",
                                     relief=RIDGE, bd=10)
        self.student_dt.place(x=350, y=100)
        self.book_name = Label(self.student_dt, text="Book Name", bg="#5e8a5e")
        self.book_name.place(x=30, y=10)
        self.book_name_e = Entry(self.student_dt)
        self.book_name_e.place(x=140, y=10)
        self.author_l_n = Label(self.student_dt, text="Author Name", bg="#5e8a5e")
        self.author_l_n.place(x=410, y=10)
        self.author_l_n_e = Entry(self.student_dt)
        self.author_l_n_e.place(x=520, y=10)
        self.price_l = Label(self.student_dt, text="Price", bg="#5e8a5e")
        self.price_l.place(x=30, y=40)
        self.price_l_e = Entry(self.student_dt)
        self.price_l_e.place(x=140, y=40)
        self.q_l = Label(self.student_dt, text="Quantity", bg="#5e8a5e")
        self.q_l.place(x=410, y=40)
        self.quan_l_e = Entry(self.student_dt)
        self.quan_l_e.place(x=520, y=40)

        self.frame = Frame(self.i_book, bd=10, bg="#ffebb5", width=1350, height=50, relief=SUNKEN)
        self.frame.place(x=0, y=330)
        self.submit_btn = Button(self.frame, text="Submit", bg="#fbff80", command=self.book_insert, relief=RIDGE,
                                 padx=3, bd=5)
        self.submit_btn.place(x=170, y=2)
        self.update_btn = Button(self.frame, text="Update", bg="#fbff80", command=self.update_book,
                                 relief=RIDGE, padx=3, bd=5)
        self.update_btn.place(x=500, y=2)
        self.delete_btn = Button(self.frame, text="Delete", bg="#fbff80", command=self.delete_book,
                                 relief=RIDGE, padx=3, bd=5)
        self.delete_btn.place(x=800, y=2)
        self.cabtn = Button(self.frame, text="Cancel", bg="#fbff80", command=self.i_book.destroy, relief=RIDGE, padx=3, bd=5)
        self.cabtn.place(x=1100, y=2)
        self.refresh_btn = Button(self.i_book, text="Refresh", bg="#fbff80", command=self.ref1, relief=RIDGE, padx=3,
                                  bd=5)
        self.refresh_btn.place(x=1250, y=60)

        #
        self.student_details_label = Label(self.i_book, text="Book Details", fg="red", font=('calibri', 20, 'bold'),
                                           bg="#f3ffbf")
        self.student_details_label.place(x=600, y=390)
        self.student_tabel = ttk.Treeview(self.i_book)
        self.student_tabel['columns'] = (
            'bname', "aname", 'price', 'qty')
        style = ttk.Style(self.i_book)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="black", foreground="#22ff00")
        style.configure("Treeview", background="#bed1bf", foreground="#000000")
        #
        self.student_tabel.column("#0", width=0, stretch=NO)
        self.student_tabel.column("bname", anchor=CENTER, width=90)
        self.student_tabel.column("aname", anchor=CENTER, width=90)
        self.student_tabel.column("price", anchor=CENTER, width=90)
        self.student_tabel.column("qty", anchor=CENTER, width=90)
        #
        self.student_tabel.heading("#0", text="", anchor=CENTER)
        self.student_tabel.heading("bname", text="Book Name", anchor=CENTER)
        self.student_tabel.heading("aname", text="Author Name", anchor=CENTER)
        self.student_tabel.heading("price", text="Price", anchor=CENTER)
        self.student_tabel.heading("qty", text="Quantity", anchor=CENTER)

        query = "select * from insert_book"
        my_cursor.execute(query)
        data = my_cursor.fetchall()
        for i in data:
            self.student_tabel.insert("", 'end', iid=i[0],
                                      values=(i[0], i[1], i[2], i[3]))
        self.student_tabel.place(x=485, y=430)
        self.i_book.mainloop()
    def ref1(self):
        if self.book_name_e.get() == "" or self.author_l_n_e.get() == "" or self.price_l_e.get() == "" or self.quan_l_e.get() == "":
            messagebox.showwarning("Blank", "First Enter Something")
        else:
            self.book_name_e.delete(0, "end")
            self.author_l_n_e.delete(0, "end")
            self.price_l_e.delete(0,"end")
            self.quan_l_e.delete(0, "end")
    def book_insert(self):
        if self.book_name_e.get() == "" or self.author_l_n_e.get() == "" or self.price_l_e.get() == "" or self.quan_l_e.get() == "":
            messagebox.showwarning("Blank Info", "All Field Required")
        else:
            my_cursor.execute("insert into insert_book values ('" + self.book_name_e.get() + "', '" + self.author_l_n_e.get() + "', '" + self.price_l_e.get() + "', '" + self.quan_l_e.get() + "')")
            my_cursor.execute("commit")
            messagebox.showinfo("Book Info", "Book Inserted")
            self.book_name_e.delete(0, "end")
            self.author_l_n_e.delete(0, "end")
            self.price_l_e.delete(0, "end")
            self.quan_l_e.delete(0, "end")
            self.student_tabel = ttk.Treeview(self.i_book)
            self.student_tabel['columns'] = (
                'bname', "aname", 'price', 'qty')
            style = ttk.Style(self.i_book)
            style.theme_use("clam")
            style.configure("Treeview.Heading", background="black", foreground="#22ff00")
            style.configure("Treeview", background="#bed1bf", foreground="#000000")
            #
            self.student_tabel.column("#0", width=0, stretch=NO)
            self.student_tabel.column("bname", anchor=CENTER, width=90)
            self.student_tabel.column("aname", anchor=CENTER, width=90)
            self.student_tabel.column("price", anchor=CENTER, width=90)
            self.student_tabel.column("qty", anchor=CENTER, width=90)
            #
            self.student_tabel.heading("#0", text="", anchor=CENTER)
            self.student_tabel.heading("bname", text="Book Name", anchor=CENTER)
            self.student_tabel.heading("aname", text="Author Name", anchor=CENTER)
            self.student_tabel.heading("price", text="Price", anchor=CENTER)
            self.student_tabel.heading("qty", text="Quantity", anchor=CENTER)

            query = "select * from insert_book"
            my_cursor.execute(query)
            data = my_cursor.fetchall()
            for i in data:
                self.student_tabel.insert("", 'end', iid=i[0],
                                          values=(i[0], i[1], i[2], i[3]))
            self.student_tabel.place(x=485, y=430)


    def all_book(self):

        self.books1 = Toplevel()
        self.books1.title("Available Books")
        self.books1.geometry("500x300")
        self.books1.config(bg="#90d6d4")

        self.books_tabel = ttk.Treeview(self.books1)
        self.books_tabel['columns'] = ('bookname', "authorname", 'qty', 'price')
        style = ttk.Style(self.books1)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="black", foreground="#22ff00")

        self.books_tabel.column("#0", width=0, stretch=NO)
        self.books_tabel.column("bookname", anchor=CENTER, width=110)
        self.books_tabel.column("authorname", anchor=CENTER, width=110)
        self.books_tabel.column("qty", anchor=CENTER, width=110)
        self.books_tabel.column("price", anchor=CENTER, width=110)
        #
        self.books_tabel.heading("#0", text="", anchor=CENTER)
        self.books_tabel.heading("bookname", text="Book Name", anchor=CENTER)
        self.books_tabel.heading("authorname", text="Author Name", anchor=CENTER)
        self.books_tabel.heading("qty", text="Quantity", anchor=CENTER)
        self.books_tabel.heading("price", text="Price", anchor=CENTER)

        query = "select * from insert_book"
        my_cursor.execute(query)
        data = my_cursor.fetchall()
        for i in data:
            self.books_tabel.insert("", 'end', iid=i[0], values=(i[0], i[1], i[2], i[3]))
        self.books_tabel.place(x=30, y=50)
        self.books1.mainloop()

    def delete_book(self):
        self.d_book = Toplevel()
        self.d_book.title("Delete Book")
        self.d_book.geometry("300x100")
        self.d_book.config(bg="#85ffa5")
        self.d_b_l = Label(self.d_book, text="Book Name", bg="#85ffa5")
        self.d_b_l.place(x=50, y=20)
        self.d_b_l_e = Entry(self.d_book)
        self.d_b_l_e.place(x=120, y=20)
        self.d_btn = Button(self.d_book, text="Delete", command=self.delete_book_btn)
        self.d_btn.place(x=120, y=50)
        self.d_book.mainloop()

    def delete_book_btn(self):
        if self.d_b_l_e.get() == "":
            messagebox.showwarning("Delete", "Enter Book Name")
        else:
            my_cursor.execute("delete from insert_book where b_name = '" + self.d_b_l_e.get() + "'")
            my_cursor.execute("commit")
            messagebox.showinfo("Delete", "Book Deleted")
            self.d_b_l_e.delete(0, END)
            self.d_book.destroy()
    def update_book(self):

        self.update_b = Toplevel()
        self.update_b.geometry("600x430")
        self.update_b.config(bg="#adbbff")
        self.update_b.title("Update Book")

        self.book_tabel = ttk.Treeview(self.update_b)
        self.book_tabel['columns'] = (
            'bookname', "authorname", 'qty', 'price')
        style = ttk.Style(self.update_b)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="black", foreground="#22ff00")

        self.book_tabel.column("#0", width=0, stretch=NO)
        self.book_tabel.column("bookname", anchor=CENTER, width=110)
        self.book_tabel.column("authorname", anchor=CENTER, width=110)
        self.book_tabel.column("qty", anchor=CENTER, width=110)
        self.book_tabel.column("price", anchor=CENTER, width=110)
        #
        self.book_tabel.heading("#0", text="", anchor=CENTER)
        self.book_tabel.heading("bookname", text="Book Name", anchor=CENTER)
        self.book_tabel.heading("authorname", text="Author Name", anchor=CENTER)
        self.book_tabel.heading("qty", text="Quantity", anchor=CENTER)
        self.book_tabel.heading("price", text="Price", anchor=CENTER)
        self.book_tabel.place(x=75, y=20)
        self.u_l = Label(self.update_b, text="Book Name", bg="#adbbff")
        self.u_l.place(x=30, y=300)
        self.u_l_e = Entry(self.update_b, width=30)
        self.u_l_e.place(x=100, y=300)
        self.u_l_a = Label(self.update_b, text="Author Name", bg="#adbbff")
        self.u_l_a.place(x=250, y=300)
        self.u_l_a_e = Entry(self.update_b, width=30)
        self.u_l_a_e.place(x=330, y=300)
        self.u_l_q = Label(self.update_b, text="Quantity", bg="#adbbff")
        self.u_l_q.place(x=30, y=330)
        self.u_l_q_e = Entry(self.update_b)
        self.u_l_q_e.place(x=100, y=330)
        self.u_l_p = Label(self.update_b, text="Price", bg="#adbbff")
        self.u_l_p.place(x=250, y=330)
        self.u_l_p_e = Entry(self.update_b)
        self.u_l_p_e.place(x=330, y=330)
        self.update_btn = Button(self.update_b, text="Update", command=self.up_date)
        self.update_btn.place(x=250, y=360)

        query = "select * from insert_book"
        my_cursor.execute(query)
        data = my_cursor.fetchall()
        for i in data:
            self.book_tabel.insert("", 'end', iid=i[0], values=(i[0], i[1], i[2], i[3]))

        self.book_tabel.bind("<ButtonRelease-1>", self.up)
        self.update_b.mainloop()
    def up_date(self):
        if self.u_l_e.get() == "" or self.u_l_a_e.get() == "" or self.u_l_q_e.get() == "" or self.u_l_p_e.get() == "":
            messagebox.showwarning("Update", "Please Select Data")
        else:
            my_cursor.execute("update insert_book set b_a_name = '"+self.u_l_a_e.get()+"', b_q = '"+self.u_l_q_e.get()+"', b_price = '"+self.u_l_p_e.get()+"' where b_name = '"+self.u_l_e.get()+"'")
            messagebox.showinfo("Updated", "Data Updated")
            self.u_l_e.delete(0, END)
            self.u_l_a_e.delete(0, END)
            self.u_l_q_e.delete(0, END)
            self.u_l_p_e.delete(0, END)

    def up(self, e):
        self.u_l_e.delete(0, END)
        self.u_l_a_e.delete(0, END)
        self.u_l_q_e.delete(0, END)
        self.u_l_p_e.delete(0, END)
        self.selected = self.book_tabel.focus()
        self.values = self.book_tabel.item(self.selected, 'values')
        self.u_l_e.insert(0, self.values[0])
        self.u_l_a_e.insert(0, self.values[1])
        self.u_l_q_e.insert(0, self.values[2])
        self.u_l_p_e.insert(0, self.values[3])

    def search_book(self):
        self.s_book = Toplevel()
        self.s_book.title("Show Book")
        self.s_book.geometry("600x300")
        self.s_book.config(bg="#f7f6a6")
        self.s_l = Label(self.s_book, text="Search Book", bg="#f7f6a6")
        self.s_l.place(x=20, y=20)
        self.s_l_e = Entry(self.s_book, width=50)
        self.s_l_e.place(x=100, y=20)
        self.s_su_btn = Button(self.s_book, text="Search", command=self.se_book)
        self.s_su_btn.place(x=450, y=20)

        self.book_tabel = ttk.Treeview(self.s_book)
        self.book_tabel['columns'] = (
            'bookname', "authorname", 'qty', 'price')
        style = ttk.Style(self.s_book)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="black", foreground="#22ff00")
        #
        self.book_tabel.column("#0", width=0, stretch=NO)
        self.book_tabel.column("bookname", anchor=CENTER, width=110)
        self.book_tabel.column("authorname", anchor=CENTER, width=110)
        self.book_tabel.column("qty", anchor=CENTER, width=110)
        self.book_tabel.column("price", anchor=CENTER, width=110)
        #
        self.book_tabel.heading("#0", text="", anchor=CENTER)
        self.book_tabel.heading("bookname", text="Book Name", anchor=CENTER)
        self.book_tabel.heading("authorname", text="Author Name", anchor=CENTER)
        self.book_tabel.heading("qty", text="Quantity", anchor=CENTER)
        self.book_tabel.heading("price", text="Price", anchor=CENTER)
        self.book_tabel.insert(parent='', index='end', text='',
                                  values=('Clean Code', 'Robert C. Martin', '10', '200'))
        self.book_tabel.insert(parent='', index='end', text='',
                                  values=('Introduction to Algorithms', 'Thomas H', '12', '150'))
        self.book_tabel.insert(parent='', index='end', text='',
                                  values=('SICP', 'Harold Abelson', '5', '250',))
        self.book_tabel.insert(parent='', index='end', text='',
                                  values=(
                                      'The Clean Coder', 'Robert C. Martin', '3', '300'))
        self.book_tabel.insert(parent='', index='end', text='',
                                  values=(
                                      'Code Complete', 'Steve McConnell', '20', '160'))
        self.book_tabel.insert(parent='', index='end', text='',
                                  values=('Design Patterns', ' Erich Gamma', '22', '400'))
        self.book_tabel.insert(parent='', index='end', text='',
                               values=('The Pragmatic Programmer', ' Andrew Hunt', '2', '500'))
        self.book_tabel.insert(parent='', index='end', text='',
                               values=('Head First Design Patterns', 'Eric Freeman', '6', '900'))
        self.book_tabel.insert(parent='', index='end', text='',
                               values=('Refactoring', 'Martin Fowler', '2', '1000'))
        self.book_tabel.place(x=75, y=60)

        self.s_book.mainloop()

    #

    def se_book(self):
        if self.s_l_e.get() == "":
            messagebox.showwarning("Blank", "Please Enter Book Name")
            # if self.s_l_e.get() != "select * from insert_book where b_name = '%s'" % (self.s_l_e.get(),):
            #     messagebox.showwarning("Book Warning", "Book Not Available")
            #     my_cursor.execute("commit")
        # elif self.s_l_e.get() != "select * from insert_book where b_name = '%s'" % (self.s_l_e.get(),):
        #     messagebox.showwarning("Search Book", "Not Available")
        #     my_cursor.execute("commit")
        else:
            query = "select * from insert_book where b_name = '%s'" % (self.s_l_e.get(),)
            my_cursor.execute(query)
            data = my_cursor.fetchall()
            for i in data:
                self.book_tabel.insert("", 'end', iid=i[0], values=(i[0], i[1], i[2], i[3]))
        self.s_l_e.delete(0, END)

    #


    def insert_book(self):


        self.insert_b = Toplevel()
        self.insert_b.geometry("300x200")
        self.insert_b.title("Book Insert Window")
        self.insert_b.config(bg="#dea09b")
        self.b_l = Label(self.insert_b, text="Book Name", bg="#dea09b")
        self.b_l.place(x=15, y=30)
        self.b_l_e = Entry(self.insert_b, width=30)
        self.b_l_e.place(x=95, y=30)
        self.b_l_a = Label(self.insert_b, text="Author Name", bg="#dea09b")
        self.b_l_a.place(x=15, y=50)
        self.b_l_a_e = Entry(self.insert_b, width=30)
        self.b_l_a_e.place(x=95, y=50)
        self.b_l_q = Label(self.insert_b, text="Quantity", bg="#dea09b")
        self.b_l_q.place(x=15, y=70)
        self.b_l_q_e = Entry(self.insert_b)
        self.b_l_q_e.place(x=95, y=70)
        self.b_l_p = Label(self.insert_b, text="Price", bg="#dea09b")
        self.b_l_p.place(x=15, y=90)
        self.b_l_p_e = Entry(self.insert_b)
        self.b_l_p_e.place(x=95, y=90)
        self.b_btn = Button(self.insert_b, text="Submit", command=self.b_s)
        self.b_btn.place(x=50, y=130)
        self.b_btn_c = Button(self.insert_b, text="Cancel", command=self.insert_b.destroy)
        self.b_btn_c.place(x=170, y=130)

        self.insert_b.mainloop()
    def b_s(self):
        if self.b_l_e.get() == "" or self.b_l_a_e.get() == "" or self.b_l_p_e.get() == "" or self.b_l_q_e.get() == "":
            messagebox.showwarning("Insert Book Data", "Please Enter Book Detail")
        else:
            my_cursor.execute("insert into insert_book values ('"+self.b_l_e.get()+"', '"+self.b_l_a_e.get()+"', '"+self.b_l_q_e.get()+"', '"+self.b_l_p_e.get()+"')")
            my_cursor.execute("commit")
            messagebox.showinfo("Book Info", "Book Detail Inserted")
            self.insert_b.destroy()

    def all_student(self):
        self.all_record = Toplevel()
        self.all_record.title("All Student Record")
        self.all_record.geometry("1030x300")
        self.all_record.config(bg="#9393bf")
        self.student_details_label = Label(self.all_record, text="Student Details", fg="red", font=('calibri', 20, 'bold'),
                                           bg="#f3ffbf")
        self.student_details_label.place(x=600, y=390)
        self.student_tabel = ttk.Treeview(self.all_record)
        self.student_tabel['columns'] = (
            'fname', "lname", 'faname', 'moname', 'age', "panumber", "stuname", "rollno", "standard", "teachername")
        style = ttk.Style(self.all_record)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="black", foreground="#22ff00")
        style.configure("Treeview", background="#bed1bf", foreground="#000000")
        #
        self.student_tabel.column("#0", width=0, stretch=NO)
        self.student_tabel.column("fname", anchor=CENTER, width=90)
        self.student_tabel.column("lname", anchor=CENTER, width=90)
        self.student_tabel.column("faname", anchor=CENTER, width=90)
        self.student_tabel.column("moname", anchor=CENTER, width=90)
        self.student_tabel.column("age", anchor=CENTER, width=90)
        self.student_tabel.column("panumber", anchor=CENTER, width=150)
        self.student_tabel.column("stuname", anchor=CENTER, width=90)
        self.student_tabel.column("rollno", anchor=CENTER, width=90)
        self.student_tabel.column("standard", anchor=CENTER, width=90)
        self.student_tabel.column("teachername", anchor=CENTER, width=120)
        #
        self.student_tabel.heading("#0", text="", anchor=CENTER)
        self.student_tabel.heading("fname", text="First Name", anchor=CENTER)
        self.student_tabel.heading("lname", text="Last Name", anchor=CENTER)
        self.student_tabel.heading("faname", text="Father Name", anchor=CENTER)
        self.student_tabel.heading("moname", text="Mother Name", anchor=CENTER)
        self.student_tabel.heading("age", text="Age", anchor=CENTER)
        self.student_tabel.heading("panumber", text="Parents Mobile No", anchor=CENTER)
        self.student_tabel.heading("stuname", text="Student Name", anchor=CENTER)
        self.student_tabel.heading("rollno", text="Roll No", anchor=CENTER)
        self.student_tabel.heading("standard", text="Standard", anchor=CENTER)
        self.student_tabel.heading("teachername", text="Teacher Name", anchor=CENTER)
        query = "select * from student_detail1"
        my_cursor.execute(query)
        data = my_cursor.fetchall()
        for i in data:
            self.student_tabel.insert("", 'end', iid=i[0],
                                      values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
        self.student_tabel.place(x=7, y=20)
        self.all_record.mainloop()
    def delete_student_record(self):
        self.delete_window = Toplevel()
        self.delete_window.geometry("350x200")
        self.delete_window.title("Delete Record")
        self.delete_window.config(bg="#dcdea0")
        self.d_l = Label(self.delete_window, text="Student Name")
        self.d_l.place(x=20, y=20)
        self.d_l_e = Entry(self.delete_window)
        self.d_l_e.place(x=120, y=20)
        self.number = Label(self.delete_window, text="Mobile Number")
        self.number.place(x=20, y=50)
        self.number_e = Entry(self.delete_window)
        self.number_e.place(x=120, y=50)
        self.delete = Button(self.delete_window, text="Delete", command=self.s_delete)
        self.delete.place(x=20, y=80)
        self.delete_window.mainloop()
    def s_delete(self):
        if self.d_l_e.get() == "" or self.number_e.get() == "":
            messagebox.showwarning("Blank", "Please Enter Detail")
        if len(self.number_e.get()) < 10 or len(self.number_e.get()) > 10:
            messagebox.showwarning("Phone Number", "Phone Number Must Be Enter 10 Digit")
        else:
            my_cursor.execute("delete from student_detail1 where parents_mo_no = '"+self.number_e.get()+"'")
            my_cursor.execute("commit")
            messagebox.showinfo("Delete", "student has Been Deleted")
        self.d_l_e.delete(0, END)
        self.number_e.delete(0, E)
    def update_student_record(self):
        self.search_s = Toplevel()
        self.search_s.geometry("1050x400")
        self.search_s.config(bg="#adeda4")
        self.search_s.title("Update Student Record")
        self.search_st_l = Label(self.search_s, text="Student Name", bg="#adeda4")
        self.search_st_l.place(x=30, y=15)
        self.search_st_e = Entry(self.search_s, width=100)
        self.search_st_e.place(x=120, y=15)
        self.search_st_btn = Button(self.search_s, text="Search", width=20, command=self.student_btn)
        self.search_st_btn.place(x=730, y=15)
        #
        self.student_details_label = Label(self.search_s, text="Student Details", fg="red", font=('calibri', 20, 'bold'),
                                           bg="#f3ffbf")
        self.student_details_label.place(x=600, y=390)
        self.student_tabel = ttk.Treeview(self.search_s)
        self.student_tabel['columns'] = (
            'fname', "lname", 'faname', 'moname', 'age', "panumber", "stuname", "rollno", "standard", "teachername")
        style = ttk.Style(self.search_s)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="black", foreground="#22ff00")
        style.configure("Treeview", background="#bed1bf", foreground="#000000")
        #
        self.student_tabel.column("#0", width=0, stretch=NO)
        self.student_tabel.column("fname", anchor=CENTER, width=90)
        self.student_tabel.column("lname", anchor=CENTER, width=90)
        self.student_tabel.column("faname", anchor=CENTER, width=90)
        self.student_tabel.column("moname", anchor=CENTER, width=90)
        self.student_tabel.column("age", anchor=CENTER, width=90)
        self.student_tabel.column("panumber", anchor=CENTER, width=150)
        self.student_tabel.column("stuname", anchor=CENTER, width=90)
        self.student_tabel.column("rollno", anchor=CENTER, width=90)
        self.student_tabel.column("standard", anchor=CENTER, width=90)
        self.student_tabel.column("teachername", anchor=CENTER, width=120)
        #
        self.student_tabel.heading("#0", text="", anchor=CENTER)
        self.student_tabel.heading("fname", text="First Name", anchor=CENTER)
        self.student_tabel.heading("lname", text="Last Name", anchor=CENTER)
        self.student_tabel.heading("faname", text="Father Name", anchor=CENTER)
        self.student_tabel.heading("moname", text="Mother Name", anchor=CENTER)
        self.student_tabel.heading("age", text="Age", anchor=CENTER)
        self.student_tabel.heading("panumber", text="Parents Mobile No", anchor=CENTER)
        self.student_tabel.heading("stuname", text="Student Name", anchor=CENTER)
        self.student_tabel.heading("rollno", text="Roll No", anchor=CENTER)
        self.student_tabel.heading("standard", text="Standard", anchor=CENTER)
        self.student_tabel.heading("teachername", text="Teacher Name", anchor=CENTER)
        query = "select * from student_detail1"
        my_cursor.execute(query)
        data = my_cursor.fetchall()
        for i in data:
            self.student_tabel.insert("", 'end', iid=i[0],
                                      values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
        self.student_tabel.place(x=20, y=60)

        self.s_name = Label(self.search_s, text="Student Name", bg="#548be3", relief=RIDGE)
        self.s_name.place(x=10, y=300)
        self.s_name_e = Entry(self.search_s)
        self.s_name_e.place(x=110, y=300)
        self.standard = Label(self.search_s, text="Standard", bg="#548be3", relief=RIDGE)
        self.standard.place(x=240, y=300)
        self.standard_e = Entry(self.search_s)
        self.standard_e.place(x=300, y=300)
        self.s_roll_no = Label(self.search_s, text="Roll No", bg="#548be3", relief=RIDGE)
        self.s_roll_no.place(x=450, y=300)
        self.s_roll_no_e = Entry(self.search_s)
        self.s_roll_no_e.place(x=500, y=300)
        self.s_parents_no = Label(self.search_s, text="Parents No", bg="#548be3", relief=RIDGE)
        self.s_parents_no.place(x=630, y=300)
        self.s_parents_no_e = Entry(self.search_s)
        self.s_parents_no_e.place(x=700, y=300)
        self.s_u_btn = Button(self.search_s, text="Update", command=self.update_record)
        self.s_u_btn.place(x=830, y=300)
        # self.student_tabel.bind("<Double-1>", self.click)


        self.student_tabel.bind("<ButtonRelease-1>", self.click1)
        self.search_s.mainloop()
    def click1(self, e):
        self.s_name_e.delete(0, END)
        self.standard_e.delete(0, END)
        self.s_roll_no_e.delete(0, END)
        self.s_parents_no_e.delete(0, END)
        self.selected = self.student_tabel.focus()
        self.values = self.student_tabel.item(self.selected, 'values')
        self.s_name_e.insert(0, self.values[0])
        self.standard_e.insert(0, self.values[3])
        self.s_roll_no_e.insert(0, self.values[4])
        self.s_parents_no_e.insert(0, self.values[5])

    def update_record(self):
        if self.standard_e.get() == "" or self.s_roll_no_e.get() == "" or self.s_parents_no_e.get() == "":
            messagebox.showwarning("Update", "Please Select Entry In Tree View")
        if len(self.s_parents_no_e.get()) < 10 or len(self.s_parents_no_e.get()) > 10:
            messagebox.showwarning("Phone Number", "Phone Number Must Be Enter 10 Digit")
        else:
            my_cursor.execute("update student_detail1 set standard = '"+self.standard_e.get()+"', rool_no = '"+self.s_roll_no_e.get()+"', parents_mo_no = '"+self.s_parents_no_e.get()+"' where student_name = '"+self.s_name_e.get()+"'")
            my_cursor.execute("commit")
            messagebox.showinfo("Updated", "Your Data is Updated")
            self.s_name_e.delete(0, END)
            self.standard_e.delete(0, END)
            self.s_roll_no_e.delete(0, END)
            self.s_parents_no_e.delete(0, END)
    def search_student(self):
        self.search_s = Toplevel()
        self.search_s.geometry("1050x400")
        self.search_s.config(bg="#adeda4")
        self.search_s.title("Search Student Record")
        self.search_st_l = Label(self.search_s, text="Student Name", bg="#adeda4")
        self.search_st_l.place(x=30, y=29)
        self.search_st_e = Entry(self.search_s, width=100)
        self.search_st_e.place(x=120, y=29)
        self.search_st_btn = Button(self.search_s, text="Search", width=20, command=self.student_btn)
        self.search_st_btn.place(x=730, y=29)
        #
        self.student_details_label = Label(self.search_s, text="Student Details", fg="red", font=('calibri', 20, 'bold'),
                                           bg="#f3ffbf")
        self.student_details_label.place(x=400, y=55)
        self.student_tabel = ttk.Treeview(self.search_s)
        self.student_tabel['columns'] = (
            'fname', "lname", 'faname', 'moname', 'age', "panumber", "stuname", "rollno", "standard", "teachername")
        style = ttk.Style(self.search_s)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="black", foreground="#22ff00")
        style.configure("Treeview", background="#bed1bf", foreground="#000000")
        #
        self.student_tabel.column("#0", width=0, stretch=NO)
        self.student_tabel.column("fname", anchor=CENTER, width=90)
        self.student_tabel.column("lname", anchor=CENTER, width=90)
        self.student_tabel.column("faname", anchor=CENTER, width=90)
        self.student_tabel.column("moname", anchor=CENTER, width=90)
        self.student_tabel.column("age", anchor=CENTER, width=90)
        self.student_tabel.column("panumber", anchor=CENTER, width=150)
        self.student_tabel.column("stuname", anchor=CENTER, width=90)
        self.student_tabel.column("rollno", anchor=CENTER, width=90)
        self.student_tabel.column("standard", anchor=CENTER, width=90)
        self.student_tabel.column("teachername", anchor=CENTER, width=120)
        #
        self.student_tabel.heading("#0", text="", anchor=CENTER)
        self.student_tabel.heading("fname", text="First Name", anchor=CENTER)
        self.student_tabel.heading("lname", text="Last Name", anchor=CENTER)
        self.student_tabel.heading("faname", text="Father Name", anchor=CENTER)
        self.student_tabel.heading("moname", text="Mother Name", anchor=CENTER)
        self.student_tabel.heading("age", text="Age", anchor=CENTER)
        self.student_tabel.heading("panumber", text="Parents Mobile No", anchor=CENTER)
        self.student_tabel.heading("stuname", text="Student Name", anchor=CENTER)
        self.student_tabel.heading("rollno", text="Roll No", anchor=CENTER)
        self.student_tabel.heading("standard", text="Standard", anchor=CENTER)
        self.student_tabel.heading("teachername", text="Teacher Name", anchor=CENTER)
        self.student_tabel.place(x=15, y=110)
        self.search_s.mainloop()

    def student_btn(self):
        self.query = "select * from student_detail1 where student_name = '%s'" % (self.search_st_e.get(),)
        if self.search_st_e.get() == "":
            messagebox.showwarning("Blank", "Please Enter Student Name")
        elif self.query:
            my_cursor.execute(self.query)
            data = my_cursor.fetchall()
            for i in data:
                self.student_tabel.insert("", 'end', iid=i[0],
                                          values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))

        else:
            messagebox.showwarning("Name", "Student Name Dose Not Match In Data Base.")
        self.search_st_e.delete(0, END)
    #             print(i)
    def canbtn(self):
        self.window3.destroy()
    def submit_btn1(self):
        if self.student_f_name_e.get() == "" or self.student_l_n_e.get() == "" or self.student_father_name_e.get() == "" or self.student_mother_name_e.get() == "" or self.agechoosen.get() == "" or self.parents_no_e.get() == "" or self.student_name_e.get() == "" or self.roll_no_e.get() == "" or self.std_e.get() == "" or self.teacher_name_e.get() == "":
            messagebox.showwarning("Warning", "All Field Required")
        if len(self.parents_no_e.get()) < 10 or len(self.parents_no_e.get()) > 10:
            messagebox.showwarning("Warning", "Please Enter 10 Digit Number")
        # try:
        #     int(self.roll_no_e.get())
        # except ValueError:
        #     messagebox.showwarning("Roll No", "Please Enter Only Integer")
        else:
            my_cursor.execute("insert into student_detail1 values('"+self.student_f_name_e.get()+"', '"+self.student_l_n_e.get()+"', '"+self.student_father_name_e.get()+"', '"+self.student_mother_name_e.get()+"', '"+self.agechoosen.get()+"', '"+self.parents_no_e.get()+"', '"+self.student_name_e.get()+"', '"+self.roll_no_e.get()+"', '"+self.std_e.get()+"', '"+self.teacher_name_e.get()+"')")
            my_cursor.execute("commit")
            messagebox.showinfo("Student Info", "Data Submitted Successfully")
            self.student_f_name_e.delete(0, "end")
            self.student_l_n_e.delete(0, "end")
            self.student_father_name_e.delete(0, "end")
            self.student_mother_name_e.delete(0, "end")
            self.parents_no_e.delete(0, "end")
            self.student_name_e.delete(0, "end")
            self.roll_no_e.delete(0, "end")
            self.std_e.delete(0, "end")
            self.teacher_name_e.delete(0, "end")

            self.student_tabel = ttk.Treeview(self.window3)
            self.student_tabel['columns'] = (
                'fname', "lname", 'faname', 'moname', 'age', "panumber", "stuname", "rollno", "standard", "teachername")
            style = ttk.Style(self.window3)
            style.theme_use("clam")
            style.configure("Treeview.Heading", background="black", foreground="#22ff00")
            style.configure("Treeview", background="#bed1bf", foreground="#000000")
            #
            self.student_tabel.column("#0", width=0, stretch=NO)
            self.student_tabel.column("fname", anchor=CENTER, width=90)
            self.student_tabel.column("lname", anchor=CENTER, width=90)
            self.student_tabel.column("faname", anchor=CENTER, width=90)
            self.student_tabel.column("moname", anchor=CENTER, width=90)
            self.student_tabel.column("age", anchor=CENTER, width=90)
            self.student_tabel.column("panumber", anchor=CENTER, width=150)
            self.student_tabel.column("stuname", anchor=CENTER, width=90)
            self.student_tabel.column("rollno", anchor=CENTER, width=90)
            self.student_tabel.column("standard", anchor=CENTER, width=90)
            self.student_tabel.column("teachername", anchor=CENTER, width=120)
            #
            self.student_tabel.heading("#0", text="", anchor=CENTER)
            self.student_tabel.heading("fname", text="First Name", anchor=CENTER)
            self.student_tabel.heading("lname", text="Last Name", anchor=CENTER)
            self.student_tabel.heading("faname", text="Father Name", anchor=CENTER)
            self.student_tabel.heading("moname", text="Mother Name", anchor=CENTER)
            self.student_tabel.heading("age", text="Age", anchor=CENTER)
            self.student_tabel.heading("panumber", text="Parents Mobile No", anchor=CENTER)
            self.student_tabel.heading("stuname", text="Student Name", anchor=CENTER)
            self.student_tabel.heading("rollno", text="Roll No", anchor=CENTER)
            self.student_tabel.heading("standard", text="Standard", anchor=CENTER)
            self.student_tabel.heading("teachername", text="Teacher Name", anchor=CENTER)
            query = "select * from student_detail1"
            my_cursor.execute(query)
            data = my_cursor.fetchall()
            for i in data:
                self.student_tabel.insert("", 'end', iid=i[0],
                                          values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
            self.student_tabel.place(x=185, y=430)
    def ref(self):
        if self.student_f_name_e.get() == "" or self.student_l_n_e.get() == "" or self.student_father_name_e.get() == "" or self.student_mother_name_e.get() == "" or self.agechoosen.get() == "" or self.parents_no_e.get() == "" or self.student_name_e.get() == "" or self.roll_no_e.get() == "" or self.std_e.get() == "" or self.teacher_name_e.get() == "":
            messagebox.showwarning("Warning", "First You Enter Detail")
        else:
            self.student_f_name_e.delete(0, "end")
            self.student_l_n_e.delete(0, "end")
            self.student_father_name_e.delete(0, "end")
            self.student_mother_name_e.delete(0, "end")
            self.parents_no_e.delete(0, "end")
            self.student_name_e.delete(0, "end")
            self.roll_no_e.delete(0, "end")
            self.std_e.delete(0, "end")
            self.teacher_name_e.delete(0, "end")
            self.agechoosen.delete(0, "end")

    def forgot_password(self):
        self.window2 = Toplevel()
        self.window2.resizable(False, False)
        self.window2.geometry("300x300")
        self.window2.title("Recover Password")
        self.window2.config(bg="#f5dbd3")
        self.first_name = Label(self.window2, text="First Name", bg="#f08d6e")
        self.first_name.place(x=10, y=30)
        self.first_name_e = Entry(self.window2)
        self.first_name_e.place(x=80, y=30)
        self.last_name = Label(self.window2, text="Last Name", bg="#f08d6e")
        self.last_name.place(x=10, y=70)
        self.last_name_e = Entry(self.window2)
        self.last_name_e.place(x=80, y=70)
        self.user_name = Label(self.window2, text="Username", bg="#f08d6e")
        self.user_name.place(x=10,y=110)
        self.user_name_e = Entry(self.window2)
        self.user_name_e.place(x=80, y=110)
        self.new_pwd = Label(self.window2, text="New Password", bg="#f08d6e")
        self.new_pwd.place(x=10, y=150)
        self.new_pwd_e = Entry(self.window2, show="*")
        self.new_pwd_e.place(x=100, y=150)
        self.showp = Button(self.window2, text="Show", command=self.showpass)
        self.showp.place(x=225, y=150)
        self.con_pwd = Label(self.window2, text="Re-Enter Password", bg="#f08d6e")
        self.con_pwd.place(x=10, y=180)
        self.showp1 = Button(self.window2, text="Show", command=self.showpass1)
        self.showp1.place(x=245, y=180)
        self.con_pwd_e = Entry(self.window2, show="*")
        self.con_pwd_e.place(x=120, y=180)
        self.next = Button(self.window2, text="Submit", bg="#9bc4e8", command=self.submit)
        self.next.place(x=40, y=250)
        self.cancel =Button(self.window2, text="Cancel", bg="#9bc4e8", command=self.cancel1)
        self.cancel.place(x=170, y=250)
        self.window2.mainloop()

    def showpass(self):
        if self.new_pwd_e.cget('show') == '':
            self.new_pwd_e.config(show='*')
            self.showp.config(text='Show')
        else:
            self.new_pwd_e.config(show='')
            self.showp.config(text='Hide')

    def showpass1(self):
        if self.con_pwd_e.cget('show') == '':
            self.con_pwd_e.config(show='*')
            self.showp1.config(text='Show')
        else:
            self.con_pwd_e.config(show='')
            self.showp1.config(text='Hide')

    def submit(self):
        if self.first_name_e.get() == "" or self.last_name_e.get() == "" or self.user_name_e.get() == "" or self.new_pwd_e.get() == "" or self.con_pwd_e.get() == "":
            messagebox.showwarning("Warning", "All Field Required")
        elif self.new_pwd_e.get() != self.con_pwd_e.get():
            messagebox.showwarning("Password", "Password Is Incorrect")
        else:
            my_cursor.execute("update create_ac_data set c_password='" + self.new_pwd_e.get() + "' where c_username='" + self.user_name_e.get() + "'")
            my_cursor.execute("commit")
            messagebox.showinfo("Info", "Your Password Is Successfully Updated")


    def cancel1(self):
        self.window2.destroy()


    def show(self):
        if self.password_e.cget('show') == '':
            self.password_e.config(show='*')
            self.show_pass.config(text='Show')
        else:
            self.password_e.config(show='')
            self.show_pass.config(text='Hide')


    def create_account(self):
        self.window1 = Toplevel()
        self.window1.resizable(False, False)
        self.window1.title("Create Account (Page)")
        self.window1.geometry("350x300")
        self.window1.config(bg="#b1eff0")
        self.f_name = Label(self.window1, text="First Name ", bg="#b1e381")
        self.f_name.place(x=10, y=20)
        self.f_name_e = Entry(self.window1)
        self.f_name_e.place(x=80, y=22)
        self.l1_name = Label(self.window1, text="Last Name ", bg="#b1e381")
        self.l1_name.place(x=10, y=50)
        self.l_name_e = Entry(self.window1)
        self.l_name_e.place(x=80, y=50)
        self.email = Label(self.window1, text="Email", bg="#b1e381")
        self.email.place(x=10, y=80)
        self.email_e = Entry(self.window1, width=30)
        self.email_e.place(x=80, y=80)
        self.phone_no = Label(self.window1, text="Phone No", bg="#b1e381")
        self.phone_no.place(x=10, y=110)
        self.phone_no_e = Entry(self.window1)
        self.phone_no_e.place(x=80, y=110)
        self.user_n = Label(self.window1, text="Username", bg="#b1e381")
        self.user_n.place(x=10, y=140)
        self.user_n_e = Entry(self.window1)
        self.user_n_e.place(x=80, y=140)
        self.pwd = Label(self.window1, text="Password", bg="#b1e381")
        self.pwd.place(x=10, y=170)
        self.pwd_e = Entry(self.window1, show="*")
        self.pwd_e.place(x=80, y=170)
        self.show_pass1 = Button(self.window1, text="Show", command=self.show1)
        self.show_pass1.place(x=220, y=170)
        self.create_btn_1 = Button(self.window1, text=" Sign ", bg="#f792f2", command=self.login)
        self.create_btn_1.place(x=30, y=220)
        self.cancel_btn = Button(self.window1, text="Cancel", bg="#f792f2", command=self.cancel_button)
        self.cancel_btn.place(x=140, y=220)
        self.window1.mainloop()


    def show1(self):
        if self.pwd_e.cget('show') == '':
            self.pwd_e.config(show='*')
            self.show_pass1.config(text='Show')
        else:
            self.pwd_e.config(show='')
            self.show_pass1.config(text='Hide')


    def login(self):
        if self.f_name_e.get() == "" or self.l_name_e.get() == "" or self.email_e.get() == "" or self.phone_no_e.get() == "" or self.user_n_e.get() == "" or self.pwd_e.get() == "":
            messagebox.showwarning("Blank Place Warning", "All Field Required")
        elif len(self.phone_no_e.get()) < 10 or len(self.phone_no_e.get()) > 10:
            messagebox.showwarning("Phone Number", "Phone Number Must Be Enter 10 Digit")
        else:
            messagebox.showinfo("Account Info", "Your Account Has been Created\n\n\tPlease Login The Page")
            my_db = mysql.connector.connect(host="localhost", user="root", password="400102", database="library")
            my_cursor = my_db.cursor()
            my_cursor.execute("insert into create_ac_data values('"+self.f_name_e.get()+"', '"+self.l_name_e.get()+"', '"+self.email_e.get()+"', '"+self.phone_no_e.get()+"', '"+self.user_n_e.get()+"', '"+self.pwd_e.get()+"')")
            my_cursor.execute("commit")
            self.window1.destroy()


    def cancel_button(self):
        self.window1.destroy()

window = Tk()
window.resizable(False, False)
window.title("Library Management (Login page)")
window.geometry("500x250+50+50")
window.config(bg="#bcd2f5")
l_m = library_management()
l_m.login_page()
window.mainloop()
