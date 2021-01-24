#Detection

 # import 
import cv2
import sys




# Programme
cascPath = r'./opencv-xml/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Arret de la capture
video_capture.release()
cv2.destroyAllWindows()