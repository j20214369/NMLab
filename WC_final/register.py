from deepface import DeepFace
import os
from os.path import join
import cv2
import sys
from sys import exit
import glob
import time
from API import detect
from Person import Person
def registered_headers():
    os.system("clear")
    print("******************* Registering ************************")

def echo(string, padding=80,  for_input = False):
    padding = " " * (padding - len(string)) if padding else ""
    print(string + padding, end='\r')

def pass_registration(name, registered_name):
    if name in registered_name:
        time.sleep(1)
        registered_headers()
        print("The name you entered is registered, please enter other name")
        return False
    return True

def re_type(ans):

    if ans.capitalize()[0] == "N":
        return False
    elif ans.capitalize()[0] == "Y":
        return True
    else:
        return "Redo"
    
def verify(name, registered_name):

    goal = "Age"
    if registered_name is not None:
        goal = "User name"
    while (registered_name is not None) and (not pass_registration(name, registered_name)):
        return False

    while True:
        time.sleep(1)
        registered_headers()
        ans = re_type(input(f"{goal} is {name}, do you want to re-type the {goal.lower()} (Yes/No)? ")) 
        if ans == "Redo":
            continue
        elif ans:
            registered_headers()
            return False
        elif not ans:
            registered_headers()
            return True
        else:
            print("SHIT, it wents wrong !!")
            
def take_pic(img_path):
    pass
def detect_face(img_path):
    
    representation = detect(img_path)
    if 'error' in representation.keys() :
        if representation['error'] == "Face could not be detected. Please confirm that the picture is a face photo or consider to set enforce_detection param to False.":
            print("Could not detect face, pls take picture again !")
            
        else:
            print(representation['error'])
            
        return False, 0
    elif 'embedding' in representation.keys():
        return True, representation['idx']
def registeration():
    pic = sorted(glob.glob(join('picture', '*.jpg'))) # Should be a folder
    # Make sure face is detected by the camera !
    detect, path = detect_face(pic)
    print('path' , path)
    if not detect:
        #exit(0)
        return "NO Face Detected"
    pic = join('picture', f'img{path}.jpg')
    register_dir = "Auth"
    register_file = os.path.join(register_dir, "name_list.txt")
    user = Person()
    name_list = open(register_file)
    registered_name = []
    for r in name_list:
        registered_name.append(r.replace("\n", ""))

    registered_headers()
    echo("Hello sir, let's start registeration !")
    time.sleep(2.5)

# ****************************************************************
# Name
    registered_headers()
    name = input("Please type your name here : ")
    while not verify(name = name, registered_name=registered_name):
        name = input("Please type your name here : ")

    print(f"User name : {name}")
    time.sleep(2.5)
# ****************************************************************
# Age
    def is_int(value):
        try:
            int(value)
            return True
        except:
            return False
    def verify_age(age):

        while not is_int(age):
            time.sleep(1)
            registered_headers()
            print("Your input is not a valid age !")
            age = input("Please type your Age here : ")
        return age
    registered_headers()
    age = verify_age(input("Please type your Age here : "))
    verified = False
    while not verified:
        os.system("clear")
        print("******************* Registering ************************")
        ans = input(f"Your age is {age}, do you want to re-type your age (Yes/No)? ")
    # print(ans.capitalize()[0])
        if ans.capitalize()[0] == "N":
            verified = True
        elif ans.capitalize()[0] == "Y":
            os.system("clear")
            print("******************* Registering ************************")
            age = verify_age(input("Please type your Age here : "))
        
    registered_headers()
    print(f"User age : {age}")
    time.sleep(2.5)

# ****************************************************************
# take pictures here


    user.register(name=name, age=age, pic_path=pic)
    with open(register_file, "a") as f:
        f.writelines("\n")
        f.writelines(name)

    print("Successfully registered !!")

if __name__ == '__main__':
    registeration()  



