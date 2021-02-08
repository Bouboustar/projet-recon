#!/usr/bin/env python3

#Imports
from detection import detection
from enregistrement import enregistrement
import cv2


#Main program
def main():
    
    choix = int(input("Choissisez 1. Pour l'enregistrement 2. Pour la reconnaissance du visage : "))
    
    if choix == 1 :
        print("Bienvenue dans le mode enregistrement")
        video_capture = cv2.VideoCapture(0)
        
        # appel de la fonction detection avec retour de l'image detecté
        face = detection(video_capture)
        #mise en forme de l'image 
        nom = input("Nom de la personne : ")
        face = enregistrement(face,nom)
        #enregistrement de l'image
        #
        

    elif choix == 2 :
        print("Bienvenue dans le mode reconnaissance")
        
        # appel de la fonction detection avec retour de l'image detecté
        #face = detection()
        #mise en forme de l'image 
        #face = format(face)
        #comparaison avec la base de donnée
        
        
        
        
   
        
        
        
        
        
        
        
    elif choix != 1 and choix != 2: 
        choix = int(input("Choissisez 1. Pour l'enregistrement 2. Pour la reconnaissance du visage : "))
        
        
if __name__ == "__main__":
    main()
