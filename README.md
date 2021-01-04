# License-Plate-Detection
This Project is made through the Open CV Library of the Python.

It involves the pytesseract for the conversion of the Image obtained to text.

Pytesseract :- Python-tesseract is an optical character recognition (OCR) tool for python.
That is, it will recognize and “read” the text embedded in images. Python-tesseract is a wrapper for Google's Tesseract-OCR Engine.

We Created contour around the image and then throughout the image we select the region ,having the
top (30 contours) and then selected the region which was bounded by the 4 sides throughout.

->
    This perimeter finding thing was done through the function called ArcLength() in python 
->

After finding the Cropped image of the Number Plate/License Plate,
At the end we used the Pytesseract module to get the text from the cropped image i.e Licensed Plate
and Finally print it through to the console.

Thankyou!

Abhigyan Sharma 
