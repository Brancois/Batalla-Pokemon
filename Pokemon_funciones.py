import random

PS_jugador = 100  
PS_oponente = 100
defensa_oponente = 100
defensa_jugador = 100

def ataques_del_jugador(tipo_de_ataque):             #Funcion que define los ataques
        PS_oponente = 100
        defensa_oponente = 100
        
        if tipo_de_ataque == "malicioso":
            defensa_oponente -10
        
        elif tipo_de_ataque == "placaje":
            (PS_oponente-35)/(defensa_oponente/100)
        
        elif tipo_de_ataque == "ascuas":
            PS_oponente -20
            
        else:
            print("Que estas haciendo? Tus ataques son malicioso, placaje y ascuas")



while PS_jugador > 0 and PS_oponente > 0:
        
    ataque = input("ataque: ")
    ataques_del_jugador(ataque)


    if defensa_oponente <= 0:  #Esto es para evitar de que al restarle a la defensa, quede un numero negativo, y que la division sea negativa
        defensa_oponente = 1



#Turno del oponente
    ataque_oponente = random.randrange(1,3+1)
    if ataque_oponente == 1: #Latigo
        defensa_jugador -= 10

    if defensa_jugador <= 0:
        defensa_jugador = 1

    elif ataque_oponente == 2: #placaje
        PS_jugador -= 35 * (100/defensa_jugador)

    elif ataque_oponente == 3: #pistola de agua
        PS_jugador -= 40  

#Si termina el ciclo, alguien ha ganado
    if PS_oponente <= 0 and PS_jugador <=0:
        print("Empate")

    elif PS_oponente <= 0: 
        print ("Felicidades, has ganado")

    else:  #Ya sabemos que el oponente es > 0
        print("Lo siento, has perdido")