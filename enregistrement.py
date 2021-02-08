import cv2 
import os 
import sys

def enregistrement(face,nom):
    cv2.imwrite("./img/"+nom+".jpg", face)

if __name__ == '__main__':
    enregistrement()