import random

PS_jugador = 100  #PS es Puntos de Salud
PS_oponente = 100
defensa_oponente = 100
defensa_jugador = 100

while PS_jugador > 0 and PS_oponente > 0:
    
    ataques = {"malicioso": defensa_oponente -10, "placaje": (PS_oponente-35)/(defensa_oponente/100), "ascuas": PS_oponente -20}    #Este es el diccionario con los ataques del jugador

    ataque_jugador = input("ataque: ")            #El jugador indica que ataque quiere
    ataque_jugador = ataque_jugador.lower()       #Asegura que sea en minuscula
   
    if ataque_jugador == "malicioso":
        defensa_oponente = ataques["malicioso"]
        
        if defensa_oponente <= 0:  #Esto es para evitar de que al restarle a la defensa, quede un numero negativo, y que la division sea negativa
            defensa_oponente = 1
   
    elif ataque_jugador == "placaje":
        PS_oponente = ataques["placaje"]  
    
    elif ataque_jugador == "ascuas":
        PS_oponente = ataques["ascuas"]
   
    else:
        print("Que estas haciendo? Tus ataques son malicioso, placaje y ascuas")
        

        
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
    #randrange esta garantizado a ser 1, 2 o 3
    
#Si termina el ciclo, alguien ha ganado
if PS_oponente <= 0 and PS_jugador <=0:
    print("Empate")
    
elif PS_oponente <= 0: 
    print ("Felicidades, has ganado")
    
else:  #Ya sabemos que el oponente es > 0
    print("Lo siento, has perdido")