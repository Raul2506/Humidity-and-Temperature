#Se importa bibliotecile necesare in realizarea programului. "serial" pentru importarea datelor de la Arduino si "matplotlib.pyplot" pentru desenarea graficelor.
import serial
import matplotlib.pyplot as plot
from drawnow import *

#Se declara 3 variabile de tip vector pentru starile celor 3 culori din led-ul RGB:
#"L1" pentru culoarea rosu;
#"L2" pentru culoarea verde;
#"L3" pentru culoarea albastru.
L1=[]
L2=[]
L3=[]
#Se declara 2 variabile de tip vector pentru temperatura si pentru umiditate.
temp =[]
hum =[]

#Se initializeaza o conexiune cu port-ul serial unde este conectat Arduino.
serialArduino = serial.Serial('com10',9600)

#Functie care are ca scop construirea graficului cu datele parsate.
def plotValues():
    plt.title('Grafic senzor DHT11')
    plt.grid(True)
    plt.ylabel('Valoare')
    plt.plot(temp, 'ro-', label='Senzor temperatura='+tempRead+'L1='+L1+' L2='+L2+'L3='+L3,color = 'red')
    plt.plot(hum, 'bo-',label='Senzor humiditate='+humRead+'L1='+L1+' L2='+L2+'L3='+L3,color = 'blue')
    plt.legend(loc ='upper left')
    plt.xlabel('Timp')
    plt.ylabel('Temperatura si Umiditatea')

#Instructiune folosita pentru 
for i in range(0,40):
    values.append(0)
 
while True:
    while (serialArduino.inWaiting()==0):
        pass
    tempRead ,humRead ,L1 ,L2 ,L3 = serialArduino.readline().decode('utf8').split(';')

    try:
        tempInFloat = float(tempRead)
        humInFloat = float(humRead)
        print(tempInFloat)
        print(humInFloat)
        if tempInFloat <= 150 and humInFloat <=150:
            if tempInFloat >=0 and humInFloat >=0:
                temp.append(tempInFloat)
                hum.append(humInFloat)
                temp.pop(0)
                hum.pop(0)
                drawnow(plotValues)
            else:
                print("Numar negativ")
        else:
            print("Valoarea venita de la Ardiuno este mai mare de 150")
    except ValueError:
        print("Valoarea nu poate fi parsata")
