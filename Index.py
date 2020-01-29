from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBase

# Criando uma janela
home = Tk()
home.title("MS Sistemas - Login de acesso")
home.geometry("600x300")
home.configure(background = "white")
home.resizable(width = False, height = False)
home.attributes("-alpha", 0.9)
# home.iconbitmap(default = "icons/LogoIcon.ico")

#----- Logo -----------
# logo = PhotoImage(file="./icons/logo.png")

# ------- Widgets -----------
letfFrame = Frame(home, width = 150, height = 300, bg = "MIDNIGHTBLUE", relief = "raise")
letfFrame.pack(side = LEFT)

rightFrame = Frame(home, width = 450, height = 300, bg = "WHITE", relief = "raise")
rightFrame.pack(side = RIGHT)

# LogoLabel = Label(letfFrame, image = logo, bg = "MIDNIGHTBLUE")
# LogoLabel.place(x = 50, y = 100) 

UserLabel = Label(rightFrame, text = "Username:", font=("Century Gothic", 20), 
  bg = "WHITE", fg = "MIDNIGHTBLUE")
UserLabel.place(x = 5, y = 50)

UserEntry = ttk.Entry(rightFrame, width = 45)
UserEntry.place(x = 150, y = 65)

PassLabel = Label(rightFrame, text = "Password:", font=("Century Gothic", 20), 
  bg = "WHITE", fg = "MIDNIGHTBLUE")
PassLabel.place(x = 5, y = 100)

PassEntry = ttk.Entry(rightFrame, width = 45, show = "*")
PassEntry.place(x = 150, y = 115)

# ----------------------- Função que busca se o usuário existe no BD ----------------
def LoginUser():
  User = UserEntry.get()
  Pass = PassEntry.get()

  DataBase.cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (User, Pass))
  
  VerifyLogin = DataBase.cursor.fetchone()

  try:
    if (User in VerifyLogin and Pass in VerifyLogin):
      messagebox.showinfo(title = "Login", message = "Bem Vindo!")
    else:
      pass
  except:
    messagebox.showinfo(title = "Login", message = "Erro, Usuário não encontrado!") 

LoginButton = ttk.Button(rightFrame, text = "Login", width = 45, command = LoginUser)
LoginButton.place(x = 150, y = 150)

# -------------------- Função para alternar para a tela de registro ----------------------
def Register():
  # Removendo os botões de login
  LoginButton.place(x = 5000)
  RegisterButton.place(x = 5000)

  # inserindo os campos e botões do cadastro
  NomeLabel = Label(rightFrame, text = "Name:", font=("Century Gothic", 20), 
    bg = "WHITE", fg = "MIDNIGHTBLUE")
  NomeLabel.place(x = 5, y = 140)
  NomeEntry = ttk.Entry(rightFrame, width = 45)
  NomeEntry.place(x = 150, y = 155)

  EmailLabel = Label(rightFrame, text = "Email:", font=("Century Gothic", 20), 
    bg = "WHITE", fg = "MIDNIGHTBLUE")
  EmailLabel.place(x = 5, y = 180)
  EmailEntry = ttk.Entry(rightFrame, width = 45)
  EmailEntry.place(x = 150, y = 190)

  # ------------------- Função para salvar os dados dos inputs no DB --------------------
  def SalveToDataBase():
    Name = NomeEntry.get()
    Email = EmailEntry.get()
    User = UserEntry.get()
    Pass = PassEntry.get()

    if (Name == "" or Email == "" or User == "" or Pass == ""):
      messagebox.showwarning(title = "Aviso", message = "Dados do usuário não informados!")
    else: 
      DataBase.cursor.execute("INSERT INTO users(name, email, username, password) VALUES('"+Name+"', '"+Email+"', '"+User+"', '"+Pass+"')")
      DataBase.conn.commit()
      messagebox.showinfo(title = "Registro Info", message = "Usuário salvo com súcesso!")

  SalveButton = ttk.Button(rightFrame, text = "Salvar", width = 45, command = SalveToDataBase)
  SalveButton.place(x = 150, y = 220)

  # -------------------- Função para voltar para a tela de login --------------------------
  def CancelBackToLogin():
    NomeLabel.place(x = 5000)
    NomeEntry.place(x = 5000)
    EmailLabel.place(x = 5000)
    EmailEntry.place(x = 5000)
    SalveButton.place(x = 5000)
    CancelButton.place(x = 5000)

    LoginButton.place(x = 150)
    RegisterButton.place(x = 150)

  CancelButton = ttk.Button(rightFrame, text = "Cancelar", width = 45, command = CancelBackToLogin)
  CancelButton.place(x = 150, y = 255)

RegisterButton = ttk.Button(rightFrame, text = "Registro", width = 45, command = Register)
RegisterButton.place(x = 150, y = 180)

home.mainloop() # Finaliza a criação da janela com suas configurações