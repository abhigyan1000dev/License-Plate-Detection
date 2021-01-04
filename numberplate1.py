import cv2
import imutils
import  pytesseract

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Now to read the image
image=cv2.imread('Car2.jpg')

image=imutils.resize(image,width=500)
cv2.imshow("Orignal Image",image)   
cv2.waitKey(0)   



#  We will now convert it to Grayscale , there are many algorithm such as haar ,
# cnn, canny which work only in Grayscale feature as well as it reduces the complexity .
grayscaled_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Converted Image",grayscaled_image)
cv2.waitKey(0)  

#  Now Make the  image Smooth By using func bilateralFilter
grayscaled_image=cv2.bilateralFilter(grayscaled_image,11,17,17)
cv2.imshow("Smoothness Wli image",grayscaled_image)
cv2.waitKey(0)


#  Now find Edges of the Images 
edge=cv2.Canny(grayscaled_image,170,200)
cv2.imshow("Edges Wli image",edge)
cv2.waitKey(0)

#  NOw will find the contour
cnts,new=cv2.findContours(edge.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
# Retr list retrieves all the contours
# Chain approx simple  :- Removes all reduntant points and compresses the contour

 
image1=image.copy()
cv2.drawContours(image1,cnts,-1,(0,255,0),3)
cv2.imshow("After Contouring the Image GREEN ",image1)
cv2.waitKey(0)  

# Now we don't want the All grreen green area i.e contours so what we do is se
# select the top 30 areas  but it gives a sorted list as in order of min to maximum
# Reverse the order of sorting
cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:30]
Numberplatecount=None
#  as we dont have any contour now as we havnt selected the Top 30 contours
#   Draw the top 30 contours


#  make a copy o the original image
image2=image.copy()
cv2.drawContours(image2,cnts,-1,(0,255,0),3)
cv2.imshow("After  Top 30 Contouring the Image GREEN ",image2)
cv2.waitKey(0)

count=0
name=1

for i in cnts: 
    perimeter=cv2.arcLength(i,True)
    # arcfunction  is used to find the perimeter in pyhton directly
    approx=cv2.approxPolyDP(i,0.02*perimeter,True)
    # approxPolydp is used as it calcuates the curve fo a polygon with 
    # precision
    
    # Now WE HAVE TO SELECT THOSE FIGURES IN IMAGE
    # WHICH HAVE A BOUNDARY I.E 4 SIDE ENCLOSED I.E NUMBER PLATE
    if(len(approx)==4): 
        #  4 I.e 4 sided enclosed 
        Numberplatecount=approx
        x,y,w,h=cv2.boundingRect(i)
        crp_img=image[y:y+h,x:x+w]
        #  Y axis + height
        #  X axis + width
         # THIS PART CROPS THE IMAGE
        cv2.imwrite(str(name)+'.jpg',crp_img)
        name+=1
        
        
        break
    
    
# Now draw final contour in our image (main) in which we have identified number plate
cv2.drawContours(image,[Numberplatecount],-1,(0,255,0),3)
cv2.imshow("Final NO Plate",image)
cv2.waitKey(0)
        

#   Now We Will Crop that image
crp_image_plate='1.jpg'
cv2.imshow("Cropped Plate",cv2.imread(crp_image_plate))
cv2.waitKey(0)

#  Now It's time to use the terseeract Libarray
text=pytesseract.image_to_string(crp_image_plate,lang='eng',config='--psm 6')
print("THE OBTAINED NUMBER PLATE IS : ",text)
cv2.waitKey(0)
