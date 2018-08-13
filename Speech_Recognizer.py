import speech_recognition as sr
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import threading
import time

entries = {}
textbs = {}
textpops = ""
def subm(a):
    e = entries["mic"]
    rep = int(e.get())
    mic_list = sr.Microphone.list_microphone_names()
    j = 1
    mic_name = ""
    sample_rate = 48000
    chunk_size = 2048
    for i, microphone_name in enumerate(mic_list):
        if j == rep:
            mic_name = microphone_name
        j += 1
    r = sr.Recognizer()
    mic_list = sr.Microphone.list_microphone_names()

    for i, microphone_name in enumerate(mic_list):
        if microphone_name == mic_name:
            device_id = i

    def exitf(a):
        root.destroy()

    def status_popup():
        global textpops
        savp = Tk()
        savp.iconbitmap('wait.ico')
        savp.wm_title("Recognition in progress...")
        #Label(savp, text="Please wait...").grid(row=1, column=0, sticky="ew")
        prog = Text(savp, height=10, width=40, bd=5, font=("Times", 20))
        prog.grid(row=2, columnspan=3, sticky="ew")
        print("txtpps - ", textpops)
        prog.insert(INSERT, "           Recognition in progress, Please wait!    \n")
        prog.insert(INSERT, "                                 Loading!    \n")
        start = time.time()
        while not textpops:
            if (time.time() - start) > 5:
                break
            prog.insert(INSERT, ".")
            savp.update_idletasks()
            savp.update()
        textpops = ""



    def speakeng(a):
        with sr.Microphone(device_index=device_id, sample_rate=sample_rate, chunk_size=chunk_size) as source:
            # Adjusting noise level
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            global textpops
            t1 = threading.Thread(target=status_popup)
            t1.start()
            try:
                text = r.recognize_google(audio, language='en-IN')
                textpops = text
                print("Speakeng - ",textpops)
                text = text + "\n"
                eng.insert(INSERT, text)
            except sr.UnknownValueError:
                text = "\n---\nGoogle Speech Recognition could not understand audio\n---\n"
                eng.insert(INSERT, text)
            except sr.RequestError as e:
                eng.insert(INSERT,"---")
                eng.insert(INSERT,"Could not request results from Google Speech Recognition service; {0}".format(e))
                eng.insert(INSERT,"---")
            t1.join()

            print("\nt1 still alive - ", t1.is_alive())
    def speakhin(a):
        with sr.Microphone(device_index=device_id, sample_rate=sample_rate, chunk_size=chunk_size) as source:
            # Adjusting noise level
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            global textpops
            t1 = threading.Thread(target=status_popup)
            t1.start()
            try:
                text = r.recognize_google(audio, language='hi-IN')
                textpops = text
                print("Speakhin - ", textpops)
                text = text + "\n"
                hin.insert(INSERT, text)
            except sr.UnknownValueError:
                text = "\n---\nGoogle Speech Recognition could not understand audio\n---\n"
                hin.insert(INSERT, text)
            except sr.RequestError as e:
                hin.insert(INSERT,"---")
                hin.insert(INSERT,"Could not request results from Google Speech Recognition service; {0}".format(e))
                hin.insert(INSERT,"---")
            t1.join()
            print("\nt1 still alive - ", t1.is_alive())
    def cleareng(a):
        eng.delete(1.0, END)
    def clearhin(a):
        hin.delete(1.0, END)
    def saveeng(a):
        location = ""
        def browse(a):
            x = filedialog.askdirectory()
            e = entries["save_file_location"]
            e.insert(0, x)
            location = x
        def savv(a):
            e = entries["save_file_location"]
            location = str(e.get())
            e = entries["save_file_name"]
            name = str(e.get())
            input = eng.get("1.0", 'end-1c')
            print(name)
            loc = location + "/" + name + ".txt"
            print("\nFinal loc\n", loc)
            f = open(loc, 'w')
            f.write(input)
            f.close()
            sav.destroy()
        sav = Tk()
        sav.iconbitmap('save.ico')
        sav.wm_title("Save English Transcript")
        Label(sav, text="Enter the file name you want: ").grid(row=0,column=0,sticky=W)
        e = Entry(sav, width=50)
        e.grid(row=1,columnspan=2, sticky="ew")
        entries["save_file_name"] = e
        Label(sav, text="Choose the location to save at: ").grid(row=2, column=0, sticky=W)
        folentry = Entry(sav, width=77)
        folentry.grid(row=3,column=0, sticky="ew")
        entries["save_file_location"] = folentry
        ch = Button(sav, text="Browse")
        ch.bind("<Button-1>", browse)
        ch.grid(row=3, column=1, sticky="ew")
        ttk.Separator(sav).grid(row=4, pady=2, padx=2, columnspan=3, sticky="ew")
        ent = Button(sav, text="Save", width=11)
        ent.bind("<Button-1>", savv)
        ent.grid(row=5, column=1, sticky="ew")
        sav.mainloop()

    def savehin(a):
        location = ""
        def browse(a):
            x = filedialog.askdirectory()
            e = entries["save_file_location"]
            e.insert(0, x)
            location = x
        def savv(a):
            e = entries["save_file_location"]
            location = str(e.get())
            e = entries["save_file_name"]
            name = str(e.get())
            input = hin.get("1.0", 'end-1c')
            print(name)
            loc = location + "/" + name + ".txt"
            print("\nFinal loc\n", loc)
            f = open(loc, 'w', encoding="utf-8")
            f.write(input)
            f.close()
            sav.destroy()
        sav = Tk()
        sav.iconbitmap('save.ico')
        sav.wm_title("Save Hindi Transcript")
        Label(sav, text="Enter the file name you want: ").grid(row=0,column=0,sticky=W)
        e = Entry(sav, width=50)
        e.grid(row=1,columnspan=2, sticky="ew")
        entries["save_file_name"] = e
        Label(sav, text="Choose the location to save at: ").grid(row=2, column=0, sticky=W)
        folentry = Entry(sav, width=77)
        folentry.grid(row=3,column=0, sticky="ew")
        entries["save_file_location"] = folentry
        ch = Button(sav, text="Browse")
        ch.bind("<Button-1>", browse)
        ch.grid(row=3, column=1, sticky="ew")
        ttk.Separator(sav).grid(row=4, pady=2, padx=2, columnspan=3, sticky="ew")
        ent = Button(sav, text="Save", width=11)
        ent.bind("<Button-1>", savv)
        ent.grid(row=5, column=1, sticky="ew")
        sav.mainloop()

    popup.destroy()
    root = Tk()


    root.iconbitmap('icon.ico')
    root.title("Speech Recognizer (Speech to Text using Google API)")
    Label(root, text="English Speech to text:").grid(row=0, column=0, sticky=W)
    eng = Text(root, height=12, width=72, bd=5, font=("Times", 12))
    eng.grid(row=3, columnspan=3)
    se = Button(root, text="Speak English", width=11)
    se.bind("<Button-1>",speakeng)
    se.grid(row=6, column=0)
    es = Button(root, text="Clear English", width=11)
    es.bind("<Button-1>",cleareng)
    es.grid(row=6, column=1)
    ce = Button(root, text="Save English", width=11)
    ce.bind("<Button-1>",saveeng)
    ce.grid(row=6, column=2)
    Label(root, text="Hindi Speech to text:").grid(row=7, column=0, sticky=W)
    hin = Text(root, height=12, width=72, bd=5, font=("Times", 12))
    hin.grid(row=10, columnspan=3)
    sh = Button(root, text="Speak Hindi", width=11)
    sh.bind("<Button-1>",speakhin)
    sh.grid(row=13, column=0)
    hs = Button(root, text="Clear Hindi", width=11)
    hs.bind("<Button-1>",clearhin)
    hs.grid(row=13, column=1)
    ch = Button(root, text="Save Hindi", width=11)
    ch.bind("<Button-1>",savehin)
    ch.grid(row=13, column=2)
    ttk.Separator(root).grid(row=14, pady=2, padx=2,columnspan=3, sticky="ew")
    ex = Button(root, text="Exit", width=11)
    ex.bind("<Button-1>", exitf)
    ex.grid(row=16, columnspan=3,sticky="ew")
    root.mainloop()



def genlist(a):
    mic_list = sr.Microphone.list_microphone_names()
    j = 1
    li = ""
    for i, microphone_name in enumerate(mic_list):
        temp = str(j)
        temp = temp + " - " + microphone_name + "\n"
        li = li + temp
        j += 1
    print("\ngenlist's --\n",li)
    e = textbs["miclist"]
    print("\ninslist's --\n", li)
    e.insert(INSERT, li)

popup = Tk()
popup.iconbitmap('mic.ico')
popup.wm_title("Microphone Confirmation")
Label(popup, text="Enter the serial number of the appropriate mic from the following list").grid(row=0,column=0,sticky=W)
micl = Text(popup, height=6, width=30, bd=9, font=("Times", 12))
micl.grid(row=1, columnspan=1, sticky = "ew")
textbs["miclist"] = micl
gl = Button(popup, text="Generate list", width=11)
gl.bind("<Button-1>",genlist)
gl.grid(row=1, column=1, sticky = "ew")
e = Entry(popup,width = 50)
e.grid(row=7,sticky = "ew")
entries["mic"] = e
ent = Button(popup, text="Submit", width=11)
ent.bind("<Button-1>", subm)
ent.grid(row=7, column=1, sticky = "ew")
popup.mainloop()