from tkinter import *
import random

def arriba():
    c.move(ball, 0, -10)
    

def abajo():
    c.move(ball, 0, 10)
    

def izquierda():
    c.move(ball, -10, 0)
  
def derecha():
    c.move(ball, 10, 0)
    

      
BASE=480
ALTURA=240
ventana_principal=Tk()
ventana_principal.geometry("500x500")
ventana_principal.title("Taller_nave")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="white")



frame_graficacion=Frame(ventana_principal)
frame_graficacion.config(bg="black",width=480 , height=240)
frame_graficacion.place(x=10, y=10)

c=Canvas(frame_graficacion, width=480, height=240)
c.config(bg="azure")
c.place(x=0, y=0)

photo= PhotoImage(file="universo.png")
c.create_image(0,-60, image=photo, anchor=NW)



for i in range (10):
    x=random.randint(10, BASE-20)
    y=random.randint(0,ALTURA-2)
    color="#" 
    for caracter in range(6):
      color=color+random.choice("0123456789ABCDEF")
    circulo1=c.create_oval(x,y,x+5,y+5, fill=color)
for i in range (20):
    x=random.randint(0, BASE-20)
    y=random.randint(0,ALTURA-2)
    color="#" 
    for caracter in range(6):
      color=color+random.choice("0123456789ABCDEF")
    circulo2=c.create_oval(x,y,x+10,y+10, fill=color)
    
for i in range (10):
    x=random.randint(10, BASE-20)
    y=random.randint(0,ALTURA-2)
    color="#" 
    for caracter in range(6):
      color=color+random.choice("0123456789ABCDEF")
    circulo3=c.create_oval(x,y,x+15,y+15, fill=color)

ball_image= PhotoImage(file="nave.png")
initial_position = (200, 200)
ball = c.create_image(initial_position[0], initial_position[1], image=ball_image)

frame_controles=Frame(ventana_principal)
frame_controles.config(bg="SlateGray2", width=480, height=230)
frame_controles.place(x=10,y=260)

boton_1= PhotoImage(file="f2.png")
boton_2 = PhotoImage(file="f4.png")
boton_3 = PhotoImage(file="f1.png")
boton_4= PhotoImage(file="f3.png")

bt_1 = Button(frame_controles, image=boton_1, text="boton_1",command=arriba)
bt_1.place(x=BASE/2-10,y=ALTURA/2-70, anchor="center")

bt_4=Button(frame_controles, image=boton_4, text="boton_4",command=abajo)
bt_4.place(x=BASE/2-40, y=ALTURA/2+20)

bt_2 = Button(frame_controles, image=boton_2, text="boton_2",command=derecha)
bt_2.place(x=BASE/2+20, y=ALTURA/2-45 )

bt_3=Button(frame_controles, image=boton_3, text="boton_3",command=izquierda)
bt_3.place(x=BASE/2-100, y=ALTURA/2-45)





ventana_principal.mainloop()