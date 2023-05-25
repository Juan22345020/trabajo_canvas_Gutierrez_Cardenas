import random
from tkinter import *



#VARIABLES GLOBALES
BASE = 355
ALTURA = 220
ANCHO_CANVAS = BASE + 20
ALTO_CANVAS = ALTURA + 20
VELOCIDAD_PELOTA = 2
direccion_x = 1
direccion_y = 1



#DEFINICION DE LA FUNCION
def mover_pelota():
    global direccion_x, direccion_y  
    x0, y0, _ , _ = c.coords(pelota)
    nuevo_x = x0 + direccion_x * VELOCIDAD_PELOTA
    nuevo_y = y0 + direccion_y * VELOCIDAD_PELOTA

    if nuevo_x + radio < 0 or nuevo_x + radio > ANCHO_CANVAS:
        direccion_x = -direccion_x  

    if nuevo_y + radio < 0 or nuevo_y + radio > ALTO_CANVAS:
        direccion_y = -direccion_y  

 
    c.move(pelota, direccion_x * VELOCIDAD_PELOTA, direccion_y * VELOCIDAD_PELOTA)
   
    c.after(10, mover_pelota)



#VENTANA PRINCIPAL
ventana_principal=Tk()
ventana_principal.geometry("400x350")
ventana_principal.title("Soccer Aleatorio")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="gray")

#FRAME DONDE SE GRAFICARÁ EL CANVAS

frame_graficacion=Frame(ventana_principal)
frame_graficacion.config(bg="light cyan",width=380 , height=330)
frame_graficacion.place(x=10, y=10)


#CANVAS DE FUTBOL
c=Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="green")
c.place(x=10, y=10)



#LINEAS DE LA CANCHA
linea1=c.create_line(10,10, BASE-10,10, fill="white",width=10)
linea2=c.create_line(BASE-10,10,BASE-10, ALTURA-10, fill="white",width=10)
linea3=c.create_line(BASE-10, ALTURA-10,10,ALTURA-10,fill="white",width=10)
linea4=c.create_line(10, ALTURA-10,10,10, fill="white",width=10)
linea5=c.create_line(BASE-177,10,BASE-177, ALTURA-10, fill="white",width=10)
linea6=c.create_line(BASE-59,ALTURA-140,BASE-59, ALTURA-70, fill="white",width=10)
linea7=c.create_line(BASE-296,ALTURA-140,BASE-296, ALTURA-70, fill="white",width=10)
linea8=c.create_line(ALTURA-210,80,BASE-295,80, fill="white",width=10)
linea9=c.create_line(ALTURA-210,149,BASE-295,149, fill="white",width=10)
linea10=c.create_line(ALTURA+125,80,BASE-60,80, fill="white",width=10)
linea11=c.create_line(ALTURA+125,149,BASE-60,149, fill="white",width=10)
circle=c.create_oval(BASE/2-30,ALTURA/2-30,BASE/2 +30,ALTURA/2+30, fill="white")


# Definir el radio y coordenadas del óvalo
radio = 20
x0 = BASE/2 - radio
y0 = ALTURA/2 - radio
x1 = BASE/2 + radio
y1 = ALTURA/2 + radio

pelota = c.create_oval(x0, y0, x1, y1, fill="grey")



#BOTON DE MOVER PELOTA
boton = Button(frame_graficacion, text="Mover Balón", command=mover_pelota)
boton.place(x=130, y=280, width=100, height=20)

ventana_principal.mainloop()