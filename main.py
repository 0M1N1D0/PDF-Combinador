
from tkinter import messagebox
from PyPDF2 import PdfFileMerger, PdfFileReader
import os 
from tkinter import *
from tkinter import filedialog



root = Tk() # raíz

# configuración de atributos
root.title("PDF Combinador")
# root.iconbitmap(r"C:\Users\vctr2\Desktop\python\proyectos\pdf_merge\icono3.ico") 
root.iconbitmap("icono3.ico") 
root.resizable(False, False)
root.geometry("260x300")

frame = Frame(root, bd=10) # el marco se introduce dentro de la raíz 
frame.pack()  #el marco de empaqueta o se distribuye dentro de la raíz 
frame.config(width=480, height=320) # se establece el tamaño de la ventana en pixeles

lista_portada = []
lista_bases = []
dir_portada = ""
dir_bases = ""
dir_destino = ""

def obtener_ruta_portada():
    global lista_portada
    global dir_portada
    dir_portada = filedialog.askdirectory()
    lista_portada = os.listdir(dir_portada)
    # print("Dirección portada: {0}".format(dir_portada))
    # print("Lista portada: {0}".format(lista_portada))
    messagebox.showinfo(title="PDF Combinador", message="Se ha seleccionado la ruta del archivo portada")


def obtener_ruta_bases():
    global lista_bases
    global dir_bases
    dir_bases = filedialog.askdirectory()
    lista_bases = os.listdir(dir_bases)
    # print("Dirección bases: {0}".format(dir_bases))
    # print("Lista bases: {0}".format(lista_bases))
    messagebox.showinfo(title="PDF Combinador", message="Se ha seleccionado la ruta del archivo bases")
    
def obtener_ruta_destino():
    global dir_destino
    dir_destino = filedialog.askdirectory()
    # print("Dirección destino: {0}".format(dir_destino))
    messagebox.showinfo(title="PDF Combinador", message="Se ha seleccionado la ruta del archivo destino")

def generar_combinaciones():
    global dir_destino
    global dir_portada
    global dir_bases

    # comprueba que las rutas no estén vacías
    if dir_portada == "" or dir_destino == "" or dir_bases == "":
        messagebox.showerror(title="PDF Combinador", message="Ha ocurrido un error. Alguna de las rutas no se ha seleccionado")
    else: 

        i = 1
        # evalúa que el merge se haga correctamente
        try:
            for file in lista_bases:

                merger = PdfFileMerger()
                merger.append(PdfFileReader(dir_portada + '\\' + lista_portada[0]))
                merger.append(PdfFileReader(dir_bases + '\\' + file))
                merger.write(r"{0}\result{1}.pdf".format(dir_destino, i))
                i += 1

                # messagebox.showerror(title="PDF Combinador", message="Ha ocurrido un error en la instacia de PdfFileMerger()")

                merger.close()
        except:
            messagebox.showerror(title="PDF Combinador", message="Ha ocurrido un error en el ciclo con la instancia merger.")
        else: 
            messagebox.showinfo("PDF Combinador", message="Combinación exitosa")

# ***********************************************
# v = StringVar()
# Label(master, textvariable=v).pack()

# v.set("New Text!")


# label portada
label_portada = Label(frame, text="Carpeta de archivo de portada", justify="left")
label_portada.grid(column=0, row=0, sticky="NW", pady=10)
# boton portada
button_portada = Button(frame, text="Seleccionar", command=obtener_ruta_portada)
button_portada.grid(column=1, row=0)


# label bases
label_bases =  Label(frame, text="Carpeta de archivos de bases", justify="left")
label_bases.grid(column=0, row=1, sticky="NW")
# boton bases
button_bases = Button(frame, text="Seleccionar", command=obtener_ruta_bases)
button_bases.grid(column=1, row=1)

# sepatador (siempre se pone dentro del root)
#separador = Separator(root, orient="horizontal").pack(fill='x')

# label destino
label_destino = Label(frame, text="Carpeta destino", justify="left")
label_destino.grid(column=0, row=2, sticky="NW", pady=10)
# boton destino
boton_destino = Button(frame, text="Seleccionar", command=obtener_ruta_destino)
boton_destino.grid(column=1, row=2)
# boton generar
boton_generar = Button(frame, text="Generar combinación", justify='center', command=generar_combinaciones)
boton_generar.grid(columnspan=2, sticky="EW")

# root.wm_attributes('-toolwindow', 'True')
root.mainloop()







