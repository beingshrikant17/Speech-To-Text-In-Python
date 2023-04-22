import speech_recognition as sr
import tkinter as tk
from tkinter import messagebox
from tkinter import*
from gtts import gTTS
import os
import sys
import pyaudio
from tkinter import scrolledtext
import  socket
from tkinter import PhotoImage
from playsound import playsound

#initialize the Speaking engine with properties
def text_to_speech(text, filename):
    tts = gTTS(text=text,tld='co.in', lang='en')
    tts.save("./audio/Test.mp3")  
    # Play the exam.mp3 file  
    playsound("./audio/Test.mp3")  
    #tts.save(filename)
    #os.system(f'mpg321 {filename}')

#initializing  the  flag  variable which will be use to change the voice to boy to girl and vice versa 
global flag
flag=0

#for after clicking the close icon by mistake to take confirmation from user
def on_closing():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        sys.exit()

#to check whether the internet connection is working or not
def is_connected():
        try:
            # Connect to a known website to check for internet connectivity
            host = socket.gethostbyname("www.google.com")
            # Use the command ping to check if the host is reachable
            s = socket.create_connection((host, 80), 2)
            return True
        except:
            pass
        return False

#setting the colors for the buttons present in class after press and before press

#1) For Speak button
class RoundedButton1(tk.Button):
    def __init__(self, master=None, **kw):
        tk.Button.__init__(self, master, **kw)
        self.config(bg="#0292F2", relief="raised", bd=15)
        self["font"] = ("Helvetica", 16)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self.config(bg="darkblue", fg="white")

    def on_leave(self, e):
        self.config(bg="#0292F2", fg="black")

#2) for Text to voice Button
class RoundedButton3(tk.Button):
    def __init__(self, master=None, **kw):
        tk.Button.__init__(self, master, **kw)
        self.config(bg="#0292F2", relief="raised", bd=15)
        self["font"] = ("Helvetica", 16)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self.config(bg="darkblue", fg="white")

    def on_leave(self, e):
        self.config(bg="#0292F2", fg="black")

#3) For Copy text Button
class RoundedButton2(tk.Button):
    def __init__(self, master=None, **kw):
        tk.Button.__init__(self, master, **kw)
        self.config(bg="#0292F2", relief="raised", bd=15)
        self["font"] = ("Helvetica", 16)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self.config(bg="#14667B", fg="white")

    def on_leave(self, e):
        self.config(bg="#0292F2", fg="black")

#4) For Change voice Button
class RoundedButton4(tk.Button):
    def __init__(self, master=None, **kw):
        tk.Button.__init__(self, master, **kw)
        self.config(bg="#0292F2", relief="raised", bd=15)
        self["font"] = ("Helvetica", 16)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self.config(bg="#14667B", fg="white")

    def on_leave(self, e):
        self.config(bg="#0292F2", fg="black")

#5) For Exit Button
class RoundedButton5(tk.Button):
    def __init__(self, master=None, **kw):
        tk.Button.__init__(self, master, **kw)
        self.config(bg="#0292F2", relief="raised", bd=15)
        self["font"] = ("Helvetica", 16)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self.config(bg="#EE2C2C", fg="white")

    def on_leave(self, e):
        self.config(bg="#0292F2", fg="black")

class SpeechRecognitionApp(tk.Tk):
    def __init__(self):
        #initializing the application parameters
        tk.Tk.__init__(self)
        self.title("Speech Recognition")                        #setting up the title
        #getting screen resolution
        screen_width=self.winfo_screenwidth()
        screen_height=self.winfo_screenheight()
        
        self.geometry(f'{screen_width}x{screen_height}') #setting up the resolution  
        self.config(bg = "#26292b",bd=7, relief="solid")        #defining the background color
        self.protocol("WM_DELETE_WINDOW", on_closing)
        
        #Upeer Heading of app with app name
        self.image = PhotoImage(file=r"./images/Text.png")    # Path of photo
        self.image_label = tk.Label(self, image=self.image)
        self.image_label.pack()

        # Initialize recognizer class (for recognizing the speech)
        self.r = sr.Recognizer()

        #declaring the Scrolledtext for  displaying output
        self.scr = scrolledtext.ScrolledText(self, width=30, height=4)
        self.scr.insert(1.0,"Enter your input or Speak")
        self.scr.pack(pady=15)
        self.scr.config(font=("Arial", 13))
        self.scr.pack()

        #Declaring the frame of buttons to arrange the buttons properly
        self.button_frame = tk.Frame(self, bg = "#474973")
        self.button_frame.pack()    

        #Declaring the Speak Button
        self.speak_button = RoundedButton1(self.button_frame, text="Speak", command=self.start_listening, bg = "dark blue", fg = "black", font=("Helvetica", 16),width=10, height=1)
        self.speak_button.grid(row=0, column=0, padx=10, pady=10)

        #Declaring the Text to voice Button
        self.TextToVoice_button = RoundedButton3(self.button_frame, text="Text to Voice", command=self.speak, bg = "#80669d", fg = "black", font=("Helvetica", 16),width=10, height=1)
        self.TextToVoice_button.grid(row=0, column=1, padx=10, pady=10)

        #Declaring the Copy Text Button
        self.copy_button = RoundedButton2(self.button_frame, text="Copy Text", command=self.copy_text, bg = "green", fg = "black", font=("Helvetica", 16),width=10, height=1)
        self.copy_button.grid(row=1, column=0, padx=10, pady=10)

        #Declaring the Change voice Button
        self.Change_Voice_button = RoundedButton4(self.button_frame, text="Clear Scrollbar", command=self.delete_scrollbar, bg = "gray", fg = "black", font=("Helvetica", 16),width=10, height=1)
        self.Change_Voice_button.grid(row=1, column=1, padx=10, pady=10)

        #Declaring the Exit Button
        self.exit_button = RoundedButton5(self.button_frame, text="Exit", command=self.exit_app, bg = "red", fg = "black", font=("Helvetica", 16),width=10, height=1)
        self.exit_button.grid(row=2, column=0, padx=10, pady=10,columnspan=2)


    #the method to be called when user will click the Change Voice Button
    def delete_scrollbar(self):
    	self.scr.delete(1.0, tk.END)
    	self.scr.pack()					
    	
    #the method to be called when user will click the Speak Button
    def start_listening(self):
    	with sr.Microphone() as source:
        	self.audio_text = self.r.listen(source)
    	try:
        	recognized_text = self.r.recognize_google(self.audio_text)
        	self.scr.delete(1.0, tk.END)
        	self.scr.insert(1.0, f"{recognized_text}")
        	self.scr.pack()
    	except sr.RequestError as e:
        	if not is_connected():
        	    messagebox.showinfo("Opps !!!","Internet is not connected")
        	else:
        	    self.text_label.delete(0, END)
        	    self.text_label.insert(0, f"Unable to provide speech recognition; {e}")       



       	 
    #the method to be called when user will click the Copy Text Button
    def copy_text(self):
        recognized_text=self.scr.get("1.0", END)
        self.clipboard_clear()
        self.clipboard_append(recognized_text)
        self.update()
        messagebox.showinfo("Copied","Text has been copied to clipboard")

    def exit_app(self):
        choice = messagebox.askyesno("Exit", "Are you sure you want to exit the app?")
        if choice == True:
            sys.exit()
        else:
            pass

    #the method to be called when user will click the Text To Voice Button
    def speak(self):
        recognized_text=self.scr.get("1.0", END)
        text_to_speech(recognized_text, "exam.mp3")

if __name__ == "__main__":
    #Declaring the object of the Class
    app = SpeechRecognitionApp()
    app.mainloop()                      #loop to run app Continously
