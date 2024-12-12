from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10**6), 3)) + " Mbps"
    up = str(round(sp.upload() / (10**6), 3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x700")
sp.config(bg="blue")

title_label = Label(sp, text="Internet Speed Test", font=("Time New Roman", 30, "bold"), bg="Blue", fg="white" )
title_label.place(x=60, y=40, height=50, width=380)

download_label = Label(sp, text="Download Speed", font=("Time New Roman", 30, "bold"), bg="Blue")
download_label.place(x=60, y=130, height=50, width=380)

lab_down = Label(sp, text="00", font=("Time New Roman", 30, "bold"))
lab_down.place(x=60, y=210, height=50, width=380)

upload_label = Label(sp, text="Upload Speed", font=("Time New Roman", 30, "bold"), bg="Blue", )
upload_label.place(x=60, y=290, height=50, width=380)

lab_up = Label(sp, text="00", font=("Time New Roman", 30, "bold"))
lab_up.place(x=60, y=370, height=50, width=380)

check_button = Button(sp, text="Check Speed", font=("Time New Roman", 30, "bold"), relief=RAISED, bg="green", command=speedcheck)
check_button.place(x=60, y=460, height=50, width=380)

sp.mainloop()
