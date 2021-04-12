import threading as thr
import tkinter as tk
import math as m
import time as t
import GraphicLib as GrL
import datetime

TermoPot0 = 5.58
TermoPot1 = 4.26
TermoPot2 = 9.42
#TermoPot3 = 1.16666666666
TermoPotSec0 = 0.00069444444
TermoPotSec1 = 0.00060185185
TermoPotSec2 = 0.00060185185
#TermoPotSec3 = 0.00032407407
TermoPotSec0 = TermoPot0 / 3600
TermoPotSec1 = TermoPot1 / 3600
TermoPotSec2 = TermoPot2 / 3600
#TermoPotSec3 = TermoPot3 / 3600
#GrL.buildGraph([10,50,40,30,0,20],"black", 200, 300, False)
def CC():
  global forfg, forbg
  tempo = forfg
  forfg = forbg
  forbg = tempo
  main.configure(bg=forbg)
  ishI.configure(fg=forbg,bg=forfg)
  komnI.configure(fg=forbg, bg=forfg)
  textO.configure(fg=forfg,bg=forbg)
  text1.configure(fg=forfg, bg=forbg)
  one.configure(fg=forfg, bg=forbg)
  two.configure(fg=forfg, bg=forbg)
  three.configure(fg=forfg, bg=forbg)
  st.configure(fg=forfg, bg=forbg)
  changeCol.configure(fg=forbg, bg=forfg)
  ishI.focus_set()
  print(forfg,forbg)
def thermo():
  ishl = ish
  komnl = komn
  TermopotTemp0 = ishl
  TermopotTemp1 = ishl
  TermopotTemp2 = ishl
  TermopotTemp3 = ishl

  TermopotTime0 = 0
  TermopotTime1 = 0
  TermopotTime2 = 0
  TermopotTime3 = 0
  t1 = thr.Thread(target=TPot, args=(komnl,ishl,"IKEA Беховд 1Л 399₽: ",TermoPotSec0,"green",one))
  t2 = thr.Thread(target=TPot, args=(komnl,ishl,"IKEA Ундерсока 0,4Л 649₽: ",TermoPotSec1,"blue",two))
  t3 = thr.Thread(target=TPot, args=(komnl,ishl,"Фикс Прайс 0,35Л 99₽: ",TermoPotSec2,'red',three))
  #t4 = thr.Thread(target=TPot, args=(komnl,ishl,"4:",TermoPotSec3,'green'))
  t1.run()
  t2.run()
  t3.run()
  #t4.run()

def TPot(komn, Temp, Named, OnSec, col, lab):
  #komn =10
  Time = 0
  df = []
  DI = 0
  Temp = Temp.get()
  komn = komn.get()
  while Temp > komn:
    Time += 10
    Temp -= OnSec * 10
    #print(Temp)
    #slider.set(Temp)
    #print(Time)
    DI += 1
    if DI % 1000 == 0:
      df.append(Temp*10)
  print(Named,Time,"Sec,", (Time/60)/2,"Min,",(((Time*1)/60)/60),"Hours")
  #print(Named,((Time)/60/60).__round__(2),(Time - (((Time)/60/60).__round__(0))*60*60))
  print(Named,datetime.timedelta(seconds=Time))
  lab.configure(text=(Named + str(datetime.timedelta(seconds=Time))))
  GrL.buildGraph(df, col, 300, 100, False, m.inf, 0.1)

forbg = "SystemButtonFace"
forfg = "gray19"
main = tk.Tk()
main.title("TermoPots3")
main.geometry("400x400")
main.resizable(0, 0)

komn = tk.IntVar()
ish = tk.IntVar()

st = tk.Button(main, text="Start", width = 20,command = thermo)
changeCol = tk.Button(main, text="☯", command=CC)
textO = tk.Label(main, text="Температура воды")
text1 = tk.Label(main, text="Темрература воздуха")
ishI = tk.Entry(main, bg=forfg, fg=forbg, textvariable = ish)
komnI = tk.Entry(main, bg=forfg, fg=forbg,textvariable = komn)
ishI.place(x=250,y=100)
komnI.place(x=250,y=120)
textO.place(x=100, y= 100)
text1.place(x=100, y= 120)
changeCol.place(x=370,y=370)
st.place(x=250,y=140)
one = tk.Label(main, text="")
two = tk.Label(main,text="")
three = tk.Label(main, text="")
#four = tk.Scale()
one.place(x=100, y= 200)
two.place(x=100, y= 220)
three.place(x=100, y= 240)
#four.place(x=220,y=200)
main.mainloop()

#print("Введите температуру")
#ish = int(input())
#print("Bведите комнатную температуру")
#komn = int(input())



print("Литр в термосе остывает за:")
#TPot(komn,ish,"1:", TermoPotSec0)
#TPot(komn,ish,"2:", TermoPotSec1)
#TPot(komn,ish,"3:", TermoPotSec2)
#TPot(komn,ish,"4:", TermoPotSec3)



'''while TermopotTemp0 > komn:
  TermopotTime0 = TermopotTime0 + 1
  TermopotTemp0 = TermopotTemp0 - TermoPotSec0 * 100
  #print(TermopotTemp0)
print("Термос 1, 1 Литр, Металл:",TermopotTime0 * 100,"Sec,", (TermopotTime0*100)/60,"Min,",((TermopotTime0*100)/60)/60,"Hours")


while TermopotTemp1 > komn:
  TermopotTime1 = TermopotTime1 + 1
  TermopotTemp1 = TermopotTemp1 - TermoPotSec1 * 100
  #print(TermopotTemp1)
print("Термос 2, 2 Литра, Металл",(TermopotTime1 * 100),"Sec,", ((TermopotTime1*100)/60)/2,"Min,",(((TermopotTime1*100)/60)/60),"Hours")


while TermopotTemp2 > komn:
  TermopotTime2 = TermopotTime2 + 1
  TermopotTemp2 = TermopotTemp2 - TermoPotSec2 * 100
  #print(TermopotTemp2)
print("Термос 3, 1 Литр, Стекло:",TermopotTime2 * 100,"Sec,", (TermopotTime2*100)/60,"Min,",((TermopotTime2*100)/60)/60,"Hours")'''

input("Нажмите Enter Для Закрытия")