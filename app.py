import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = Image
os.chdir(path)
images = []
classNames = []

myList = os.listdir(path)
print("Files found:", myList)

for cl in myList:
    if cl.endswith(('.jpg', '.png', '.jpeg')):
        curImg = cv2.imread(os.path.join(path, cl))
        if curImg is not None:
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0].replace('_', ' '))

print("Class Names:", classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodes = face_recognition.face_encodings(img)
        if len(encodes) > 0:
            encodeList.append(encodes[0])
    return encodeList

encodeListKnown = findEncodings(images)
print("Encoding Complete")

def markAttendance(name):
    fileName = 'Attendance.csv'

    if not os.path.exists(fileName):
        with open(fileName, 'w') as f:
            f.write('Name,Time\n')

    with open(fileName, 'r+') as f:
        myDataList = f.readlines()
        nameList = [line.split(',')[0] for line in myDataList]

        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

cap = cv2.VideoCapture(0)

print("Press 'Q' to exit")

while True:
    success, img = cap.read()

    if not success:
        print("Failed to grab frame")
        break

    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex] and faceDis[matchIndex] < 0.5:
            name = classNames[matchIndex].upper()
            color = (0, 255, 0)
            markAttendance(name)
        else:
            name = "UNKNOWN"
            color = (0, 0, 255)

        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4

        cv2.rectangle(img, (x1,y1), (x2,y2), color, 2)
        cv2.rectangle(img, (x1,y2-35), (x2,y2), color, cv2.FILLED)
        cv2.putText(img, name, (x1+6,y2-6),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

    cv2.imshow('Face Attendance System', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
