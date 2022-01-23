# NMLab
## Introduction
First of all, users have to register for our service. We’ll take a picture of the user and ask them to key-in their personal info. 
After registeration, our system can recognize the identity of users and unlock the lock for registered users.
We choose a centralized-based structure to implement our system. Since the power and ability of edge device is limited, computation can’t be performed locally. Instead, we have to leave heavy job to the server. 

## Required utensils
Jetson nano, camera(for nano), moter mg90s, a computer for server and real-time screen

## Connect to server
Download WC_server on your laptop or a device rather than Nano
In the WC_server directory, use the command
```bash
$ python3 api/api.py
```

## main process
Download WC_final on your  Nano
In the WC_final directory, use the command
```bash
$ python main_stream.py 
```
to turn on the camera and streaming service. 
Turn on another terminal and use the command
```bash
$ python3 interface.py
```
(Note: you have to connect the lock to Nano)

First, we can register by using the command r, and then type the name and age to create a new user.
Second, we use the command d to detect the face and check whether the face has been registered. If the identity is recognized, the lock will unlock, otherwise the lock will remain locking.
In the process of registration and detection, it will take 10 pictures to ensure the correctness and clearness. And we can watch the real-time screen through the screen of the computer.# NMLab
