

import math,cmath
from tkinter import *
from tkinter import ttk

#Metodi
#Inserisce risultato operazioni tra Z1 e Z2 in Z3
def Risultato(c,Z):
    #a = round(c.real, 4)
    #b = round(c.imag, 4)
    #tiene 3 cifre significative della parte reale e di quella immaginaria
    #'%s': ciò che segue % (operatore di formato) sarà una stringa una stringa
    #'%.3g' il numero reale che segue % sarà trasformato in stringa che ne
    #considera 3 cifre significative
    #la stringa prodotta deve essere convertita in numero reale
    a = float('%s' % float('%.3g' % c.real))
    b = float('%s' % float('%.3g' % c.imag))
    c = a + b * 1j
    Z.delete(0, END)
    Z.insert(0, c)
    RtoP(Zr,Mr,Fr)
    Messaggi.delete(0, END)

#Somma Z1 con Z2
def SommaZ1Z2():
    try:
        a=Z1.get()
        b=Z2.get()
        c=complex(a)+complex(b)
        Risultato(c,Zr)
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')
#Sottrai Z2 da Z1
def SottrazioneZ1Z2():
    try:
        a=Z1.get()
        b=Z2.get()
        c=complex(a)-complex(b)
        Risultato(c,Zr)
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')

#moltiplica Z1 con Z2
def MoltiplicazioneZ1Z2():
    try:
        a=Z1.get()
        b=Z2.get()
        c=complex(a)*complex(b)
        Risultato(c,Zr)
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')
#dividi Z1 con Z2
def DivisioneZ1Z2():
    try:
        a=Z1.get()
        b=Z2.get()
        c=complex(a)/complex(b)
        Risultato(c,Zr)
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')
#calcola il parallelo tra Z1 e Z2
def Parallelo2():
    try:
        a=Z1.get()
        b=Z2.get()
        c=(complex(a)*complex(b))/(complex(a)+complex(b))
        Risultato(c,Zr)
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')

def Parallelo3():
    try:
        a=complex(Z1.get())
        b=complex(Z2.get())
        c=complex(Z3.get())
        try:
            d=1/(1/a+1/b+1/c)
            Risultato(d, Zr)
        except ZeroDivisionError:
            Messaggi.delete(0, END)
            Messaggi.insert(0, 'Non si può dividere per zero')
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')

#trasforma in coordinare cartesiane
def PtoR(M,F,Z):
    try:
        a = float(M.get())
        b = float(F.get()) * math.pi / 180
        c = cmath.rect(a, b)
        Risultato(c, Z)
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')

#trasforma in coordinate polari Z

def RtoP(Z,M,F):
    try:
        z=cmath.polar(complex(Z.get()))
        M.delete(0, END)
        F.delete(0, END)
        gradi= z[1]* 180 / math.pi
        M.insert(0,str(float('%s' % float('%.3g' % z[0]))))
        F.insert(0,str(float('%s' % float('%.3g' % gradi))))
        Messaggi.delete(0, END)
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')

#copia Zr in Z (Z1 o Z2)
def ZrtoZ(Z,M,F):
    Z.delete(0,END)
    Z.insert(0,Zr.get())
    RtoP(Z,M,F)

#scambia Z1 con Z2
def ScambioZ(Z1,Z2,M1,F1,M2,F2):
    a=Z1.get()
    b=Z2.get()
    Z1.delete(0,END)
    Z2.delete(0, END)
    Z1.insert(0,b)
    Z2.insert(0,a)
    RtoP(Z1,M1,F1)
    RtoP(Z2,M2,F2)

def Memoria(Z,M,F,Mem):

    a=Z.get()
    Z.delete(0,END)
    Z.insert(0,Mem.get())
    Mem.delete(0,END)
    Mem.insert(0,a)

#calcola l'inverso
def invZ(Z):
    try:
        a=complex(Z.get())
        if a !=0:
            a=1/a
            Risultato(a,Z)
        else:
            Messaggi.delete(0, END)
            Messaggi.insert(0, 'Non si può dividere per zero')
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')

def PiuMeno(Z):
    try:
        a=-complex(Z.get())
        Risultato(a,Z)
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')

def ResetBottone():
    for i in range(12):
        Campi[i].delete(0,END)
        #Campi[i].insert(0,c[i])

#finestra principale

root = Tk()
root.title("Calcolatrice per numeri complessi")
root.configure(background="green")


#definizioni etichette
z1lbl=ttk.Label(text="Z1",font="Helvetica 24")
z2lbl=ttk.Label(text="Z2",font="Helvetica 24")
z3lbl=ttk.Label(text="Z3",font="Helvetica 24")
zrlbl=ttk.Label(text="Zr", foreground="red", font="Helvetica 24")


cartesianalbl=ttk.Label(text="a+bj",font="Helvetica 24")
Modulolbl=ttk.Label(text="Modulo",font="Helvetica 24")
Faselbl=ttk.Label(text="Fase in gradi",font="Helvetica 24")

#definizione campi di ingresso
LEZ=15 #Larghezza Entry Z
LEM=8 #Larghezza Entry M ed F
FEZ="Baskerville 24"#Font Entry Z, M, F
c=ttk.Style()#definisce l'aspetto del campo come colore del fomdo, del carattere
c.configure('Z.TEntry',font=FEZ, foreground="black",background="yellow")
p=ttk.Style()
p.configure('P.TEntry',font=FEZ,foreground='red')
m=ttk.Style()
m.configure('M.TEntry',font=FEZ,background="yellow",foreground="red")
Z1=ttk.Entry(width=LEZ,style="Z.TEntry",font=FEZ,justify=RIGHT)
Z2=ttk.Entry(width=LEZ,style="Z.TEntry",font=FEZ,justify=RIGHT)
Z3=ttk.Entry(width=LEZ,style="Z.TEntry",font=FEZ,justify=RIGHT)
Zr=ttk.Entry(width=LEZ,font=FEZ,justify=RIGHT)
Zr.configure(background="yellow",foreground="red",font=FEZ,justify=RIGHT)
M1=ttk.Entry(width=LEM,font=FEZ,justify=RIGHT)
M2=ttk.Entry(width=LEM,font=FEZ,justify=RIGHT)
M3=ttk.Entry(width=LEM,font=FEZ,justify=RIGHT)
Mr=ttk.Entry(width=LEM,font=FEZ,justify=RIGHT,style="P.TEntry")
#Mr.configure(background="yellow",foreground="blue",justify=RIGHT)

F1=ttk.Entry(width=LEM,font=FEZ,justify=RIGHT)
F2=ttk.Entry(width=LEM,font=FEZ,justify=RIGHT)
F3=ttk.Entry(width=LEM,font=FEZ,justify=RIGHT)
Fr=ttk.Entry(width=LEM,font=FEZ,justify=RIGHT)
Fr.configure(background="yellow",foreground="red",font=FEZ,justify=RIGHT)
Mem1=ttk.Entry(width=LEM,font=FEZ)
Mem1.delete(0,END)
Mem1.insert(0,'0')
Mem2=ttk.Entry(width=LEM,font=FEZ)
Mem2.delete(0,END)
Mem2.insert(0,'0')
Mem3=ttk.Entry(width=LEM,font=FEZ)
Mem3.delete(0,END)
Mem3.insert(0,'0')

Messaggi=ttk.Entry(width=8*LEM,font=FEZ,justify=LEFT,style="M.TEntry")


Campi=(Z1,Z2,Z3,M1,M2,M3,F1,F2,F3,Zr,Mr,Fr)
#valori iniziali campi
c = (1+1j,3+4j,4+5j,1.41,5,6.4,45,53.1,75.9,0)
ResetBottone()

s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 18), foreground="blue")


#definizione bottoni
Somma = ttk.Button(text="Zr=Z1+Z2",style="my.TButton",command=SommaZ1Z2)
Sottrazione = ttk.Button(text="Zr=Z1-Z2",style="my.TButton",command=SottrazioneZ1Z2)
Moltiplicazione = ttk.Button(text="Zr=Z1xZ2",style="my.TButton",command=MoltiplicazioneZ1Z2)
Divisione = ttk.Button(text="Zr=Z1/Z2",style="my.TButton", command=DivisioneZ1Z2)
Parallelo = ttk.Button(text="Zr=Z1||Z2",style="my.TButton",command=Parallelo2)
Parallelo3 = ttk.Button(text="Zr=Z1||Z2||Z3",style="my.TButton",command=Parallelo3)

PtoR1 = ttk.Button(text="P->R",style="my.TButton", command=lambda: PtoR(M1,F1,Z1))
PtoR2 = ttk.Button(text="P->R",style="my.TButton", command=lambda:PtoR(M2,F2,Z2))
PtoR3 = ttk.Button(text="P->R",style="my.TButton", command=lambda:PtoR(M3,F3,Z3))
RtoP1 = ttk.Button(text="R->P",style="my.TButton", command=lambda:RtoP(Z1,M1,F1))
RtoP2 = ttk.Button(text="R->P",style="my.TButton", command=lambda:RtoP(Z2,M2,F2))
RtoP3 = ttk.Button(text="R->P",style="my.TButton", command=lambda:RtoP(Z3,M3,F3))

ZrtoZ1 = ttk.Button(text="Zr->Z1",style="my.TButton",command=lambda:ZrtoZ(Z1,M1,F1))
ZrtoZ2 = ttk.Button(text="Zr->Z2",style="my.TButton",command=lambda:ZrtoZ(Z2,M2,F2))
ZrtoZ3 = ttk.Button(text="Zr->Z3",style="my.TButton",command=lambda:ZrtoZ(Z3,M3,F3))


Z1Z2Scambio = ttk.Button(text="Z1<->Z2",style="my.TButton",command=lambda:ScambioZ(Z1,Z2,M1,F1,M2,F2))
Z2Z3Scambio = ttk.Button(text="Z3<->Z2",style="my.TButton",command=lambda:ScambioZ(Z2,Z3,M2,F2,M3,F3))
Z1Z3Scambio = ttk.Button(text="Z1<->Z3",style="my.TButton",command=lambda:ScambioZ(Z1,Z3,M1,F1,M3,F3))

Z1inv = ttk.Button(text="1/Z",style="my.TButton",command=lambda:invZ(Z1))
Z2inv = ttk.Button(text="1/Z",style="my.TButton",command=lambda:invZ(Z2))
Z3inv = ttk.Button(text="1/Z",style="my.TButton",command=lambda:invZ(Z3))
Zrinv = ttk.Button(text="1/Z",style="my.TButton",command=lambda:invZ(Zr))

Z1PiuMeno=ttk.Button(text="+/-",style="my.TButton",command=lambda:PiuMeno(Z1))
Z2PiuMeno=ttk.Button(text="+/-",style="my.TButton",command=lambda:PiuMeno(Z2))
Z3PiuMeno=ttk.Button(text="+/-",style="my.TButton",command=lambda:PiuMeno(Z3))
ZrPiuMeno=ttk.Button(text="+/-",style="my.TButton",command=lambda:PiuMeno(Zr))

Z1Mem=ttk.Button(text="M",style="my.TButton",command=lambda:Memoria(Z1,M1,F1,Mem1))
Z2Mem=ttk.Button(text="M",style="my.TButton",command=lambda:Memoria(Z2,M2,F2,Mem2))
Z3Mem=ttk.Button(text="M",style="my.TButton",command=lambda:Memoria(Z3,M3,F3,Mem3))


Reset = ttk.Button(text="Reset",style="my.TButton",command=ResetBottone)

#posizionamento etichette
cz=3 #colonna delle z
rb=5 #start colonna bottoni operazioni
cartesianalbl.grid(column=cz+1, row=0)
Modulolbl.grid(column=cz+4, row=0)
Faselbl.grid(column=cz+5,row=0)

z1lbl.grid(column=cz, row=1)
z2lbl.grid(column=cz, row=2)
z3lbl.grid(column=cz, row=3)
zrlbl.grid(column=cz,row=4)

#posizionamente campi di ingresso
Z1.grid(column=cz+1,row=1)
Z2.grid(column=cz+1,row=2)
Z3.grid(column=cz+1,row=3)
Zr.grid(column=cz+1,row=4)
M1.grid(column=cz+4,row=1)
M2.grid(column=cz+4,row=2)
M3.grid(column=cz+4,row=3)
Mr.grid(column=cz+4,row=4)
F1.grid(column=cz+5,row=1)
F2.grid(column=cz+5,row=2)
F3.grid(column=cz+5,row=3)
Fr.grid(column=cz+5,row=4)
Messaggi.grid(column=cz+1,row=10,columnspan=5)
#Mem1.grid(column=cz-3,row=5)


#posizionamento bottoni
Somma.grid(column=cz-3, row=rb+1,ipadx=5,ipady=5)
Sottrazione.grid(column=cz-2, row=rb+1,ipadx=5,ipady=5)
Moltiplicazione.grid(column=cz-1, row=rb+1,ipadx=5,ipady=5)
Divisione.grid(column=cz, row=rb+1,ipadx=5,ipady=5)
Parallelo.grid(column=cz-3, row=rb+5,ipadx=5,ipady=5)
Parallelo3.grid(column=cz-2,row=rb+5,ipadx=5,ipady=5)
PtoR1.grid(column=cz+3, row=1)#,ipady=1)
PtoR2.grid(column=cz+3,row=2)#,ipady=1)
PtoR3.grid(column=cz+3,row=3)#,ipady=1)

#PtoR.grid(column=7,row=1)
RtoP1.grid(column=cz+2, row=1)#,ipady=1)
RtoP2.grid(column=cz+2, row=2)#,ipady=1)
RtoP3.grid(column=cz+2, row=3)#,ipady=1)

ZrtoZ1.grid(column=cz-3,row=rb+2,ipadx=5,ipady=5)
ZrtoZ2.grid(column=cz-2,row=rb+2,ipadx=5,ipady=5)
ZrtoZ3.grid(column=cz-1,row=rb+2,ipadx=5,ipady=5)

Z1Z2Scambio.grid(column=cz-3,row=rb+3,ipadx=5,ipady=5) #(per allargare o rstringere il bottone internamente
Z2Z3Scambio.grid(column=cz-1,row=rb+3,ipadx=5,ipady=5)
Z1Z3Scambio.grid(column=cz-2,row=rb+3,ipadx=5,ipady=5)


Z1inv.grid(column=cz-1,row=1)
Z2inv.grid(column=cz-1,row=2)
Z3inv.grid(column=cz-1,row=3)
Zrinv.grid(column=cz-1,row=4)

Z1PiuMeno.grid(column=cz-2,row=1)
Z2PiuMeno.grid(column=cz-2,row=2)
Z3PiuMeno.grid(column=cz-2,row=3)
ZrPiuMeno.grid(column=cz-2,row=4)

Z1Mem.grid(column=cz-3,row=1)
Z2Mem.grid(column=cz-3,row=2)
Z3Mem.grid(column=cz-3,row=3)


Reset.grid(column=cz-1, row=0,ipadx=5,ipady=1)


#start

root.mainloop()

