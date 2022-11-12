# Interfaz gráfica de 

from tkinter import *
from tkinter import messagebox
from math import sqrt


# Funciones de la app

def calcular():
    messagebox.showinfo("Cálculo v1.0" , "Hizo cluck en el botón Calcular...")
    a = int(x.get())
    b = int(y.get())
    c = int(z.get())
    
    k = (b**2)-4*(a)*(c)
    if k < 0:
        messagebox.showwarning(message="¡La Entrada es Compleja!\nLa solución estará dada por números complejos.",title="Precaución")  
    elif k > 0:
        x1 = (b*(-1) + sqrt(k))/(2*a)
        x2 = (b*(-1) - sqrt(k))/(2*a)
        t_resultados.insert(INSERT, "La ecuación que involucra a "+ x.get()+" como término cuadrático, "+ y.get()+" como término lineal y "+ z.get()+ " como término independiente es " "\n"+str(x1)+ "\n" +str(x2)+ "\n")


def borrar():
    messagebox.showinfo("Cálculo v1.0", "Los datos a continuación serán borrados...")
    x.set("")
    y.set("")
    z.set("")
    t_resultados.delete("1.0","end")


def salir():
    messagebox.showinfo("Cálculo v1.0", "La app se cerrará...")
    principal.destroy()


# Ventana principal
principal = Tk()

principal.title("Ecuación Cuadrática")

principal.geometry("600x500")

principal.resizable(False , False)

principal.config(bg="purple")



# Variables Globales

x = StringVar()
y = StringVar()
z = StringVar()

# Frame entrada

frame_entrada = Frame(principal)
frame_entrada.config(bg="white", width=580 , height=240)
frame_entrada.place(x=10 , y=10)

# Etiqueta para el título de la app
titulo = Label(frame_entrada, text= "Ecuación de Segundo grado")
titulo.config(bg= "white", fg="saddle brown", font=("Times New Roman", 20))
titulo.place(x=140 , y=10, width=330 , height=30)

# Etiqueta para x
lb_x = Label(frame_entrada, text= "= A² ")
lb_x.config(bg="white", fg="green" , font=("Times New Roman", 22))
lb_x.place(x=150 , y= 50 , width=115 , height=30) 

# Entry para x
entry_x = Entry(frame_entrada, textvariable=x)
entry_x.config(font=("Times New Roman", 24), justify=LEFT, fg="blue")
entry_x.focus_set()
entry_x.place(x=60 , y=50 , width=115 , height=30)

# Etiqueta para y
lb_y = Label(frame_entrada , text= "= B ")
lb_y.config(bg="white", fg="blue", font=("Times New Roman",22))
lb_y.place(x=270, y=90, width=115, height=30)

# Entry para y
entry_y = Entry(frame_entrada,textvariable=y)
entry_y.config(font=("Times New Roman",22), justify=LEFT, fg="blue")
entry_y.place(x=180,y=90,width=115, height=30)

#Etiqueta para z
lb_z = Label(frame_entrada , text="= C ")
lb_z.config(bg= "white" , fg="red" , font=("Times New Roman", 22))
lb_z.place(x=390 , y=130, width=115 , height=30)

#Entry para z
entry_z = Entry(frame_entrada , textvariable=z)
entry_z.config(font=("Times New Roman", 22), justify=LEFT , fg="blue")
entry_z.place(x=300, y=130 , width=115, height=30)

# Frame operaciones


frame_operaciones = Frame(principal)
frame_operaciones.config(bg="white", width=580 , height=90)
frame_operaciones.place(x=10 , y=270)

# Botón para Calcular

bt_calcular = Button(frame_operaciones, text="Calcular", command=calcular)
bt_calcular. place(x=30, y=35 , width=100 , height=30)

#Botón para Borrar
bt_borrar = Button(frame_operaciones, text="Borrar" , command=borrar)
bt_borrar.place(x=230,y=35, width=100, height=30)


#Botón para salir
bt_salir = Button(frame_operaciones, text="Salir", command=salir)
bt_salir.place(x=420,y=35, width=100, height=30)


# Frame resultados
frame_resultados = Frame(principal)
frame_resultados.config(bg="white" , width=580 , height=110)
frame_resultados.place(x=10 , y=380)

# area de texto para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="steelblue1", fg="black", font=("Times New Roman",16))
t_resultados.place(x=10,y=10,width=560,height=90)


principal.mainloop()
