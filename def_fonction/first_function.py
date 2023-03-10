# import random
import sys

MIN = 0
MAX = 99

def demander_saisie_nombre(invite):
      
    while True:  
        
        saisie = input(invite + ": ")  
        
        try:  
            
            saisie = int(saisie)  
            
        except:  
            print("Seul les caractères [0-9] sont autorisés.", 
                  file=sys.stderr)  
        else:  
            
            return saisie 

def demander_saisie_nombre_borne(invite, minimum=MIN, 
                                 maximum=MAX):  
    
    invite = f"{invite} entre {minimum} et {maximum} inclus"
    
    while True: 
        
        saisie = demander_saisie_nombre(invite)  
        
        if minimum <= saisie <= maximum:  
            return saisie 
        
# nombre = random.randint(0,100)
minimum = maximum = 0
while True:
    minimum = demander_saisie_nombre("choisissez le minimum")
    maximum = demander_saisie_nombre("choisissez le maximum")
    if maximum > minimum:
        break

nombre = demander_saisie_nombre_borne("Saisissez le nombre à deviner", minimum, maximum)


while True:
    
    joueur = demander_saisie_nombre_borne(f"Saisissez un nombre", minimum, maximum)
    
    if nombre > joueur:
        print("plus grand")
        minimum = joueur + 1
    elif nombre < joueur:
        print("plus petit")
        maximum = joueur - 1
    else:
        print(f"\nbravo c'était bien {joueur}")
        break
