import qrcode
import numpy as np 
import cv2 

def generateQR(data): 
	img = qrcode.make(data)

	# To numpy array. 
	return np.uint8(np.asarray(img)) * 255 

if __name__ == '__main__':
	img = generateQR("1")
	cv2.imshow("img", img) 
	cv2.waitKey(0) 
	cv2.destroyAllWindows() 
