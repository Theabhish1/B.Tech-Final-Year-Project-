from tkinter import *
from tkinter import ttk   #for stylish entry fill
from PIL import Image, ImageTk

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.geometry("730x620+0+0")
        self.root.title("Chatbot")
        self.root.iconbitmap(r'C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\neel.ico')
        self.root.bind('<Return>',self.enter_func)

        main_frame = Frame(self.root, bd=4, bg='powder blue', width=610)
        main_frame.pack()

        img_chat = Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\chatbot.png")  # Assuming the image is in the same directory as your script
        img_chat = img_chat.resize((100, 100), Image.LANCZOS)  # Adjusted the size for better visibility
        self.photoimg = ImageTk.PhotoImage(img_chat)

        Title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=1010, compound=LEFT,
                            image=self.photoimg, text='CHAT WITH ME', font=('arial', 24, 'bold'), fg='green', bg='white')
        Title_label.pack(side=TOP, pady=(0, 0))  # Adjusted the padding for better alignment

        # Making Text area +scroll bar
        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=90, height=19, bd=3, relief=RAISED, font=('arial', 14),
                         yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack(pady=(0, 0))  # Adjusted the padding for better alignment

        # Making Button Frame
        btn_frame = Frame(self.root, bd=4, bg='white', width=720)
        btn_frame.pack()

        label_1 = Label(btn_frame, text='Type Something', font=('arial', 14, 'bold'), foreground='green', background='white')
        label_1.grid(row=0, column=0, padx=5, sticky=W)  # stick to west-->Sticky
        back_button = Button(self.root, text="Back",cursor="hand2", font=("times new roman", 10, "bold"),width=18, bg="orange", command=self.go_back,activebackground="orange")
        back_button.place(x=570, y=70)  # Adjust x and y coordinates as needed
        #   # Bind the backspace key key to the go_back method
        # self.root.bind('<BackSpace>', lambda event: self.go_back())

    

        # Create variable 
        self.entry = StringVar()
        self.entry1 = ttk.Entry(btn_frame, textvariable=self.entry, width=40, font=('times new roman', 16, 'bold'))
        self.entry1.grid(row=0, column=1, padx=5, sticky=W)  # stick to west-->Sticky
        self.entry1.focus()

        # Send Button
        self.send = Button(btn_frame, text="Send", command=self.send, font=("arial", 10, "bold"), width=9, bg='green', fg='white', activebackground='green', activeforeground='white')
        self.send.grid(row=0, column=2, padx=5, sticky=W)  # stick to west-->Sticky)

        # Clear Button
        self.clear = Button(btn_frame, text="Clear Data", command=self.clear, font=("arial", 10, "bold"), width=9, bg='red', fg='white', activebackground='red', activeforeground='white')
        self.clear.grid(row=1, column=0, padx=5, sticky=W)  # stick to west-->Sticky)

        self.msg = ''
        self.label_11 = Label(btn_frame, text=self.msg, font=('arial', 14, 'bold'), foreground='red', background='white')
        self.label_11.grid(row=1, column=1, padx=5, sticky=W)  # stick to west-->Sticky



    # Function declaration
    def enter_func(self, event):
        self.send.invoke()

    def clear(self):
        self.text.delete('1.0', END)
        self.entry.set('')   # set come from var string()

    def send(self):
        user_input = self.entry.get().strip()  # Get data from entry and remove any leading/trailing spaces
        if user_input == '':
            self.msg = 'Please enter some input'
            self.label_11.config(text=self.msg, fg='red')
        else:
            self.msg = ''
            self.label_11.config(text=self.msg, fg='red')

            send = '\t\t\t' + 'You: ' + user_input
            self.text.insert(END, '\n' + send)  # Insert text into the textbox
            self.text.yview(END)

            user_input = user_input.lower()  # Convert user input to lowercase for case insensitivity
            if user_input.lower() == 'hello':
                self.text.insert(END, '\n\n' + 'Bot: Namaste Ji, How may I help You')
            elif user_input.lower() == 'hi':
                self.text.insert(END, '\n\n' + 'Bot: Hello Ji, Kem Cho Maja Ma?')
            elif user_input.lower() == 'ok':
                self.text.insert(END, '\n\n' + 'Bot: Yeah!')
            elif user_input.lower() == 'how are you':
                self.text.insert(END, '\n\n' + 'Bot: Fine and You')
            elif user_input.lower() == 'fantastic':
                self.text.insert(END, '\n\n' + 'Bot: Nice to Hear')
            elif user_input.lower() == 'who created you':
                self.text.insert(END, '\n\n' + 'Bot: The Student of B.Tech 4th Year of Neelkanth Institute of Technology, Meerut. Their Names are Jaiswal Abhishek Manoj, Kushal, and Vikash Tripathi.')
            elif user_input.lower() == 'what is your name':
                self.text.insert(END, '\n\n' + 'Bot: My Name is Samvidhan')
            elif user_input.lower() == 'bye':
                self.text.insert(END, '\n\n' + 'Bot: Thank You For Chatting, Have a Good Day!')
            elif user_input.lower() == 'do you know hindi':
                self.text.insert(END, '\n\n' + 'Bot: No, But I am Learning it')
            elif user_input.lower() == 'what is your pet name':
                self.text.insert(END, '\n\n' + 'Bot: My Name is Sam')
            elif user_input.lower() == 'what is face recognition attendance system':
                self.text.insert(END, '\n\n' + 'Bot: A face recognition attendance system is a technology that uses facial recognition algorithms to automatically identify and record the presence of individuals for attendance purposes. It enhances accuracy and efficiency by eliminating the need for manual attendance tracking methods.')
            elif user_input.lower() == 'what is machine learning':
                self.text.insert(END, '\n\n' + 'Bot: Machine learning is a subset of artificial intelligence where computers use data and algorithms to improve their performance on tasks without explicit programming. It involves training models on data to make predictions or decisions based on new inputs.')
            elif user_input.lower() == 'what is chatbot':
                self.text.insert(END, '\n\n' + 'Bot: A chatbot is an AI-powered software application designed to simulate conversation with human users, typically over the internet. It can provide automated customer service, answer questions, or engage in small talk through text or voice interactions.')
            elif user_input.lower() == 'what is ai':
                self.text.insert(END, '\n\n' + 'Bot: Artificial intelligence (AI), in its broadest sense, is intelligence exhibited by machines, particularly computer systems. It is a field of research in computer science that develops and studies methods and software that enable machines to perceive their environment and uses learning and intelligence to take actions that maximize their chances of achieving defined goals.')
            elif user_input.lower() == 'what is artificial intelligence':
                self.text.insert(END, '\n\n' + 'Bot: Artificial intelligence (AI), in its broadest sense, is intelligence exhibited by machines, particularly computer systems. It is a field of research in computer science that develops and studies methods and software that enable machines to perceive their environment and uses learning and intelligence to take actions that maximize their chances of achieving defined goals.')
        
            else:
                self.text.insert(END, "\n\n" + "Bot: Sorry, I didn't get it")


        # Clear the entry box
        self.entry.set('')
    def go_back(self):
        self.root.destroy()  # This will close the current window
        # Alternatively, if you want to navigate to another screen, you can implement that logic here
if __name__ == "__main__":
    root = Tk()
    obj = ChatBot(root)  # object of class
    root.mainloop()
