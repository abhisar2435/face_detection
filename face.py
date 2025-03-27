import cv2
face_cap=cv2.CascadeClassifier(r"C:\Users\tushr\AppData\Local\Programs\Python\Python313\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
 # for default path of face points like eyes, nose, mouth etc.
video_cap=cv2.VideoCapture(0)  # 0 for default camera  #cv2.VideoCapture(1) for camera enabling
while True:
    ret,video_data=video_cap.read() # to read the video data
    col=cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    faces=face_cap.detectMultiScale(   #to detect face in the video
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for(x,y,w,h) in faces:
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2) # to draw rectangle around the face
    cv2.imshow("live_video",video_data) 
    if cv2.waitKey(1)==ord("a"): # to stop the video press "a"
        break 
video_cap.release()# to release the camera
cv2.destroyAllWindows()# to close the window
