import tkinter as tk
import math,cmath

from tkinter import *
from tkinter import ttk

#Metodi
#Inserisce risultato operazioni tra Z1 e Z2 in Z3
def Risultato(c, Z, M, F):
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
    RtoP(Z, M, F)
    Messaggi.delete(0, END)
    Impedenze=(Z1.get(),Z2.get(),Z3.get(),Z4.get())


#Somma Z1 con Z2
def SommaZ1Z2():
    try:
        a=Z1.get()
        b=Z2.get()
        c=complex(a)+complex(b)
        Risultato(c, Zr, Mr, Fr)
        print(z1var.get())
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')
#Sottrai Z2 da Z1
def SottrazioneZ1Z2():
    try:
        a=Z1.get()
        b=Z2.get()
        c=complex(a)-complex(b)
        Risultato(c, Zr, Mr, Fr)
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')

#moltiplica Z1 con Z2
def MoltiplicazioneZ1Z2():
    try:
        a=Z1.get()
        b=Z2.get()
        c=complex(a)*complex(b)
        Risultato(c, Zr, Mr, Fr)
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')
#dividi Z1 con Z2
def DivisioneZ1Z2():
    try:
        a=Z1.get()
        b=Z2.get()
        try:
            c=complex(a)/complex(b)
            Risultato(c, Zr, Mr, Fr)
        except ZeroDivisionError:
            Zr.delete(0, END)
            Zr.insert(0, 'infinito')
            Messaggi.delete(0, END)
            Messaggi.insert(0, 'Non si può dividere per zero')

    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')
#calcola il parallelo tra Z1 e Z2

def ZParalleli(n,Impedenze):
    y=0
    for i in range(0, n):
        #print(i)
        #print(complex(Impedenze[i].get()))
        try:
            x=complex(Impedenze[i].get())
            if x==0:
                Zr.delete(0, END)
                Zr.insert(0, '0')
                break
            else:
                try:
                    y=1/x+y
                    #print(x)
                except ZeroDivisionError:
                    Zr.delete(0,END)
                    Zr.insert(0,'infinito')
                    Messaggi.delete(0, END)
                    break
        except ValueError:
            Messaggi.delete(0, END)
            Messaggi.insert(0, "Scrittura errata di almeno un'impedenza")
            break
        try:
            z = 1 / y
            Risultato(z, Zr, Mr, Fr)
        except ZeroDivisionError:
            Zr.delete(0, END)
            Zr.insert(0, "infinito")

#trasforma in coordinare cartesiane
def PtoRs():
    if z1var.get():
        PtoR(M1, F1, Z1)
    if z2var.get():
        PtoR(M2, F2, Z2)
    if z3var.get():
        PtoR(M3, F3, Z3)
    if z4var.get():
        PtoR(M4, F4, Z4)

def PtoR(M,F,Z):
    try:
        a = float(M.get())
        b = float(F.get()) * math.pi / 180
        c = cmath.rect(a, b)
        Risultato(c, Z, M, F)
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')

#trasforma in coordinate polari Z
def RtoPs():
    if z1var.get():
        RtoP(Z1, M1, F1)
    if z2var.get():
        RtoP(Z2, M2, F2)
    if z3var.get():
        RtoP(Z3, M3, F3)
    if z4var.get():
        RtoP(Z4, M4, F4)

def RtoP(Z, M, F):
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

#copia Zr in una delle Z
def ZrtoZ(Z,M,F):
    Z.delete(0,END)
    Z.insert(0,Zr.get())
    RtoP(Z,M,F)


def ScambioZSpuntate():
    if z1var.get():
        if z2var.get():
            ScambioZ(Z1, Z2, M1, F1, M2, F2)
            if z3var.get():
                ScambioZ(Z2, Z3, M2, F2, M3, F3)
                if z4var.get():
                    ScambioZ(Z3, Z4, M3, F3, M4, F4)
            else:
                if z4var.get():
                    ScambioZ(Z1, Z4, M1, F1, M4, F4)
        else:
            if z3var.get():
                ScambioZ(Z1, Z3, M1, F1, M3, F3)
                if z4var.get():
                    ScambioZ(Z3, Z4, M3, F3, M4, F4)
            else:
                if z4var.get():
                    ScambioZ(Z1, Z4, M1, F1, M4, F4)
    else:
        if z2var.get():
            if z3var.get():
                ScambioZ(Z2, Z3, M2, F2, M3, F3)
                if z4var.get():
                    ScambioZ(Z3, Z4, M3, F3, M4, F4)
            else:
                if z4var.get():
                    ScambioZ(Z2, Z4, M2, F2, M4, F4)
        else:
            if z3var.get():
                if z4var.get():
                    ScambioZ(Z3, Z4, M3, F3, M4, F4)


#scambia tra due Z
def ScambioZ(Z1,Z2,M1,F1,M2,F2):

    a=Z1.get()
    b=Z2.get()
    Z1.delete(0,END)
    Z2.delete(0, END)
    Z1.insert(0,b)
    Z2.insert(0,a)
    #print(len(a),len(b))
    if len(Z1.get()) !=0:
        RtoP(Z1,M1,F1)
    if len(Z2.get()) !=0:
        RtoP(Z2,M2,F2)
def MemZs():
    if z1var.get():
        Memoria(Z1, M1, F1, Mem1)
    if z2var.get():
        Memoria(Z2, M2, F2, Mem2)
    if z3var.get():
        Memoria(Z3, M3, F3, Mem3)
    if z4var.get():
        Memoria(Z4, M4, F4, Mem4)


def Memoria(Z,M,F,Mem):
    a=Z.get()
    b=Mem.get()
    if a !='':
        #Z.delete(0,END)
        #Z.insert(0,Mem.get())
        Mem.delete(0,END)
        Mem.insert(0,a)
        if b != '':
            Z.delete(0,END)
            Z.insert(0,b)

    #print(Mem.get(),Z.get())

#calcola l'inverso
def invZS():
    if z1var.get():
        invZ(Z1, M1, F1)
    if z2var.get():
        invZ(Z2, M2, F2)
    if z3var.get():
        invZ(Z3, M3, F3)
    if z4var.get():
        invZ(Z4, M4, F4)


#calcola l'inverso
def invZ(Z, M, F):
    try:
        a=complex(Z.get())
        if a !=0:
            a=1/a
            Risultato(a, Z, M, F)
        else:
            Messaggi.delete(0, END)
            Messaggi.insert(0, 'Non si può dividere per zero')
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')
def PiuMenoZs():
    if z1var.get():
        PiuMeno(Z1, M1, F1)
    if z2var.get():
        PiuMeno(Z2, M2, F2)
    if z3var.get():
        PiuMeno(Z3, M3, F3)
    if z4var.get():
        PiuMeno(Z4, M4, F4)

def PiuMeno(Z, M, F):
    try:
        a=-complex(Z.get())
        Risultato(a, Z, M, F)
        #print(a)
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')

def ResetBottone():
    for i in range(19):
        Campi[i].delete(0,END)
    Messaggi.delete(0, END)
def YtoD():
    try:
        a=complex(Z1.get())
        b=complex(Z2.get())
        c=complex(Z3.get())
        if a*b*c ==0:
            Messaggi.delete(0, END)
            Messaggi.insert(0, 'Non è una stella:qualche impedenza è nulla')
        else:
            Memoria(Z1,M1,F1,Mem1)
            Memoria(Z2, M2, F2, Mem2)
            Memoria(Z3, M3, F3, Mem3)
            N=a * b + b * c + a * c
            c1= N / c
            Risultato(c1, Z1, M1, F1)
            c1= N/ a
            Risultato(c1, Z2, M2, F2)
            c1=N / b
            Risultato(c1, Z3, M3, F3)

    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata di qualche impedenza')

def DtoY():
    try:
        a = complex(Z1.get())
        b = complex(Z2.get())
        c = complex(Z3.get())
        if a + b + c == 0:
            Messaggi.delete(0, END)
            Messaggi.insert(0, 'Trasformazione impossibile')
        else:
            Memoria(Z1, M1, F1, Mem1)
            Memoria(Z2, M2, F2, Mem2)
            Memoria(Z3, M3, F3, Mem3)
            D=a+b+c
            c1=a*c/D
            Risultato(c1, Z1, M1, F1)
            c1=b*a/D
            Risultato(c1, Z2, M2, F2)
            c1=b*c/D
            Risultato(c1, Z3, M3, F3)

    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata di qualche impedenza')
def SpostamentoCentroStella():
   try:
        a = complex(Z1.get())
        b = complex(Z2.get())
        c = complex(Z3.get())
        d=complex(Z4.get())/math.sqrt(3)
        #print(a,b,c,d)
        if 1 / a + 1 / b + 1 / c == 0:
            Messaggi.delete(0, END)
            Messaggi.insert(0, 'Spostamento infinito o indefinito')
        else:
            f2=cmath.rect(1, -2 * math.pi / 3)
            f3=cmath.rect(1, 2 * math.pi / 3)
            #print(f2,f3)

            V = d*(1 / a + f2 / b + f3 / c) / ( 1 / a + 1 / b + 1 / c)
            Risultato(V, Zr, Mr, Fr)
   except ValueError:
       Messaggi.delete(0, END)
       Messaggi.insert(0, "C'è almeno una scrittura errata nei dati")


def DisegnaGrafici():
    # coordinate relative grafico
    try:
        z1=cmath.polar(complex(Z1.get()))
        z2=cmath.polar(complex(Z2.get()))
        z3=cmath.polar(complex(Z3.get()))
        z4=cmath.polar(complex(Z4.get()))
        zr=cmath.polar(complex(Z4.get()))

        L= max(z1[0],z2[0],z3[0],z4[0],zr[0])

        xmin = -L
        xmax = L
        ymin = -L
        ymax = L

        k1=LargTela/(xmax-xmin) # calcolo costanti di conversione
        k2=AltTela/(ymax-ymin)

        PZn=[]
        for i in range(len(Impedenze)):
            PZ = (k1 * complex(Impedenze[i].get()).real + Xv0, Yv0 - k2 * complex(Impedenze[i].get()).imag)
            PZn.append(PZ)

        r=5

        for i in range(len(PZn)):
            cz = canv.create_oval(PZn[i][0] + r, PZn[i][1] - r, PZn[i][0] - r, PZn[i][1] + r, fill=Zcolor[i])
            Pdisegnati.append(cz)
        del PZn[:]

    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata di qualche impedenza')

def CancellaGrafici():
    #print(len(Pdisegnati))
    for i in range(len(Pdisegnati)):
        canv.delete(Pdisegnati[i])
    del Pdisegnati[:]

#finestra principale

root = Tk()
root.title("Calcolatrice per numeri complessi")
root.configure(background="green")

sinistra=10
sopra=10
destra=10
sotto=10
impacchettamento=(sinistra,sopra,destra,sotto)
rilievo=("flat", "raised", "sunken", "groove", "ridge")
#genera il widget "frame principale" di nome content
content = ttk.Frame(root, padding=impacchettamento,relief="sunken")
content1 = ttk.Frame(root, padding=impacchettamento,relief="sunken")
LargTela=500
AltTela=500
Xv0 = LargTela / 2
Yv0 = AltTela / 2
canv = tk.Canvas(content1, highlightthickness=0, bg='white', width=LargTela, height=AltTela)
#canv1 = tk.Canvas(content1, highlightthickness=0, bg='lightgreen', width=LargTela, height=AltTela, relief="sunken")


#definizioni etichette
z1lbl=ttk.Label(content, text="Z1", font="Helvetica 24")
z2lbl=ttk.Label(content, text="Z2", font="Helvetica 24")
z3lbl=ttk.Label(content, text="Z3", font="Helvetica 24")
z4lbl=ttk.Label(content, text="Z4", font="Helvetica 24")
zrlbl=ttk.Label(content, text="Zr", foreground="red", font="Helvetica 24",justify=CENTER)

cartesianalbl=ttk.Label(content, text="a+bj",font="Helvetica 16")
Modulolbl=ttk.Label(content, text="Modulo",font="Helvetica 16")
Faselbl=ttk.Label(content, text="Fase in gradi",font="Helvetica 16")

#definizione campi di ingresso
LEZ=15 #Larghezza Entry Z
LEM=8 #Larghezza Entry M ed F
FEZ="Baskerville 24"#Font Entry Z, M, F
FEM="Arial 14"
Zcolor=('firebrick','royalblue','seagreen','goldenrod','red')
c1=ttk.Style()#definisce l'aspetto del campo come colore del fomdo, del carattere
c1.configure('Z1.TEntry',foreground=Zcolor[0],background="whitesmoke")
c2=ttk.Style()#definisce l'aspetto del campo come colore del fomdo, del carattere
c2.configure('Z2.TEntry',foreground=Zcolor[1],background="whitesmoke")
c3=ttk.Style()#definisce l'aspetto del campo come colore del fomdo, del carattere
c3.configure('Z3.TEntry',foreground=Zcolor[2],background="whitesmoke")
c4=ttk.Style()#definisce l'aspetto del campo come colore del fomdo, del carattere
c4.configure('Z4.TEntry',foreground=Zcolor[3],background="whitesmoke")
p=ttk.Style()
p.configure('P.TEntry', font=FEZ, foreground=Zcolor[4])
m=ttk.Style()
m.configure('M.TEntry', font=FEM, background="lightyellow", foreground=Zcolor[4])

Z1=ttk.Entry(content, width=LEZ, style="Z1.TEntry",justify=RIGHT,font=FEZ)
Z2=ttk.Entry(content, width=LEZ, style="Z2.TEntry",justify=RIGHT,font=FEZ)
Z3=ttk.Entry(content, width=LEZ, style="Z3.TEntry",justify=RIGHT,font=FEZ)
Z4=ttk.Entry(content, width=LEZ, style="Z4.TEntry",justify=RIGHT,font=FEZ)
Zr=ttk.Entry(content, width=LEZ, style="P.TEntry",justify=RIGHT,font=FEZ)
M1=ttk.Entry(content, width=LEM, font=FEZ,justify=RIGHT)
M2=ttk.Entry(content, width=LEM, font=FEZ,justify=RIGHT)
M3=ttk.Entry(content, width=LEM, font=FEZ,justify=RIGHT)
M4=ttk.Entry(content, width=LEM, font=FEZ,justify=RIGHT)
Mr=ttk.Entry(content, width=LEM, font=FEZ,justify=RIGHT,style="P.TEntry")


F1=ttk.Entry(content, width=LEM, font=FEZ, justify=RIGHT)
F2=ttk.Entry(content, width=LEM, font=FEZ, justify=RIGHT)
F3=ttk.Entry(content, width=LEM, font=FEZ, justify=RIGHT)
F4=ttk.Entry(content, width=LEM, font=FEZ, justify=RIGHT)

Fr=ttk.Entry(content, width=LEM, font=FEZ, justify=RIGHT, style="P.TEntry")
Fr.configure(background="yellow", foreground="red", font=FEZ, justify=RIGHT)
Mem1=ttk.Entry(content, width=LEM, font=FEZ)
Mem2=ttk.Entry(content, width=LEM, font=FEZ)
Mem3=ttk.Entry(content, width=LEM, font=FEZ)
Mem4=ttk.Entry(content, width=LEM, font=FEZ)
Memr=ttk.Entry(content, width=LEM, font=FEZ)


Messaggi=ttk.Entry(content1, width=8*LEM, font=FEM, justify=LEFT, style="M.TEntry")

Campi=(Z1, Z2, Z3, Z4, M1, M2, M3, M4, F1, F2, F3, F4, Zr, Mr, Fr, Mem1, Mem2, Mem3, Mem4)
Impedenze=(Z1, Z2, Z3, Z4,Zr)

ResetBottone()

s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 18), foreground="blue")

#definizione bottoni
Somma = ttk.Button(content, text="Z1+Z2", style="my.TButton", command=SommaZ1Z2)
Sottrazione = ttk.Button(content, text="Z1-Z2",style="my.TButton", command=SottrazioneZ1Z2)
Moltiplicazione = ttk.Button(content, text="Z1xZ2", style="my.TButton", command=MoltiplicazioneZ1Z2)
Divisione = ttk.Button(content, text="Z1/Z2", style="my.TButton", command=DivisioneZ1Z2)
Parallelo = ttk.Button(content, text="Z1||Z2", style="my.TButton", command=lambda:ZParalleli(2, Impedenze))
Parallelo3 = ttk.Button(content, text="Z1||Z2||Z3", style="my.TButton", command=lambda:ZParalleli(3, Impedenze))
Parallelo4 = ttk.Button(content, text="Z1||Z2||Z3||Z4", style="my.TButton", command=lambda:ZParalleli(4, Impedenze))

PtoRZs = ttk.Button(content, text="P->R", style="my.TButton", command=PtoRs)

RtoPZs = ttk.Button(content, text="R->P", style="my.TButton", command=RtoPs)

ZrtoZ4 = ttk.Button(content, text="Zr->Z4", style="my.TButton", command=lambda:ZrtoZ(Z4, M4, F4))

z1var=BooleanVar()
z2var=BooleanVar()
z3var=BooleanVar()
z4var=BooleanVar()

z1 = ttk.Checkbutton(content, text="Z1", variable=z1var, onvalue=True)
z2 = ttk.Checkbutton(content, text="Z2", variable=z2var, onvalue=True)
z3 = ttk.Checkbutton(content, text="Z3", variable=z3var, onvalue=True)
z4 = ttk.Checkbutton(content, text="Z4", variable=z4var, onvalue=True)

z1var.set(False)
z2var.set(False)
z3var.set(False)
z4var.set(False)

ScambioZS = ttk.Button(content, text="Scambio Z", style="my.TButton", command=ScambioZSpuntate)

Zsinv = ttk.Button(content, text="1/Z", style="my.TButton", command=invZS)

ZsPiuMeno=ttk.Button(content, text="+/-", style="my.TButton", command=PiuMenoZs)

ZsMem=ttk.Button(content, text="M<->Z", style="my.TButton", command=MemZs)

YD=ttk.Button(content, text="YD123", style="my.TButton", command=YtoD)
DY=ttk.Button(content, text="DY123", style="my.TButton", command=DtoY)
SCS=ttk.Button(content, text="SCY:Z4=U", style="my.TButton", command=SpostamentoCentroStella)

Reset = ttk.Button(content, text="Reset", style="my.TButton", command=ResetBottone)
Disegna = ttk.Button(content, text="Disegna", style="my.TButton", command=DisegnaGrafici)
Cancella = ttk.Button(content, text="Cancella", style="my.TButton", command=CancellaGrafici)



#Posizionamento content in root
content.grid(column=0, row=0, sticky=(N, S, E, W))
content1.grid(column=0, row=1, sticky=(N, S, E, W))
canv.grid(column=1, row=1, sticky=(E))
#canv1.grid(column=7, row=1, sticky=(W))

#posizionamento etichette
cz=3 #colonna delle z
rb=6 #start colonna bottoni operazioni
cartesianalbl.grid(column=cz+2, row=0)
Modulolbl.grid(column=cz+3, row=0)
Faselbl.grid(column=cz+4, row=0)

z1.grid(column=cz+1, row=1)
z2.grid(column=cz+1, row=2)
z3.grid(column=cz+1, row=3)
z4.grid(column=cz+1, row=4)


#posizionamente campi di ingresso
Z1.grid(column=cz+2, row=1, sticky=(W))
Z2.grid(column=cz+2, row=2, sticky=(W))
Z3.grid(column=cz+2, row=3, sticky=(W))
Z4.grid(column=cz+2, row=4, sticky=(W))
Zr.grid(column=cz+2, row=5, sticky=(W))
M1.grid(column=cz+3, row=1, sticky=(W))
M2.grid(column=cz+3, row=2, sticky=(W))
M3.grid(column=cz+3, row=3, sticky=(W))
M4.grid(column=cz+3, row=4, sticky=(W))
Mr.grid(column=cz+3, row=5, sticky=(W))

F1.grid(column=cz+4,  row=1, sticky=(W))
F2.grid(column=cz+4, row=2, sticky=(W))
F3.grid(column=cz+4, row=3, sticky=(W))
F4.grid(column=cz+4, row=4, sticky=(W))
Fr.grid(column=cz+4, row=5, sticky=(W))

#Messaggi.grid(column=cz+1, row=rb+2, columnspan=4, sticky=(W,E))#,column=cz-3)#, columnspan=8)#column=cz+1,
Messaggi.grid(column=0, row=0, columnspan=10, sticky=(W,E))#,column=cz-3)#, columnspan=8)#column=cz+1,


#posizionamento bottoni
Somma.grid(column=cz-3, row=rb+1, ipadx=5)
Sottrazione.grid(column=cz-2, row=rb+1, ipadx=5)
Moltiplicazione.grid(column=cz-1, row=rb+1, ipadx=5)
Divisione.grid(column=cz, row=rb+1, ipadx=5)
Parallelo.grid(column=cz-3, row=rb+2, ipadx=5)
Parallelo3.grid(column=cz-2, row=rb+2, ipadx=5)
Parallelo4.grid(column=cz-1, row=rb+2, ipadx=5)
YD.grid(column=cz-3,row=rb+3, ipadx=5)
DY.grid(column=cz-2,row=rb+3, ipadx=5)
SCS.grid(column=cz-1,row=rb+3, ipadx=5)

PtoRZs.grid(column=2, row=2)

RtoPZs.grid(column=2, row=1)

ZrtoZ4.grid(column=cz,row=rb-1, ipadx=5)

ScambioZS.grid(column=cz, row=rb-4, ipadx=5)

Zsinv.grid(column=cz, row=rb-3, ipadx=5)

ZsPiuMeno.grid(column=cz, row=rb-5)

ZsMem.grid(column=cz, row=rb-2, ipadx=5)

Reset.grid(column=0, row=0, ipadx=10)
Disegna.grid(column=1, row=0, ipadx=10)
Cancella.grid(column=2, row=0, ipadx=10)

# funzioni di conversione

    # Griglia ed assi
stepx = LargTela/10
stepy = AltTela/10
nx = int(Xv0 / 50) + 1
ny = int(Yv0 / 50) + 1
Griglia=[]
for i in range(-nx, nx):
    grix = canv.create_line(i * stepx + Xv0, 0, i * stepx + Xv0, AltTela, fill="lightgrey")

for i in range(-ny, ny):
    griyy = canv.create_line(0, Yv0 + i * stepy, LargTela, Yv0 + i * stepy, fill="lightgrey")

assex = canv.create_line(Xv0, 0, Xv0, AltTela, fill="grey")
assey = canv.create_line(0, Yv0, LargTela, Yv0, fill="grey")


#start

Pdisegnati=[]

root.mainloop()

