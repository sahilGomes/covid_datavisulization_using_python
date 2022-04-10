import warnings
from tkinter import (Button, Entry, Frame, Label, PhotoImage, StringVar, Tk,
                     font, messagebox)
from tkinter.ttk import Combobox, Style


import mysql.connector as mc
import pandas as pd
from matplotlib import ticker
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.dates import DateFormatter, WeekdayLocator
from matplotlib.figure import Figure
from matplotlib.pyplot import axis
from mysql.connector.locales.eng import client_error

import Home_Window

warnings.filterwarnings("ignore")


class afterSignIn_mainWindow():
    '''It is the afterSingin window'''

    def __init__(self, UserName) -> None:
        # -> 1)Creating main window and its properties
        self.window1 = Tk()
        self.window1.minsize(width=1200, height=614)
        self.window1.geometry("1200x614+2+2")
        self.window1.state("zoomed")
        self.window1.title("Welcome to CovidInfo")
        self.window1.iconbitmap(r".\miniprojectPL_pictures\Main_icon.ico")
        self.window1.protocol("WM_DELETE_WINDOW", self.emptyFile)
        self.UserName = UserName

        # -> 2)Creating Navigation Panel Frame
        self.NavFrame = Frame(self.window1,
                              background="#1B2838",
                              width=122,
                              borderwidth=0)
        self.NavFrame.pack(side="left", fill="y")

        # 2.1)Creating Label for Blue image
        self.BlueImage = PhotoImage(
            master=self.NavFrame, file=r".\miniprojectPL_pictures\AfterSingin Page\Navigation Pannel\Blue_background.png")
        self.BlueLabel = Label(self.NavFrame,
                               image=self.BlueImage,
                               background="#1B2838")
        self.BlueLabel.place(x=7, y=10)

        # 2.2)Creating Images of Navigation panel
        # 1]
        self.HomeImage = PhotoImage(
            master=self.NavFrame, file=r".\miniprojectPL_pictures\AfterSingin Page\Navigation Pannel\Home.png")
        self.HomeButton_label = Button(self.NavFrame,
                                       image=self.HomeImage,
                                       background="#66C0F4",
                                       borderwidth=0,
                                       activebackground="#66C0F4",
                                       cursor="hand2",
                                       command=self.HomeButton_method)
        self.HomeButton_label.place(x=18, y=238)
        # 2]
        self.SettingImage = PhotoImage(
            master=self.NavFrame, file=r".\miniprojectPL_pictures\AfterSingin Page\Navigation Pannel\Settings.png")
        self.SettingImage_label = Button(self.NavFrame,
                                         image=self.SettingImage,
                                         background="#66C0F4",
                                         borderwidth=0,
                                         activebackground="#66C0F4",
                                         cursor="hand2",
                                         command=self.SettingButton_method)
        self.SettingImage_label.place(x=18, y=357)
        # 3]
        self.SignoutImage = PhotoImage(
            master=self.NavFrame, file=r".\miniprojectPL_pictures\AfterSingin Page\Navigation Pannel\Signout.png")
        self.SignoutImage_label = Button(self.NavFrame,
                                         image=self.SignoutImage,
                                         background="#66C0F4",
                                         borderwidth=0,
                                         activebackground="#66C0F4",
                                         cursor="hand2",
                                         command=self.SignOut_method)
        self.SignoutImage_label.place(x=18, y=476)
        # 4]
        self.CircleImage = PhotoImage(
            master=self.NavFrame, file=r".\miniprojectPL_pictures\AfterSingin Page\Navigation Pannel\Circle.png")
        self.CircleImage_label = Label(self.NavFrame,
                                       image=self.CircleImage,
                                       background="#66C0F4",
                                       borderwidth=0)
        self.CircleImage_label.place(x=18, y=34)
        #------#
        try:
            connection_obj = mc.connect(host="localhost",
                                        username="root",
                                        password="root",
                                        database="pyminiproject")
            cursor_obj = connection_obj.cursor()
            query = "select First_Name,Last_Name,Password from signup_info where Email_address =%s"
            values = (self.UserName,)
            cursor_obj.execute(query, values)
        except:
            print('Error')
        else:
            self.name_last_tuple = cursor_obj.fetchone()
            self.firstName = self.name_last_tuple[0]
            self.lastName = self.name_last_tuple[1]
            self.Password = self.name_last_tuple[2]
        self.NameInitial_letter = Label(self.NavFrame,
                                        text=self.firstName[0] +
                                        self.lastName[0],
                                        background="#C7D5E0",
                                        foreground="#09496D",
                                        font=("Bungee", 19, "bold"))
        self.NameInitial_letter.place(x=38, y=40)

        # 5]Hover Effect...
        self.CircleImage_label.bind("<Enter>", self.Enter_CircleImage)
        self.CircleImage_label.bind("<Leave>", self.Leave_CircleImage)
        self.HomeButton_label.bind("<Enter>", self.Enter_HomeButton)
        self.HomeButton_label.bind("<Leave>", self.Leave_HomeButton)
        self.SettingImage_label.bind("<Enter>", self.Enter_SettingButton)
        self.SettingImage_label.bind("<Leave>", self.Leave_SettingButton)
        self.SignoutImage_label.bind("<Enter>", self.Enter_SingOutButton)
        self.SignoutImage_label.bind("<Leave>", self.Leave_SingOutButton)

        # -> 3)Creating Right Frame a...........
        self.CreateRight_frame()

        # -> -1)to run the mainloop()
        self.window1.mainloop()

    # Methods of Hover Label over Navbar................
    # 1]
    def Enter_HomeButton(self, event):
        self.textHome = Label(self.window1,
                              text="Home",
                              background="#1B2838",
                              font=("Bahnschrift", 15, "bold"),
                              foreground='#C7D5E0',
                              borderwidth=2,
                              relief="ridge")
        self.textHome.place(x=115, y=265)

    def Leave_HomeButton(self, event):
        self.textHome.destroy()

    # 2]
    def Enter_SettingButton(self, event):
        self.textSetting = Label(self.window1,
                                 text="Settings",
                                 background="#1B2838",
                                 font=("Bahnschrift", 15, "bold"),
                                 foreground='#C7D5E0',
                                 borderwidth=2,
                                 relief="ridge")
        self.textSetting.place(x=115, y=387)

    def Leave_SettingButton(self, event):
        self.textSetting.destroy()

    # 3]
    def Enter_SingOutButton(self, event):
        self.textSignout = Label(self.window1,
                                 text="SignOut",
                                 background="#1B2838",
                                 font=("Bahnschrift", 15, "bold"),
                                 foreground='#C7D5E0',
                                 borderwidth=2,
                                 relief="ridge")
        self.textSignout.place(x=115, y=500)

    def Leave_SingOutButton(self, event):
        self.textSignout.destroy()

    # 4]
    def Enter_CircleImage(self, event):
        self.textUser = Label(self.window1,
                              text=self.firstName+" "+self.lastName,
                              background="#1B2838",
                              font=("Bahnschrift", 15, "bold"),
                              foreground='#C7D5E0',
                              borderwidth=2,
                              relief="ridge")
        self.textUser.place(x=115, y=50)

    def Leave_CircleImage(self, event):
        self.textUser.destroy()

    #------------Right frame code and special method for HomeButton method--------#
    def CreateRight_frame(self):
        # 3.1)Creating Right Frame
        self.rightFrame = Frame(self.window1,
                                background="#1B2838",
                                borderwidth=8,
                                relief="ridge")
        self.rightFrame.pack(side="left", fill="both", expand=1)

        # ->4)Creating Buttons for actions of plots
        # 1]Creating PhotoImage for Covid Cases..
        self.CovidcaseImageActive = PhotoImage(master=self.rightFrame,
                                               file=r".\miniprojectPL_pictures\AfterSingin Page\Buttons in right Frame\Active\Covid_cases.png")
        self.CovidcaseImageNotActive = PhotoImage(master=self.rightFrame,
                                                  file=r".\miniprojectPL_pictures\AfterSingin Page\Buttons in right Frame\Not Active\Covid Cases.png")
        self.CovidcaseButton = Button(self.rightFrame,
                                      image=self.CovidcaseImageActive,
                                      background="#1B2838",
                                      activebackground="#1B2838",
                                      borderwidth=0, cursor="hand2",
                                      command=self.CovidCase_button_method)
        self.CovidcaseButton.place(x=105, y=15)

        # 2]Creating PhotoImage for  Vaccination.
        self.VaccinationImageActive = PhotoImage(master=self.rightFrame,
                                                 file=r".\miniprojectPL_pictures\AfterSingin Page\Buttons in right Frame\Active\vaccination.png")
        self.VaccinationImageNotActive = PhotoImage(master=self.rightFrame,
                                                    file=r".\miniprojectPL_pictures\AfterSingin Page\Buttons in right Frame\Not Active\Vaccination.png")
        self.VaccinationButton = Button(self.rightFrame,
                                        image=self.VaccinationImageNotActive,
                                        background="#1B2838",
                                        activebackground="#1B2838",
                                        borderwidth=0, cursor="hand2",
                                        command=self.Vaccination_button_method)
        self.VaccinationButton.place(x=510, y=15)

        # 3]Creating PhotoImage for tota Cases and deaths..
        self.casesAndDeathsImageActive = PhotoImage(master=self.rightFrame,
                                                    file=r".\miniprojectPL_pictures\AfterSingin Page\Buttons in right Frame\Active\covid deaths.png")
        self.casesAndDeathsImageNotActive = PhotoImage(master=self.rightFrame,
                                                       file=r".\miniprojectPL_pictures\AfterSingin Page\Buttons in right Frame\Not Active\covid deaths.png")
        self.casesAndDeathsButton = Button(self.rightFrame,
                                           image=self.casesAndDeathsImageNotActive,
                                           background="#1B2838",
                                           activebackground="#1B2838",
                                           borderwidth=0, cursor="hand2",
                                           command=self.TotalCases_button_method)
        self.casesAndDeathsButton.place(x=935, y=15)

        # -> 6)Creating Frame for graph...........
        self.graphFrame = Frame(self.rightFrame)
        self.graphFrame.place(x=21, y=80)

        # first call to method to display plotting or graph
        self.CovidCase_button_method()

        #-------------------------------------------------------------------------------#

    # This Class Methods........
    def SignOut_method(self):
        if messagebox.askyesno("Signout!", "Do you want to signout?"):
            with open("Remember_me.txt", "w") as rm:
                rm.write(" ")
            self.window1.destroy()
            Create_Home_Window = Home_Window.CreateHome_Window()

    def HomeButton_method(self):
        self.rightFrame.destroy()
        self.CreateRight_frame()

    def SettingButton_method(self):
        self.rightFrame.destroy()
        self.rightFrame = Frame(self.window1,
                                background="#1B2838",
                                borderwidth=8,
                                relief="ridge")
        self.rightFrame.pack(side="left", fill="both", expand=1)
        # self.rightFrame.bind("<Button 1>", self.setFocus_window)

        # 1)Setting Label..
        self.BigText_settingLabel = Label(self.rightFrame,
                                          text="Account Settings",
                                          background="#1B2838",
                                          foreground="#C7D5E0",
                                          font=("Bahnschrift", 25, "bold"))
        self.BigText_settingLabel.pack(anchor="center")

        # 2)Creating the frame to hold all adjustment........
        self.Frameinside_RightFrame = Frame(self.rightFrame)
        self.Frameinside_RightFrame.pack(pady=60)

        # 2.1)Creating label and image for it..
        self.ImageFor_RoundedBox = PhotoImage(master=self.Frameinside_RightFrame,
                                              file=r".\miniprojectPL_pictures\AfterSingin Page\Navigation Pannel\Rectangle.png")
        self.LabelFor_roundefBox = Label(self.Frameinside_RightFrame,
                                         background="#1B2838",
                                         image=self.ImageFor_RoundedBox)
        self.LabelFor_roundefBox.pack(anchor="center")

        # 2.2)Creating Email Address label...........
        self.Emailaddress_label = Label(self.Frameinside_RightFrame,
                                        text="Email Address",
                                        foreground="#C7D5E0",
                                        background="#2A475E",
                                        font=("Bahnschrift", 15))
        self.Emailaddress_label.place(x=39, y=40)

        # 2.3)Creating Label For Email Address display........
        self.EmailDisplay_label = Label(self.Frameinside_RightFrame,
                                        text=self.UserName,
                                        foreground="#66C0F4",
                                        background="#1B2838",
                                        width=82,
                                        font=("Bahnschrift", 15),
                                        anchor="w")
        self.EmailDisplay_label.place(x=39, y=66)

        # 2.4)Creating First Name label...........
        self.FirstName_label = Label(self.Frameinside_RightFrame,
                                     text="First Name",
                                     foreground="#C7D5E0",
                                     background="#2A475E",
                                     font=("Bahnschrift", 15))
        self.FirstName_label.place(x=39, y=120)

        # 2.5)Creating Entry For First Name display........
        self.FirstName_var = StringVar(value=self.firstName)
        self.FirstName_Display_label = Entry(self.Frameinside_RightFrame,
                                             textvariable=self.FirstName_var,
                                             foreground="#66C0F4",
                                             background="#1B2838",
                                             width=82,
                                             font=("Bahnschrift", 15),
                                             borderwidth=0,
                                             state="disabled",
                                             disabledbackground="#1B2838",
                                             disabledforeground="#66C0F4",
                                             cursor="arrow"
                                             )
        self.FirstName_Display_label.place(x=39, y=146)

        # 2.6)Creating Last Name label...........
        self.LastName_label = Label(self.Frameinside_RightFrame,
                                    text="Last Name",
                                    foreground="#C7D5E0",
                                    background="#2A475E",
                                    font=("Bahnschrift", 15))
        self.LastName_label.place(x=39, y=202)

        # 2.7)Creating Entry For Last Name display........
        self.LastName_var = StringVar(value=self.lastName)
        self.LastName_Display_label = Entry(self.Frameinside_RightFrame,
                                            textvariable=self.LastName_var,
                                            foreground="#66C0F4",
                                            background="#1B2838",
                                            width=82,
                                            font=("Bahnschrift", 15),
                                            borderwidth=0,
                                            state="disabled",
                                            disabledbackground="#1B2838",
                                            disabledforeground="#66C0F4",
                                            cursor="arrow"
                                            )
        self.LastName_Display_label.place(x=39, y=226)

        # 2.8)Creating Password label...........
        self.Password_label = Label(self.Frameinside_RightFrame,
                                    text="Password",
                                    foreground="#C7D5E0",
                                    background="#2A475E",
                                    font=("Bahnschrift", 15))
        self.Password_label.place(x=39, y=280)

        # 2.9)Creating Entry For Password display........
        self.Password_var = StringVar(value=self.Password)
        self.Password_Display_label = Entry(self.Frameinside_RightFrame,
                                            textvariable=self.Password_var,
                                            foreground="#66C0F4",
                                            background="#1B2838",
                                            width=82,
                                            font=("Bahnschrift", 15),
                                            borderwidth=0,
                                            state="disabled",
                                            disabledbackground="#1B2838",
                                            disabledforeground="#66C0F4",
                                            cursor="arrow"
                                            )
        self.Password_Display_label.place(x=39, y=306)

        # 3)Create Edit Button...
        self.EditButton = Button(self.Frameinside_RightFrame,
                                 text="Edit",
                                 font="Bungee 15",
                                 background="#1B2838",
                                 foreground="#C7D5E0",
                                 padx=50,
                                 cursor="hand2",
                                 activebackground="#1B2838",
                                 command=self.EditButton_command)
        self.EditButton.place(x=380, y=420)

    def CovidCase_button_method(self):
        self.CovidcaseButton.config(image=self.CovidcaseImageActive)
        self.VaccinationButton.config(image=self.VaccinationImageNotActive)
        self.casesAndDeathsButton.config(
            image=self.casesAndDeathsImageNotActive)
        self.graphFrame.destroy()
        # -> 1)Creating Frame for graph...........
        self.graphFrame = Frame(self.rightFrame, background="#2A475E")
        self.graphFrame.place(x=21, y=80)

        #__________________________Plotting code________________________________#

        # create a figure
        self.figure = Figure(figsize=(13.5, 6.4), dpi=100, facecolor="#2A475E")

        # create FigureCanvasTkAgg object
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self.graphFrame)

        # create the toolbar
        try:
            NavigationToolbar2Tk(self.figure_canvas, self.graphFrame)
        except:
            print("Ignore it  :)")

        # Getting data
        try:
            mydb = mc.connect(host="localhost",
                              username="root",
                              password="root",
                              database="pyminiproject", use_pure=True)
            query = "Select date,new_cases from covid_data_import;"
            self.result_dataFrame = pd.read_sql(query, mydb)
            mydb.close()
        except Exception as e:
            print(e, "Error in line block to get DataFrame")
        finally:
            mydb.close()

        self.x = self.result_dataFrame.iloc[:, 0].to_list()
        self.y = self.result_dataFrame.iloc[:, 1].to_list()

        # create axes
        axes = self.figure.add_subplot()
        axes.plot(self.x, self.y,
                  linewidth=2,
                  color='#66C0F4')
        axes.grid(linewidth=0.4, color='#8f8f8f', axis="y")
        axes.set_xlabel("Dates", size=12, color="#C7D5E0", font="Bahnschrift")
        axes.set_ylabel("New Cases", size=12,
                        color="#C7D5E0", font="Bahnschrift")
        axes.set_title("India's  Covid  Cases  Graph", font="Bungee",
                       color="#66C0F4", size=15)
        axes.set_facecolor("#2A475E")
        axes.xaxis.set_major_locator(WeekdayLocator(interval=9))
        axes.xaxis.set_major_formatter(DateFormatter("%d-%m-%y"))
        axes.yaxis.set_major_locator(ticker.MultipleLocator(30000))
        axes.margins(x=0.001, y=0.02)
        axes.legend(title="Scale:\n1 grid=30,000 people",
                    facecolor="#C7D5E0")

        self.figure.tight_layout()
        self.figure_canvas.get_tk_widget().pack(fill="both", expand=1, anchor="center")

    def Vaccination_button_method(self):
        self.CovidcaseButton.config(image=self.CovidcaseImageNotActive)
        self.VaccinationButton.config(image=self.VaccinationImageActive)
        self.casesAndDeathsButton.config(
            image=self.casesAndDeathsImageNotActive)
        self.graphFrame.destroy()
        # -> 1)Creating Frame for graph...........
        self.graphFrame = Frame(self.rightFrame, background="#2A475E")
        self.graphFrame.place(x=21, y=80)

        #__________________________Plotting code________________________________#

        # create a figure
        self.figure = Figure(figsize=(13.5, 6.4), dpi=100, facecolor="#2A475E")

        # create FigureCanvasTkAgg object
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self.graphFrame)

        # create the toolbar
        try:
            NavigationToolbar2Tk(self.figure_canvas, self.graphFrame)
        except:
            print("Ignore it  :)")

        # Getting data
        try:
            mydb = mc.connect(host="localhost",
                              username="root",
                              password="root",
                              database="pyminiproject", use_pure=True)
            query = "Select date,total_vaccinations from vaccination_info;"
            self.result_dataFrame = pd.read_sql(query, mydb)
            mydb.close()
        except Exception as e:
            print(e, "Error in line block to get DataFrame")
        finally:
            mydb.close()

        self.x = self.result_dataFrame.iloc[:, 0].to_list()
        self.y = self.result_dataFrame.iloc[:, 1].to_list()

        # create axes
        axes = self.figure.add_subplot()
        axes.plot(self.x, self.y,
                  linewidth=2,
                  color='#66C0F4')
        axes.grid(linewidth=0.4, color='#8f8f8f', axis="y")
        axes.set_xlabel("Dates", size=12, color="#C7D5E0", font="Bahnschrift")
        axes.set_ylabel("Vaccination", size=12,
                        color="#C7D5E0", font="Bahnschrift")
        axes.set_title("India's  Vaccination  Graph", font="Bungee",
                       color="#66C0F4", size=15)
        axes.set_facecolor("#2A475E")
        axes.xaxis.set_major_locator(WeekdayLocator(interval=5))
        axes.xaxis.set_major_formatter(DateFormatter("%d-%m-%y"))
        axes.yaxis.set_major_locator(ticker.MultipleLocator(100000000))
        axes.margins(x=0.001, y=0.02)
        axes.legend(title="Scale:\n1 grid=10,00,00,000 people",
                    facecolor="#C7D5E0")

        self.figure.tight_layout()
        self.figure_canvas.get_tk_widget().pack(fill="both", expand=1, anchor="center")

    def TotalCases_button_method(self):
        self.CovidcaseButton.config(image=self.CovidcaseImageNotActive)
        self.VaccinationButton.config(image=self.VaccinationImageNotActive)
        self.casesAndDeathsButton.config(image=self.casesAndDeathsImageActive)
        self.graphFrame.destroy()
        # -> 1)Creating Frame for graph...........
        self.graphFrame = Frame(self.rightFrame, background="#2A475E")
        self.graphFrame.place(x=21, y=80)

        #__________________________Plotting code________________________________#

        # create a figure
        self.figure = Figure(figsize=(13.5, 6.4), dpi=100, facecolor="#2A475E")

        # create FigureCanvasTkAgg object
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self.graphFrame)

        # create the toolbar
        try:
            NavigationToolbar2Tk(self.figure_canvas, self.graphFrame)
        except:
            print("Ignore it  :)")

        # Getting data
        try:
            mydb = mc.connect(host="localhost",
                              username="root",
                              password="root",
                              database="pyminiproject", use_pure=True)
            query = "Select date,new_deaths from covid_data_import;"
            self.result_dataFrame = pd.read_sql(query, mydb)
            mydb.close()
        except Exception as e:
            print(e, "Error in line block to get DataFrame")
        finally:
            mydb.close()

        self.x = self.result_dataFrame.iloc[:, 0].values
        self.y = self.result_dataFrame.iloc[:, 1].values

        # create axes
        axes = self.figure.add_subplot()
        axes.plot(self.x, self.y,
                  linewidth=2,
                  color='#66C0F4')
        axes.grid(linewidth=0.4, color='#8f8f8f', axis="y")
        axes.set_xlabel("Dates", size=12, color="#C7D5E0", font="Bahnschrift")
        axes.set_ylabel("Deaths", size=12,
                        color="#C7D5E0", font="Bahnschrift")
        axes.set_title("India's  Covid  Deaths  Graph", font="Bungee",
                       color="#66C0F4", size=15)
        axes.set_facecolor("#2A475E")
        axes.xaxis.set_major_locator(WeekdayLocator(interval=9))
        axes.xaxis.set_major_formatter(DateFormatter("%d-%m-%y"))
        axes.yaxis.set_major_locator(ticker.MultipleLocator(500))
        axes.margins(x=0.001, y=0.02)
        axes.legend(title="Scale:\n1 grid=500 people",
                    facecolor="#C7D5E0")

        self.figure.tight_layout()
        self.figure_canvas.get_tk_widget().pack(fill="both", expand=1, anchor="center")

    def EditButton_command(self):
        self.EditButton.destroy()
        self.FirstName_Display_label.focus_force()
        self.FirstName_Display_label.configure(state="normal")
        self.LastName_Display_label.configure(state="normal")
        self.Password_Display_label.configure(state="normal")
        # 1)creating save button.
        self.saveButton = Button(self.Frameinside_RightFrame,
                                 background="#66C0F4",
                                 foreground="#C7D5E0",
                                 text="Save",
                                 font="Bungee 12",
                                 padx=40,
                                 command=self.saveButton_command)
        self.saveButton.place(x=340, y=420)

        # 2)Creating cancel button.
        self.cancelButton = Button(self.Frameinside_RightFrame,
                                   background="#171A21",
                                   foreground="#C7D5E0",
                                   text="Cancel",
                                   font="Bungee 12",
                                   padx=40,
                                   command=self.cancelButton_command)
        self.cancelButton.place(x=498, y=420)

    def saveButton_command(self):
        if messagebox.askyesno("Save Data?", "Do you want to save changes?"):
            try:
                connection_obj = mc.connect(host="localhost",
                                            username="root",
                                            password="root",
                                            database="pyminiproject")
                cursor_obj = connection_obj.cursor()
                query = "update signup_info set First_Name=%s,Last_Name=%s,Password=%s where Email_address = %s"
                values = (self.FirstName_var.get(), self.LastName_var.get(
                ), self.Password_var.get(), self.UserName)
                cursor_obj.execute(query, values)
                connection_obj.commit()
            except:
                messagebox.showerror("Try Again", "Not able to process info")
            else:
                messagebox.showinfo("Successfull", "Changes are saved")
                self.FirstName_Display_label.configure(state="disabled")
                self.LastName_Display_label.configure(state="disabled")
                self.Password_Display_label.configure(state="disabled")
                self.saveButton.destroy()
                self.cancelButton.destroy()
                self.EditButton = Button(self.Frameinside_RightFrame,
                                         text="Edit",
                                         font="Bungee 15",
                                         background="#1B2838",
                                         foreground="#C7D5E0",
                                         padx=50,
                                         cursor="hand2",
                                         activebackground="#1B2838",
                                         command=self.EditButton_command)
                self.EditButton.place(x=380, y=420)
                self.firstName = self.FirstName_var.get()
                self.lastName = self.LastName_var.get()
                self.Password = self.Password_var.get()
                self.NameInitial_letter.configure(text=self.firstName[0] +
                                                  self.lastName[0])
                with open("Remember_me.txt","w") as rm:
                    rm.write(self.UserName+"\n"+self.Password)

    def cancelButton_command(self):
        self.FirstName_var.set(self.firstName)
        self.LastName_var.set(self.lastName)
        self.Password_var.set(self.Password)
        self.FirstName_Display_label.configure(state="disabled")
        self.LastName_Display_label.configure(state="disabled")
        self.Password_Display_label.configure(state="disabled")
        self.saveButton.destroy()
        self.cancelButton.destroy()

        self.EditButton = Button(self.Frameinside_RightFrame,
                                 text="Edit",
                                 font="Bungee 15",
                                 background="#1B2838",
                                 foreground="#C7D5E0",
                                 padx=50,
                                 cursor="hand2",
                                 activebackground="#1B2838",
                                 command=self.EditButton_command)
        self.EditButton.place(x=380, y=420)

    def emptyFile(self):
        self.window1.destroy()


# afterSignInwindow_obj = afterSignIn_mainWindow(None)