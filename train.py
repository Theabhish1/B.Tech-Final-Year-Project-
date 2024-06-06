from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x1000+0+0")
        self.root.title("Face Recognition Attendence System")
        self.root.iconbitmap(r'C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\neel.ico')

       

        title_lbl=Label(self.root,text="TRAIN DATASET ",font=("times new roman",35,"bold"),bg="Yellow",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        


        #""""""""""""""""""""""""""""""""""""""image top"""""""""""""""""""""""""""""""""""""
        img_top=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\developer2.png")
        img_top=img_top.resize((1300,340),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=45,width=1300,height=340)



         #""""""""""""button""
        btn=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",width=30,font=("times new roman",30,"bold"),bg="green",fg="white")
        btn.place(x=0,y=380,width=1530,height=60)
        back_button = Button(self.root, text="Back",cursor="hand2",font=("times new roman", 10, "bold"),width=14, bg="white", command=self.go_back,activebackground="white")
        back_button.place(x=1160, y=60)  # Adjust x and y coordinates as needed
         
            
    #"""""""""""""""""""""""""""""""""""""img bottom"""
        img_bottom=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\university.jpg")
        img_bottom=img_bottom.resize((1275, 200),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)


    

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1275,height= 200)
        
    def go_back(self):
        self.root.destroy()  # This will close the current window
        # Alternatively, if you want to navigate to another screen, you can implement that logic here

    

    def train_classifier(self):
        data_dir=("dataset")
        path=[os.path.join(data_dir,file)  for file in os.listdir(data_dir)]


        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')  #here we get gray scale image
            #we have to now convert in grid so we need numpy array
            imageNp=np.array(img,'uint8') #UNIT8 IS datatype
            id=int(os.path.split(image)[1].split('.')[1])

             # C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\data\user.11.1.jpg
              #0                                                                      1
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
         #""""""""""""train the classifier and save"""""""""
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!!",parent=self.root)
            





if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()