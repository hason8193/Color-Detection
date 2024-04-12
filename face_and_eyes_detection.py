import os
import matplotlib.pyplot as plt
import cv2

data_dir = 'D:\Color_Detection\eyes-detector\data'
models_dir = 'D:\Color_Detection\eyes-detector\models'

face_detector = cv2.CascadeClassifier(os.path.join(models_dir,'haarcascade_frontalface_default.xml')) #take from opencv
eye_detector = cv2.CascadeClassifier(os.path.join(models_dir,'haarcascade_eye_tree_eyeglasses.xml')) #take from opencv

for img_path in os.listdir(data_dir):
    img = cv2.imread(os.path.join(data_dir,img_path))
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(img_gray,minNeighbors=20)
    plt.figure()
    for face in faces:
        x1,y1,w,h = face
        img = cv2.rectangle(img,(x1,y1),(x1+w,y1+h),(0,255,0),10)
        factor = 0.5
        face_ = img_gray[y1:y1+h,x1:x1+w]
        eyes = eye_detector.detectMultiScale(cv2.resize(face_,(int(w*factor),int(h*factor))))
        for eye in eyes:
            eye = [int(e/factor) for e in eye]
            x1e,y1e,we,he = eye
            cv2.rectangle(img,(x1+x1e,y1+y1e),(x1+x1e+we,y1+y1e+he),(0,255,0),10)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
plt.show()
