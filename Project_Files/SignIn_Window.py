from datetime import date, datetime
from smtplib import SMTP
from tkinter import (Button, Checkbutton, Entry, Frame, Label, PhotoImage, StringVar,
                     Toplevel, messagebox)

import mysql.connector as mc
from AfterSignin_window import afterSignIn_mainWindow


class signin_mainWindow():
    '''Its singin window'''

    def __init__(self, master=None) -> None:

        # 1)defining SignIn_Window properties......
        self.window1 = Toplevel(master)
        self.window1_width = 969
        self.window1_height = 546
        self.x = (self.window1.winfo_screenwidth()//2) - \
            (self.window1_width//2)
        self.y = (self.window1.winfo_screenheight()//2) - \
            (self.window1_height//2)
        self.window1.geometry(
            f"{self.window1_width}x{self.window1_height}+{self.x}+{self.y}")
        self.window1.resizable(0, 0)
        self.window1.title("Welcome to Signin page")
        self.window1.iconbitmap(r".\miniprojectPL_pictures\Main_icon.ico")
        self.window1.configure(background="#2A475E")
        self.HomeObj = master

        # 2)Creating obj of Image for bottom of window some design like image in png.........
        self.bottom_Image_obj = PhotoImage(
            master=self.window1, file=r".\miniprojectPL_pictures\SingIn_window\Bottom_Design.png")

        # 2.1)Creating obj of Label for image...........
        self.labelFor_bottom_Image = Label(self.window1,
                                           image=self.bottom_Image_obj,
                                           borderwidth=0,
                                           relief="flat",
                                           background="#2A475E")
        self.labelFor_bottom_Image.pack(side="bottom", fill="both")

        # 3)Creating obj for frame of main content.........
        self.frameFor_Contents = Frame(self.window1,
                                       relief="flat",
                                       background="#2A475E",
                                       width=351,
                                       height=390)
        self.frameFor_Contents.place(x=309, y=23)

        # 4)Creating obj for SIGNIN label...........
        self.labelFor_SIGNIN_written = Label(self.frameFor_Contents,
                                             text="Sign in",
                                             background="#2A475E",
                                             fg="#171A21",
                                             font=("Bungee", 34)
                                             )
        self.labelFor_SIGNIN_written.place(x=80, y=-37)

        # 5)Creating obj for some info label....
        self.labelFor_info_written = Label(self.frameFor_Contents,
                                           text="Enter your details below to signin succesfully!",
                                           background="#2A475E",
                                           fg="#171A21",
                                           font=("Bahnschrift", 13, "bold"))
        self.labelFor_info_written.place(x=-4, y=47)

        # 6)Creating obj for Email id label..........
        self.labelFor_EmailId_written = Label(self.frameFor_Contents,
                                              text="Email Address",
                                              background="#2A475E",
                                              fg="#C7D5E0",
                                              font=("Bahnschrift", 13))
        self.labelFor_EmailId_written.place(x=-1, y=106)

        # 6.1)Creating obj for Email Input of Entry class..........
        self.emailId_var = StringVar()
        self.emailId_entry = Entry(self.frameFor_Contents,
                                   textvariable=self.emailId_var,
                                   background="#1B2838",
                                   foreground="#66C0F4",
                                   width=38,
                                   relief="solid",
                                   font=("Bahnschrift", 12),
                                   insertborderwidth=10)
        self.emailId_entry.place(x=0, y=130)
        self.emailId_entry.focus_force()

        # 7)Creating obj for Password id label..........
        self.labelFor_Password_written = Label(self.frameFor_Contents,
                                               text="Password",
                                               background="#2A475E",
                                               fg="#C7D5E0",
                                               font=("Bahnschrift", 13))
        self.labelFor_Password_written.place(x=-1, y=177)

        # 7.2)Creating obj for Password Input of Entry class..........
        self.passwSignin_var = StringVar()
        self.passwSignin_entry = Entry(self.frameFor_Contents,
                                       textvariable=self.passwSignin_var,
                                       background="#1B2838",
                                       foreground="#66C0F4",
                                       width=38,
                                       relief="solid",
                                       font=("Bahnschrift", 12),
                                       highlightbackground="red",
                                       insertborderwidth=10,
                                       show="*")
        self.passwSignin_entry.place(x=0, y=201)

        # 7.3)Creating obj for eye for password label............
        self.photoFor_eye = PhotoImage(master=self.window1,
                                       file=r".\miniprojectPL_pictures\Signup_Window\Eye.png")
        self.labelFor_eye_password = Label(self.frameFor_Contents,
                                           image=self.photoFor_eye,
                                           background="#1B2838")
        self.labelFor_eye_password.place(x=320, y=203)
        self.labelFor_eye_password.bind("<Enter>", self.Password_to_normal)
        self.labelFor_eye_password.bind("<Leave>", self.Password_to_hidden)

        # 8)Creating obj for label of forget password..........
        self.messageFor_ForgetPassword = Label(self.frameFor_Contents,
                                               text="Forgot password?",
                                               font=("Bahnschrift",
                                                     11, "bold"),
                                               background="#2A475E",
                                               foreground="#171A21",
                                               cursor="hand2")
        self.messageFor_ForgetPassword.place(x=-1, y=282.5)  # x=198, y=265
        self.messageFor_ForgetPassword.bind("<Button-1>", self.forgotPassword)
        self.messageFor_ForgetPassword.bind(
            "<Enter>", self.changeForgetpassword_colorTo_red)
        self.messageFor_ForgetPassword.bind(
            "<Leave>", self.changeForgetpassword_colorTo_normal)

        # 9)Creating obj for Button..............
        self.buttonFor_Signin = Button(self.frameFor_Contents,
                                       text="Sign In",
                                       font=("Bahnschrift", 18, "bold"),
                                       width=25,
                                       bd=0,
                                       foreground="#171A21",
                                       background="#66C0F4",
                                       cursor="hand2",
                                       activebackground="#00A2FF",
                                       activeforeground="#C7D5E0",
                                       command=self.signIn_action)
        self.buttonFor_Signin.place(x=8, y=320)
        self.buttonFor_Signin.bind("<Enter>", self.Enter_signIn)
        self.buttonFor_Signin.bind("<Leave>", self.Leave_signIn)

        # 10)Creating obj for Checkbox of remember me............
        self.variableFor_RememberMe = StringVar(value="Don't")
        self.RememberMe_Checkbutton = Checkbutton(self.frameFor_Contents,
                                               text="Remember me",
                                               variable=self.variableFor_RememberMe,
                                               offvalue="Don't",
                                               onvalue="Yes",
                                               takefocus=0,
                                               cursor="hand2",
                                               font=("Bahnschrift", 10),
                                               background="#2A475E",
                                               foreground="#C7D5E0",
                                               activebackground="#2A475E",
                                               activeforeground="#C7D5E0",
                                               selectcolor="#1B2838")
        self.RememberMe_Checkbutton.place(x=-1, y=240.5)

        # Restart(*-*)To run infinite loop till some exit....
        self.window1.mainloop()

    #---------------Fucntions for Hover effect---------------#
    def Enter_signIn(self, e):
        self.buttonFor_Signin.configure(borderwidth=3,
                                        relief="solid",
                                        foreground="#C7D5E0")

    def Leave_signIn(self, e):
        self.buttonFor_Signin.configure(borderwidth=0,
                                        relief="flat",
                                        foreground="#171A21")

    # ...............Creating fuctions for forgotPassword....................................
    def SendPassword(self):
        countFor_emailRegistered = 0
        try:
            connection_obj = mc.connect(host="localhost",
                                        username="root",
                                        password="root",
                                        database="pyminiproject")
            cursor_obj = connection_obj.cursor()
            query = "select Password from signup_info where Email_address =%s"
            values = (self.emailId_var.get(),)
            cursor_obj.execute(query, values)
        except:
            messagebox.showerror("Try Again", "Not able to process info")
            self.window1.focus_force()
        else:
            for i in cursor_obj:
                countFor_emailRegistered = 1
                passwordIs = i[0]
        finally:
            connection_obj.close()
        if countFor_emailRegistered != 0:
            try:
                server = SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login("Your email address", "password")

                subject = "CovidInfo!Password is Here!"
                body = f"The password for your emailId.>>{passwordIs}"

                msg = f"Subject:{subject}\n\n{body}"
                server.sendmail('Your email address',
                                self.emailId_var.get(), msg)
                messagebox.showinfo(
                    "Email send", f"Password send on {self.emailId_var.get()}")
                self.emailId_entry.focus_force()
            except:
                messagebox.showerror("Error", "Something went wrong")
                self.emailId_entry.focus_force()
            finally:
                server.close()
        else:
            messagebox.showinfo("Email not Registered",
                                "Provide a registered email address")
            self.emailId_entry.focus_force()

    # -------------------------Creating Fuctions for these class---------------------------------------
    def forgotPassword(self, event):
        if self.emailId_var.get() != "":
            try:
                connection_obj = mc.connect(host="localhost",
                                            username="root",
                                            password="root",
                                            database="pyminiproject")
                cursor_obj = connection_obj.cursor()
                query = "select Email_address from signup_info where Email_address =%s"
                values = (self.emailId_var.get(),)
                cursor_obj.execute(query, values)
            except:
                print("error")
            else:
                value = cursor_obj.fetchone()
            if value != None:
                if messagebox.askyesno("Are you sure?", "Want your password Emailed to you!"):
                    self.emailId_entry.focus_force()
                    self.SendPassword()
                else:
                    self.emailId_entry.focus_force()
            else:
                messagebox.showinfo("Provide Email id",
                                    "Enter your registered email address")
                self.emailId_entry.focus_force()
        else:
            messagebox.showinfo("Provide Email id",
                                "Enter your registered email address")
            self.emailId_entry.focus_force()

    def changeForgetpassword_colorTo_red(self, event):
        self.messageFor_ForgetPassword.configure(foreground="red")

    def changeForgetpassword_colorTo_normal(self, event):
        self.messageFor_ForgetPassword.configure(foreground="#171A21")

    def Password_to_hidden(self, event):
        self.passwSignin_entry.configure(show="*")

    def Password_to_normal(self, event):
        self.passwSignin_entry.configure(show="")

    def putIn_signinDetails(self):
        try:
            connection_obj = mc.connect(host="localhost",
                                        username="root",
                                        password="root",
                                        database="pyminiproject")
            cursor_obj = connection_obj.cursor()
            query = "insert into signin_info values(%s,%s,%s)"
            values = (self.emailId_var.get(), date.today().strftime(
                "%d/%m/%Y"), datetime.now().strftime("%H:%M:%S"))
            cursor_obj.execute(query, values)
            connection_obj.commit()
        except:
            messagebox.showerror("Try Again", "Not able to process info")
            self.window1.focus_force()
        finally:
            connection_obj.close()

    def signIn_action(self):
        if self.emailId_var.get() != "" and self.passwSignin_var.get() != "":
            try:
                connection_obj = mc.connect(host="localhost",
                                            username="root",
                                            password="root",
                                            database="pyminiproject")
                cursor_obj = connection_obj.cursor()
                query = "select Email_address,Password from signup_info where Email_address =%s"
                values = (self.emailId_var.get(),)
                cursor_obj.execute(query, values)
            except:
                messagebox.showerror("Try Again", "Not able to process info")
                self.window1.focus_force()
            else:
                try:
                    for i in cursor_obj:
                        email = i[0]
                        password = i[1]
                    if self.emailId_var.get() == email and self.passwSignin_var.get() == password:
                        with open("Remember_me.txt","w") as rm:
                            rm.write(self.emailId_var.get()+"\n"+self.passwSignin_var.get())
                        self.putIn_signinDetails()
                        self.HomeObj.destroy()
                        arSignInwindow_obj = afterSignIn_mainWindow(
                            self.emailId_var.get())
                    else:
                        messagebox.showinfo(
                            "SignIn Failed!", "Email and Password doesn't match")
                        self.window1.focus_force()
                except:
                    messagebox.showinfo(
                        "Check email Address!", "Email address is not registered")
                    self.window1.focus_force()
            finally:
                connection_obj.close()
        else:
            messagebox.showinfo("Message", "Provide every details")
            self.window1.focus_force()


# Create_SignIn_Window = signin_mainWindow()
