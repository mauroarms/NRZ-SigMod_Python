import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def on_close(event):
    plt.close()

def modulacion(secBits, R, tipo):
    v = [int(s) for s in secBits]
    l = len(v)
    Di = []
    dim = 100 
    Vx = []

    for i in range(0,l):
        f = np.ones(dim)  
        x=f*v[i]       
        Vx=np.concatenate((Vx,x))

    plt.subplot(3, 2, ((1, 2)))
    dim2=len(Vx)
    t=np.linspace(0,l,dim2)
    t2=np.linspace(0,l/R,dim2)  
    plt.plot(t2,Vx, color="darkslateblue")
    plt.title("Secuencia: "+secBits+" Codificada en NRZ con un Baud-Rate de: "+str(R), pad=8, fontsize=13, color="white", backgroundcolor="darkslateblue")
    plt.ylabel("S. Moduladora ", fontsize=9, color="white", backgroundcolor="darkslateblue")

    if(tipo=="ask"):
        
        plt.subplot(3, 2, 3)
        x_values = np.linspace(0, l/R, 100)  
        y_values = np.zeros_like(x_values)
        plt.plot(x_values, y_values, label='y=0', color="indigo")
        plt.ylim(-1, 1)
        plt.ylabel("S. Portadora (0)", fontsize=9, color="white", backgroundcolor="indigo")

        plt.subplot(3, 2, 4)
        f1=2
        w1=2*np.pi*t*f1
        y1=np.sin(w1)
        plt.plot(t,y1, color="indigo")
        plt.ylabel("S. Portadora (1)", fontsize=9, color="white", backgroundcolor="indigo")


        plt.subplot(3, 2, ((5, 6)))
        mult=Vx*y1
        plt.plot(t/R,mult, color="midnightblue")
        plt.ylabel("S. Modulada (ASK)", fontsize=9, color="white", backgroundcolor="midnightblue")  

    elif(tipo=="fsk"):
        
        plt.subplot(3, 2, 3)
        f1=2
        w1=2*np.pi*t*f1
        y1=np.sin(w1)
        plt.plot(t,y1, color="indigo")
        plt.ylabel("S. Portadora (0)", fontsize=9, color="white", backgroundcolor="indigo")

        plt.subplot(3, 2, 4)
        f2=4
        w2=2*np.pi*t*f2
        y2=np.sin(w2)
        plt.plot(t,y2, color="indigo")
        plt.ylabel("S. Portadora (1)", fontsize=9, color="white", backgroundcolor="indigo")

        plt.subplot(3, 2, ((5, 6)))
        Di = []
        for i in range (0,dim2):  
            if(Vx[i]==0):
                cero=np.array([y1[i]])
                Di=np.concatenate((Di,cero))
            else:
                uno=np.array([y2[i]])
                Di=np.concatenate((Di,uno))
        plt.plot(t/R,Di,color="midnightblue")
        plt.ylabel("S. Modulada (FSK)", fontsize=9, color="white", backgroundcolor="midnightblue")

    elif(tipo=="psk"):
        
        plt.subplot(3, 2, 3)
        f1=2
        w1=2*np.pi*f1*t
        y1=np.sin(w1)
        plt.plot(t,y1,color="indigo")
        plt.ylabel("S. Portadora (0)", fontsize=9, color="white", backgroundcolor="indigo")

        plt.subplot(3, 2, 4)
        w2=-2*np.pi*f1*t
        y2=np.sin(w2)
        plt.plot(t,y2,color="indigo")
        plt.ylabel("S. Portadora (1)", fontsize=9, color="white", backgroundcolor="indigo")

        plt.subplot(3, 2, ((5, 6)))
        res=((y2*Vx)-(y1*Vx)+(y1))
        plt.plot(t/R,res, color="midnightblue")
        plt.ylabel("S. Modulada (PSK)", fontsize=9, color="white", backgroundcolor="midnightblue")

    plt.tight_layout()
    ax_button = plt.axes([0.95, 0.01, 0.04, 0.04])  
    button = Button(ax_button, 'Volver')
    button.on_clicked(on_close)  


    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    plt.show()