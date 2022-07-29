from picamera import PiCamera
from datetime import datetime
from time import sleep

camera = PiCamera()
camera.resolution = (2592, 1944)

while True:
    camera.start_preview()
    sleep(5)
    now = datetime.now()
    file_name = f'/home/pi/data/{now}.jpg'
    camera.capture(file_name)
    camera.stop_preview()
    sleep(295)
