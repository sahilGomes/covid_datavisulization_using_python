import smtplib
from math import floor
from random import random
from tkinter import (Button, Checkbutton, Entry, Frame, Label, PhotoImage,
                     StringVar, Toplevel, messagebox, ttk)
import mysql.connector as mc

import Email_verification_Window as evw
from SignIn_Window import signin_mainWindow


class CreateAccount_Window():
    '''Its is window of Create account'''

    def __init__(self, master=None) -> None:
        # 1)defining CreateAccount_Window properties......
        self.window = Toplevel(master)
        self.window_width = 970
        self.window_height = 614
        self.x = (self.window.winfo_screenwidth()//2) - (self.window_width//2)
        self.y = (self.window.winfo_screenheight()//2) - \
            (self.window_height//2)
        self.window.geometry(
            f"{self.window_width}x{self.window_height}+{self.x}+{self.y}")
        self.window.resizable(0, 0)
        self.window.title("Welcome to Signup page")
        self.window.iconbitmap(r".\miniprojectPL_pictures\Main_icon.ico")
        self.window.configure(background="#2A475E")
        self.HomeObj = master

        # 2)Creating obj for frame of left-side Picture.........
        self.frameFor_Left_Contents = Frame(self.window,
                                            relief="flat",
                                            background="#2A475E",
                                            width=266,
                                            height=614,
                                            borderwidth=0
                                            )
        self.frameFor_Left_Contents.place(x=0, y=0)

        # 3)Creating obj of photo..............
        self.photoObjFor_side = PhotoImage(master=self.frameFor_Left_Contents,
                                           file=r".\miniprojectPL_pictures\Signup_Window\LinesDesign.png")

        # 4)Creating obj for label for photo display..............
        self.labelFor_photo = Label(self.frameFor_Left_Contents,
                                    image=self.photoObjFor_side,
                                    relief="flat",
                                    borderwidth=0)
        self.labelFor_photo.place(x=0, y=0)

        # 5)Creating obj for frame of right side contents.............
        self.frameFor_Right_Contents = Frame(self.window,
                                             relief="flat",
                                             background="#2A475E",
                                             width=493,
                                             height=534.72,
                                             borderwidth=0)
        self.frameFor_Right_Contents.place(x=372, y=40)

        # 6)Creating obj for Create your account label.........
        self.labelFor_Create_youraccount = Label(self.frameFor_Right_Contents,
                                                 relief="flat",
                                                 borderwidth=0,
                                                 text="Create your account",
                                                 font=("Bungee", 16),
                                                 background="#2A475E",
                                                 foreground="#C7D5E0")
        self.labelFor_Create_youraccount.place(x=0, y=0)

        # 7)Creating obj for some info label.........
        self.labelFor_someInfo = Label(self.frameFor_Right_Contents,
                                       relief="flat",
                                       borderwidth=0,
                                       text="Provide your proper details",
                                       font=("Bahnschrift", 10),
                                       background="#2A475E",
                                       foreground="#C7D5E0")
        self.labelFor_someInfo.place(x=0, y=36.62)

        # 8)Creating obj for FirstName label..........
        self.FirstName_written = Label(self.frameFor_Right_Contents,
                                       text="First Name",
                                       background="#2A475E",
                                       fg="#C7D5E0",
                                       font=("Bahnschrift", 11))
        self.FirstName_written.place(x=0, y=90)

        # 8.1)Creating obj for FirstName Input of Entry class..........
        self.FirstName_var = StringVar()
        self.FirstName_entry = Entry(self.frameFor_Right_Contents,
                                     textvariable=self.FirstName_var,
                                     background="#1B2838",
                                     foreground="#66C0F4",
                                     width=54,
                                     relief="solid",
                                     font=("Bahnschrift", 12),
                                     highlightbackground="red",
                                     insertborderwidth=10)
        self.FirstName_entry.place(x=0, y=110.74)
        self.FirstName_entry.focus_force()

        # 9)Creating obj for LastName label ...............
        self.LastName_written = Label(self.frameFor_Right_Contents,
                                      text="Last Name",
                                      background="#2A475E",
                                      fg="#C7D5E0",
                                      font=("Bahnschrift", 11))
        self.LastName_written.place(x=0, y=149.9)

        # 9.1)Creating obj for LastName Input of Entry class..........
        self.LastName_var = StringVar()
        self.LastName_entry = Entry(self.frameFor_Right_Contents,
                                    textvariable=self.LastName_var,
                                    background="#1B2838",
                                    foreground="#66C0F4",
                                    width=54,
                                    relief="solid",
                                    font=("Bahnschrift", 12),
                                    highlightbackground="red",
                                    insertborderwidth=10)
        self.LastName_entry.place(x=0, y=170.74)

        # 10)Creating obj for Email address label...........
        self.EmailAddress_written = Label(self.frameFor_Right_Contents,
                                          text="Email Address",
                                          background="#2A475E",
                                          fg="#C7D5E0",
                                          font=("Bahnschrift", 11))
        self.EmailAddress_written.place(x=0, y=210.6)

        # 10.1)Creating obj for EmailAddress Input of Entry calss...........
        self.EmailAddress_var = StringVar()
        self.EmailAddress_entry = Entry(self.frameFor_Right_Contents,
                                        textvariable=self.EmailAddress_var,
                                        background="#1B2838",
                                        foreground="#66C0F4",
                                        width=54,
                                        relief="solid",
                                        font=("Bahnschrift", 12),
                                        highlightbackground="red",
                                        insertborderwidth=10)
        self.EmailAddress_entry.place(x=0, y=230.60)

        # 11)Creating obj for Password label...........
        self.Password_written = Label(self.frameFor_Right_Contents,
                                      text="Password",
                                      background="#2A475E",
                                      fg="#C7D5E0",
                                      font=("Bahnschrift", 11))
        self.Password_written.place(x=0, y=264.83)

        # 11.1)Creating obj for Password Input Entry ............
        self.Password_var = StringVar()
        self.Password_entry = Entry(self.frameFor_Right_Contents,
                                    textvariable=self.Password_var,
                                    background="#1B2838",
                                    foreground="#66C0F4",
                                    width=54,
                                    relief="solid",
                                    font=("Bahnschrift", 12),
                                    highlightbackground="red",
                                    insertborderwidth=10,
                                    show="*")
        self.Password_entry.place(x=0, y=285.90)

        # 12)Creating obj for Confirm Password label...........
        self.ConfirmPassword_written = Label(self.frameFor_Right_Contents,
                                             text="Confirm Password",
                                             background="#2A475E",
                                             fg="#C7D5E0",
                                             font=("Bahnschrift", 11))
        self.ConfirmPassword_written.place(x=0, y=318.37)

        # 12.1)Creating obj for Password Input Entry ............
        self.CofirmPassword_var = StringVar()
        self.ConfirmPassword_entry = Entry(self.frameFor_Right_Contents,
                                           textvariable=self.CofirmPassword_var,
                                           background="#1B2838",
                                           foreground="#66C0F4",
                                           width=54,
                                           relief="solid",
                                           font=("Bahnschrift", 12),
                                           highlightbackground="red",
                                           insertborderwidth=10,
                                           show="*")
        self.ConfirmPassword_entry.place(x=0, y=337.90)

        # 13)Already have an account label..............
        self.label_AlreadyAccount_info = Label(self.frameFor_Right_Contents,
                                               text="Already have an account?",
                                               background="#2A475E",
                                               foreground="#C7D5E0",
                                               borderwidth=0,
                                               relief="flat",
                                               font=("Bahnschrift", 12))
        self.label_AlreadyAccount_info.place(x=0, y=510.72)

        # 14)Creating Radio for check button.......
        self.variableFor_CheckPassword_radio = StringVar(value="not equal")
        self.CheckPassword_radio = Checkbutton(self.frameFor_Right_Contents,
                                               text="Check match for Password-Confirm Password",
                                               variable=self.variableFor_CheckPassword_radio,
                                               offvalue="not equal",
                                               onvalue="equal",
                                               takefocus=0,
                                               cursor="hand2",
                                               command=self.CheckPassword_method,
                                               font=("Bahnschrift", 10),
                                               background="#2A475E",
                                               foreground="#C7D5E0",
                                               activebackground="#2A475E",
                                               activeforeground="#C7D5E0",
                                               selectcolor="#1B2838")
        self.CheckPassword_radio.place(x=0, y=390.39)

        # 15)Creating Signup button...............
        self.SignUp_button = Button(self.frameFor_Right_Contents,
                                    text="Continue",
                                    font=("Bahnschrift", 14, "bold"),
                                    borderwidth=0,
                                    relief="flat",
                                    background="#66C0F4",
                                    foreground="#171A21",
                                    cursor="hand2",
                                    activebackground="#00A2FF",
                                    activeforeground="#C7D5E0",
                                    width=15,
                                    command=self.Continue_singup)
        self.SignUp_button.place(x=0, y=420)
        self.SignUp_button.bind("<Enter>",self.Enter_signUp)
        self.SignUp_button.bind("<Leave>",self.Leave_signUp)

        # 16)Creating Signin button .............
        self.photoFor_arrow = PhotoImage(master=self.frameFor_Right_Contents,
                                         file="miniprojectPL_pictures/Signup_Window/arrow.png")
        self.Signin_button = Button(self.frameFor_Right_Contents,
                                    image=self.photoFor_arrow,
                                    compound="right",
                                    text="Signin",
                                    font=("Bahnschrift", 12, "bold"),
                                    borderwidth=0,
                                    relief="flat",
                                    background="#66C0F4",
                                    foreground="#171A21",
                                    cursor="hand2",
                                    activebackground="#00A2FF",
                                    activeforeground="#C7D5E0",
                                    width=80,
                                    command=self.OpenSignin_Window)
        self.Signin_button.place(x=189, y=508.72)
        self.Signin_button.bind("<Enter>",self.Enter_signIn)
        self.Signin_button.bind("<Leave>",self.Leave_signIn)

        # 17)Creating Eye symbolLabel for Password................
        self.photoFor_eye = PhotoImage(master=self.frameFor_Right_Contents,
                                       file="miniprojectPL_pictures/Signup_Window/Eye.png")
        self.labelFor_eye_password = Label(self.frameFor_Right_Contents,
                                           image=self.photoFor_eye,
                                           background="#1B2838",
                                           cursor="")
        self.labelFor_eye_password.place(x=464, y=287.80)
        self.labelFor_eye_password.bind(
            "<Enter>", self.changePassword_to_normal)
        self.labelFor_eye_password.bind(
            "<Leave>", self.changePassword_to_hidden)

        # 18)Creating Eye symbolLabel for Password................
        self.labelFor_eye_Confirmpassword = Label(self.frameFor_Right_Contents,
                                                  image=self.photoFor_eye,
                                                  background="#1B2838")
        self.labelFor_eye_Confirmpassword.place(x=464, y=339.80)
        self.labelFor_eye_Confirmpassword.bind(
            "<Enter>", self.changeConfirmPassword_to_normal)
        self.labelFor_eye_Confirmpassword.bind(
            "<Leave>", self.changeConfirmPassword_to_hidden)

        # Restart(*-*)To run infinite loop till some exit....
        self.window.mainloop()
    
    #--------------Fuctions for Hover Effect----------------#
    #1]
    def Enter_signIn(self, e):
        self.Signin_button.configure(borderwidth=1,
                                        relief="solid",
                                        foreground="#C7D5E0")

    def Leave_signIn(self, e):
        self.Signin_button.configure(borderwidth=0,
                                        relief="flat", 
                                        foreground="#171A21")
                                    
    #2]
    def Enter_signUp(self,e):
        self.SignUp_button.configure(borderwidth=3,
                                        relief="solid",
                                        foreground="#C7D5E0")
    
    def Leave_signUp(self,e):
        self.SignUp_button.configure(borderwidth=0,
                                        relief="flat", 
                                        foreground="#171A21")

    # ------------------------creating fuctions of these class---------------------- #
    def changePassword_to_normal(self, event):
        self.Password_entry.configure(show="")

    def changePassword_to_hidden(self, event):
        self.Password_entry.configure(show="*")

    def changeConfirmPassword_to_normal(self, event):
        self.ConfirmPassword_entry.configure(show="")

    def changeConfirmPassword_to_hidden(self, event):
        self.ConfirmPassword_entry.configure(show="*")

    def OpenSignin_Window(self):
        self.window.destroy()
        global Create_SignIn_Window
        Create_SignIn_Window = signin_mainWindow(self.HomeObj)

    def CheckPassword_method(self):
        if self.Password_var.get() != "" and self.CofirmPassword_var.get() != "":
            if self.Password_var.get() == self.CofirmPassword_var.get():
                self.CheckPassword_radio.configure(
                    text="Check match for Password-Confirm Password(MATCHED)")
                # self.CheckPassword_radio.configure(state="disabled")
            else:
                messagebox.showinfo("Check password options",
                                    "Password and Confirm Password doesn\'t match")
                self.Password_entry.focus_force()
                self.CheckPassword_radio.configure(
                    text="Check match for Password-Confirm Password")
                self.variableFor_CheckPassword_radio.set("not equal")

        else:
            messagebox.showinfo("Check password options",
                                "Some field is empty")

            self.Password_entry.focus_force()
            self.variableFor_CheckPassword_radio.set("not equal")
            self.CheckPassword_radio.configure(
                text="Check match for Password-Confirm Password")

# Class methods for continue.............

    def otp(self):
        digits = "0123456789"
        OTP = ""
        for i in range(4):
            OTP += digits[floor(random() * 10)]

        return OTP

    def sendMail(self):
        count = 0
        try:
            self.otpNumber = self.otp()
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login("Your email", "Password")

            subject = "Please enter the provided otp for verification!"
            body = f"The one time password is {self.otpNumber}.Enter this for verification"

            msg = f"Subject:{subject}\n\n{body}"
            server.sendmail('Your email',
                            self.EmailAddress_var.get(), msg)
            messagebox.showinfo(
                "Email send", f"OTP send on {self.EmailAddress_var.get()}")
        except:
            messagebox.showerror("Error", "Provide valid email address")
            self.EmailAddress_entry.focus_force()
        else:
            count = 1
        finally:
            server.close()
        return count

    def CheckIf_emailRegistered(self):
        try:
            connection_obj = mc.connect(host="localhost",
                                        username="root",
                                        password="root",
                                        database="pyminiproject")
            cursor_obj = connection_obj.cursor()
            query = "select Email_address from signup_info where Email_address =%s"
            values = (self.EmailAddress_var.get(),)
            cursor_obj.execute(query, values)
        except:
            messagebox.showerror("Try Again", "Not able to process info")
            self.FirstName_entry.focus_force()
        else:
            for i in cursor_obj:
                email = i[0]
                return email
        finally:
            cursor_obj.close()

    def Continue_singup(self):
        if(self.FirstName_var.get() != "" and self.LastName_var.get() != "" and self.EmailAddress_var.get() != "" and self.Password_var.get() != "" and self.variableFor_CheckPassword_radio.get() == "equal"):
            check = self.CheckIf_emailRegistered()
            if check != self.EmailAddress_var.get():
                move = self.sendMail()
                if move == 1:
                    self.window.destroy()
                    emailverification_obj = evw.EmailVerification_Window(
                        self, self.HomeObj)
            else:
                messagebox.showerror(
                    "Email already register!", "Provide another email address")
                self.EmailAddress_entry.focus_force()
        else:
            messagebox.showerror("Error", "Provide every required details")
            self.FirstName_entry.focus_force()

# Create_Account_Window = CreateAccount_Window()
