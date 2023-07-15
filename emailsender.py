from tkinter import *
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

window= Tk()
window.geometry('500x660')
window.title("Email Sending GUI")

Label_0=Label(window, text="Set Your Account", width=20, fg="green", font=("bold",20))
Label_0.place(x=90,y=33)

Label_1=Label(window, text="Your Email Account:", width=20, font=("bold",10))
Label_1.place(x=40,y=110)

Rmail=StringVar()
Rpswrd=StringVar()
Rsender=StringVar()
Rsubject=StringVar()


emailE=Entry(window, width=40, textvariable=Rmail)
emailE.place(x=200, y=110)

Label_2=Label(window, text="Your Password:", width=20, font=("bold",10))
Label_2.place(x=40,y=160)


passwordE=Entry(window, width=40, show="*", textvariable=Rpswrd)
passwordE.place(x=200, y=160)

compose=Label(window, text="Compose", width=20, font=("bold",15))
compose.place(x=180,y=210)

Label_3=Label(window, text="Sent To Email:", width=20, font=("bold",10))
Label_3.place(x=40,y=260)


senderE=Entry(window, width=40, textvariable=Rsender)
senderE.place(x=200, y=260)

Label_4=Label(window, text="Subject:", width=20, font=("bold",10))
Label_4.place(x=40,y=310)


subjectE=Entry(window, width=40, textvariable=Rsubject)
subjectE.place(x=200, y=310)


Label_5=Label(window, text="Message:", width=20, font=("bold",10))
Label_5.place(x=40,y=360)


messagebody=Text(window, width=30, height=10)
messagebody.place(x=200, y=360)


def sendemail():

    try:
        mymsg=MIMEMultipart()
        mymsg['From']=str(Rmail.get())
        mymsg['To']= str(Rsender.get())
        mymsg['Subject']= str(Rsubject.get())

        mymsg.attach(MIMEText(messagebody.get(1.0,'end'), 'plain'))

        server=smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(str(Rmail.get()), str(Rpswrd.get()))
        text=mymsg.as_string()
        server.sendmail(str(Rmail.get()), str(Rsender.get()), text)

        Label_6=Label(window, text="Done!", width=20,fg='green', font=("bold",15))
        Label_6.place(x=140,y=550)

        server.quit()
    except:
        Label_6=Label(window, text="something went wrong!", width=20,fg='red', font=("bold",15))
        Label_6.place(x=140,y=550)


Button(window,text="Send", width=20, bg='brown',fg="white", command=sendemail).place(x=180, y=590)

window.mainloop()


