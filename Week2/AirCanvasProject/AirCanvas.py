import cv2
import numpy as np
import random
import torch
import copy

vid = cv2.VideoCapture(0)
temp = vid.read()[1].shape
img = np.zeros(temp, np.uint8)
size = 20
color = (0, 0, 255)
bar = temp[0] - 60
seg = bar/6


model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

def changeSize(i):
    global size
    if((size > 10 and i < 0) or (size < 50 and i > 0)):
        size = size + i

def drawCircle(x, y):
    global color
    cv2.circle(img, (x,y), size, color, -1)

def changeMode(x):
    mode = x
    
while(True):
    ret, frame = vid.read()
    frame = cv2.flip(frame, 1)
    results = model(frame)
    output = results.pandas().xyxy[0]
    if(output.shape[0] == 1):
        #cv2.rectangle(frame, (int(output.xmin), int(output.ymin)),(int(output.xmax), int(output.ymax)), color, 4)
        #cv2.putText(frame, str(output.name[0]), (int(output.xmin), int(output.ymin)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2, cv2.LINE_AA)

        x = int((output.xmin + output.xmax)/2)
        y = int((output.ymin + output.ymax)/2)
        match(str(output.name[0])):
            case 'thumbsUp':
                changeSize(1)
                cv2.putText(frame, str(size), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0), 1, cv2.LINE_AA)
            case 'thumbsDown':
                changeSize(-1)
                cv2.putText(frame, str(size), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0), 1, cv2.LINE_AA)
            case 'palm':
                color = (0,0,0)
                cv2.putText(frame, 'Erase', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0), 1, cv2.LINE_AA)
            case 'fist':
                if(0 < x and x < 100):
                    z = y-40
                    if(z < 0 or z > bar):
                        color = (255,255,255)
                    else:
                        per = z%seg * 1.0/seg
                        match(int(z/seg)):
                            case 0:
                                color = (0, int(per * 255), 255)
                            case 1:
                                color = (0, 255, int((1-per) * 255))
                            case 2:
                                color = (int(per * 255), 255, 0)
                            case 3:
                                color = (255, int((1-per) * 255), 0)
                            case 4:
                                color = (255, 0, int(per * 255))
                            case 5:
                                color = (int((1-per) * 255), 0, 255)
                cv2.putText(frame, str(color), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1, cv2.LINE_AA)
            case 'point':
                drawCircle(int(output.xmin), int(output.ymin))
    result = cv2.addWeighted(frame, 1, img, 1, 0)
    cv2.imshow('Webcam', result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
