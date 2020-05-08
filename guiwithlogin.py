from tkinter import *
import os

def delete2():
    screen3.destroy()
    
def delete3():
    screen4.destroy()
    
def delete4():
    screen5.destroy()

def rfid():
    screen7 = Toplevel(screen)
    screen7.title("Aisle Content")
    screen7.geometry("400x400")
    Label(screen7, text = "ITEMS").pack()
    exec(open('lol.py').read())
    screen7.destroy()

def loader():    
    
    screen6 = Toplevel(screen)
    screen6.geometry("400x400")
    exec(open('example.py').read())
    screen6.destroy()
    
    
def session():
    screen6 = Toplevel(screen)
    screen6.title("Super Mercardo Home Screen")
    screen6.geometry("400x400")
    Label(screen6, text = "SUPER MERCARDO").pack()
    Button(screen6, text ="RFID", command = rfid).pack()
    Button(screen6, text ="Weight", command = loader).pack()

def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Login Success")
    screen3.geometry("300x160")
    Label(screen3, text = "Let the Shopping begin", fg="green", font=("times New Roman", 24)).pack()
    Label(screen3, text ="").pack()
    Label(screen3, text ="").pack()
    Button(screen3, text = "Awesome" ,command =delete2).pack()
    session()
def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Incorrect Password")
    screen4.geometry("300x160")
    Label(screen4, text = "Try Again", fg="red", font=("Times New Roman", 24)).pack()
    Label(screen4, text ="").pack()
    Label(screen4, text ="").pack()
    Button(screen4, text = "OK" ,command =delete3).pack()
    
def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Not a member")
    screen5.geometry("500x150")
    Label(screen5, text = "Register to unlock exciting experience", fg="Powder blue", bg="bisque", font=("Times New Roman", 20)).pack()
    Label(screen5, text ="").pack()
    Label(screen5, text ="").pack()
    Button(screen5, text = "OK" ,command =delete4).pack()
    

def register_user():
    
    username_info = username.get()
    password_info = password.get()
    
    file=open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
    Label(screen1, text = "Registration Success.Welcome to Super Mercado family", fg = "green", font =("Times New Roman", 24)).pack()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("640x360")
    
    global username
    global password
    global username_entry
    global password_entry  
    username = StringVar()
    password = StringVar()
    
    Label(screen1, text ="Please Complete the following details", bg = "blue", width = "300", height = "3", font =("Times New Roman", 24)).pack()
    Label(screen1, text ="").pack()
    Label(screen1, text ="").pack()
    Label(screen1, text ="User Name").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text ="").pack()
    Label(screen1, text ="").pack()
    Label(screen1, text ="Password").pack()
    Label(screen1, text ="").pack()
    password_entry = Entry(screen1, textvariable = password, show = '*')
    password_entry.pack()
    Label(screen1, text ="").pack()
    Label(screen1, text ="").pack()
    Label(screen1, text ="").pack()
    Button(screen1, text = "Register", width = "30" , height = "2", bg = "powder blue", command = register_user).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1 , "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
      user_not_found()
    
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("640x360")
    
    Label(screen2, text ="Please Complete the following details to login", bg = "blue", width = "300", height = "3", font =("Times New Roman", 24)).pack()
    Label(screen2, text ="").pack()
    
    global username_verify
    global password_verify
    
    username_verify = StringVar()
    password_verify = StringVar()
    
    global username_entry1
    global password_entry1
    
    Label(screen2 , text ="User Name").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2 , text ="").pack()
    Label(screen2 , text ="").pack()
    Label(screen2 , text ="Password").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify, show ="*")
    password_entry1.pack()
    Label(screen2 , text ="").pack()
    Label(screen2 , text ="").pack()
    Button(screen2 , text = "Login", width = "30" , height = "2", bg = "powder blue", command = login_verify).pack()

    
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("640x360")
    screen.title("Super Mercardo")
    Label(text ="Welcome To Super Mercardo", bg = "blue", width = "300", height = "3", font =("Times New Roman", 24)).pack()
    Label(text ="").pack()
    Label(text ="").pack()
    Label(text ="").pack()
    Button(text = "Login", bg ="powder blue", width = "30", height = "3", command = login).pack()
    Label(text ="").pack()
    Label(text ="").pack()
    Label(text ="").pack()
    Button(text = "Register", bg ="powder blue", width = "30", height = "3", command = register).pack()
    
    screen.mainloop()

main_screen()

