import cv2


face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
def detector(gray_image, frame):
    faces = face_classifier.detectMultiScale(gray_image, 1.3, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 3)
        
        roi_gray = gray_image[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        eyes = eye_classifier.detectMultiScale(roi_gray, 1.3, 5)
        
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 3)
            
    return frame
video_cap = cv2.VideoCapture('How To Flirt Using Your Eyes.mp4')

while True:
    
    ret, frame = video_cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    detect = detector(gray_frame, frame)
    
    cv2.imshow("Video", detect)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        
video_cap.release()
cv2.destroyAllWindows()