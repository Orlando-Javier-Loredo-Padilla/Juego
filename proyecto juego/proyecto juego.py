# -*- coding: utf-8 -*-
"""
Created on Mon May 22 21:08:39 2023

@author: orlando
"""

from tkinter import Tk, Canvas, Frame, Label, Entry, Button, W, E, Listbox, END
import tkinter
import contextlib
import io
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import ttk
import random
import keyboard
#import personajes


ventana = tkinter.Tk()
ventana.title("Juego")

ventana.geometry("700x500+100+100")

image = tk.PhotoImage(file="Pantalla1.png")
Ifon = ttk.Label(image=image)
Ifon.place(x = 0, y = 0) 

###Listas y variables########################################################################

##Seleccion de personajes###############

global contadorR #Contador de personajes del rival
contadorR = 0
global contadorP  #Contador de personajes del jugador
contadorP = 0

#Contadores de vida

global PSP1 #vida de tu personaje n1
PSP1 = 0
global PSP2 #vida de tu persoanaje n2
PSP2 = 0
global PSR1 #vida de tu rival n1
PSR1 = 0
global PSR2 #vida de tu rival n2
PSR2 = 0
global activos #Personajes con vida superior a 0
activos = 0

global HP1 #vida de tu personaje n1
HP1 = 0
global HP2 #vida de tu persoanaje n2
HP2 = 0
global HR1 #vida de tu rival n1
HR1 = 0
global HR2 #vida de tu rival n2
HR2 = 0

#Acciones de combate####################
global turno_on #activa el combate
turno_on = 0
global turnos #contador de turnos
turnos = 0
global proteccion 
proteccion = 0
global potenciar 
potenciar = 0

#datos de tu personaje##############
personaje = [0, 0, 0]
vidaP = [0, 0, 0]
#datos del personaje rival#############
rival = [0, 0, 0]
vidaR = [0, 0, 0]
##Datos del combate ############
accion = []    #Prioridad, accion, destino
comandos = []
#comandos = [] #lista sin modificar 
jugadores = [0, 0, 0, 0, 0]


##Personajes#########
name = ["Null", "Caballero", "Luchador", "Hechicera",
         "Acorazado", "Sacerdotisa", "Princesa"]

###Salir###########################################################################################

def salir(ventana_a_cerrar):
    ventana_a_cerrar.destroy()
    ventana.deiconify()
    
def salir2(ventana_a_cerrar):
    global contadorR
    global contadorP
    #Recuperar los datos#############
    contadorP = 0
    contadorR = 0
    #Recuperar la pantalla anterior
    ventana_a_cerrar.destroy()
    segunda_pantalla()

def salir3(ventana_a_cerrar, user1):
    global contadorR
    global contadorP
        
    contadorP = 0
    contadorR = 0
    ventana_a_cerrar.destroy()
    user1.deiconify()
       
    
###cuarta pantalla################################################################################ 

def cuarta_pantalla(user2):
     
    user3 = tkinter.Toplevel(user2)
    user3.title("Combate")
    user3.geometry("1200x650+10+10")
    
    user2.withdraw() 
    
    image8 = tk.PhotoImage(file="Pantalla4.png")
    Ifon8 = ttk.Label(user3, image=image8)
    Ifon8.place(x = 0, y = 0) 
    
    for i in range (0, 5):
        if jugadores[i] == 1:    
            nombre = "personaje1.png"
        if jugadores[i] == 2: 
            nombre = "personaje2.png"
        if jugadores[i] == 3: 
            nombre = "personaje3.png"
        if jugadores[i] == 4:  
            nombre = "personaje4.png"
        if jugadores[i] == 5: 
            nombre = "personaje5.png" 
        if jugadores[i] == 6: 
            nombre = "personaje6.png"
        
        if i == 0: 
            image9 = tk.PhotoImage(file=nombre)   
            Ifon9 = ttk.Label(user3, image=image9)
            Ifon9.place(x = 30, y = 120)
        if i == 1:
            image10 = tk.PhotoImage(file=nombre)   
            Ifon10 = ttk.Label(user3, image=image10)
            Ifon10.place(x = 30, y = 340)
        if i == 2:
            image11 = tk.PhotoImage(file=nombre)   
            Ifon11 = ttk.Label(user3, image=image11)
            Ifon11.place(x = 970, y = 120)
        if i == 3:
            image7 = tk.PhotoImage(file=nombre)   
            Ifon7 = ttk.Label(user3, image=image7)
            Ifon7.place(x = 970, y = 340)
    #\n
    FPSP1 = PSP1
    FPSP2 = PSP2
    FPSR1 = PSR1
    FPSR2 = PSR2
    
    #Tu vida######################
    v1 = tkinter.Label(user3, text=("Vida"), font=("arial", 25))
    v1.place(x=240, y=150) 
    
    v2 = tkinter.Label(user3, text=("Vida"), font=("arial", 25))
    v2.place(x=240, y=350) 
    
    HPP1 = tkinter.Label(user3, text=(PSP1, "/", FPSP1), font=("arial", 20))
    HPP1.place(x=240, y=190) 
    
    HPP2 = tkinter.Label(user3, text=(PSP2, "/", FPSP2), font=("arial", 20))
    HPP2.place(x=240, y=390) 
    
    HaP1 = tkinter.Label(user3, text=("HAB:",  HP1), font=("arial", 20))
    HaP1.place(x=240, y=230) 
    
    HaP2 = tkinter.Label(user3, text=("HAB:", HP2), font=("arial", 20))
    HaP2.place(x=240, y=420) 
    
    #Vida del rival#############################
    
    v3 = tkinter.Label(user3, text=("Vida"), font=("arial", 25))
    v3.place(x=890, y=150) 
    
    v4 = tkinter.Label(user3, text=("Vida"), font=("arial", 25))
    v4.place(x=890, y=350) 
    
    HPR1 = tkinter.Label(user3, text=(PSR1, "/", FPSR1), font=("arial", 20))
    HPR1.place(x=850, y=190) 
    
    HPR2 = tkinter.Label(user3, text=(PSR2, "/", FPSR2), font=("arial", 20))
    HPR2.place(x=850, y=390) 

    HaR1 = tkinter.Label(user3, text=("HAB:",  HR1), font=("arial", 20))
    HaR1.place(x=870, y=230) 
    
    HaR2 = tkinter.Label(user3, text=("HAB:", HR2), font=("arial", 20))
    HaR2.place(x=870, y=420) 
    
    ############################
    
    MT = tkinter.Label(user3, text=(" "), font=("arial", 14))
    MT.place(x=400, y=560) 
    
    MC = tkinter.Label(user3, text=("Esperando acciones"), font=("arial", 14))
    MC.place(x=400, y=585) 
    
    MH = tkinter.Label(user3, text=(" "), font=("arial", 14))
    MH.place(x=400, y=610) 
  
    def botones():
        global PSP1, PSP2
        
    ##Botones del primer personaje############################################################
        if  PSP1 > 0:  
            if PSR1 > 0:
                Boton7 = tkinter.Button(user3, text=("Atacar a " + name[rival[0]]), font=("arial", 13),  bg="gray48", 
                                                      command=lambda: seleccion(1, 1, 2, 0))
                Boton7.place(x = 30, y = 20)
            
            if PSR2 > 0:  
                Boton8 = tkinter.Button(user3, text=("Atacar a " + name[rival[1]]),  font=("arial", 13),  bg="gray48",
                                                      command=lambda: seleccion(1, 1, 3, 0))
                Boton8.place(x = 30, y = 60)
            
            if HP1 > 2:  
                Boton9 = tkinter.Button(user3, text="Habilidad", font=("arial", 13),  bg="gray48",
                                                command=lambda: seleccion(2, 2, 0, 0))
                Boton9.place(x = 230, y = 20)    
            
            Boton10 = tkinter.Button(user3, text="Protegerse", font=("arial", 13),  bg="gray48",
                                     command=lambda: seleccion(3, 3, 0, 0))
            Boton10.place(x = 230, y = 60)
    
    #Botones del segundo personaje############################################################
    
        if  PSP2 > 0:
            if PSR1 > 0:
                Boton11 = tkinter.Button(user3, text=("Atacar a " + name[rival[0]]), font=("arial", 13),  bg="gray48", 
                                                       command=lambda: seleccion(1, 1, 2, 1))
                Boton11.place(x = 30, y = 560)
            if PSR2 > 0: 
                Boton12 = tkinter.Button(user3, text=("Atacar a " + name[rival[1]]), font=("arial", 13),  bg="gray48", 
                                                        command=lambda: seleccion(1, 1, 3, 1))
                Boton12.place(x = 30, y = 600)
                
            if HP2 > 2:   
                Boton13 = tkinter.Button(user3, text="Habilidad", font=("arial", 13),  bg="gray48", 
                                                             command=lambda: seleccion(2, 2, 1, 1))
                Boton13.place(x = 230, y = 560)    
            
            Boton14 = tkinter.Button(user3, text="Protegerse", font=("arial", 13),  bg="gray48", 
                                                     command=lambda: seleccion(3, 3, 1, 1))
            Boton14.place(x = 230, y = 600)
            
            
        #A0 - prioridad B1 - accion C2 - destino D3 - ejecutor  # E4 Personaje  
                                                #F5 protecion #G6 habilidad
        #0 jugador 1 
        #1 jugador 2
        #2 jugador 3
        #3 jugador 4
    
    ###guardar las acciones ##############################################################   
        def seleccion(a, b, c, d): 
            global turno_on, turnos     
    ########Aciones del jugador######################################################  
            if d == 0:
                if PSR1 > 0:
                    Boton7.place_forget()
                if PSR2 > 0: 
                    Boton8.place_forget()
                if HP1 > 2:  
                    Boton9.place_forget()
                Boton10.place_forget() 
                n = 0
            if d == 1:
                if PSR1 > 0:
                    Boton11.place_forget()
                if PSR2 > 0:
                    Boton12.place_forget()
                if HP2 > 2:  
                    Boton13.place_forget()
                Boton14.place_forget()
                n = 1
            
            e = int(jugadores[n]) #E - Personaje en accion
            accion.append([a,b,c,d,e,0,0]) 
            comandos.append([a,b,c,d,e,0,0]) 
            turno_on = turno_on + 1
            turnos = turnos + 1

            if (PSP2 <= 0) or (PSP1 <= 0):
                turno_on = turno_on + 1
                turnos = turnos + 1
                accion.append([-1,-1,-1,-1,0,0,0]) 
                comandos.append([-1,-1,-1,-1,0,0,0])
                
   #########Aciones del rival########################################################
            if turno_on == 2:
                MC.config(text=("Cargando")) 
                if PSR1 > 0:   #verificar que rival tenga vidad
                    a2 = random.randrange(1,11) #Accion
                    if a2 > 0 and a2 < 8:
                        a2 = 1
                        c2 = random.randrange(0,2) #Destino
                        if c2 == 0 and PSP1 < 1: #jugador 1 tiene 0 de vida
                            c2 = 1 
                        if c2 == 1 and PSP2 < 1: #jugador 2 tiene 0 de vida
                            c2 = 0                        
                    if a2 == 8:
                        a2 = 2
                        c2 = 2
                        if HR1 < 3:
                            a2 = 1
                            c2 = random.randrange(0,2) #Destino
                            if c2 == 0 and PSP1 < 1: #jugador 1 tiene 0 de vida
                                c2 = 1 
                            if c2 == 1 and PSP2 < 1: #jugador 2 tiene 0 de vida
                                c2 = 0  
                    if a2 == 9 or a2 == 10:
                        a2 = 3
                        c2 = 2
                    e2 = int(jugadores[2])
                    accion.append([a2,a2,c2,2,e2,0,0])
                    comandos.append([a2,a2,c2,2,e2,0,0])
                    turnos = turnos + 1
                else: 
                    turnos = turnos + 1
                    accion.append([-1,-1,-1,-1,0,0,0]) 
                    comandos.append([-1,-1,-1,-1,0,0,0]) 
                ##############
                if PSR2 > 0:
                    a2 = random.randrange(1,11)
                    if a2 > 0 and a2 < 8:  ##Se atacó
                        a2 = 1
                        c2 = random.randrange(0,2)
                        if c2 == 0 and PSP1 < 1: #jugador 1 tiene 0 de vida
                            c2 = 1 
                        if c2 == 1 and PSP2 < 1: #jugador 2 tiene 0 de vida
                            c2 = 0 
                    if a2 == 8: ##Habiliad 
                        a2 = 2
                        c2 = 3
                        if HR2 < 3:
                            a2 = 1
                            c2 = random.randrange(0,2) #Destino
                            if c2 == 0 and PSP1 < 1: #jugador 1 tiene 0 de vida
                                c2 = 1 
                            if c2 == 1 and PSP2 < 1: #jugador 2 tiene 0 de vida
                                c2 = 0  
                    if a2 == 9 or a2 == 10:#protegerse
                        a2 = 3
                        c2 = 3

                    e2 = int(jugadores[3])
                    accion.append([a2,a2,c2,3,e2,0,0])
                    comandos.append([a2,a2,c2,3,e2,0,0])
                    turnos = turnos + 1
                else: 
                    turnos = turnos + 1
                    accion.append([-1,-1,-1,-1,0,0,0])  
                    comandos.append([-1,-1,-1,-1,0,0,0])
                
                accion.sort(key=lambda turno : turno[0], reverse=True)
                print(comandos)
                print(accion)
            
                user3.after(1000, acciones) 
             
    ###Ejecución del juego##############
        def reiniciar_combate():
            global turno_on, PSP1, PSP2, PSR1, PSR2, HP1, HP2, HR1, HR2
            
            if PSP1 < 1 and PSP2 < 1:
                MT.config(text=(" ")) 
                MC.config(text=("Perdiste el combate")) 
                Boton15 = tkinter.Button(user3, text="Terminar combate", font=("arial", 13), 
                                        command=lambda: salir2(user3))
                Boton15.place(x = 530, y = 400)
                    
            elif PSR1 < 1 and PSR2 < 1:
                MT.config(text=(" ")) 
                PSP1 = 0
                PSP2 = 0
                MC.config(text=("Ganaste el combate")) 
                Boton15 = tkinter.Button(user3, text="Terminar combate", font=("arial", 13), 
                                        command=lambda: salir2(user3))
                Boton15.place(x = 530, y = 400)
                
            else: 
                MT.config(text=(" ")) 
                MC.config(text=("Esperando acciones")) 
                MH.config(text=(" ")) 
            
            HP1 = HP1 + 1
            HP2 = HP2 + 1
            HR1 = HR1 + 1
            HR2 = HR2 + 1
            
            HaP1.config(text=("HAB:",  HP1)) 
            HaP2.config(text=("HAB:",  HP2))
            HaR1.config(text=("HAB:",  HR1)) 
            HaR2.config(text=("HAB:",  HR2))
            
            turno_on = 0
            accion.clear()
            comandos.clear()
            user3.after(1000, botones) 
    
    
        def protegerse(j):
            p = accion[j][3] #Ver la posicion del personaje
            MT.config(text=("Turno de " + name[jugadores[p]]))
            MC.config(text=(name[jugadores[p]] + " se protegió"))
            MH.config(text=(" ")) 
            comandos[p][5] = 1
                    
        
        def habilidad(j):
            global turno_on, PSP1, PSP2, PSR1, PSR2,  HP1, HP2, HR1, HR2
            p = accion[j][3]
            MT.config(text=("Turno de " + name[jugadores[p]]))
            MC.config(text=("Usó su habilidad"))
            if accion[j][4] == 1:      #uso su habilidad
                MH.config(text=("Habilidad: Sacrificio del heroe")) 
                if accion[j][3] == 0 or accion[j][2] == 1:
                    PSR1 = PSR1 - 90
                    PSR2 = PSR2 - 90
                if accion[j][3] == 2 or accion[j][2] == 3:
                    PSP1 = PSP1 - 90
                    PSP2 = PSP2 - 90
                if accion[j][3] == 0:
                    PSP1 = PSP1 - 60
                if accion[j][2] == 1:
                    PSP2 = PSP2 - 60
                if accion[j][3] == 2:
                    PSR1 = PSR1 - 60
                if accion[j][2] == 3:
                    PSR2 = PSR2 - 60  
            if accion[j][4] == 2:      
                MH.config(text=("Habilidad: Tormenta de golpes")) 
                if accion[j][3] == 0 or accion[j][2] == 1:
                    PSR1 = PSR1 - 60
                    PSR2 = PSR2 - 60
                if accion[j][3] == 2 or accion[j][2] == 3:
                    PSP1 = PSP1 - 60
                    PSP2 = PSP2 - 60
            if accion[j][4] == 3:      
                MH.config(text=("Habilidad: Hechizo drenador")) 
                if accion[j][3] == 0 or accion[j][2] == 1:
                    PSR1 = PSR1 - 40
                    PSR2 = PSR2 - 40
                if accion[j][3] == 2 or accion[j][2] == 3:
                    PSP1 = PSP1 - 40
                    PSP2 = PSP2 - 40
                if accion[j][3] == 0:
                    PSP1 = PSP1 + 40
                if accion[j][2] == 1:
                    PSP2 = PSP2 + 40
                if accion[j][3] == 2:
                    PSR1 = PSR1 + 40
                if accion[j][2] == 3:
                    PSR2 = PSR2 + 40         
            if accion[j][4] == 4:      
                MH.config(text=("Habilidad: Defensa total")) 
                #p = accion[j][3] 
                #comandos[p][5] = 2
                if accion[j][3] == 0: #quine lo da 
                    comandos[1][5] = 2 #quien lo recibe
                if accion[j][3] == 1:
                    comandos[0][5] = 2
                if accion[j][3] == 2:
                    comandos[3][5] = 2
                if accion[j][3] == 3:
                    comandos[2][5] = 2
            if accion[j][4] == 5:      
                MH.config(text=("Habilidad: Plegaria a los dioses")) 
                if accion[j][3] == 0 or accion[j][2] == 1:
                    PSP1 = PSP1 + 80
                    PSP2 = PSP2 + 80                  
                if accion[j][3] == 2 or accion[j][2] == 3:
                    PSR1 = PSR1 + 80
                    PSR2 = PSR2 + 80
            if accion[j][4] == 6:      
                MH.config(text=("Habilidad: Bendición de la princesa")) 
                if accion[j][3] == 0: #quine lo da 
                    comandos[1][6] = 1 #quien lo recibe
                if accion[j][3] == 1:
                    comandos[0][6] = 1
                if accion[j][3] == 2:
                    comandos[2][6] = 1
                if accion[j][3] == 3:
                    comandos[3][6] = 1

                    
        ##Actualizar vida###########################
            if PSP1 > 0:
                HPP1.config(text=(PSP1, "/", FPSP1))
            else:       
                HPP1.config(text=(0, "/", FPSP1))
            if PSP2 > 0:
                HPP2.config(text=(PSP2, "/", FPSP2))
            else:  
                HPP2.config(text=(0, "/", FPSP2))    
            if PSR1 > 0:
                HPR1.config(text=(PSR1, "/", FPSR1))
            else:     
                HPR1.config(text=(0, "/", FPSR1))
            
            if PSR2 > 0:
                HPR2.config(text=(PSR2, "/", FPSR2)) 
            else:     
                HPR2.config(text=(0, "/", FPSR2))
                
            if accion[j][3] == 0:
                HP1 = HP1 - 3
            if accion[j][3] == 1:
                HP2 = HP2 - 3
            if accion[j][3] == 2:
                HR1 = HR1 - 3
            if accion[j][3] == 3:
                HR2 = HR2 - 3
            HaP1.config(text=("HAB:",  HP1)) 
            HaP2.config(text=("HAB:",  HP2))
            HaR1.config(text=("HAB:",  HR1)) 
            HaR2.config(text=("HAB:",  HR2))    
            #A0 - prioridad B1 - accion C2 - destino D3 - ejecutor  # E4 Personaje  
                                                    #F5 protecion #G6 habilidad
            #0 jugador 1 
            #1 jugador 2
            #2 jugador 3
            #3 jugador 4   
             
        def damage(j):     
            ##Dañoa personaje#########################
            if accion[j][4] == 1:    #Revisa que personaje atacó
                        danio = 50   #Revisa lo que el personaje hace de daño
            if accion[j][4] == 2: 
                        danio = 80
            if accion[j][4] == 3: 
                        danio = 70   
            if accion[j][4] == 4: 
                        danio = 50 
            if accion[j][4] == 5: 
                        danio = 30 
            if accion[j][4] == 6: 
                        danio = 60 
         ######Modificaciones de daño###############
            md = accion[j][2] #protecion
            mdp = accion[j][3] #aumentos
            if comandos[mdp][6] == 1: #Potenciar el ataque
                MH.config(text=("Se potenció el ataque")) 
                danio = int(danio*2)           
            if comandos[md][5] == 1: #Reducir el ataque
                MH.config(text=("Se redujo el daño")) 
                danio = int(danio/2)
            if comandos[md][5] == 2: #Habilidad de acodazado
                MH.config(text=("Se nulificó el daño")) 
                danio = 0
                  
            return(danio)        
                
        
        def combatir(j):
            global PSP1, PSR1, PSP2, PSR2, activos
            p = accion[j][2] 
            o = accion[j][3]
            MT.config(text=("Turno de " + name[jugadores[o]]))
            MC.config(text=("Atacó a " + name[jugadores[p]]))
            MH.config(text=(" ")) 
            dan = damage(j)
    #########Dañoa personaje###################################################
            if accion[j][2] == 0:  #Revisa a quien atacó
                        PSP1 = PSP1 - dan   #Baja el contador de vida
            if accion[j][2] == 1:
                        PSP2 = PSP2 - dan                    
     #########Dañoa rival###################################################
            if accion[j][2] == 2:  #Revisa a quien atacó
                        PSR1 = PSR1 - dan   #Baja el contador de vida
            if accion[j][2] == 3:
                        PSR2 = PSR2 - dan 
   #########Contador de vida#############################################################               
            if PSP1 > 0:
                HPP1.config(text=(PSP1, "/", FPSP1))
            else:       
                HPP1.config(text=(0, "/", FPSP1))
            if PSP2 > 0:
                HPP2.config(text=(PSP2, "/", FPSP2))
            else:  
                HPP2.config(text=(0, "/", FPSP2))    
            if PSR1 > 0:
                HPR1.config(text=(PSR1, "/", FPSR1))
            else:     
                HPR1.config(text=(0, "/", FPSR1))
            
            if PSR2 > 0:
                HPR2.config(text=(PSR2, "/", FPSR2)) 
            else:     
                HPR2.config(text=(0, "/", FPSR2)) 
                        
                           
        def acciones():
            global turno_on, PSP, turnos, activos
            if turnos == 0:
                user3.after(1000, reiniciar_combate)
            else:
                j = activos - turnos
                print("Turno de " + name[accion[j][4]])
                turnos = turnos - 1
                t = 0
                if accion[j][1] == 3:
                    user3.after(2000, protegerse, j) 
                if accion[j][1] == 2:
                    user3.after(2000, habilidad, j) 
                if accion[j][1] == 1:
                    user3.after(2000, combatir, j) 
                if accion[j][1] == -1:
                    t = 1
                    acciones() 
                if t == 0:
                    user3.after(5000, acciones) 
         
    #Terminar###########################
    #Boton4 = tkinter.Button(user3, text="salir", command=lambda: salir2(user3))
    #Boton4.place(x = 340, y = 20)
    
    botones()  
      
    user3.mainloop()
    
###tercera pantalla################################################################################ 

def tercera_pantalla(user1):
     
    user2 = tkinter.Toplevel(user1)
    user2.title("Personajes selecionados")
    user2.geometry("800x500+100+100")
    
    image3 = tk.PhotoImage(file="Pantalla3.png")
    Ifon3 = ttk.Label(user2, image=image3)
    Ifon3.place(x = 0, y = 0)
    
    
    for i in range (0, 5):
        if jugadores[i] == 1:    
            nombre = "personaje1.png"
        if jugadores[i] == 2: 
            nombre = "personaje2.png"
        if jugadores[i] == 3: 
            nombre = "personaje3.png"
        if jugadores[i] == 4:  
            nombre = "personaje4.png"
        if jugadores[i] == 5: 
            nombre = "personaje5.png" 
        if jugadores[i] == 6: 
            nombre = "personaje6.png"
        
        if i == 0: 
            image4 = tk.PhotoImage(file=nombre)   
            Ifon4 = ttk.Label(user2, image=image4)
            Ifon4.place(x = 30, y = 10)
        if i == 1:
            image5 = tk.PhotoImage(file=nombre)   
            Ifon5 = ttk.Label(user2, image=image5)
            Ifon5.place(x = 30, y = 210)
        if i == 2:
            image6 = tk.PhotoImage(file=nombre)   
            Ifon6 = ttk.Label(user2, image=image6)
            Ifon6.place(x = 570, y = 10)
        if i == 3:
            image7 = tk.PhotoImage(file=nombre)   
            Ifon7 = ttk.Label(user2, image=image7)
            Ifon7.place(x = 570, y = 210)
    
    user1.withdraw()    
    
    labelb = tkinter.Label(user2, text=name[personaje[0]] + " y " + name[personaje[1]], font=("arial", 20),  bg="gray48") 
    labelb.place(x=30, y=440)   
    
    labelb = tkinter.Label(user2, text=name[rival[0]] + " y " + name[rival[1]], font=("arial", 20),  bg="gray48" )
    labelb.place(x=480, y=440)     
    
    Boton3 = tkinter.Button(user2, text="Iniciar pelea", font=("arial", 15), command=lambda: iniciar())
    Boton3.place(x = 340, y = 370)
    
    Boton4 = tkinter.Button(user2, text="Regresar", font=("arial", 10), command=lambda: salir2(user2))
    Boton4.place(x = 370, y = 10)  
    
    def iniciar():
        global PSP1, PSP2, PSR1, PSR2, activos, HP1, HP2, HR1, HR2
        PSP1 = int (vidaP[0])
        PSR1 = int (vidaR[0])
        PSP2 = int (vidaP[1])
        PSR2 = int (vidaR[1])
        HP1 = int(3)
        HP2 = int(3)
        HR1 = int(3)
        HR2 = int(3)
        activos = 4
        print(PSP1, PSP2, PSR1, PSR2)  
        cuarta_pantalla(user2)
      
    user2.mainloop()


###Crear segunda pantalla################################################################################ 

def segunda_pantalla():
    
    
    user1 = tkinter.Toplevel(ventana)
    user1.title("Selección de personaje")
    user1.geometry("700x600+50+50")
    
    ventana.withdraw() 
    
    image2 = tk.PhotoImage(file="Pantalla2.png")
    Ifon2 = ttk.Label(user1, image=image2)
    Ifon2.place(x = 0, y = 0)

    per1 = tkinter.Button(user1, text="Caballero", command=lambda: iniciar(1, 600))
    per1.place(x = 100, y = 300)
    
    per2 = tkinter.Button(user1, text="Luchador", command=lambda: iniciar(2, 400))
    per2.place(x = 320, y = 300)    
    
    per3 = tkinter.Button(user1, text="Hechicera", command=lambda: iniciar(3, 500))
    per3.place(x = 530, y = 300)

    per4 = tkinter.Button(user1, text="Acorazado", command=lambda: iniciar(4, 700))
    per4.place(x = 110, y = 550)
    
    per5 = tkinter.Button(user1, text="Sacerdotisa", command=lambda: iniciar(5, 800))
    per5.place(x = 310, y = 550)
    
    per6 = tkinter.Button(user1, text="Princesa guerrera", command=lambda: iniciar(6, 500))
    per6.place(x = 510, y = 550)

    Boton4 = tkinter.Button(user1, text="salir", command=lambda: salir(user1))
    Boton4.place(x = 660, y = 560)  
    
    def iniciar(per, vid):
        global contadorP, contadorR
        personaje[contadorP] = per  
        vidaP[contadorP] = vid
        jugadores[contadorP] = per
        
        #Quitar botones ya selecionados
        if per == 1: 
            per1.place_forget()
        if per == 2: 
            per2.place_forget()
        if per == 3: 
            per3.place_forget()
        if per == 4: 
            per4.place_forget()
        if per == 5: 
            per5.place_forget()
        if per == 6: 
            per6.place_forget()
        #Aumenentar el contador de personajes 
        contadorP = contadorP + 1
    
        if contadorP == 2:
            #Borrrar los botones##############
            per1.place_forget()
            per2.place_forget()
            per3.place_forget()
            per4.place_forget()
            per5.place_forget()
            per6.place_forget()
       
            while contadorR < 2:
                r = random.randrange(1,7)
                if r not in rival:
                    rival[contadorR] = r
                    jugadores[(contadorR+2)] = r
                    if r == 1: 
                        vidaR[contadorR] = 600
                    if r == 2: 
                        vidaR[contadorR] = 400
                    if r == 3: 
                        vidaR[contadorR] = 500
                    if r == 4: 
                        vidaR[contadorR] = 700
                    if r == 5: 
                        vidaR[contadorR] = 800
                    if r == 6: 
                        vidaR[contadorR] = 500
                    contadorR = contadorR + 1
            tercera_pantalla(user1)

    user1.mainloop()

###Ventana principal##################################################


Boton1 = tkinter.Button(ventana, text="Iniciar", font=("arial", 15), command=lambda: segunda_pantalla())
Boton1.place(x = 315, y = 400)     
                            

ventana.mainloop()