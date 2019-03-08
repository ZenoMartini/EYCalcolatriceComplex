import tkinter as tk
import math, cmath

from tkinter import *
from tkinter import ttk

# Inserisce risultato operazioni tra Z1 e Z2 in Z3
from typing import Any, Union


# formatta per n cifre significative della parte reale e di quella immaginaria
# '%s': ciò che segue % (operatore di formato) sarà una stringa
# '%.4g' il numero reale che segue % sarà trasformato in stringa che ne
# considera 4 cifre significative
# la stringa prodotta deve essere convertita in numero reale
#a = float('%s' % float('%.4g' % c.real))
#b = float('%s' % float('%.4g' % c.imag))
#che vengono restituite al chiamante
def salva_Dati_Iniziali():
    DisplayHistory.insert(END, 'Salva ')
    del DatiIniziali[:]
    for z in range(len(Dati)):
        DatiIniziali.append(Dati[z].get())
def recupera_Dati_Iniziali():
    DisplayHistory.insert(END, 'Recupera ')
    ResetBottone(Campi, Pdisegnati)
    for z in range(len(Dati)):
        Dati[z].delete(0, END)
        Dati[z].insert(0, DatiIniziali[z])


def cifreSignificative(c,n):
    #cf='%.4g'
    cf='%.'+str(n)+'g'
    a = float('%s' % float(cf % c.real))
    b = float('%s' % float(cf % c.imag))
    return a, b
def risultato_enabled():
    Zr.config(state='enabled')
    Mr.config(state='enabled')
    Fr.config(state='enabled')
def risultato_disabled():
    Zr.config(state='disabled')
    Mr.config(state='disabled')
    Fr.config(state='disabled')

def risultato(c, Z, M, F):
    risultato_enabled()

    n=4
    a=cifreSignificative(c,n)[0]
    b=cifreSignificative(c,n)[1]
    #print(cifreSignificative(c)[0])
    c = a + b * 1j
    Z.delete(0, END)
    Z.insert(0, c)
    rtoP(Z, M, F)
    Messaggi.delete(0, END)
    cancellaGrafici()
    disegnaGrafici()
    risultato_disabled()



# Sottrai Z2 da Z1
def sottrazioneZ1Z2():
    DisplayHistory.insert(END, 'Z1-Z2 ')
    try:
        a = Z1.get()
        b = Z2.get()
        c = complex(a) - complex(b)
        risultato(c, Zr, Mr, Fr)
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')


# addiziona le Z spuntate
def addizione():
    DisplayHistory.insert(END, 'addizione_1:4 ')
    a = 0
    c = complex(a)
    for i in range(len(zvar) - 4):
        if zvar[i].get():
            try:
                a = Impedenze[i].get()
                c = c + complex(a)
            except ValueError:
                pass
    risultato(c, Zr, Mr, Fr)


# moltiplica le Z spuntate
def moltiplicazione():
    DisplayHistory.insert(END, 'moltiplicazione_1:4 ')
    a = 1
    c = complex(a)
    for i in range(len(zvar) - 4):
        if zvar[i].get():
            try:
                a = Impedenze[i].get()
                c = c * complex(a)
            except ValueError:
                pass
    risultato(c, Zr, Mr, Fr)


def sottrazione():
    pass


def divisione():
    pass


def QuadratoS():
    DisplayHistory.insert(END, '** ')
    for z in range(len(zvar)):
        if zvar[z].get():
            Quadrato(Impedenze[z], Moduli[z], Fasi[z])


def Quadrato(Z, M, F):
    try:
        a = complex(Z.get())
        c = a * a
        risultato(c, Z, M, F)
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata di un numero')


def RadiceQs():
    DisplayHistory.insert(END, 'RadQ ')
    for z in range(len(zvar)):
        if zvar[z].get():
            RadiceQ(Impedenze[z], Moduli[z], Fasi[z])


def RadiceQ(Z, M, F):
    try:
        a = complex(Z.get())
        c = cmath.sqrt(a)
        risultato(c, Z, M, F)
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata di un numero')


def infinito():
    Zr.delete(0, END)
    Zr.insert(0, 'infinito')
    Mr.delete(0, END)
    Fr.delete(0, END)
    Messaggi.delete(0, END)
    Messaggi.insert(0, 'Non si può dividere per zero')


# divide Z1 con Z2
def DivisioneZ1Z2():
    DisplayHistory.insert(END, 'Z1:Z2 ')
    try:
        a = Z1.get()
        b = Z2.get()
        try:
            c = complex(a) / complex(b)
            risultato(c, Zr, Mr, Fr)
        except ZeroDivisionError:
            infinito()

    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')


# calcola il parallelo di n Z

def ZParalleli(n, Impedenze):
    y = 0
    for i in range(n):
        try:
            x = complex(Impedenze[i].get())

            if x == 0:
                Zr.delete(0, END)
                Zr.insert(0, '0')
                break
            else:
                try:
                    y = 1 / x + y
                except ZeroDivisionError:
                    infinito()
                    break
        except ValueError:
            Messaggi.delete(0, END)
            Messaggi.insert(0, "Scrittura errata di almeno un'impedenza")
            break
        try:
            z = 1 / y
            risultato(z, Zr, Mr, Fr)

        except ZeroDivisionError:
            infinito()


# individua la Z da mettere in parallelo
def Paralleli():
    DisplayHistory.insert(END, 'Paralleli')
    try:
        zp = []
        i = 0
        pr = 0
        if z1var.get():
            if complex(Z1.get()).real < 0:
                pr = pr + 1
            else:
                zp.append(Z1)
                i = i + 1
        if z2var.get():
            if complex(Z2.get()).real < 0:
                pr = pr + 1
            else:
                zp.append(Z2)
                i = i + 1
        if z3var.get():
            if complex(Z3.get()).real < 0:
                pr = pr + 1
            else:
                zp.append(Z3)
                i = i + 1
        if z4var.get():
            if complex(Z4.get()).real < 0:
                pr = pr + 1
            else:
                zp.append(Z4)
                i = i + 1
        if i >= 1:
            if pr == 0:
                ZParalleli(i, zp)
            else:
                Messaggi.delete(0, END)
                Messaggi.insert(0, str(pr) + " Z con parte reale negativa")
                del zp[:]
        else:
            Messaggi.delete(0, END)
            Messaggi.insert(0, "Occorre selezionare almeno due Z")
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata di un valore selezionato')


# Individua le Z spuntate
def ptoRs():

    for z in range(len(zvar)):
        if zvar[z].get():
            #print(zvar[z].get())
            ptoR(Moduli[z], Fasi[z], Impedenze[z])


# trasforma in coordinare cartesiane la forma polare di Z
def ptoR_0():
    DisplayHistory.insert(END, 'PtoR ')
    ptoRs()

def ptoR(M: object, F: object, Z: object) -> object:
    try:
        a = float(M.get())
        b = math.radians(float(F.get())) #* math.pi / 180
        c = cmath.rect(a, b)
        risultato(c, Z, M, F)
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')


# individua le Z spuntate
def rtoP_0():

    DisplayHistory.insert(END, 'RtoP ')
    rtoPs()

def rtoPs():

    for z in range(len(zvar)):
        if zvar[z].get():
            rtoP(Impedenze[z], Moduli[z], Fasi[z])


# trasforma in coordinare polari la forma cartesiana  di Z

def rtoP(Z: object, M: object, F: object) -> object:
    """

    :type M: object
    """
    try:
        z = cmath.polar(complex(Z.get()))
        M.delete(0, END)
        F.delete(0, END)
        gradi = math.degrees(z[1])
        M.insert(0, str(float('%s' % float('%.3g' % z[0]))))
        F.insert(0, str(float('%s' % float('%.3g' % gradi))))
        Messaggi.delete(0, END)
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')


def scambiozSpuntate():
    DisplayHistory.insert(END, 'Scambio Z ')
    if z1var.get():
        if z2var.get():
            scambioz(Z1, Z2, M1, F1, M2, F2)
            if z3var.get():
                scambioz(Z2, Z3, M2, F2, M3, F3)
                if z4var.get():
                    scambioz(Z3, Z4, M3, F3, M4, F4)
                    if z5var.get():
                        scambioz(Z4, Zr, M4, F4, Mr, Fr)
                else:
                    if z5var.get():
                        scambioz(Z3, Zr, M3, F3, Mr, Fr)
            else:
                if z4var.get():
                    scambioz(Z1, Z4, M1, F1, M4, F4)
        else:
            if z3var.get():
                scambioz(Z1, Z3, M1, F1, M3, F3)
                if z4var.get():
                    scambioz(Z3, Z4, M3, F3, M4, F4)
                    if z5var.get():
                        scambioz(Zr, Z4, Mr, Fr, M4, F4)
            else:
                if z4var.get():
                    scambioz(Z1, Z4, M1, F1, M4, F4)
                    if z5var.get():
                        scambioz(Z4, Zr, M4, F4, Mr, Fr)
                else:
                    if z5var.get():
                        risultato_enabled()
                        scambioz(Z1, Zr, M1, F1, Mr, Fr)
                        risultato_disabled()

    else:
        if z2var.get():
            if z3var.get():
                scambioz(Z2, Z3, M2, F2, M3, F3)
                if z4var.get():
                    scambioz(Z3, Z4, M3, F3, M4, F4)
                    if z5var.get():
                        risultato_enabled()
                        scambioz(Z4, Zr, M4, F4, Mr, Fr)
                        risultato_disabled()
            else:
                if z4var.get():
                    scambioz(Z2, Z4, M2, F2, M4, F4)
                    if z5var.get():
                        risultato_enabled()
                        scambioz(Z4, Zr, M4, F4, Mr, Fr)
                        risultato_disabled()
                else:
                    if z5var.get():
                        risultato_enabled()
                        scambioz(Z2, Zr, M2, F2, M3, F3)
                        risultato_disabled()
        else:
            if z3var.get():
                if z4var.get():
                    scambioz(Z3, Z4, M3, F3, M4, F4)
                    if z5var.get():
                        risultato_enabled()
                        scambioz(Z4, Zr, M4, F4, Mr, Fr)
                        risultato_disabled()
                else:
                    if z5var.get():
                        risultato_enabled()
                        scambioz(Z3, Zr, M3, F3, Mr, Fr)
                        risultato_disabled()
            else:
                if z4var.get():
                    if z5var.get():
                        risultato_enabled()
                        scambioz(Z4, Zr, M4, F4, Mr, Fr)
                        risultato_disabled()



# scambia tra due Z
def scambioz(Z1, Z2, M1, F1, M2, F2):

    a = Z1.get()
    b = Z2.get()
    Z1.delete(0, END)
    Z2.delete(0, END)
    Z1.insert(0, b)
    Z2.insert(0, a)

    if len(Z1.get()) != 0:
        rtoP(Z1, M1, F1)
    if len(Z2.get()) != 0:
        rtoP(Z2, M2, F2)
    cancellaGrafici()
    disegnaGrafici()


def ztoE():
    DisplayHistory.insert(END, 'Z->E:1:3')
    Es1.delete(0, END)
    Es2.delete(0, END)
    Es3.delete(0, END)
    Es1.insert(0, Z1.get())
    Es2.insert(0, Z2.get())
    Es3.insert(0, Z3.get())


def MemZs():
    DisplayHistory.insert(END, 'M<->Z_1:4 ')
    if z1var.get():
        Memoria(Z1, M1, F1, Mem1)
    if z2var.get():
        Memoria(Z2, M2, F2, Mem2)
    if z3var.get():
        Memoria(Z3, M3, F3, Mem3)
    if z4var.get():
        Memoria(Z4, M4, F4, Mem4)
    cancellaGrafici()
    disegnaGrafici()


def Memoria(Z, M, F, Mem):
    a = Z.get()
    b = Mem.get()
    if a != '':
        Mem.delete(0, END)
        Mem.insert(0, a)
        if b != '':
            Z.delete(0, END)
            Z.insert(0, b)
            rtoP(Z, M, F)


# calcola l'inverso
def invZS():
    DisplayHistory.insert(END, 'Inverso ')
    for z in range(len(zvar)):
        if zvar[z].get():
            invZ(Impedenze[z], Moduli[z], Fasi[z])


# calcola l'inverso
def invZ(Z, M, F):
    Messaggi.delete(0, END)
    try:
        a = complex(Z.get())
        if a != 0:
            a = 1 / a
            risultato(a, Z, M, F)
        else:
            Messaggi.insert(0, 'Non si può dividere per zero')
    except ValueError:
        # Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata Z')


def MemDivisoZ():
    DisplayHistory.insert(END, 'M/Z_1:4 ')
    if z1var.get():
        a = complex(Mem1.get()) / complex(Z1.get())
        risultato(a, Z1, M1, F1)
    if z2var.get():
        a = complex(Mem2.get()) / complex(Z2.get())
        risultato(a, Z2, M2, F2)
    if z3var.get():
        a = complex(Mem3.get()) / complex(Z3.get())
        risultato(a, Z3, M3, F3)
    if z4var.get():
        a = complex(Mem4.get()) / complex(Z4.get())
        risultato(a, Z4, M4, F4)


def PiuMenoZs():
    DisplayHistory.insert(END, '+/- ')
    for z in range(len(zvar)):
        if zvar[z].get():
            piuMeno(Impedenze[z], Moduli[z], Fasi[z])


def piuMeno(Z, M, F):

    try:
        a = -complex(Z.get())
        risultato(a, Z, M, F)
        # print(a)
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata del numero')

def reset_0():
    DisplayHistory.insert(END, 'Reset')
    risultato_enabled()
    ResetBottone(Campi, Pdisegnati)
    risultato_disabled()

def ResetBottone(Campi, Pdisegnati):

    for i in range(len(Campi)):
        Campi[i].delete(0, END)
    Messaggi.delete(0, END)
    if len(Pdisegnati) > 0:
        cancellaGrafici()
def setZ_0():
    DisplayHistory.insert(END, 'Set')
    ResetBottone(Campi, Pdisegnati)
    setZ()

def setZ():

    Z1.delete(0, END)
    Z1.insert(0, "10+8j")
    Z2.delete(0, END)
    Z2.insert(0, "-16j")
    Z3.delete(0, END)
    Z3.insert(0, "18-8j")
    Z4.delete(0, END)
    Z4.insert(0, "400")
    ME1.delete(0, END)
    ME1.insert(0, "231")
    ME2.delete(0, END)
    ME2.insert(0, "231")
    ME3.delete(0, END)
    ME3.insert(0, "231")
    FE1.delete(0, END)
    FE1.insert(0, "0")
    FE2.delete(0, END)
    FE2.insert(0, "-120")
    FE3.delete(0, END)
    FE3.insert(0, "120")
    Zr.delete(0, END)
    Zr.insert(0, '10-8j')
    Mem1.delete(0,END)
    Mem1.insert(0,'1')
    Mem2.delete(0, END)
    Mem2.insert(0, '1')
    Mem3.delete(0, END)
    Mem3.insert(0, '1')
    Mem4.delete(0, END)
    Mem4.insert(0, '1')
    Memr.delete(0, END)
    Memr.insert(0, '1')


# trasforma le prime tre Z considerate rami di una stella in lati del triangolo equivalente
# e memorizza i rami della stella
def YtoD():
    DisplayHistory.insert(END, 'YDZ123')
    try:
        a = complex(Z1.get())
        b = complex(Z2.get())
        c = complex(Z3.get())
        if a * b * c == 0:
            Messaggi.delete(0, END)
            Messaggi.insert(0, 'Non è una stella:qualche impedenza è nulla')
        else:
            Memoria(Z1, M1, F1, Mem1)
            Memoria(Z2, M2, F2, Mem2)
            Memoria(Z3, M3, F3, Mem3)
            N = a * b + b * c + a * c
            c1 = N / c
            risultato(c1, Z1, M1, F1)
            c1 = N / a
            risultato(c1, Z2, M2, F2)
            c1 = N / b
            risultato(c1, Z3, M3, F3)

    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata di qualche impedenza')


# trasforma le prime tre Z considerate lati di un triangolo i rami della stella equivalente
# e memorizza i lati del triangolo
def DtoY():
    DisplayHistory.insert(END, 'DY123')
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
            D = a + b + c
            c1 = a * c / D
            risultato(c1, Z1, M1, F1)
            c1 = b * a / D
            risultato(c1, Z2, M2, F2)
            c1 = b * c / D
            risultato(c1, Z3, M3, F3)

    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata di qualche impedenza')


def spostamentoCentroStella_S():
    DisplayHistory.insert(END, ' \n SCY:Z4=U \n')
    try:
        a = complex(Z1.get())
        b = complex(Z2.get())
        c = complex(Z3.get())
        d = complex(Z4.get()) / math.sqrt(3)
        e = f2 * d
        f = f3 * d
        spostamentoCentroStella(a, b, c, d, e, f)

    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, "C'è almeno una scrittura errata nei dati")


def spostamentoCentroStella_D():
    DisplayHistory.insert(END, '\n SCY_G \n')
    try:
        a = complex(Z1.get())
        b = complex(Z2.get())
        c = complex(Z3.get())
        d = complex(Es1.get())
        e = complex(Es2.get())
        f = complex(Es3.get())
        spostamentoCentroStella(a, b, c, d, e, f)
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, "C'è almeno una scrittura errata nei dati")


# Z1,Z2,3 sono i valori della stella squilibrata
# in Z4 va inserito il valore della tensione concatenata del sistema simmetrico di alimentazione
# In Zr viene posto il valore dello spostamento rispetto al centro stella ideale del sistema
# quest'ultimo corrispondente allo zero.


def spostamentoCentroStella(a, b, c, d, e, f):
# Le tensioni di fase risultanti son inserite in Z1, Z2, Z3
# le correnti in Mem1, Mem2, Mem3
#le tensione dei generatori sono in E1, E2, E3
#in Z5 lo spostamento del centro stella

    try:
        if 1 / a + 1 / b + 1 / c == 0:
            Messaggi.delete(0, END)
            Messaggi.insert(0, 'spostamento infinito o indefinito')
        else:
            V: Union[complex, Any] = (d / a + e / b + f / c) / (1 / a + 1 / b + 1 / c)
            E1 = d - V
            E2 = e - V
            E3 = f - V
            I1 = E1 / a
            I2 = E2 / b
            I3 = E3 / c
    except ZeroDivisionError:
        print('divisione per zero')
        if a == 0:
            if b == 0:
                Messaggi.delete(0, END)
                Messaggi.insert(0, 'Indeterminato')
            else:
                if c == 0:
                    Messaggi.delete(0, END)
                    Messaggi.insert(0, 'Indeterminato')
                else:
                    V = d
                    E1 = d - V
                    E2 = e - V
                    E3 = f - V
                    I2 = E2 / b
                    I3 = E3 / c
                    I1 = -I2 - I3

        else:
            if b == 0:
                if c == 0:
                    Messaggi.delete(0, END)
                    Messaggi.insert(0, 'Indeterminato')
                else:
                    V = e
                    E1 = d - V
                    E2 = e - V
                    E3 = f - V
                    I1 = E1 / a
                    I3 = E3 / c
                    I2 = -I1 - I3

            else:
                if c == 0:
                    V = f
                    E1 = d - V
                    E2 = e - V
                    E3 = f - V
                    I1 = E1 / a
                    I2 = E2 / b
                    I3 = -I1 - I2
                else:
                    E1 = d - V
                    E2 = d * f2 - V
                    E3 = d * f3 - V
                    I1 = E1 / a
                    I2 = E2 / b
                    I3 = E3 / c

    risultato(V, Zr, Mr, Fr)
    risultato(I1, Z1, M1, F1)
    risultato(I2, Z2, M2, F2)
    risultato(I3, Z3, M3, F3)
    Memoria(Z1, M1, F1, Mem1)
    Memoria(Z2, M2, F2, Mem2)
    Memoria(Z3, M3, F3, Mem3)
    risultato(E1, Z1, M1, F1)
    risultato(E2, Z2, M2, F2)
    risultato(E3, Z3, M3, F3)
    DisplayHistory.insert(END, 'V:' + Zr.get() + '\n' + 'E1=' + Z1.get() + " E2=" +Z2.get() + ' E3=' + Z3.get()
                          + '\n'+ 'I1= '+ Mem1.get() + ' I2=' + Mem2.get() +' I3=' + Mem3.get() + '\n')


# Scompone la terna quilibrata Z1,Z2,Z3 nelle terne diretta, inversa, omopolare
# La terna squilibrata viene memorizzata nelle Mem
# In Z1 c'è il valore del primo vettore della terna diretta
# In Z2 quello del primo valore della terna inversa
# In Z3 il valore della terna omopolare
def sequenze():
    DisplayHistory.insert(END, '\n sequenze \n')
    try:
        a = complex(Z1.get())
        b = complex(Z2.get())
        c = complex(Z3.get())
        # diretta
        diretta = (a + b * f3 + c * f2) / 3
        Memoria(Z1, M1, F1, Mem1)
        risultato(diretta, Z1, M1, F1)
        # inversa
        inversa = (a + b * f2 + c * f3) / 3
        Memoria(Z2, M2, F2, Mem2)
        risultato(inversa, Z2, M2, F2)
        # omopolare
        zero = (a + b + c) / 3
        Memoria(Z3, M3, F3, Mem3)
        risultato(zero, Z3, M3, F3)
        DisplayHistory.insert(END,'1:'+str(a)+' 2:'+ str(b) + ' 3:' + str(c) +'\n'+
                              'Ed='+Z1.get() + 'Ei=' + Z2.get() + 'E0=' + Z3.get() + '\n')
    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, "C'è almeno una scrittura errata nei dati")


# rappresenta con dei punti nel piano complesso Z1,Z2,Z3,Z4,Zr
def disegna_0():
    DisplayHistory.insert(END, 'Disegna')
    disegnaGrafici()
def disegnaGrafici():

    Messaggi.delete(0, END)
    # coordinate relative grafico
    zs = []

    for i in range(len(Impedenze)):
        if zvar[i].get():
            zs.append(i)
    try:
        zi = []
        for z in range(len(zs)):
            c = cmath.polar(complex(Impedenze[zs[z]].get()))
            zi.append(c)

        l = 0
        pos = 0
        while pos < len(zi):
            if zi[pos][0] > l:
                l = zi[pos][0]
            pos = pos + 1

        if l > 0:
            del zi[:]
            DaiDisegna(l, zs)
        else:
            Messaggi.delete(0, END)
            Messaggi.insert(0, 'Impossibile disegnare')
    except ValueError:

        Messaggi.delete(0, END)
        Messaggi.insert(0, 'Scrittura errata Z' + str(zs[z] + 1))


def DaiDisegna(l, zs):

    xmin = -l
    xmax = l
    ymin = -l
    ymax = l

    k1 = LargTela / (xmax - xmin)  # calcolo costanti di conversione
    k2 = AltTela / (ymax - ymin)
    s = l / 5  # scala

    PZn = []

    for z in range(len(zs)):
        PZ = (k1 * complex(Impedenze[zs[z]].get()).real + Xv0, Yv0 - k2 * complex(Impedenze[zs[z]].get()).imag)
        PZn.append(PZ)

    r = 3

    for z in range(len(PZn)):
        cz = canv.create_oval(PZn[z][0] + r, PZn[z][1] - r, PZn[z][0] - r, PZn[z][1] + r, fill=Zcolor[zs[z]])
        lz = canv.create_line(Xv0, Yv0, PZn[z][0], PZn[z][1], fill=Zcolor[zs[z]], arrow=LAST)
        Pdisegnati.append(cz)
        Pdisegnati.append(lz)
    um = canv.create_text(25, 40, text="1:" + str(round(s, 2)))
    Pdisegnati.append(um)
    del PZn[:]
    del zs[:]


# elimina tutti gli elementi del disegno
def cancellaR():
    DisplayHistory.insert(END, 'Cancella')
    cancellaGrafici()


def cancellaGrafici():
    for z in range(len(Pdisegnati)):
        canv.delete(Pdisegnati[z])
    del Pdisegnati[:]
    Messaggi.delete(0, END)



def select(value):
    DisplayHistory.insert(END, value)

    if value != "C" and value != "SetMod" and value != "SetFase":
        if value != 'real/10' and value != '<-':

            if z1var.get():
                Z1.insert(END, value)
            if z2var.get():
                Z2.insert(END, value)
            if z3var.get():
                Z3.insert(END, value)
            if z4var.get():
                Z4.insert(END, value)

        else:
            if value == 'real/10':
                if z1var.get():
                    a = complex(Z1.get()).real
                    Z1.delete(0, END)
                    Z1.insert(END, str(a / 10))
                if z2var.get():
                    a = complex(Z2.get()).real
                    Z2.delete(0, END)
                    Z2.insert(END, str(a / 10))
                if z3var.get():
                    a = complex(Z3.get()).real
                    Z3.delete(0, END)
                    Z3.insert(END, str(a / 10))
                if z4var.get():
                    a = complex(Z4.get()).real
                    Z4.delete(0, END)
                    Z4.insert(END, str(a / 10))

            else:
                if z1var.get():
                    Z1.delete(len(Z1.get()) - 1, END)
                if z2var.get():
                    Z2.delete(len(Z2.get()) - 1, END)
                if z3var.get():
                    Z3.delete(len(Z3.get()) - 1, END)
                if z4var.get():
                    Z4.delete(len(Z4.get()) - 1, END)

    else:

        if value == "C":
            DisplayHistory.delete('1.0', END)
            if z1var.get():
                Z1.delete(0, END)
                M1.delete(0, END)
                F1.delete(0, END)
            if z2var.get():
                Z2.delete(0, END)
                M2.delete(0, END)
                F2.delete(0, END)
            if z3var.get():
                Z3.delete(0, END)
                M3.delete(0, END)
                F3.delete(0, END)
            if z4var.get():
                Z4.delete(0, END)
                M4.delete(0, END)
                F4.delete(0, END)
        else:
            if value == "SetMod":
                if z1var.get():
                    M1.delete(0, END)
                    M1.insert(END, math.fabs(complex(Z1.get()).real))
                    Z1.delete(0, END)
                if z2var.get():
                    M2.delete(0, END)
                    M2.insert(END, math.fabs(complex(Z2.get()).real))
                    Z2.delete(0, END)
                if z3var.get():
                    M3.delete(0, END)
                    M3.insert(END, math.fabs(complex(Z3.get()).real))
                    Z3.delete(0, END)
                if z4var.get():
                    M4.delete(0, END)
                    M4.insert(END, math.fabs(complex(Z4.get()).real))
                    Z4.delete(0, END)
            else:
                if z1var.get():
                    F1.delete(0, END)
                    F1.insert(END, complex(Z1.get()).real)
                    Z1.delete(0, END)
                if z2var.get():
                    F2.delete(0, END)
                    F2.insert(END, complex(Z2.get()).real)
                    Z2.delete(0, END)
                if z3var.get():
                    F3.delete(0, END)
                    F3.insert(END, complex(Z3.get()).real)
                    Z3.delete(0, END)
                if z4var.get():
                    F4.delete(0, END)
                    F4.insert(END, complex(Z4.get()).real)
                    Z4.delete(0, END)

def matriceTrasmissione():

    DisplayHistory.insert(END,  '\n zyx->[ABCD] \n')
    try:
        del MatriceTrasmissione[:]
        z = complex(Z1.get())
        y = complex(Z2.get())
        x = complex(Z3.get()).real
        Z0 = cmath.sqrt(z/y)
        k = cmath.sqrt(z*y)
        print(Z0, k)
        try:
            n=4
            A = cmath.cosh(k*x)
            B = Z0*cmath.sinh(k*x)
            C = cmath.sinh(k*x)/Z0
            D = cmath.cosh(k*x)

            A=cifreSignificative(A,n)[0]+cifreSignificative(A,n)[1]*1j
            B=cifreSignificative(B,n)[0]+cifreSignificative(B,n)[1]*1j
            C=cifreSignificative(C,n)[0]+cifreSignificative(C,n)[1]*1j
            D=cifreSignificative(D,n)[0]+cifreSignificative(D,n)[1]*1j

            MatriceTrasmissione.append([A,B])
            MatriceTrasmissione.append([C,D])
            print("A:", MatriceTrasmissione[0][0], "B:", MatriceTrasmissione[0][1],
                  'C:', MatriceTrasmissione[1][0], 'D:', MatriceTrasmissione[1][1])
            DisplayHistory.insert(END, "A:"+ str(MatriceTrasmissione[0][0])+ " B:" + str(MatriceTrasmissione[0][1]) +'\n'+
                                  'C:'+str(MatriceTrasmissione[1][0]) +' D:'+ str(MatriceTrasmissione[1][1])+'\n')
                  #)
        except OverflowError:
            Messaggi.delete(0, END)
            Messaggi.insert(0, "Valori inammissibili: errore di overflow")

    except ValueError:
        Messaggi.delete(0, END)
        Messaggi.insert(0, "Qualche valore errato: Z1>z; Z2->y, Z3->x(reale)")




# costanti varie

# operatori di sequenza
f2 = cmath.rect(1, -2 * math.pi / 3)  # 2
f3 = cmath.rect(1, 2 * math.pi / 3)  # 3

# margini esterni del widget
sinistra = 10
sopra = 10
destra = 10
sotto = 10
impacchettamento = (sinistra, sopra, destra, sotto)
# aspetto del frame
rilievo = ("flat", "raised", "sunken", "groove", "ridge")
# dimensioni widget
LEZ = 20  # Larghezza Entry campi Z
LEM = 8  # Larghezza Entry campi M ed F
FEZ = "Baskerville 24"  # Font Entry campi Z
FEM = "Arial 14"  # Font Entry campi M ed F
# parametro posizione widget
cz = 3  # colonna delle z
rb = 6  # start colonna bottoni operazioni

# riquadro grafico e punto centrale
LargTela = 500
AltTela = 500
Xv0 = LargTela / 2
Yv0 = AltTela / 2
# parametri griglia ed assi
stepx = LargTela / 10  # distanza tra linee verticali
stepy = AltTela / 10  # distanza tra linee orizzontali
nx = int(Xv0 / 50) + 1
ny = int(Yv0 / 50) + 1
# colori usati
Zcolor = ('firebrick', 'dodgerblue', 'darkgreen', 'goldenrod', 'red', 'magenta',
          'blueviolet', 'saddlebrown', 'chocolate', 'dimgrey', 'black', 'indianred', 'beige',
          'ivory', 'lightgreen', 'skyblue', 'white', 'gold')

# finestra principale

root = Tk()
root.title("Calcolatrice per numeri complessi")
root.configure(background="green")
#root.resizable(0, 0)

# genera due widget "frame" dentro la finestra principale
# contenitore tasti funzione e campi di I/O
content = ttk.Frame(root, padding=impacchettamento, relief="sunken")
# contenitore messaggi errore e grafico

content1 = ttk.Frame(root, padding=impacchettamento, relief="sunken")
# contenitore tastierino
content2 = ttk.Frame(root, padding=impacchettamento, relief="sunken")
# genera la tela per disegnare
canv = tk.Canvas(content1, highlightthickness=0, bg='white', width=LargTela, height=AltTela)

# definizioni etichette


cartesianalbl = ttk.Label(content, text="a+bj", font="Helvetica 16")
Modulolbl = ttk.Label(content, text="Modulo", font="Helvetica 16")
Faselbl = ttk.Label(content, text="Fase in gradi", font="Helvetica 16")

# definizione campi di ingresso


c1 = ttk.Style()  # definisce l'aspetto del campo come colore del fondo, del carattere
c1.configure('Z1.TEntry', foreground=Zcolor[0]) #, background="whitesmoke")
c2 = ttk.Style()  # definisce l'aspetto del campo come colore del fondo, del carattere
c2.configure('Z2.TEntry', foreground=Zcolor[1]) #, background="whitesmoke")
c3 = ttk.Style()  # definisce l'aspetto del campo come colore del fondo, del carattere
c3.configure('Z3.TEntry', foreground=Zcolor[2]) #, background="whitesmoke")
c4 = ttk.Style()  # definisce l'aspetto del campo come colore del fondo, del carattere
c4.configure('Z4.TEntry', foreground=Zcolor[3]) #, background="whitesmoke")
p = ttk.Style()
p.configure('P1.TEntry', foreground=Zcolor[4], background="whitesmoke")
m = ttk.Style()
m.configure('M.TEntry', font=FEM, background="lightyellow", foreground=Zcolor[4])
c5 = ttk.Style()  # definisce l'aspetto del campo come colore del fondo, del carattere
c5.configure('E1.TEntry', foreground=Zcolor[5], background="whitesmoke")
c6 = ttk.Style()  # definisce l'aspetto del campo come colore del fondo, del carattere
c6.configure('E2.TEntry', foreground=Zcolor[11], background="whitesmoke")
c7 = ttk.Style()  # definisce l'aspetto del campo come colore del fondo, del carattere
c7.configure('E3.TEntry', foreground=Zcolor[9], background="whitesmoke")

Z1 = ttk.Entry(content, width=LEZ, style="Z1.TEntry", justify=RIGHT, font=FEZ)
Z2 = ttk.Entry(content, width=LEZ, style="Z2.TEntry", justify=RIGHT, font=FEZ)
Z3 = ttk.Entry(content, width=LEZ, style="Z3.TEntry", justify=RIGHT, font=FEZ)
Z4 = ttk.Entry(content, width=LEZ, style="Z4.TEntry", justify=RIGHT, font=FEZ)

Zr = ttk.Entry(content, width=LEZ, style="P1.TEntry", state='disabled')
Zr.configure(foreground="red", font=FEZ, justify=RIGHT)

M1 = ttk.Entry(content, width=LEM, font=FEZ, justify=RIGHT)
M2 = ttk.Entry(content, width=LEM, font=FEZ, justify=RIGHT)
M3 = ttk.Entry(content, width=LEM, font=FEZ, justify=RIGHT)
M4 = ttk.Entry(content, width=LEM, font=FEZ, justify=RIGHT)
Mr = ttk.Entry(content, width=LEM, style="P1.TEntry", state='disabled')
Mr.configure(foreground="red", font=FEZ, justify=RIGHT)

ME1 = ttk.Entry(content, width=LEM, font=FEZ, justify=RIGHT)
ME2 = ttk.Entry(content, width=LEM, font=FEZ, justify=RIGHT)
ME3 = ttk.Entry(content, width=LEM, font=FEZ, justify=RIGHT)

Es1 = ttk.Entry(content, width=LEZ, style="E1.TEntry", justify=RIGHT, font=FEZ)
Es2 = ttk.Entry(content, width=LEZ, style="E2.TEntry", justify=RIGHT, font=FEZ)
Es3 = ttk.Entry(content, width=LEZ, style="E3.TEntry", justify=RIGHT, font=FEZ)

F1 = ttk.Entry(content, width=LEM, font=FEZ, justify=RIGHT)
F2 = ttk.Entry(content, width=LEM, font=FEZ, justify=RIGHT)
F3 = ttk.Entry(content, width=LEM, font=FEZ, justify=RIGHT)
F4 = ttk.Entry(content, width=LEM, font=FEZ, justify=RIGHT)

Fr = ttk.Entry(content, width=LEM, style="P1.TEntry", state='disabled')
Fr.configure(foreground="red", font=FEZ, justify=RIGHT)

FE1 = ttk.Entry(content, width=LEM, font=FEZ, justify=RIGHT)
FE2 = ttk.Entry(content, width=LEM, font=FEZ, justify=RIGHT)
FE3 = ttk.Entry(content, width=LEM, font=FEZ, justify=RIGHT)

Mem1 = ttk.Entry(content, width=LEM, font=FEZ)
Mem2 = ttk.Entry(content, width=LEM, font=FEZ)
Mem3 = ttk.Entry(content, width=LEM, font=FEZ)
Mem4 = ttk.Entry(content, width=LEM, font=FEZ)
Memr = ttk.Entry(content, width=LEM, font=FEZ)

Messaggi = ttk.Entry(content1, width=9 * LEM, font=FEM, justify=LEFT, style="M.TEntry")

Campi = (Z1, Z2, Z3, Z4, M1, M2, M3, M4, F1, F2, F3, F4, Zr, Mr, Fr,
         Mem1, Mem2, Mem3, Mem4, Es1, Es2, Es3, ME1, ME2, ME3, FE1, FE2, FE3)
Impedenze = (Z1, Z2, Z3, Z4, Zr, Es1, Es2, Es3)
Moduli = (M1, M2, M3, M4, Mr, ME1, ME2, ME3)
Fasi = (F1, F2, F3, F4, Fr, FE1, FE2, FE3)

Dati = (Z1, Z2, Z3, Z4, Es1, Es2, Es3)
DatiIniziali=[]

s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 18), foreground="blue", background='lightblue')

# definizione bottoni
Somma = ttk.Button(content, text="addizione_1:4", style="my.TButton", command=addizione)
Sottrazione = ttk.Button(content, text="Z1-Z2", style="my.TButton", command=sottrazioneZ1Z2)
Moltiplicazione = ttk.Button(content, text="moltiplicazione_1:4", style="my.TButton", command=moltiplicazione)
Divisione = ttk.Button(content, text="Z1/Z2", style="my.TButton", command=DivisioneZ1Z2)

ParalleliButton = ttk.Button(content, text="Paralleli_1:4", style="my.TButton", command=Paralleli)

PtoRZs = ttk.Button(content, text="P->R", style="my.TButton", command=ptoR_0)

RtoPZs = ttk.Button(content, text="R->P", style="my.TButton", command=rtoP_0)

z1var = BooleanVar()
z2var = BooleanVar()
z3var = BooleanVar()
z4var = BooleanVar()
z5var = BooleanVar()
z6var = BooleanVar()
z7var = BooleanVar()
z8var = BooleanVar()

z1 = ttk.Checkbutton(content, text="Z1", variable=z1var)
z2 = ttk.Checkbutton(content, text="Z2", variable=z2var)
z3 = ttk.Checkbutton(content, text="Z3", variable=z3var)
z4 = ttk.Checkbutton(content, text="Z4", variable=z4var)
z5 = ttk.Checkbutton(content, text="ZR", variable=z5var)

E1 = ttk.Checkbutton(content, text="E1", variable=z6var)
E2 = ttk.Checkbutton(content, text="E2", variable=z7var)
E3 = ttk.Checkbutton(content, text="E3", variable=z8var)

zvar = (z1var, z2var, z3var, z4var, z5var, z6var, z7var, z8var)

scambiozS = ttk.Button(content, text="Scambio Z", style="my.TButton", command=scambiozSpuntate)

Zsinv = ttk.Button(content, text="Inverso", style="my.TButton", command=invZS)
MsuZ = ttk.Button(content, text="M/Z_1:4", style="my.TButton", command=MemDivisoZ)
Zradq = ttk.Button(content, text="RadQ", style="my.TButton", command=RadiceQs)
Zquad = ttk.Button(content, text="**", style="my.TButton", command=QuadratoS)

ZtoEs = ttk.Button(content, text="Z->E:1:3", style="my.TButton", command=ztoE)

ZsPiuMeno = ttk.Button(content, text="+/-", style="my.TButton", command=PiuMenoZs)

ZsMem = ttk.Button(content, text="M<->Z_1:4", style="my.TButton", command=MemZs)

YD = ttk.Button(content, text="YDZ123", style="my.TButton", command=YtoD)
DY = ttk.Button(content, text="DY123", style="my.TButton", command=DtoY)
SCS = ttk.Button(content, text="SCY:Z4=U", style="my.TButton", command=spostamentoCentroStella_S)
SCS_G = ttk.Button(content, text="SCY_G", style="my.TButton", command=spostamentoCentroStella_D)
MatriceTrasmissioneButton = ttk.Button(content, text="zyx->[ABCD]", style="my.TButton", command=matriceTrasmissione)


sequenzeBottone = ttk.Button(content, text="sequenze", style="my.TButton", command=sequenze)

Reset = ttk.Button(content, text="Reset", style="my.TButton", command = reset_0) # lambda: ResetBottone(Campi, Pdisegnati))
Disegna = ttk.Button(content, text="Disegna", style="my.TButton", command = disegna_0)
Cancella = ttk.Button(content, text="Cancella", style="my.TButton", command = cancellaR)

SetZButton = ttk.Button(content, text="Set", style="my.TButton", command = setZ_0)
SalvaDIButton = ttk.Button(content, text="Salva", style="my.TButton", command = salva_Dati_Iniziali)
RecuperaDIButton = ttk.Button(content, text="Recupera", style="my.TButton", command = recupera_Dati_Iniziali)


# testo storia
DisplayHistory = Text(content2, height=24, width=65, bd=5, bg=Zcolor[12], fg="red", cursor='circle',
                      font=('Arial', 14 ),
                      padx=5, pady=5)

# Posizionamento content in root
content.grid(column=0, row=0, columnspan=2, sticky=(N, S, E, W))
content1.grid(column=0, row=1, rowspan=5, sticky=(W, N, E))
content2.grid(column=1, row=1, sticky=(N, E))
# posizionamento tela disegno

canv.grid(column=0, row=1, sticky=(W, E, N))
DisplayHistory.grid(column=0, row=5, columnspan=4, sticky=(S))

# posizionamento etichette

cartesianalbl.grid(column=cz + 2, row=0)
Modulolbl.grid(column=cz + 3, row=0)
Faselbl.grid(column=cz + 4, row=0)
#Albl.grid(column=cz + 1, row=6)
#Blbl.grid(column=cz + 1, row=7)
#Clbl.grid(column=cz + 1, row=8)


# zrlbl.grid(column=cz+1,row=5)

z1.grid(column=cz + 1, row=1)
z2.grid(column=cz + 1, row=2)
z3.grid(column=cz + 1, row=3)
z4.grid(column=cz + 1, row=4)
z5.grid(column=cz + 1, row=5)
E1.grid(column=cz + 1, row=6)
E2.grid(column=cz + 1, row=7)
E3.grid(column=cz + 1, row=8)

# posizionamente campi di ingresso
Z1.grid(column=cz + 2, row=1, sticky=(W))
Z2.grid(column=cz + 2, row=2, sticky=(W))
Z3.grid(column=cz + 2, row=3, sticky=(W))
Z4.grid(column=cz + 2, row=4, sticky=(W))
Zr.grid(column=cz + 2, row=5, sticky=(W))
M1.grid(column=cz + 3, row=1, sticky=(W))
M2.grid(column=cz + 3, row=2, sticky=(W))
M3.grid(column=cz + 3, row=3, sticky=(W))
M4.grid(column=cz + 3, row=4, sticky=(W))
Mr.grid(column=cz + 3, row=5, sticky=(W))
Es1.grid(column=cz + 2, row=6, sticky=(W))
Es2.grid(column=cz + 2, row=7, sticky=(W))
Es3.grid(column=cz + 2, row=8, sticky=(W))

ME1.grid(column=cz + 3, row=6, sticky=(W))
ME2.grid(column=cz + 3, row=7, sticky=(W))
ME3.grid(column=cz + 3, row=8, sticky=(W))

F1.grid(column=cz + 4, row=1, sticky=(W))
F2.grid(column=cz + 4, row=2, sticky=(W))
F3.grid(column=cz + 4, row=3, sticky=(W))
F4.grid(column=cz + 4, row=4, sticky=(W))
Fr.grid(column=cz + 4, row=5, sticky=(W))
FE1.grid(column=cz + 4, row=6, sticky=(W))
FE2.grid(column=cz + 4, row=7, sticky=(W))
FE3.grid(column=cz + 4, row=8, sticky=(W))

Messaggi.grid(column=0, row=0, columnspan=10, sticky=(N, W, E))

# posizionamento bottoni
Somma.grid(column=cz - 3, row=rb + 1, ipadx=5)
Sottrazione.grid(column=cz - 2, row=rb + 1, ipadx=5)
Moltiplicazione.grid(column=cz - 1, row=rb + 1, ipadx=5)
Divisione.grid(column=cz, row=rb + 1, ipadx=5)
ParalleliButton.grid(column=cz, row=rb + 2, ipadx=5)

YD.grid(column=cz - 3, row=rb + 3, ipadx=5)
DY.grid(column=cz - 2, row=rb + 3, ipadx=5)
SCS.grid(column=cz - 1, row=rb + 3, ipadx=5)
SCS_G.grid(column=cz - 1, row=rb + 2, ipadx=5)
MatriceTrasmissioneButton.grid(column=cz - 2, row=rb + 2, ipadx=5)


sequenzeBottone.grid(column=cz, row=rb + 3, ipadx=5)

PtoRZs.grid(column=2, row=2)

RtoPZs.grid(column=2, row=1)

scambiozS.grid(column=cz, row=rb - 4, ipadx=5)

Zsinv.grid(column=cz, row=rb - 3, ipadx=5)

MsuZ.grid(column=cz - 1, row=rb - 3, ipadx=5)
Zradq.grid(column=cz - 1, row=rb - 2, ipadx=5)
Zquad.grid(column=cz - 1, row=rb - 1, ipadx=5)

ZsPiuMeno.grid(column=cz, row=rb - 5)

ZsMem.grid(column=cz, row=rb - 2, ipadx=5)
ZtoEs.grid(column=cz, row=rb - 1, ipadx=5)

Reset.grid(column=0, row=0, ipadx=10)
SetZButton.grid(column=0, row=1, ipadx=10)
SalvaDIButton.grid(column=0, row=2, ipadx=10)
RecuperaDIButton.grid(column=0, row=3, ipadx=10)



Disegna.grid(column=1, row=0, ipadx=10)
Cancella.grid(column=2, row=0, ipadx=10)

# Tracciamento griglia ed assi

Griglia = []
for i in range(-nx, nx):
    grix = canv.create_line(i * stepx + Xv0, 0, i * stepx + Xv0, AltTela, fill="lightgrey")

for i in range(-ny, ny):
    griy = canv.create_line(0, Yv0 + i * stepy, LargTela, Yv0 + i * stepy, fill="lightgrey")

assex = canv.create_line(Xv0, 0, Xv0, AltTela, fill="grey")
assey = canv.create_line(0, Yv0, LargTela, Yv0, fill="grey")

MatriceTrasmissione = []

# start

Pdisegnati = []

buttons = ['C', 'real/10', 'e', 'SetMod',
           '7', '8', '9', 'SetFase',
           '4', '5', '6', '-',
           '1', '2', '3', '+',
           '0', 'j', '.', '<-']

varRow = 0
varColumn = 0

for button in buttons:
    command = lambda x=button: select(x)
    ttk.Button(content2, text=button, width=8, style="my.TButton",
               command=command).grid(row=varRow, column=varColumn)

    varColumn += 1

    if varColumn == 4 and varRow == 0:
        varColumn = 0
        varRow += 1
    if varColumn == 4 and varRow == 1:
        varColumn = 0
        varRow += 1
    if varColumn == 4 and varRow == 2:
        varColumn = 0
        varRow += 1
    if varColumn == 4 and varRow == 3:
        varColumn = 0
        varRow += 1

ResetBottone(Campi, Pdisegnati)

root.mainloop()
