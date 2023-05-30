
def moto1(velocidade,nome):
    distancia = 0
    while distancia <= 500:
        print("Moto1:",nome,distancia)
        distancia += velocidade
        time.sleep(0.5)

def moto2(velocidade,nome):
    distancia = 0
    while distancia <= 500:
        print("Moto2:",nome,distancia)
        distancia += velocidade
        time.sleep(0.5)

moto1()
moto2()