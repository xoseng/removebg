# coding=utf8
# author: Xosé Brais Noya García

# IMPORTS

#info about imports
#pip install opencv-python
#pip install scikit-image
#pip install tensorflow matplotlib
#pip install imageio

#imports personal libraries
import cmd_command
import tkinter_library_functions
import img_library_functions
#import data_loader

import os

#removebg necesary imports
#from torch import *

#tkinter neccesary imports
from PIL import Image
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import webbrowser
import threading
from tkinter import ttk

def main_start():

    # NO TK FUNCTIONS
    def clear_vals():

        val_filelist.set('')
        val_workfile.set('')
        val_numfile.set(0)
        val_filepath.set('')

        if os.path.exists('./static') == False:
            try:
                cmd_command.wincmd('mkdir static')
            except:
                pass

        if os.path.exists('./static/inputs') == False:
            try:
                cmd_command.wincmd('cd static && mkdir inputs')
            except:
                pass

        if os.path.exists('./static/masks') == False:
            try:
                cmd_command.wincmd('cd static && mkdir masks')
            except:
                pass

        if os.path.exists('./static/results') == False:
            try:
                cmd_command.wincmd('cd static && mkdir results')
            except:
                pass

        try:
            cmd_command.wincmd('cd static && cd inputs &&  DEL /F/Q/S *.* > NUL')
        except:
            pass

        try:
            cmd_command.wincmd('cd static && cd masks &&  DEL /F/Q/S *.* > NUL')
        except:
            pass

        try:
            cmd_command.wincmd('cd static && cd results &&  DEL /F/Q/S *.* > NUL')
        except:
            pass

    def set_file():
        pathtoset = tkinter_library_functions.get_filepathload()
        val_filelist.set(pathtoset)
        num_files=len(pathtoset)
        val_numfile.set(num_files)
        if num_files == 0:
            num_files=str(num_files)
            val_workfile.set('No images selected!')
        elif num_files == 1:
            val_workfile.set('You have selected ' + str(num_files) + ' image!')
        else:
            val_workfile.set('You have selected '+str(num_files)+' images!')

    def start_work():
        if val_filelist.get() == '':
            clear_vals()
            tkinter_library_functions.warning_file()
        else:
            filepath=tkinter_library_functions.set_folderpathsave()
            val_filepath.set(filepath)
            if filepath == '':
                clear_vals()
                tkinter_library_functions.warning_path()
            else:
               #print ("Procesar fotos, guardar en "+filepath)
               filelist = val_filelist.get()
               files_number = val_numfile.get()
               files_number = files_number
               i = 0
               while (i < files_number):
                   file_path = filelist.split(',')[i]
                   file_path = file_path.split("'")[1]
                   file_path = file_path.replace("/", "\\")
                   file_path = file_path.strip()
                   # ELIMINAR FONDO
                   img_library_functions.startremovebg(file_path)
                   i = i + 1

               #MOVER AL PATH EL CONTENIDO DE RESULTS
               try:
                   cmd_command.wincmd('cd static && cd results && copy * "' + filepath + '"')
               except:
                   pass
               #LIMPIAR TEMPORALES
               clear_vals()
               #ABRIR CARPETA
               try:
                cmd_command.wincmd('explorer "' + filepath + '"')
               except:
                   pass

    # MAIN SCREEN
    version_software = 'RemoveBG v0.1'
    logo_path='./img/logo.ico'
    root = Tk()
    root.config(bd=30)
    root.title(version_software)  # Titulo de la ventana
    root.iconbitmap(logo_path)  # Icono de la ventana, en ico o xbm en Linux
    root.resizable(0, 0)  # Desactivar redimension de ventana

    menubar = Menu(root)
    root.config(menu=menubar)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="License agreement", command=tkinter_library_functions.license_agreement_gnu)
    helpmenu.add_command(label="Project website", command=tkinter_library_functions.project_website)
    helpmenu.add_command(label="About", command=tkinter_library_functions.about_program)
    helpmenu.add_command(label="Exit", command=tkinter_library_functions.exit_program)
    menubar.add_cascade(label="Info", menu=helpmenu)

    imgpath = './img/logo.png'
    img_tk = ImageTk.PhotoImage(Image.open(imgpath))
    imglabel = Label(root, image=img_tk).grid(row=1, column=1, padx=5, pady=5)

    # GLOBAL TK VARS DECLARATION
    val_workfile = StringVar()
    val_filelist = StringVar()
    val_numfile = IntVar()
    val_filepath = StringVar()

    # BUTTONS LABEL FORM
    workfile_button=Button(root, justify="left", text="SELECT FILES", command=set_file).grid(row=2, column=0, padx=5, pady=2)
    workfile_value=Entry(root, justify="center", textvariable=val_workfile, state="disabled", width=40).grid(row=2, column=1, padx=5, pady=2)
    reset_button=Button(root, justify="left", text="RESTART", command=clear_vals).grid(row=2, column=2, padx=5, pady=2)
    starbutton=Button(root, justify="left", text="START", command=start_work).grid(row=7, column=1, padx=5, pady=5)

    # CENTER WINDOW TO SCREEN
    tkinter_library_functions.center(root)
    # LOOP TK
    root.mainloop()

main_start()
