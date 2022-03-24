import tkinter as tk
from tkinter import messagebox
from constatnts import ACTIVE_OPTION, BG_BUTTON, DATA_BASE, OPTION_FONT, TABLE
from data_base import run_sql


class Users(tk.Frame):
    def __init__(self, window):
        super(Users, self).__init__(window)
        # Variables
        self.name_db = DATA_BASE
        # Frame options
        self.frame_options = tk.Frame(self)
        self.opt_login = tk.Label(self.frame_options, text=" Login ", cursor="hand2", font=OPTION_FONT, bg="red")
        self.opt_signup = tk. Label(self.frame_options, text=" Sign up ", cursor="hand2", font=OPTION_FONT, bg="green")
        self.opt_login.bind("<Button 1>", self.change_option)
        self.opt_signup.bind("<Button 1>", self.change_option)
        # Frame login
        self.frame_login = tk.Frame(self)
        self.lb_login_user = tk.Label(self.frame_login, text="User: ")
        self.txt_login_user = tk.Entry(self.frame_login, width=25, highlightthickness=0, bd=0, relief="flat")
        self.lb_login_pass = tk.Label(self.frame_login, text="Password: ")
        self.txt_login_pass = tk.Entry(self.frame_login, width=25, highlightthickness=0, bd=0, relief="flat", 
            show="*")
        self.bt_login = tk.Button(self.frame_login, text="Login", width=10, bg=BG_BUTTON, cursor="hand2", 
            activebackground=ACTIVE_OPTION, highlightthickness=0, bd=0, relief="flat", font=ACTIVE_OPTION, 
            command=self.login)
        # Frame sign up
        self.frame_signup = tk.Frame(self)
        self.lb_signup_user = tk.Label(self.frame_signup, text="User: ")
        self.txt_signup_user = tk.Entry(self.frame_signup, width=25, highlightthickness=0, bd=0, relief="flat")
        self.lb_signup_pass = tk.Label(self.frame_signup, text="Password: ")
        self.txt_signup_pass = tk.Entry(self.frame_signup, width=25, highlightthickness=0, bd=0, relief="flat", 
            show="*")
        self.lb_signup_confirm_pass = tk.Label(self.frame_signup, text="Confirm password: ")
        self.txt_signup_confirm_pass = tk.Entry(self.frame_signup, width=25, highlightthickness=0, bd=0, 
            relief="flat", show="*")
        self.bt_signup = tk.Button(self.frame_signup, text="Sign up", width=10, bg=BG_BUTTON, cursor="hand2",
            activebackground=ACTIVE_OPTION, highlightthickness=0, bd=0, relief="flat", font=ACTIVE_OPTION, 
            command=self.signup)
        self.draw()
        self.draw_login()
        self.create_db()

    def draw(self):
        self.pack(fill=tk.BOTH)
        self.frame_options.pack(fill=tk.X)
        self.opt_login.grid(row=0, column=0,ipadx=25)
        self.opt_signup.grid(row=0, column=1, ipadx=25)

    def draw_login(self):
        self.opt_login["bg"] = ACTIVE_OPTION
        self.opt_signup["bg"] = self.cget("bg")
        self.frame_signup.pack_forget()
        self.frame_login.pack(fill=tk.X, pady=10)
        self.lb_login_user.pack(fill=tk.X, pady=(10, 0))
        self.txt_login_user.pack(padx=10)
        self.lb_login_pass.pack(fill=tk.X, pady=(10, 0))
        self.txt_login_pass.pack(padx=10)
        self.bt_login.pack(padx=20, pady=(15, 0))
        self.txt_login_user.focus()

    def draw_signup(self):
        self.opt_signup["bg"] = ACTIVE_OPTION
        self.opt_login["bg"] = self.cget("bg")
        self.frame_login.pack_forget()
        self.frame_signup.pack(fill=tk.X, pady=10)
        self.lb_signup_user.pack(fill=tk.X, pady=(10, 0))
        self.txt_signup_user.pack(padx=10)
        self.lb_signup_pass.pack(fill=tk.X, pady=(10, 0))
        self.txt_signup_pass.pack(padx=10)
        self.lb_signup_confirm_pass.pack(fill=tk.X, pady=(10, 0))
        self.txt_signup_confirm_pass.pack(padx=10)
        self.bt_signup.pack(padx=20, pady=(15, 0))
        self.txt_signup_user.focus()
        
    def change_option(self, event):
        if event.widget == self.opt_login:
            self.draw_login()
        elif event.widget == self.opt_signup:
            self.draw_signup()

    def check_login_fields(self):
        if self.txt_login_user.get() != "" and self.txt_login_pass.get() != "":
            return True
        return messagebox.showerror("Login", "Must fill the fields")

    def check_signup_fields(self):
        if (self.txt_signup_user.get() != "" and self.txt_signup_pass.get() != "" and 
            self.txt_signup_confirm_pass.get() != ""):
            return True
        return messagebox.showerror("Sign up", "Must fill the fields")

    def check_passwords(self):
        if self.txt_signup_pass.get() == self.txt_signup_confirm_pass.get():
            return True
        return messagebox.showerror("Sign up", "The passwords have to be equals")

    def delete_fields(self, login):
        if login:
            self.txt_login_user.delete(0, tk.END)
            self.txt_login_pass.delete(0, tk.END)
            self.txt_login_user.focus()
        else:
            self.txt_signup_user.delete(0, tk.END)
            self.txt_signup_pass.delete(0, tk.END)
            self.txt_signup_confirm_pass.delete(0, tk.END)
            self.txt_signup_user.focus()

    def login(self):
        if self.check_login_fields() == True:
            if self.check_user(self.txt_login_user.get(), True) == self.txt_login_pass.get():
                messagebox.showinfo("Login", "You have accessed")

    def signup(self):
        if self.check_signup_fields() == True:
            if self.check_passwords() == True:
                if self.check_user(self.txt_signup_user.get(), False):
                    self.add_user()
                    self.delete_fields(False)

    def create_db(self):
        sql = TABLE
        run_sql(name=self.name_db, query=sql)

    def fin_id(self):
        num_id = 1
        sql = "SELECT ID FROM USERS ORDER BY ID ASC"
        data = run_sql(name=self.name_db, query=sql, read=True)
        for item in data:
            if item[0] != num_id:
                break
            num_id += 1
        return num_id

    def check_user(self, user, login):
        sql = "SELECT PASSWORD FROM USERS WHERE USER=?"
        params = (user, )
        item = run_sql(name=self.name_db, query=sql, parameters=params, read=True)
        if login:
            if item:
                return item[0][0]
            messagebox.showerror("Login", "The user doesn't exist.")
            self.delete_fields(True)
            return False
        else:
            if item:
                messagebox.showerror("Sign up", "The user just exists.")
                self.delete_fields(False)
                return False
            return True

    def add_user(self):
        sql = "INSERT INTO USERS VALUES(?, ?, ?)"
        params = (self.fin_id(), self.txt_login_user.get(), self.txt_login_pass.get())
        run_sql(name=self.name_db, query=sql, parameters=params)
        messagebox.showinfo("Sign up", "User creates successfully")