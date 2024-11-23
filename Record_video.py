from djitellopy import tello
from time import sleep
import cv2

drone = tello()
drone.connect()

keepRecording = True
drone.streamon()
frame_read = drone.get_frame_read()

def videoRecorder():
    # create a VideoWrite object, recoring to ./video.avi
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()

# we need to run the recorder in a seperate thread, otherwise blocking options
#  would prevent frames from getting added to the video
recorder = Thread(target=videoRecorder)
recorder.start()

drone.takeoff()
drone.move_up(100)
drone.rotate_counter_clockwise(360)
drone.land()

keepRecording = False
recorder.join()


