from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os
import csv
import webbrowser
from tkinter import filedialog

class Developer:
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("1630x1000+0+0")
        self.root.title("Face Recognition Attendance System")
        self.root.iconbitmap(r'C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\neel.ico')


        
        title_lbl=Label(self.root,text="DEVELOPERS",font=("times new roman",35,"bold"),bg="Pink",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        


        #""""""""""""""""""""""""""""""""""""""image full"""""""""""""""""""""""""""""""""""""
        img_top=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\developers.jpg")
        img_top=img_top.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=45,width=1530,height=720)


            #   "main frame"
        main_frame=Frame(f_lbl,bd=2,bg="white")#bd-border
        main_frame.place(x=800,y=0,width=500,height=330)

        
        #""""""""""""""""""""""""""""""""""""""image frame's"""""""""""""""""""""""""""""""""""""
        img_top1=Image.open(r"Images\abhi4.jpg")
        img_top1=img_top1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img_top1)
        

        f_lbl=Label(self.root,image=self.photoimg8)
        f_lbl.place(x=800,y=47,width=100,height=100)

        img_top2=Image.open(r"Images\kushal.jpg")
        img_top2=img_top2.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img_top2)
        

        f_lbl=Label(self.root,image=self.photoimg4)
        f_lbl.place(x=980,y=47,width=100,height=100)

        img_top3=Image.open(r"Images\vikash.jpg")
        img_top3=img_top3.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img_top3)
        

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1175,y=47,width=100,height=100)

        
        dev_Label = Label(main_frame, text="Jaiswal Abhishek M.", font=("times new roman", 10, "bold"), bg="white")
        dev_Label.place(x=0,y=100)
        dev_Label_1 = Label(main_frame, text="Kushal", font=("times new roman", 10, "bold"), bg="white")
        dev_Label_1.place(x=175,y=100)
        dev_Label_2 = Label(main_frame, text="Vikash Tripathi", font=("times new roman", 10, "bold"), bg="white")
        dev_Label_2.place(x=370,y=100)
        
        dev1_Label = Label(main_frame, text="Roll No: 2103730109002             2003730100010                                 2103730109007", font=("times new roman", 10, "bold"), bg="white")
        dev1_Label.place(x=0,y=120)

        dev2_Label = Label(main_frame, text="Course : B.Tech. C.S.E(Final Year)", font=("times new roman", 10, "bold"), bg="white")
        dev2_Label.place(x=0,y=140)
         
          
        dev3_Label = Label(main_frame, text="Student of Neelkanth Insitite of Technology,Meerut", font=("times new roman", 12, "bold"), bg="white")
        dev3_Label.place(x=0,y=160)
        
        dev4_Label = Label(main_frame, text="For any issue contact us on:", font=("times new roman", 17, "bold"), bg="white")
        dev4_Label.place(x=0,y=190)
         
    # Load and resize the LinkedIn logo image
        linkedin_logo = Image.open(r"Images\linkedin.png")
        linkedin_logo = linkedin_logo.resize((50, 30), Image.Resampling.LANCZOS)
        photoimg8 = ImageTk.PhotoImage(linkedin_logo)

        # Create a Label widget with the LinkedIn logo image
        f_lbl = Label(main_frame,cursor="hand2", image=photoimg8)
        f_lbl.place(x=120, y=220, width=50, height=30)

        # Bind the click event to the Label widget
        f_lbl.bind("<Button-1>", self.open_linkedin1)

        # Keep a reference to the image to prevent garbage collection
        f_lbl.image = photoimg8
        # Load and resize the LinkedIn logo image
        linkedin_logo1 = Image.open(r"Images\linkedin.png")
        linkedin_logo1 = linkedin_logo1.resize((50, 30), Image.Resampling.LANCZOS)
        photoimg9 = ImageTk.PhotoImage(linkedin_logo1)

        # Create a Label widget with the LinkedIn logo image
        f_lbl = Label(main_frame,cursor="hand2", image=photoimg9)
        f_lbl.place(x=120, y=260, width=50, height=30)

        # Bind the click event to the Label widget
        f_lbl.bind("<Button-1>", self.open_linkedin)

        # Keep a reference to the image to prevent garbage collection
        f_lbl.image = photoimg9
        
        dev5_Label = Label(main_frame, text="Kushal- ", font=("times new roman", 17, "bold"), bg="white")
        dev5_Label.place(x=0,y=220)

        dev6_Label = Label(main_frame, text="Abhishek- ",font=("times new roman", 17, "bold"), bg="white")
        dev6_Label.place(x=0,y=260)
        
        back_button = Button(self.root, text="Back", cursor="hand2",font=("times new roman", 10, "bold"),width=18, bg="orange", command=self.go_back,activebackground="orange")
        back_button.place(x=1120, y=10)  # Adjust x and y coordinates as needed
        
        
           
      

    def open_linkedin(self, event):
    # Function to open LinkedIn profile in web browser
            webbrowser.open_new("https://www.linkedin.com/in/abhishekjaiswal99")

    def open_linkedin1(self, event):
    # Function to open LinkedIn profile in web browser
            webbrowser.open_new("https://www.linkedin.com/in/kushal-chauhan-a96650228/")
    def go_back(self):
        self.root.destroy()  # This will close the current window
        # Alternatively, if you want to navigate to another screen, you can 



if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
