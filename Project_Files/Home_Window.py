from datetime import date, datetime
import webbrowser
from tkinter import Button, Frame, Label, PhotoImage, Tk, Toplevel, messagebox
from Createaccount_Window import CreateAccount_Window
import mysql.connector as mc
from AfterSignin_window import afterSignIn_mainWindow
from SignIn_Window import signin_mainWindow
from os.path import exists

class CreateHome_Window():
    '''It creates home window1'''

    def __init__(self) -> None:
        # 1)defining CreateAccount_Window properties......
        self.exits = exists(r"Remember_me.txt")
        if self.exits == False:
            self.rm = open("Remember_me.txt","w")
            self.rm.close()
        if exists(r"Remember_me.txt"):
            with open("Remember_me.txt","r+") as rm:
                self.check = rm.readline().strip()
            if self.check == "":
                self.window1 = Tk()
                self.window1.minsize(width=1200, height=614)
                self.window1.geometry("1200x614+2+2")
                self.window1.state("zoomed")
                self.window1.title("Welcome to CovidInfo")
                self.window1.iconbitmap(r".\miniprojectPL_pictures\Main_icon.ico")
                self.window1.protocol("WM_DELETE_WINDOW", self.on_closing)

                # 2)Creating Frame for left content.................
                self.frameFor_Left_Contents = Frame(self.window1,
                                                    relief="flat",
                                                    background="#2A475E",
                                                    width=323,
                                                    borderwidth=0
                                                    )
                self.frameFor_Left_Contents.pack(side="left", fill="y")

                # 3)Creating Frame for bottom content.................
                self.frameFor_Bottom_Contents = Frame(self.window1,
                                                    relief="flat",
                                                    background="#171A21",
                                                    #   width=266,
                                                    height=173,
                                                    borderwidth=0
                                                    )
                self.frameFor_Bottom_Contents.pack(side="bottom", fill="x")

                # 4)Creating Frame for Right content.................
                self.frameFor_Right_Contents = Frame(self.window1,
                                                    relief="flat",
                                                    background="#1B2838",
                                                    #  width=1213,
                                                    height=780,
                                                    borderwidth=0
                                                    )
                self.frameFor_Right_Contents.pack(side="top", fill="both")

                # 5)Creating Signin button ................
                self.imageFor_signinButton = PhotoImage(
                    file=r".\miniprojectPL_pictures\HomePage\ActionButtons\LoginButthon.png")
                self.SignIn_button = Button(self.frameFor_Left_Contents,
                                            image=self.imageFor_signinButton,
                                            width=287,
                                            height=52,
                                            borderwidth=0,
                                            cursor="hand2",
                                            background="#2A475E",
                                            activebackground="#2A475E",
                                            command=self.OpenSignin_Window)
                self.SignIn_button.place(x=18, y=27)
                self.SignIn_button.bind("<Enter>", self.Enter_signin)
                self.SignIn_button.bind("<Leave>", self.Leave_signin)

                # 6)Creating CreateAccount button ................
                self.imageFor_CreateAccount = PhotoImage(
                    file=r".\miniprojectPL_pictures\HomePage\ActionButtons\CreateAccount.png")
                self.CreateAccount_button = Button(self.frameFor_Left_Contents,
                                                image=self.imageFor_CreateAccount,
                                                width=287,
                                                height=52,
                                                borderwidth=0,
                                                cursor="hand2",
                                                background="#2A475E",
                                                activebackground="#2A475E",
                                                command=self.OpenCreateAccount_Window)
                self.CreateAccount_button.place(x=18, y=102)
                self.CreateAccount_button.bind("<Enter>", self.Enter_CreateAccount)
                self.CreateAccount_button.bind("<Leave>", self.Leave_CreateAccount)

                # 7)Creating Help Button...............
                self.imageFor_HelpButton = PhotoImage(
                    file=r".\miniprojectPL_pictures\HomePage\ActionButtons\Helpbutton.png")
                self.HelpButton_button = Button(self.frameFor_Left_Contents,
                                                image=self.imageFor_HelpButton,
                                                width=287,
                                                height=52,
                                                borderwidth=0,
                                                cursor="hand2",
                                                background="#2A475E",
                                                activebackground="#2A475E",
                                                command=self.Openwebbrowser)
                self.HelpButton_button.place(x=18, y=177)
                self.HelpButton_button.bind("<Enter>",self.Enter_Help)
                self.HelpButton_button.bind("<Leave>",self.Leave_Help)

                # 8)Sage Image label...................
                self.imageLeft_side = PhotoImage(
                    file=r".\miniprojectPL_pictures\HomePage\Sage.png")
                self.labelFor_leftImage = Label(self.frameFor_Left_Contents,
                                                image=self.imageLeft_side,
                                                background="#2A475E")
                self.labelFor_leftImage.place(x=15.95, y=246.38)

                # 9)SaGo label....................
                self.sago_label = Label(self.frameFor_Left_Contents,
                                        text="SaGo©2022-2023",
                                        background="#2A475E",
                                        foreground="#66C0F4",
                                        font=("Microsoft Sans Serif", 10))
                self.sago_label.pack(side="bottom", padx=107)

                # 10)Creating Frame and image labels for bottom part...........
                # 1]
                self.bottom1_image = PhotoImage(
                    file=r".\miniprojectPL_pictures\HomePage\bottom\Wear Mask.png")
                self.bottom1_labelFor_image = Label(self.frameFor_Bottom_Contents,
                                                    image=self.bottom1_image,
                                                    background="#171A21")
                self.bottom1_labelFor_image.pack(side="left", padx=80)
                # 2]
                self.bottom2_image = PhotoImage(
                    file=r".\miniprojectPL_pictures\HomePage\bottom\Wash hands.png")
                self.bottom2_labelFor_image = Label(self.frameFor_Bottom_Contents,
                                                    image=self.bottom2_image,
                                                    background="#171A21")
                self.bottom2_labelFor_image.pack(side="left")
                # 3]
                self.bottom3_image = PhotoImage(
                    file=r".\miniprojectPL_pictures\HomePage\bottom\Use Sanitizer.png")
                self.bottom3_labelFor_image = Label(self.frameFor_Bottom_Contents,
                                                    image=self.bottom3_image,
                                                    background="#171A21")
                # 4]
                self.bottom4_image = PhotoImage(
                    file=r".\miniprojectPL_pictures\HomePage\bottom\Keep Social Distanc.png")
                self.bottom4_labelFor_image = Label(self.frameFor_Bottom_Contents,
                                                    image=self.bottom4_image,
                                                    background="#171A21")
                # 5]
                self.bottom5_image = PhotoImage(
                    file=r".\miniprojectPL_pictures\HomePage\bottom\Stay in Home.png")
                self.bottom5_labelFor_image = Label(self.frameFor_Bottom_Contents,
                                                    image=self.bottom5_image,
                                                    background="#171A21")
                self.bottom5_labelFor_image.pack(side="right", padx=80)
                self.bottom4_labelFor_image.pack(side="right")
                self.bottom3_labelFor_image.pack(anchor="center")

                # Creating chains for right frame................
                self.image_forChains = PhotoImage(master=self.frameFor_Right_Contents,
                                                file=r".\miniprojectPL_pictures\HomePage\Chain.png")
                # 1]chain left
                self.LeftchainImage_label = Label(self.frameFor_Right_Contents,
                                                image=self.image_forChains,
                                                borderwidth=0,
                                                background="#1B2838")
                self.LeftchainImage_label.place(x=147, y=0)
                # 2]chain right
                self.RightchainImage_label = Label(self.frameFor_Right_Contents,
                                                image=self.image_forChains,
                                                borderwidth=0,
                                                background="#1B2838")
                self.RightchainImage_label.place(x=1021, y=0)

                # 11)Creating frame for image..............
                self.FrameFor_images = Frame(self.frameFor_Right_Contents,
                                            width=1145,
                                            height=550,
                                            background="#1B2838",
                                            borderwidth=0)
                self.FrameFor_images.pack(
                    anchor="center", padx=29, pady=43, fill="both")

                # 12)Creating label for images.........
                self.listOf_images = [r".\miniprojectPL_pictures\HomePage\Images_For_home\first.png",r".\miniprojectPL_pictures\HomePage\Images_For_home\second.png",r".\miniprojectPL_pictures\HomePage\Images_For_home\Third.png",
                r".\miniprojectPL_pictures\HomePage\Images_For_home\Fourth.png",r".\miniprojectPL_pictures\HomePage\Images_For_home\fifth.png"]
                self.Counterof_listIndex = 0
                self.labelFor_MainImages = Label(self.FrameFor_images,
                                                background="#171A21",
                                                width=1145,
                                                height=528,
                                                borderwidth=4,
                                                relief="ridge")
                self.labelFor_MainImages.place(x=0, y=0)
                self.ImageMethod_call()

                # Restart(*-*)To run infinite loop till some exit....
                self.window1.mainloop()
            else:
                with open("Remember_me.txt","r") as rm:
                    self.email = rm.readline().strip()
                    self.password = rm.readline().strip()
                try:
                    connection_obj = mc.connect(host="localhost",
                                                username="root",
                                                password="root",
                                                database="pyminiproject")
                    cursor_obj = connection_obj.cursor()
                    query = "select Email_address,Password from signup_info where Email_address =%s"
                    values = (self.email,)
                    cursor_obj.execute(query, values)
                except:
                    messagebox.showerror("Try Again", "Not able to process info")
                    self.window1.focus_force()
                else:
                    try:
                        for i in cursor_obj:
                            email = i[0]
                            password = i[1]
                        if self.email == email and self.password == password:
                            with open("Remember_me.txt","w") as rm:
                                rm.write(self.email+"\n"+self.password)
                            
                            try:
                                connection_obj = mc.connect(host="localhost",
                                                            username="root",
                                                            password="root",
                                                            database="pyminiproject")
                                cursor_obj = connection_obj.cursor()
                                query = "insert into signin_info values(%s,%s,%s)"
                                values = (self.email, date.today().strftime(
                                    "%d/%m/%Y"), datetime.now().strftime("%H:%M:%S"))
                                cursor_obj.execute(query, values)
                                connection_obj.commit()
                            except:
                                messagebox.showerror("Try Again", "Not able to process info")
                                self.window1.focus_force()
                            finally:
                                connection_obj.close()
                            arSignInwindow_obj = afterSignIn_mainWindow(
                                self.email)
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

    #-------------Methods for Hover Effects------------------#
    # 1]
    def Enter_signin(self, e):
        self.EnterSignin_Img = PhotoImage(
            file=r".\miniprojectPL_pictures\HomePage\AcionButton_OnHover\SinginHover.png")
        self.SignIn_button.configure(image=self.EnterSignin_Img)
                #-----------#
    def Leave_signin(self, e):
        self.SignIn_button.configure(image=self.imageFor_signinButton)

    # 2]
    def Enter_CreateAccount(self, e):
        self.EnterCreateAccount_Img = PhotoImage(
            file=r".\miniprojectPL_pictures\HomePage\AcionButton_OnHover\CreateAccoutnHover.png")
        self.CreateAccount_button.configure(image=self.EnterCreateAccount_Img)
                #----------#
    def Leave_CreateAccount(self, e):
        self.CreateAccount_button.configure(image=self.imageFor_CreateAccount)

    # 3]
    def Enter_Help(self, e):
        self.EnterSign_Img = PhotoImage(
            file=r".\miniprojectPL_pictures\HomePage\AcionButton_OnHover\NeedHelpHover.png")
        self.HelpButton_button.configure(image=self.EnterSign_Img)
                #-----------#
    def Leave_Help(self, e):
        self.HelpButton_button.configure(image=self.imageFor_HelpButton)

    #-------------Methods for these class-------------#

    def on_closing(self):
        if messagebox.askyesno("Quit", "Do you want to quit?"):
            self.window1.destroy()

    def OpenSignin_Window(self):
        self.Create_SignIn_Window = signin_mainWindow(self.window1)

    def OpenCreateAccount_Window(self):
        self.Create_Account_Window = CreateAccount_Window(self.window1)

    def ImageMethod_call(self):
        self.photoFor_labelof_mainImages = PhotoImage(master=self.FrameFor_images,
                                                      file=self.listOf_images[self.Counterof_listIndex])
        self.labelFor_MainImages.configure(
            image=self.photoFor_labelof_mainImages)
        self.Counterof_listIndex += 1
        if self.Counterof_listIndex > 4:
            self.Counterof_listIndex = 0
        self.window1.after(3500, self.ImageMethod_call)

    def Openwebbrowser(self):
        webbrowser.open_new(
            r".\Needhelp.html")

# Create_Home_Window = CreateHome_Window()
