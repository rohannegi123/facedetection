import cv2

video = cv2.VideoCapture(0)

a = 1
while True:
    a = a +1
    check ,frame = video.read()
    print(frame)
    facecas = cv2.CascadeClassifier('D:\Face-detection\cascade.xml')
    faces = facecas.detectMultiScale(frame , scaleFactor=1.05 , minNeighbors=5)
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        name = 'rohan'
        cv2.putText(frame, name, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('capturing',frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows()
