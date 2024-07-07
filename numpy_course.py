import numpy as np
from PIL import Image
from random import randint

# Creat 800pixel/800pixel array with RGB

first_ran = randint(0 , 1)
second_ran = randint(0 , 1)

Gris = (96 , 96 , 96)
yellow = (255 , 255 , 51)


if first_ran == second_ran == 1 :
    first_co = yellow 
    second_co = yellow
    Back_Ground = (0 , 204 , 204)
elif first_ran == 1 or second_ran == 1 :
    if first_ran == 1 :
       first_co = yellow 
       second_co = Gris
    else : 
        first_co = Gris
        second_co = yellow

    Back_Ground = (0 , 102 , 102)
else : 
     Back_Ground = (0 , 25 , 51)
     first_co = Gris
     second_co = Gris


file = open("image.png" , "w")
file.close()





T = 800
R = 800

image = np.zeros((800 , 800 , 3) , dtype = np.uint8)

image[: , :] = Back_Ground


#Supports
image[:int(T*0.4) , int(R*0.25):int(R*0.285)] = Gris

image[:int(T*0.4) , int(R*0.75):int(R*0.785)] = Gris

#lamps

image[int(T*0.4):int(T*0.55) , int(R*0.17):int(R*0.350)] = first_co

image[int(T*0.4):int(T*0.55) , int(R*0.67):int(R*0.850)] = second_co
location = input("the file where u will store the image (png/jpj extensio : ")
Image.fromarray(image).save(location)
