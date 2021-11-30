from tkinter import *
import pyttsx3 as pp
import threading
import datetime

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)


def speak(words):
    engine.say(words)
    engine.runAndWait()



main = Tk()

main.geometry("500x650")

main.title("Aman Raj bot")

img = PhotoImage(file="pp.png")

photoL = Label(main, image=img)

photoL.pack(pady=5)


def queries():
        query = textF.get().lower()
        msgs.insert(END, "You : " + query)  
        print(type(queries))
        # msgs.insert(END, "Aman bot : " + str(queries))
        speak(queries)
        textF.delete(0, END)
        msgs.yview(END)
        

        if 'hello' in query:
            s = "Hey! how are you"
            msgs.insert(END, "Aman bot : " + s)
            speak(s)
            
        

        elif "i am good" in query or "i am fine" in query or "good" in query or "fine" in query:
            s = "Glad to hear that"
            msgs.insert(END, "Aman bot : " + s)
            speak(s)
            r = "Which language do you speak."
            msgs.insert(END, "Aman bot : " + r)
            speak(r)
            


        elif "english" in query:
            s = "I know english as well"
            msgs.insert(END, "Aman bot : " + s)
            speak(s)
            r = "We can talk"
            msgs.insert(END, "Aman bot : " + r)
            speak(r)
            


        elif "hindi" in query:
            s = "I am still learning it."
            msgs.insert(END, "Aman bot : " + s)
            speak(s)
            r = "But I know"
            msgs.insert(END, "Aman bot : " + r)
            speak(r)
            t = "Namaasta"
            msgs.insert(END, "Aman bot : " + t)
            speak(t)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

            
        
        



frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

# creating text field

textF = Entry(main, font=("Courier", 10))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask Aman Raj bot", font=(
    "Courier", 10),bg='Green', command=queries)
btn.pack()


# creating a function
def enter_function(event):
    btn.invoke()


# going to bind main window with enter key...

main.bind('<Return>', enter_function)


def repeatL():
    # while True:
    queries()


t = threading.Thread(target=repeatL)

t.start()

main.mainloop()
