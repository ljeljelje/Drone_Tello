from djitellopy import tello
from time import sleep
import cv2

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.streamon()
frame_read = drone.get_frame_read()

drone.takeoff()

cv2.imwrite("Picture.png", frame_read)

drone.streamoff()

drone.land()

