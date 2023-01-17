import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox, Menu
from Users import *
from FrmAdmin1 import *
from FrmAdmin2 import *
from FrmAdmin3 import *
from FrmManager1 import *
from FrmManager2 import *
from FrmManager3 import *
from FrmOperator1 import *
from FrmOperator2 import *
from FrmOperator3 import *


class Dashboard:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("600x600")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.my_w_child = None
        self.aturKomponen()
        
    def new_window( self, number, _class):
        new = tk.Toplevel()
        new.transient()
        new.grab_set()
        _class(new, number)
       
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        mainmenu = Menu(self.parent)
        self.parent.config(menu=mainmenu)
        file_menu1 = Menu(mainmenu)
        
        # Menu Awal
        file_menu1.add_command(
            label='Login', command=self.show_login
        )
        file_menu1.add_command(
            label='Exit', command=root.destroy
        )
        
        # Tampilkan menu ke layar
        mainmenu.add_cascade(
            label="File", menu=file_menu1
        )
        
        

    def menuAdmin(self):
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
       
        # create a menu
        file_menu = Menu(menubar)
        admin_menu = Menu(menubar)

        # Menu File
       
        file_menu.add_command(
            label='Logout', command=self.onLogout
        )
        file_menu.add_command(
            label='Exit', command=root.destroy
        )

      
        # Menu Admin
        admin_menu.add_command(
            label='Menu Admin 1', command= lambda: self.new_window("Menu Admin 1", FrmAdmin1)
        )
        admin_menu.add_command(
            label='Menu Admin 2', command= lambda: self.new_window("Menu Admin 2", FrmAdmin2)
        )
        admin_menu.add_command(
            label='Menu Admin 3', command= lambda: self.new_window("Menu Admin 3", FrmAdmin3)
        )

        
        # Tampilkan menu ke layar
        menubar.add_cascade(
            label="File", menu=file_menu
        )
        
        menubar.add_cascade(
            label="Menu Admin", menu=admin_menu
        )
       

    def menuManager(self):
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
       
        # create a menu
        file_menu = Menu(menubar)
        manager_menu = Menu(menubar)
        
        # Menu File
        file_menu.add_command(
            label='Logout', command=self.onLogout
        )
        file_menu.add_command(
            label='Exit', command=root.destroy
        )

      

        # Menu Manager
        manager_menu.add_command(
            label='Menu Manager 1', command= lambda: self.new_window("Menu Manager 1", FrmManager1)
        )
        manager_menu.add_command(
            label='Menu Manager 2', command= lambda: self.new_window("Menu Manager 2", FrmManager2)
        )
        manager_menu.add_command(
            label='Menu Manager 3', command= lambda: self.new_window("Menu Manager 3", FrmManager3)
        )
        

        
        # Tampilkan menu ke layar
        menubar.add_cascade(
            label="File", menu=file_menu
        )    
        menubar.add_cascade(
            label="Menu Manager", menu=manager_menu
        )
             

    def menuOperator(self):
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
       
        # create a menu
        file_menu = Menu(menubar)
        operator_menu = Menu(menubar)

        # Menu File
       
        file_menu.add_command(
            label='Logout', command=self.onLogout
        )
        file_menu.add_command(
            label='Exit', command=root.destroy
        )

      
        # Menu Operator
        operator_menu.add_command(
            label='Menu Operator 1', command= lambda: self.new_window("Menu Operator 1", FrmOperator1)
        )
        operator_menu.add_command(
            label='Menu Operator 2', command= lambda: self.new_window("Menu Operator 2", FrmOperator2)
        )
        operator_menu.add_command(
            label='Menu Operator 3', command= lambda: self.new_window("Menu Operator 3", FrmOperator3)
        )
        
        # Tampilkan menu ke layar
        menubar.add_cascade(
            label="File", menu=file_menu
        )
        menubar.add_cascade(
            label="Menu Operator", menu=operator_menu
        )
        
    def show_login(self):
        self.my_w_child=tk.Toplevel(root)
        self.my_w_child.geometry("250x200") 
                # pasang Label
        Label(self.my_w_child, text='Username:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(self.my_w_child, text="Password:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtUsername = Entry(self.my_w_child) 
        self.txtUsername.grid(row=0, column=1, padx=5, pady=5)
        
        self.txtPassword = Entry(self.my_w_child) 
        self.txtPassword.grid(row=1, column=1, padx=5, pady=5)  
        self.txtPassword.config(show='*')
                
        # Pasang Button
        self.btnLogin = tk.Button(self.my_w_child, text='Login',
            command=self.onLogin)
        self.btnLogin.grid(row=2, column=1, padx=5, pady=5)
        

    def onLogin(self, event=None):
        u = self.txtUsername.get()
        p = self.txtPassword.get()
        A = Users()
        B =[]
        B = A.Login(u,p)
        
        if(B[0]=='True'):           
            if(B[1]=='admin'):
                self.my_w_child.destroy()
                self.menuAdmin()
            elif(B[1]=='manager'): 
                self.my_w_child.destroy() 
                self.menuManager()
            elif(B[1]=='operator'):
                self.my_w_child.destroy()
                self.menuOperator()
            else: 
                messagebox.showinfo("showinfo", "Maaf, User tidak dikenal")    
            
        else:
            messagebox.showinfo("showinfo", "Login Not Valid")   

    def onLogout(self):
        self.aturKomponen()
                    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
    

if __name__ == '__main__':
    root = tk.Tk()
    my_str = tk.StringVar()
    aplikasi = Dashboard(root, "Dashboard Aplikasi")
    root.mainloop() 