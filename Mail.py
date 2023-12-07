import tkinter as tk
import smtplib

canvas = tk.Tk()
canvas.title("Tanvi's Python Email Application with GUI")
canvas.geometry("400x300")
canvas.config(bg='purple')

def send():
    try:
        username = t_username.get()
        password = t_password.get()
        to = t_reciever.get()
        subject = t_subject.get()
        body = t_body.get()
        if username =="" or password=="" or to == "" or subject=="" or body == "":
            noti.config(text="All Fields Required",fg="red")
            return
        else:
            final_message = 'Subject:{}\n\n{}'.format(subject,body)
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(username,password)
            server.sendmail(username,to,final_message)
            noti.config(text="Email has been sent",fg="green")
    except:
        noti.config(text="Error sending email",fg='red')


    print("Sent")
def Reset():
    usernameEntry.delete(0,'end')
    passwordEntry.delete(0,'end')
    recieverEntry.delete(0,'end')
    subjectEntry.delete(0,'end')
    bodyEntry.delete(0,'end')
    print("Reset")

tk.Label(canvas,text="Email Application",font=("poppins",15),fg="white",bg="black").grid(row=0,sticky="N",padx=20,pady=10)
tk.Label(canvas,text="Use the form to send a email",font=("poppins",10),fg="white",bg="black").grid(row=1,sticky="W",padx=5)

tk.Label(canvas,text="Your Email",font=("poppins",10),fg="white",bg="black").grid(row=3,sticky="W",padx=10)
tk.Label(canvas,text="Password",font=("poppins",10),fg="white",bg="black").grid(row=4,sticky="W",padx=10)
tk.Label(canvas,text="To",font=("poppins",10),fg="white",bg="black").grid(row=5,sticky="W",padx=10)
tk.Label(canvas,text="Subject",font=("poppins",10),fg="white",bg="black").grid(row=6,sticky="W",padx=10)
tk.Label(canvas,text="Body",font=("poppins",10),fg="white",bg="black").grid(row=7,sticky='W',padx=10)

noti = tk.Label(canvas,text="",font=("poppins",10),fg="white",bg="black")
noti.grid(row=8,sticky="W",padx=5)

t_username = tk.StringVar()
t_password = tk.StringVar()
t_reciever = tk.StringVar()
t_subject = tk.StringVar()
t_body = tk.StringVar()

usernameEntry = tk.Entry(canvas,textvariable=t_username)
usernameEntry.grid(row=3,column=1)
passwordEntry = tk.Entry(canvas,textvariable=t_password)
passwordEntry.grid(row=4,column=1)
recieverEntry = tk.Entry(canvas,textvariable=t_reciever)
recieverEntry.grid(row=5,column=1)
subjectEntry = tk.Entry(canvas,textvariable=t_subject)
subjectEntry.grid(row=6,column=1)
bodyEntry = tk.Entry(canvas,textvariable=t_body)
bodyEntry.grid(row=7,column=1)

send_Button = tk.Button(canvas,text="send",command=send,fg="cyan",bg="black").grid(row=9,sticky='w',pady=10,padx=60)
reset_Button = tk.Button(canvas,text="Reset",command=Reset,fg="cyan",bg="black").grid(row=9,stick='w',pady=10,padx=100)

canvas.mainloop()