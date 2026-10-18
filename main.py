import datetime

def salutation():
    # Récupère l'heure actuelle
    heure = datetime.datetime.now().hour
    
    print("=========================================")
    print("   👋 BIENVENUE SUR MON PREMIER PROJET !   ")
    print("=========================================")
    
    if heure < 12:
        print("Bon matin ! Bravo d'apprendre à coder de bonne heure.")
    elif heure < 18:
        print("Bon après-midi ! Ce projet est maintenant sur GitHub.")
    else:
        print("Bonsoir ! Fin de journée productive sur Git.")
        
    print("\nFélicitations, votre environnement de script fonctionne correctement ! 🎉")
    print("=========================================")

if __name__ == "__main__":
    salutation()
