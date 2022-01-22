import cv2
import argparse
import multiprocessing as mp
import os
from PIL import Image
import numpy as np
import time

def gstreamer_camera(queue):
    pipeline = (
        "nvarguscamerasrc ! "
            "video/x-raw(memory:NVMM), "
            "width=(int)1920, height=(int)1080, "
            "format=(string)NV12, framerate=(fraction)30/1 ! "
        "queue ! "
            "nvvidconv flip-method=2 ! "
                "video/x-raw, "
                "width=(int)1920, height=(int)1080, "
                "format=(string)BGRx, framerate=(fraction)30/1 ! "
            "videoconvert ! "
                "video/x-raw, format=(string)BGR ! "
            "appsink"
        )

    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
    count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        count += 1
        queue.put([frame,count])
        print("[CAM] READ",count)


def gstreamer_rtmpstream(queue):
    pipeline = (
        "appsrc ! "
            "video/x-raw, format=(string)BGR ! "
        "queue ! "
            "videoconvert ! "
                "video/x-raw, format=RGBA ! "
            "nvvidconv ! "
            "nvv4l2h264enc bitrate=8000000 ! "
            "h264parse ! "
            "flvmux ! "
            'rtmpsink location="rtmp://localhost/rtmp/live live=1"'
        )

    writer = cv2.VideoWriter(pipeline, cv2.CAP_GSTREAMER, 0, 30.0, (1920, 1080))
    while True:
        timelength = 9 #frame
        pic_num = 10
        #time.sleep(1)
        data = queue.get()
        if data is None:
            break
        frame = data[0]
        count = data[1]
        #print(frame, count)
        
        #if count % timelength == 0:
            
            #frame = data[0]
            #j = (count//timelength) % pic_num
            #s = 'picture/img' + str(j) + '.jpg'
            #frame2 = frame[:,:,::-1]            
            #new_image = Image.fromarray(frame2)
            #new_image.save(s)
            #print(s)

        #cv2.putText(frame,'TEST',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),1)
        writer.write(frame)
        print("[RTMP] WRITE", count)
        print(np.shape(frame))

if __name__ == "__main__":
    pic_num = 10
    for i in range(pic_num):
        s = 'picture/img' + str(i) + '.jpg'
        if os.path.exists(s):
            os.remove(s)
    queue = mp.Queue(maxsize=1)
    reader = mp.Process(target=gstreamer_camera, args=(queue,))
    reader.start()
    writer = mp.Process(target=gstreamer_rtmpstream, args=(queue,))
    writer.start()

    try:
        reader.join()
        writer.join()
    except KeyboardInterrupt as e:
        reader.terminate()
        writer.terminate()
