#Imports
 import detection.py


#Main program
def main():
    
    choix = int(input("Choissisez 1. Pour l'enregistrement 2. Pour la reconnaissance du visage : "))
    
    if choix == 1 :
        print("Bienvenue dans le mode enregistrement")
        
        # appel de la fonction detection avec retour de l'image detecté
        #face = detection()
        #mise en forme de l'image 
        #face = format(face)
        #enregistrement de l'image
        #
        

    elif choix == 2 :
        print("Bienvenue dans le mode reconnaissance")
        
        
        
        
        
        
   
        
        
        
        
        
        
        
    elif choix != 1 and choix != 2: 
        choix = int(input("Choissisez 1. Pour l'enregistrement 2. Pour la reconnaissance du visage : "))
        
        
if __name__ == "__main__":
    main()
