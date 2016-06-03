import numpy as np
import cv2
from matplotlib import pyplot as plt
cap=cv2.VideoCapture(0)

ret, frame0=cap.read()
sum=frame0
while(1):
	ret, frame=cap.read()
	#sum=cv2.add(frame0,frame)
	sum=cv2.addWeighted(frame0,0.9,frame,0.1,0)
	#frame0=sum
		 
	cv2.imshow('frame',frame)

	cv2.imshow('sum',sum)
	if cv2.waitKey(1) & 0xFF == ord('p'):
		break
	
cap.release() 
cv2.destroyAllWindows()
	
