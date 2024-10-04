import time
import psutil
import collections
import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
import os

#Functie afisare grafic cpu
def CPU():
    
    plt.clf
    plt.cla
    n = 100
    x = collections.deque(maxlen=n)
    y = collections.deque(maxlen=n)
    (line, ) = plt.plot(x, y, linestyle="-",color="darkblue")
    font2 = {'family':'serif','color':'darkred','size':15}
    plt.xlabel("Timp(s)",font2)
    plt.ylabel("CPU(%)",font2)
    plt.grid()
    cpu = psutil.Process(os.getpid())
    start = time.time()
    font1 = {'family':'serif','color':'blue','size':20}

    while True:
        x.append(time.time() - start)
        y.append(cpu.cpu_percent())
        plt.title( "{}%".format(y[-1]),font1)
        line.set_xdata(x)
        line.set_ydata(y)
        plt.gca().relim()
        plt.gca().autoscale_view()
        plt.pause(1)

#Functie afisare grafic ram
def RAM():
    
    plt.clf
    plt.cla
    n=100
    x=collections.deque(maxlen=n)
    y=collections.deque(maxlen=n)
    (line, )=plt.plot(x,y,linestyle="-",color="orangered")
    font2 = {'family':'serif','color':'darkorange','size':15}
    plt.grid()
    plt.xlabel("Timp(s)",font2)
    plt.ylabel("RAM(%)",font2)
    ram=psutil.virtual_memory()
    start=time.time()
    font1 = {'family':'serif','color':'darkorange','size':20}

    while True:
        x.append(time.time()- start)
        y.append(ram.percent)
        plt.title( "{}%".format(y[-1]),font1)
        line.set_xdata(x)
        line.set_ydata(y)
        plt.gca().relim()
        plt.gca().autoscale_view()
        plt.pause(1)  

#Functie afisare grafic disk
def DISK():
    
    plt.clf
    plt.cla
    disk=psutil.disk_usage("/")
    a=int(disk.used/(1024.0**3))
    b=int(disk.free/(1024.0**3))
    x=np.array(["Disk Free","Disk Used"],)
    y=np.array([b,a])
    plt.text(0.9,a,"{}GB".format(a))
    plt.text(-0.1,b,"{}GB".format(b))
    plt.title("Total {}GB".format(int(disk.total/(1024.0**3))))
    plt.ylim(0, int(disk.total/(1024.0**3)))
    plt.bar(x,y, color=['midnightblue', 'darkorange'])
    plt.clf
    plt.show()

#inchidere program

def inchidere():
    quit()

#fereastra grafica
   
fereastra=Tk()
fereastra.title("Resource Monitor")
fereastra.geometry("350x200")
mesaj=StringVar()
mesaj.set("RESOURCE MONITOR")
label=Label(fereastra, textvariable=mesaj, bd=3, font=20,anchor=CENTER,pady=4).pack()
b1= Button(fereastra, text = 'CPU', command = CPU,activebackground="lime", bd= 4,bg="peachpuff",width=20).pack() 
b2 = Button(fereastra, text = 'RAM', command = RAM,activebackground="darkred", bd=4,bg="peachpuff",width=20).pack() 
b3 = Button(fereastra, text = 'DISK', command = DISK,activebackground="darkblue", bd =4,bg="peachpuff",width=20).pack() 
b4 = Button(fereastra, text = 'EXIT', command = inchidere,activebackground="darkorange",bd=4,bg="peachpuff",width=20).pack() 
fereastra.mainloop()

#SURSE :https://stackoverflow.com/questions/11874767/how-do-i-plot-in-real-time-in-a-while-loop-using-matplotlib
#https://www.w3schools.com/python/matplotlib_bars.asp