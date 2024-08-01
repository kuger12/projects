import json as js
import random
from os import system as sys


while True : 
    os = input("are you windows or linux (w/l) : ")
    if os == "w" :
        command = 'cls'
        break
    elif os == "l" :
        command = "clear"
        break
    else : 
        print('your answer is not acceptable')

sys(command)



def open_json() :
    with open("frames.json" , "r") as f : 
        data =  js.load(f) 
    tracker = random.randint(0 , 2)
    for index , key in enumerate(data.keys()) :
       if index == tracker : 
          return data , key

def game(data , key) :

    list_ = data[key]
    word =  random.choice(list_)

    l_word = [*word]
    new_l = ["-"]*len(word)
    x = 0 
    while x != len(new_l)//2 :
        num = random.randint(0 , len(l_word)-1)
        if new_l[num] != l_word[num] :
            new_l[num] = l_word[num]
            x+=1

    print(f"{key} :")
    for letter in new_l :
       print(letter , end = '')
    print()
    x = 0
    i = 1

    for x in range(len(new_l)//3+1) :
        guess = input("guess : ")
        sys(command)
        print(f"{key} :")
        if l_word == [*guess] :
            print('True')
            break
        else :
            while x != i :
                num = random.randint(0 , len(l_word)-1)
                if new_l[num] != l_word[num] :
                    new_l[num] = l_word[num]
                    x+=1
            print("false")
            for letter in new_l :
                print(letter , end = '')
            print()
            i+=1
    else :
        print('u ran out of tries')
        print(f"right answer is : {word}")

data , key = open_json()
while True : 
    game(data , key)
    ans = input("do you want to retry(y/n)").lower()
    sys(command)
    if ans != 'y' :
      print("app shut down")
      quit()
    

                

