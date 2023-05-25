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

photo= PhotoImage(file="cancha.png")
c.create_image(0,0, image=photo, anchor=NW)





#
radio = 20
x0 = BASE/2 - radio
y0 = ALTURA/2 - radio
x1 = BASE/2 + radio
y1 = ALTURA/2 + radio

pelota = c.create_oval(x0, y0, x1, y1, fill="DarkSeaGreen2")




boton = Button(frame_graficacion, text="Mover Balón", command=mover_pelota)
boton.place(x=130, y=280, width=100, height=20)

ventana_principal.mainloop()