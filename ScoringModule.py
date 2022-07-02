from email.policy import default
from tkinter import *
from  ttkthemes import ThemedStyle
from tkinter.messagebox import *

p1_win=0
p2_win=0

def verif_match():
    global p1_win
    global p2_win
    if p1_win==2 or p2_win==2:
        return True
    return False

def verif_set1():
    global pts_player1_set1
    global pts_player2_set1
    pts1=pts_player1_set1.get()
    pts2=pts_player2_set1.get()

    if (pts1>=21 and pts1-pts2>=2) or (pts2>=21 and pts2-pts1>=2) or (pts1==30 or pts2==30):
        return True
    return False

def verif_set2():
    global pts_player1_set2
    global pts_player2_set2
    pts1=pts_player1_set2.get()
    pts2=pts_player2_set2.get()

    if (pts1>=21 and pts1-pts2>=2) or (pts2>=21 and pts2-pts1>=2) or (pts1==30 or pts2==30):
        return True
    return False

def verif_set3():
    global pts_player1_set3
    global pts_player2_set3
    pts1=pts_player1_set3.get()
    pts2=pts_player2_set3.get()

    if (pts1>=21 and pts1-pts2>=2) or (pts2>=21 and pts2-pts1>=2) or (pts1==30 or pts2==30):
        return True
    return False


fenetre = Tk()
fenetre.geometry("1010x310")
fenetre.title("Live Scoring by Esteban")
fenetre.configure(bg="grey14")
style =ThemedStyle(fenetre)
style.set_theme('equilux') 


nom_player1 = StringVar()
label = Label( fenetre, textvariable=nom_player1,font=(default,100),bg="grey14")
nom_player1.set("Player 1")
label.grid(row=0,column=1)

pts_player1_set1 = IntVar()
label2 = Label( fenetre, textvariable=pts_player1_set1,font=(default,100),bg="grey")
pts_player1_set1.set(0)
label2.grid(row=0,column=2)

pts_player1_set2 = IntVar()
label3 = Label( fenetre, textvariable=pts_player1_set2,font=(default,100),bg="grey")
pts_player1_set2.set(0)
label3.grid(row=0,column=3)

pts_player1_set3 = IntVar()
label4 = Label( fenetre, textvariable=pts_player1_set3,font=(default,100),bg="grey")
pts_player1_set3.set(0)
label4.grid(row=0,column=4)


nom_player2 = StringVar()
label21 = Label( fenetre, textvariable=nom_player2,font=(default,100),bg="grey14")
nom_player2.set("Player 2")
label21.grid(row=1,column=1)

pts_player2_set1 = IntVar()
label22 = Label( fenetre, textvariable=pts_player2_set1,font=(default,100),bg="grey")
pts_player2_set1.set(0)
label22.grid(row=1,column=2)

pts_player2_set2 = IntVar()
label23 = Label( fenetre, textvariable=pts_player2_set2,font=(default,100),bg="grey")
pts_player2_set2.set(0)
label23.grid(row=1,column=3)

pts_player2_set3 = IntVar()
label24 = Label( fenetre, textvariable=pts_player2_set3,font=(default,100),bg="grey")
pts_player2_set3.set(0)
label24.grid(row=1,column=4)

def plusPlayer1():
    global pts_player2_set2
    global pts_player2_set1
    global pts_player2_set3
    global pts_player1_set3
    global pts_player1_set2
    global pts_player1_set1
    global p1_win
    if verif_set1()==True:
        if verif_set2()==True:
            if verif_set3()==False:
                pts_player1_set3.set(pts_player1_set3.get()+1)
            if verif_set3()==True:
                label4 = Label( fenetre, textvariable=pts_player1_set3,font=(default,100),bg="green")
                label4.grid(row=0,column=4)
                label24 = Label( fenetre, textvariable=pts_player2_set3,font=(default,100),bg="red")
                label24.grid(row=1,column=4)
                showinfo("Terminé", "Le match est terminé.\nFermer cet onglet pour terminer le programme")
                fenetre.destroy()
                return
        else:
            pts_player1_set2.set(pts_player1_set2.get()+1)
            if verif_set2()==True:
                p1_win+=1
                label3 = Label( fenetre, textvariable=pts_player1_set2,font=(default,100),bg="green")
                label3.grid(row=0,column=3)
                label23 = Label( fenetre, textvariable=pts_player2_set2,font=(default,100),bg="red")
                label23.grid(row=1,column=3)
                if verif_match()==True:
                    showinfo("Terminé", "Le match est terminé.\nFermer cet onglet pour terminer le programme")
                    fenetre.destroy()
                return
    else:
        pts_player1_set1.set(pts_player1_set1.get()+1)
        if verif_set1()==True:
                p1_win=1
                label2 = Label( fenetre, textvariable=pts_player1_set1,font=(default,100),bg="green")
                label2.grid(row=0,column=2)
                label22 = Label( fenetre, textvariable=pts_player2_set1,font=(default,100),bg="red")
                label22.grid(row=1,column=2)
                return

def plusPlayer2():
    global pts_player2_set2
    global pts_player2_set1
    global pts_player2_set3
    global pts_player1_set3
    global pts_player1_set2
    global pts_player1_set1
    global p2_win
    if verif_set1()==True:
        if verif_set2()==True:
            if verif_set3()==False:
                pts_player2_set3.set(pts_player2_set3.get()+1)
            if verif_set3()==True:
                label24 = Label( fenetre, textvariable=pts_player2_set3,font=(default,100),bg="green")
                label24.grid(row=1,column=4)
                label4 = Label( fenetre, textvariable=pts_player1_set3,font=(default,100),bg="red")
                label4.grid(row=0,column=4)
                showinfo("Terminé", "Le match est terminé.\nFermer cet onglet pour terminer le programme")
                fenetre.destroy()
                return
        else:
            pts_player2_set2.set(pts_player2_set2.get()+1)
            if verif_set2()==True:
                p2_win+=1
                label23 = Label( fenetre, textvariable=pts_player2_set2,font=(default,100),bg="green")
                label23.grid(row=1,column=3)
                label3 = Label( fenetre, textvariable=pts_player1_set2,font=(default,100),bg="red")
                label3.grid(row=0,column=3)
                if verif_match()==True:
                    showinfo("Terminé", "Le match est terminé")
                    fenetre.destroy()
                return
    else:
        pts_player2_set1.set(pts_player2_set1.get()+1)
        if verif_set1()==True:
                p2_win=1
                label22 = Label( fenetre, textvariable=pts_player2_set1,font=(default,100),bg="green")
                label22.grid(row=1,column=2)
                label2 = Label( fenetre, textvariable=pts_player1_set1,font=(default,100),bg="red")
                label2.grid(row=0,column=2)
                return
        
        



bouton = Button(fenetre, text="Player 1", command=plusPlayer1,bg="green")
bouton.grid(row=0,column=5)

bouton2 = Button(fenetre, text="Player 2", command=plusPlayer2,bg="green")
bouton2.grid(row=1,column=5)


fenetre.mainloop()