import RPi.GPIO as GPIO
import time
import os
import random
from threading import Thread
import datetime

GPIO.setmode(GPIO.BCM)
GPIO_SCHALTER = 24
GPIO_RELAIS = 22
GPIO_BEW = 25

GPIO.setup(GPIO_SCHALTER, GPIO.IN,  pull_up_down = GPIO.PUD_UP)
GPIO.setup(GPIO_RELAIS, GPIO.OUT)
GPIO.setup(GPIO_BEW, GPIO.IN)

prev_Time = datetime.datetime.now() + datetime.timedelta(minutes=5)
randomfile_prev = None

def rndmp3 ():
    global randomfile_prev
    now_time = datetime.datetime.now().time()
    start = datetime.time(16, 00)
    end = datetime.time(6, 00)
    if now_time >= start or now_time <= end:
      verz = "/root/mp3"
      verz1 = '  /root/mp3/'
    else:
      verz = "/root/mp31"
      verz1 = '  /root/mp31/'
    randomfile = random.choice(os.listdir(verz))
    while randomfile_prev==randomfile:
      randomfile = random.choice(os.listdir(verz))
    else:
     file = verz1+ randomfile
     os.system ('mpg123 -m' + file)
     randomfile_prev=randomfile

def rndafter5():
    global prev_Time
    if datetime.datetime.now() >= prev_Time:
      randomfiles = random.choice(os.listdir("/root/mp32"))
      files = ' /root/mp32/'+ randomfiles
      os.system ('mpg123 -m' + files)
      prev_Time = datetime.datetime.now() + datetime.timedelta(minutes=5)
    else:
      prev_Time = datetime.datetime.now() + datetime.timedelta(minutes=5)

Current_State = 1
Previous_State = 1
CurrentBew_State = 1
PreviousBew_State = 1

try:
   
   GPIO.output(GPIO_RELAIS, 1)
   time.sleep(2)
   GPIO.output(GPIO_RELAIS, 0)

   while True:
   
      CurrentBew_State = GPIO.input(GPIO_BEW)
      Current_State = GPIO.input(GPIO_SCHALTER)
      if Current_State==0 and Previous_State==1:
         GPIO.output(GPIO_RELAIS, 1)
         Thread(target=rndmp3).start()
         Previous_State=0

      elif Current_State==1 and Previous_State==0:
         GPIO.output(GPIO_RELAIS, 0)
         Previous_State=1
	 time.sleep(0.5)
      
      elif CurrentBew_State==1 and PreviousBew_State==0:
	 Thread(target=rndafter5).start()
	 PreviousBew_State=1
      
      elif CurrentBew_State==0 and PreviousBew_State==1:
	 PreviousBew_State=0	
      time.sleep(0.01)

except KeyboardInterrupt:
     GPIO.cleanup()

