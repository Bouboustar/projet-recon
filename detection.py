#Detection

 # import 
import cv2
import sys


# Programme

def detection(video_capture):
    i = 0
    cascPath = r'./opencv-xml/haarcascade_frontalface_default.xml'
    faceCascade = cv2.CascadeClassifier(cascPath)

    #video_capture = cv2.VideoCapture(0)

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
        
# ajout d'un rectangle pour encadré le visage
        for (x, y, w, h) in faces:

            #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            r = max(w, h) / 2 
            centerx = x + w / 2
            centery = y + h / 2
            nx = int(centerx - r)
            ny = int(centery - r)
            nr = int(r * 2) + 10

            faceimg = frame[ny-10:ny+nr, nx-10:nx+nr]
            lastimg = cv2.resize(faceimg, (128, 128))
          
            
        cv2.imshow("Frame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Arret de la capture
    return lastimg
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detection()