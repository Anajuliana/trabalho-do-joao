from threading import Thread

def aluno(nota,nome):
    nota >= 2
    while nota >= 2:
        print("Aluno ",nota)
        time.sleep(0.20)

aluno1 = Thread(target=aluno,args=[7,"Ana"])
aluno2 = Thread(target=aluno,args=[7,"Vinicius"])


aluno1.start()
aluno2.start()

