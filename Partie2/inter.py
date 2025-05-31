import tkinter as tk
import os


fr=None
fw=None


import subprocess


#---------------------------------------
def on_sign_in():
    send_message(1)

def on_sign_up():
    send_message(2)
    Welcome_frame.grid_forget()
    sign_up_frame.grid(row=1, column=0, columnspan=3)

def on_quit():
    send_message(3)
    close(fw)
    close(fr)
    window.destroy()
#-------------------------------------------
def send_message(action_number):
    global fw
    try:
        
            os.write(fw,str(action_number).encode())
    except FileNotFoundError:
        print("Tube nommé non trouvé: ./pipes/py_in")
#-----------------------------------------------
def afficher_user_label():
    message.config(text="Ce nom d'utilisateur existe déjà ou contient une virgule", fg='#ff3333')
    message.grid(row=3, column=0, columnspan=2, pady=(5, 0),padx=(5,5))
    erreur_vide.grid_forget()

def afficher_vide_label():
    erreur_vide.config(text="Veuillez remplir tous les champs", fg='#ff3333')
    erreur_vide.grid(row=3, column=0, columnspan=3,padx=(5,0) ,pady=(5, 0))
    message.grid_forget()

def submit():
    contenu_user = username_entry.get()
    contenu_pass = password_entry.get()

    if (not contenu_pass or not contenu_user):
        afficher_vide_label()
        return None  
    else :
        if(contenu_pass   and (";" in contenu_user  )):
            afficher_user_label()
            return None

    
    try:
        # Écrire le nom d'utilisateur dans le tube nommé
        global fw 
        global fr
        os.write(fw,str(contenu_user).encode())
        # Lire le drapeau à partir du tube nommé
        data=os.read(fr,256)
        flag = int(data.strip())
        print(flag)
        if flag == 0:
            afficher_user_label()
            return None
        else:
            # Écrire le mot de passe dans le tube nommé
            os.writee(fw,str(contenu_pass).encode)
            print("success")
            
    except FileNotFoundError:
        print("Tube nommé non trouvé:", pipe_path_in)
    except ValueError:
        print("Contenu invalide dans le tube nommé:", pipe_path_in)

window = tk.Tk()
window.title("Talk to me")
window.geometry('330x400')
window.configure(bg='#333333')
Welcome_frame=tk.Frame(window, bg='#333333')
sign_up_frame=tk.Frame(window, bg='#333333')
pipe_path_in = "./pipes/py_in"
pipe_path_out="./pipes/py_out"

fw = os.open(pipe_path_in , os.O_WRONLY)
fr = os.open(pipe_path_out, os.O_RDONLY)


Welcome_frame.grid(row=1, column=0, columnspan=3)
Welcome_label = tk.Label(Welcome_frame, text="Welcome", bg='#333333', fg='#20b4aa', font=('Arial', 40))
Welcome_label.grid(row=0, column=0, columnspan=3, pady=40, padx=40)
new_one_button=tk.Button(Welcome_frame, text="Sign IN", bg='#20b4aa', fg='#FFFFFF', font=('Arial', 10), highlightbackground='#1dc8bd', activebackground='#1dc8bd', command=on_sign_in)
old_one_button=tk.Button(Welcome_frame, text="Sign Up", bg='#20b4aa', fg='#FFFFFF', font=('Arial', 10), highlightbackground='#1dc8bd', activebackground='#1dc8bd', command=on_sign_up)
quitt_button=tk.Button(Welcome_frame, text="EXIT", bg='#20b4aa', fg='#FFFFFF', font=('Arial', 10), highlightbackground='#1dc8bd', activebackground='#1dc8bd', command=on_quit)
new_one_button.grid(row=1, column=0, columnspan=3, pady=20)
old_one_button.grid(row=2, column=0, columnspan=3, pady=20)
quitt_button.grid(row=3, column=0, columnspan=3, pady=20)



user_frame = tk.Frame(sign_up_frame, bg='#333333')
pass_frame = tk.Frame(sign_up_frame, bg='#333333')
sign_up_label = tk.Label(sign_up_frame, text="Sign Up", bg='#333333', fg='#20b4aa', font=('Arial', 40))
username_label = tk.Label(user_frame, text="Username", bg='#333333', fg='#FFFFFF', font=('Arial', 10))
username_entry = tk.Entry(user_frame, font=('Arial', 10))
message = tk.Label(window, bg='#333333', font=('Arial', 10))
password_entry = tk.Entry(pass_frame, font=('Arial', 10))
password_label = tk.Label(pass_frame, text="PassWord", bg='#333333', fg='#FFFFFF', font=('Arial', 10))
erreur_vide = tk.Label(window, bg='#333333', font=('Arial', 10))
sign_up_button = tk.Button(sign_up_frame, text="Sign Up", bg='#20b4aa', fg='#FFFFFF', font=('Arial', 10), highlightbackground='#1dc8bd', activebackground='#1dc8bd', command=submit)
sign_up_label.grid(row=0, column=0, columnspan=3, pady=40, padx=40)
user_frame.grid(row=1, column=0, columnspan=3, pady=10, padx=20)
pass_frame.grid(row=2, column=0, columnspan=3, pady=10, padx=20)
username_label.grid(row=0, column=0, padx=(0, 10))
username_entry.grid(row=0, column=1, padx=(10, 0))
password_label.grid(row=0, column=0, padx=(0, 10))
password_entry.grid(row=0, column=1, padx=(10, 0))

sign_up_button.grid(row=4, column=0, columnspan=3, pady=30)

window.mainloop()
