from threading import Thread
import time


def moto(velocidade,nome):
    distancia = 0
    while distancia <= 500:
        print("Moto :",nome,distancia)
        distancia += velocidade
        time.sleep(0.5)



moto1 = Thread(target=moto,args=[1.1,"Matheus"])
moto2 = Thread(target=moto,args=[1.2,"Lucas"])


moto1.start()
moto2.start()