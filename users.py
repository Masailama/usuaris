import tkinter as tk
from tkinter import messagebox
from constatnts import ACTIVE_OPTION, BG_BUTTON, OPTION_FONT


class Users(tk.Frame):
    def __init__(self, window):
        super(Users, self).__init__(window)
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
