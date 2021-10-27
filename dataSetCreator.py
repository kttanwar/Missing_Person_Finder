import cv2
import numpy as np
import sqlite3


def insertOrUpdate(Id,Name,Age,Gen):
    conn=sqlite3.connect("facerecognition.db")
    cmd="SELECT * FROM People WHERE ID = "+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        conn.execute("UPDATE People SET Name =? WHERE ID =?",(Name,Id))
        conn.execute("UPDATE People SET Age =? WHERE ID =?",(Age,Id))
        conn.execute("UPDATE People SET Gender =? WHERE ID =?",(Gen,Id))
       
    else:
        params= (Id, Name, Age, Gen)
        conn.execute("INSERT INTO People Values(?, ?, ?, ?)",params)
        cmd2=""
        cmd3=""
       
    
    
    conn.commit()
    conn.close()
def test(form_name, form_age, form_gen):
    
    faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    cam=cv2.VideoCapture(0);
    Id=input('Enter User Id ')
    # name=input('Enter User Name ')
    # age=input('Enter User Age ')
    # gen=input('Enter User Gender ')
    name = str(form_name)
    age = int(form_age)
    gen = form_gen
    
    

    insertOrUpdate(Id,name,age,gen)
    sampleNum=0
    while(True):
        ret,img=cam.read();
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5);
        for(x,y,w,h) in faces:
            sampleNum=sampleNum+1;
            cv2.imwrite("dataSet/User."+str(Id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.waitKey(50);
        cv2.imshow("Face",img);
        if(sampleNum>35):
            break;
    cam.release()
    cv2.destroyAllWindows()