from tkinter import Button, Entry, Label, StringVar, Tk, Toplevel, messagebox
import mysql.connector as mc
# import Createaccount_Window as cw


class EmailVerification_Window():
    def __init__(self, someObj,master=None) -> None:
        # print(.CofirmPassword_var.get())
        # 1)main window properties
        self.someObj = someObj
        self.window = Toplevel(master)
        self.window_width = 400
        self.window_height = 250
        self.x = (self.window.winfo_screenwidth()//2) - (self.window_width//2)
        self.y = (self.window.winfo_screenheight()//2) - \
            (self.window_height//2)
        self.window.geometry(
            f"{self.window_width}x{self.window_height}+{self.x}+{self.y}")
        self.window.resizable(0, 0)
        self.window.title("Email validation")
        self.window.iconbitmap(r".\miniprojectPL_pictures\Main_icon.ico")
        self.window.configure(background="#2A475E")

        # 2)label for message...........
        self.label_for_Message = Label(self.window,
                                       text=f"Enter the OTP send on {self.someObj.EmailAddress_var.get()} to continue",
                                       font=("Bahnschrift", 10, "bold"),
                                       background="#2A475E",
                                       foreground="#C7D5E0")
        self.label_for_Message.pack(side="top", pady=28)

        # 3)Entry for otp recieved............
        self.OtpRecieved_var = StringVar()
        self.OtpRecieved_entry = Entry(self.window,
                                       textvariable=self.OtpRecieved_var,
                                       background="#1B2838",
                                       foreground="#66C0F4",
                                       width=10,
                                       relief="solid",
                                       font=("Bahnschrift", 25),
                                       highlightbackground="red",
                                       insertborderwidth=10,
                                       justify="center")
        self.OtpRecieved_entry.place(x=110, y=90)
        self.OtpRecieved_entry.focus_force()

        # 4)Button for verify..........
        self.Verify_Button = Button(self.window,
                                    text="Verify",
                                    background="#66C0F4",
                                    foreground="#171A21",
                                    cursor="hand2",
                                    font=("Bahnschrift", 14, "bold"),
                                    activebackground="#00A2FF",
                                    activeforeground="#C7D5E0",
                                    relief="solid",
                                    width=20,
                                    command=self.verifyOtp)
        self.Verify_Button.pack(side="bottom", anchor="center", pady=15)

        # -1)Mainloop
        self.window.mainloop()

    # ----------------Fuction of these class------------------------#
    def PutInDatabase(self):
        try:
            connection_obj = mc.connect(host="localhost",
                                        username="root",
                                        password="root",
                                        database="pyminiproject")
            cursor_obj = connection_obj.cursor()
            query = "insert into pyminiproject.signup_info values(%s,%s,%s,%s)"
            values = (self.someObj.FirstName_var.get(), self.someObj.LastName_var.get(
            ), self.someObj.EmailAddress_var.get(), self.someObj.Password_var.get())
            cursor_obj.execute(query, values)
            connection_obj.commit()
        except:
            messagebox.showerror("Try Again", "Not able to process info")
            self.OtpRecieved_entry.focus_force()
        finally:
            cursor_obj.close()

    def verifyOtp(self):
        if self.someObj.otpNumber == self.OtpRecieved_var.get():
            self.PutInDatabase()
            self.window.destroy()
            messagebox.showinfo("Succesfull Singup","You can Signin now!")
        else:
            messagebox.showinfo("Verfication failed", "OTP doesn't match")
            self.OtpRecieved_entry.focus_force()

# emailverification_obj = EmailVerification_Window(12)