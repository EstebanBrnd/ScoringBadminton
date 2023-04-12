from email.policy import default
from tkinter import *
from ttkthemes import ThemedStyle
from tkinter.messagebox import *
from tkinter import ttk

fenetre3 = Tk()
fenetre3.geometry("300x105")
fenetre3.title("Live Scoring by Esteban")
fenetre3.configure(bg="grey14")
style =ThemedStyle(fenetre3)
style.set_theme('equilux')

nom1=StringVar()
n1= Entry(fenetre3, textvariable=nom1,font=(default,20),bg="grey14",fg="white")
n1.pack()
nom2=StringVar()
n2= Entry(fenetre3, textvariable=nom2,font=(default,20),bg="grey14",fg="white")
n2.pack()
Button(fenetre3, text="Commencer", command=fenetre3.destroy,bg="grey14").pack()
fenetre3.mainloop()

p1_win=0
p2_win=0

fenetre2 = None
fenetre = Tk()
fenetre.geometry("1120x280")
fenetre.configure(bg="grey14")
style =ThemedStyle(fenetre)
style.set_theme('equilux') 

points = [[IntVar(),IntVar(),-1],[IntVar(),IntVar(),-1],[IntVar(),IntVar(),-1]] # 3 sets : pts J1 / pts J2 / gagnant (0 ou 1 ou -1 si pas encore de gagnant)

actions = []
current_set = 0

def verif_match():
    global p1_win
    global p2_win
    if p1_win==2 or p2_win==2:
        return True
    return False

def verif_set1():
    pts1=points[0][0].get()
    pts2=points[0][1].get()
    if (pts1>=21 and pts1-pts2>=2) or (pts2>=21 and pts2-pts1>=2) or (pts1==30 or pts2==30):
        return True
    return False

def verif_set2():
    pts1=points[1][0].get()
    pts2=points[1][1].get()
    if (pts1>=21 and pts1-pts2>=2) or (pts2>=21 and pts2-pts1>=2) or (pts1==30 or pts2==30):
        return True
    return False

def verif_set3():
    pts1=points[2][0].get()
    pts2=points[2][1].get()
    if (pts1>=21 and pts1-pts2>=2) or (pts2>=21 and pts2-pts1>=2) or (pts1==30 or pts2==30):
        return True
    return False


nom_player1 = StringVar()
label = Label( fenetre, textvariable=nom_player1,font=(default,100),bg="grey14")
nom_player1.set("Player 1")
label.grid(row=0,column=1)


label2 = Label( fenetre, textvariable=points[0][0],font=(default,100),bg="grey")
label2.grid(row=0,column=2)

label3 = Label( fenetre, textvariable=points[1][0],font=(default,100),bg="grey")
label3.grid(row=0,column=3)

label4 = Label( fenetre, textvariable=points[2][0],font=(default,100),bg="grey")
label4.grid(row=0,column=4)


nom_player2 = StringVar()
label21 = Label( fenetre, textvariable=nom_player2,font=(default,100),bg="grey14")
nom_player2.set("Player 2")
label21.grid(row=2,column=1)

label22 = Label( fenetre, textvariable=points[0][1],font=(default,100),bg="grey")
label22.grid(row=2,column=2)

label23 = Label( fenetre, textvariable=points[1][1],font=(default,100),bg="grey")
label23.grid(row=2,column=3)

label24 = Label( fenetre, textvariable=points[2][1],font=(default,100),bg="grey")
label24.grid(row=2,column=4)

def closeAll():
    global fenetre
    global fenetre2
    fenetre.destroy()
    fenetre2.destroy()

def match_end(vainqueur):
    global fenetre2
    fenetre2 = Tk()
    fenetre2.geometry("600x200")
    fenetre2.title("Live Scoring by Esteban")
    fenetre2.configure(bg="grey14")
    style =ThemedStyle(fenetre2)
    style.set_theme('equilux') 
    
    label = Label(fenetre2, text="Match terminé",font=(default,30),bg="grey14")
    label.pack()
    if vainqueur==0:
        label = Label(fenetre2,font=(default,20),bg="grey14",fg="white", text=f"{nom_player1.get()} a gagné le match {p1_win} sets à {p2_win} ( {points[0][0].get()} - {points[0][1].get()} ; {points[1][0].get()} - {points[1][1].get()} ; {points[2][0].get()} - {points[2][1].get()} )")
    else:
        label = Label(fenetre2,font=(default,20),bg="grey14",fg="white", text=f"{nom_player2.get()} a gagné le match {p2_win} sets à {p1_win} ( {points[0][1].get()} - {points[0][0].get()} ; {points[1][1].get()} - {points[1][0].get()} ; {points[2][1].get()} - {points[2][0].get()} )")
    label.pack()
    button = Button(fenetre2, text="Valider", command=closeAll)
    button.pack()
    button2 = Button(fenetre2, text="Rejouer le dernier point", command=annuleEnd)
    button2.pack()
    fenetre2.mainloop()

def annuleEnd():
    global fenetre2
    fenetre2.destroy()
    annule()
    

def plusPlayer1():
    global points
    global p1_win
    global p2_win
    global actions
    global current_set
    if p1_win==2 or p2_win==2:
        return
    actions.append("1")
    points[current_set][0].set(points[current_set][0].get()+1)
    if current_set==0:
        if verif_set1()==True:
            current_set+=1
            p1_win+=1
            label2 = Label( fenetre, textvariable=points[0][0],font=(default,100),bg="green")
            label2.grid(row=0,column=2)
            label22 = Label( fenetre, textvariable=points[0][1],font=(default,100),bg="red")
            label22.grid(row=2,column=2)
            points[0][2]=0
            return
    if current_set==1:
        if verif_set2()==True:
            current_set+=1
            p1_win+=1
            label3 = Label( fenetre, textvariable=points[1][0],font=(default,100),bg="green")
            label3.grid(row=0,column=3)
            label23 = Label( fenetre, textvariable=points[1][1],font=(default,100),bg="red")
            label23.grid(row=2,column=3)
            points[1][2]=0
        if verif_match()==True:
            fenetre.update()
            match_end(0)
        return
    if current_set==2:
        if verif_set3()==True:
            current_set+=1
            p1_win+=1
            label4 = Label( fenetre, textvariable=points[2][0],font=(default,100),bg="green")
            label4.grid(row=0,column=4)
            label24 = Label( fenetre, textvariable=points[2][1],font=(default,100),bg="red")
            label24.grid(row=2,column=4)
            points[2][2]=0
            fenetre.update()
            match_end(0)
            return



def plusPlayer2():
    global points
    global p2_win
    global p1_win
    global actions
    global current_set
    if p1_win==2 or p2_win==2:
        # Match terminé
        return
    actions.append("2")
    points[current_set][1].set(points[current_set][1].get()+1)
    if current_set==0:
        if verif_set1()==True:
            current_set+=1
            p2_win+=1
            label2 = Label( fenetre, textvariable=points[0][0],font=(default,100),bg="red")
            label2.grid(row=0,column=2)
            label22 = Label( fenetre, textvariable=points[0][1],font=(default,100),bg="green")
            label22.grid(row=2,column=2)
            points[0][2]=1
            return
    if current_set==1:
        if verif_set2()==True:
            current_set+=1
            p2_win+=1
            label3 = Label( fenetre, textvariable=points[1][0],font=(default,100),bg="red")
            label3.grid(row=0,column=3)
            label23 = Label( fenetre, textvariable=points[1][1],font=(default,100),bg="green")
            label23.grid(row=2,column=3)
            points[1][2]=1
        if verif_match()==True:
            fenetre.update()
            match_end(1)
        return
    if current_set==2:
        if verif_set3()==True:
            current_set+=1
            p2_win+=1
            label4 = Label( fenetre, textvariable=points[2][0],font=(default,100),bg="red")
            label4.grid(row=0,column=4)
            label24 = Label( fenetre, textvariable=points[2][1],font=(default,100),bg="green")
            label24.grid(row=2,column=4)
            points[2][2]=1
            fenetre.update()
            match_end(1)
            return

        
def annule():
    global current_set
    global p1_win
    global p2_win
    try:
        player = actions.pop()
    except:
        print("Pas d'action à annuler")
        return
    if player=="1":
        if points[current_set][0].get()==0:
            current_set-=1
            p1_win-=1
            points[current_set][0].set(points[current_set][0].get()-1)
            label = Label( fenetre, textvariable=points[current_set][0],font=(default,100),bg="grey")
            label.grid(row=0,column=current_set+2)
            label2 = Label( fenetre, textvariable=points[current_set][1],font=(default,100),bg="grey")
            label2.grid(row=2,column=current_set+2)
            return
        points[current_set][0].set(points[current_set][0].get()-1)  
    else:
        if points[current_set][1].get()==0:
            current_set-=1
            p2_win-=1
            points[current_set][1].set(points[current_set][1].get()-1)
            label = Label( fenetre, textvariable=points[current_set][0],font=(default,100),bg="grey")
            label.grid(row=0,column=current_set+2)
            label2 = Label( fenetre, textvariable=points[current_set][1],font=(default,100),bg="grey")
            label2.grid(row=2,column=current_set+2)
            return
        points[current_set][1].set(points[current_set][1].get()-1)



bouton = Button(fenetre, text="🏸", command=plusPlayer1,bg="green")
bouton.grid(row=0,column=5)

bouton3 = Button(fenetre, text="Annule", command=annule,bg="red")
bouton3.grid(row=1,column=5)

bouton2 = Button(fenetre, text="🏸", command=plusPlayer2,bg="green")
bouton2.grid(row=2,column=5)

ttk.Separator(
    master=fenetre,
    orient=HORIZONTAL,
    style='blue.TSeparator',
    class_= ttk.Separator,
    takefocus= 1,
    cursor='plus'    
).grid(row=1, column=1, ipadx=300, pady=10)


label = Label( fenetre, textvariable=nom_player1,font=(default,100),bg="grey14")
label21 = Label( fenetre, textvariable=nom_player2,font=(default,100),bg="grey14")
if nom1.get()!="":
    nom_player1.set(nom1.get())
else:
    nom_player1.set("Joueur 1")
if nom2.get()!="":
    nom_player2.set(nom2.get())
else:
    nom_player2.set("Joueur 2")
label.grid(row=0,column=1)
label21.grid(row=2,column=1)
fenetre.title(f"{nom_player1.get()} / {nom_player2.get()} - Live Scoring by Esteban")



fenetre.mainloop()

