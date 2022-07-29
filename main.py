from picamera import PiCamera
from datetime import datetime
from time import sleep

camera = PiCamera()
camera.resolution = (2592, 1944)

while True:
    camera.start_preview()
    sleep(5)
    now = datetime.now().strftime("%Y-%m-%d--%H:%M:%S")
    file_name = f'data/{now}.jpg'
    print(f'Saving img at {file_name}')
    camera.capture(file_name)
    camera.stop_preview()
    sleep(295)
