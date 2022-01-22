import numpy as np
import cv2
from PIL import Image
import sys
#import keyboard
import time
import  queue, threading
from multiprocessing import Process, Manager
from register import registeration
from face_recognition import face_recognition
from lock import choose_mode



def capture(val,detect):
    # file_path = sys.argv[1]
    pic_num = 10
    myrtmp_addr = "rtmp://192.168.30.247/rtmp/live"

    cap = cv2.VideoCapture(myrtmp_addr)
    print('Connected')
    skip_time = 0.3
    frame_cycle = int(skip_time * 30)
    
    while(True):
        
        ret, frame = cap.read()
        access = False
        count = 0
        if val.value :
            skip = 0
            while(count<pic_num):
                ret, frame = cap.read()
                if (skip%frame_cycle == 0):
                    frame = frame[:,:,::-1]
                    new_image = Image.fromarray(frame)
                    img_path = 'picture/img' + str(count) + '.jpg'
                    new_image.save(img_path)

                    print('Finish picture ', count)
                    count += 1 
                skip += 1
            print("Finish taking picture")
            detect.value = True
            """
            if detect.value:
                print('Detecting')
                access = face_recognition()
                print('face recognition return',access)
            else:
                print('Registering')
                registeration()
            """
        val.value = False


if __name__ == '__main__':
    # shared value flag
    manager = Manager()
    go_flag = manager.Value('flag', False)
    manager2 = Manager()
    detect = manager2.Value('flag',False)
    # other process that is printing
    Process(target=capture, args=(go_flag,detect,)).start()
    manager3 = Manager()
    lock = manager3.Value('flag',False)
    Process(target = choose_mode,args = (lock,)).start()

    # normal main thread; toggle on and off the other process
    while True:
        text = input('Command:')
        if text == 'd':
            go_flag.value = True
            while detect.value == False:
                1
            print("Detecting")
            access = face_recognition()
            print("Face recognition returns", access)
            detect.value = False
            if access == 'ACCESS':
                lock.value = True
            print("Finish Detection")
        elif text == 'r':
            go_flag.value = True
            while detect.value == False:
                1
            print("Detecting")
            registeration()
            detect.value = False
            print("Finish Recognition")
        elif text == 'q':

            break
        else:
            print('Wrong command')

        print('capture value', go_flag.value)
                
