#importing the necessary packages
import cv2

#storing image
img_file = "cars.jpg"

#using the pre-trained algorithm to detect cars 
classifier_file = "cars.xml"

#reading the image.
img = cv2.imread(img_file)

#detetcing using the algorithm
car_tracker = cv2.CascadeClassifier(classifier_file)

#coverting the image into grayscale
gray_img  = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

#detecting the multiscale image
cars = car_tracker.detectMultiScale(gray_img)


#loop to detect if there are more than 1 number of cars 
for (x , y , w , h) in cars:
    cv2.rectangle(img , (x , y) , (x+w , y+h) , (0 , 0 , 255) ,2)


#to display the image with the detected square
cv2.imshow('car detector' , img)

#to display the image until it is closed by pressing any key or manually killing it.
cv2.waitKey()








print("code completed")
