#Imports



#Main program
def main():
    choix = int(input("Choissisez 1. Pour l'enregistrement 2. Pour la reconnaissance du visage"))
    if choix == 1 :
        print("Bienvenue dans le mode enregistrement")
    if choix == 2 :
        print("Bienvenue dans le mode reconnaissance")
    else : 
        choix = int(input("Choissisez 1. Pour l'enregistrement 2. Pour la reconnaissance du visage"))
if __name__ == "__main__":
    main()