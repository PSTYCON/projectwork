import cv2
import time
from sys import platform



if platform == "linux" or platform == "linux2":
    print("Linux Os spotted")
elif platform == "darwin":
    print("Mac Os spotted")
elif platform == "win32":
    print("Windows spotted")

time.sleep(5)
#img = cv2.imread('test.png')
img = cv2.imread('test.jpg')
gs = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gs_plus = img.astype(int) + 100
gs_plus[gs_plus>255] = 255
gs_plus = gs_plus.astype('uint8')

gs_cont = img.astype(int) * 2
gs_cont[gs_cont>255] = 255
gs_cont = gs_cont.astype('uint8')

th_val = 60
ret1,threshold = cv2.threshold(gs,th_val,255,cv2.THRESH_BINARY)

th_range_1 = 100
th_range_2 = 200
inrange_th = cv2.inRange(gs, th_range_1, th_range_2)

#noise = cv2.randn(img,)

# SHOWING IMAGE ALGORITHMS ---------------------------------------------------------------------- START
#Resize settings
resize = True
rheight = 600
rwidth = 800

#Show Image List
show_imagename = [ 'Enhanced', ]
show_image = [ gs_cont]
              
n_showimg = len(show_image)
#Image Showing Sequencing
for k in range (0,n_showimg):
    if resize == False:
        cv2.namedWindow(show_imagename[k],cv2.WINDOW_NORMAL)    
        cv2.resizeWindow(show_imagename[k],rwidth,rheight)    
    cv2.imshow(show_imagename[k],show_image[k])

# SHOWING IMAGE ALGORITHMS---------------------------------------------------------------------------------- END
cv2.waitKey(0)
#cv2.destroyAllWindows()
