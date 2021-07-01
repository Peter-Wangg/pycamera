import picamera
import datetime as dt
from subprocess import call
import io
import time

with picamera.PiCamera() as camera:
    
    #camera.annotate_background=picamera.Color('black')
    #camera.annotate_text=dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    
    #set up camera
    camera.resolution=(1280,1440)
    camera.framerate=25
    camera.annotate_text_size=20
    # camera.saturation = 50
    # camera.brightness = 40
    # camera.shutter_speed = 6000000
    # camera.iso = 150
    # camera.sharpness = 0
    
    camera.start_preview()
    camera.start_recording('fileName.h264')#fileName
    
    #warmup camera
    time.sleep(2)
    
    start=dt.datetime.now()
    while(dt.datetime.now()-start).seconds<10:        
        camera.annotate_text=dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
              
        #camera.wait_recording(0)
        #frame_index=str(camera.frame.index)
		
        #Timestamp_File.write()
        #Timestamp_File.write("frame index: "+frame_index+"  system time: "+camera.annotate_text+"\n")
        
    camera.stop_recording()
    camera.stop_preview()
    print("OK")
    
command="MP4Box -add fileName.h264 fileName.mp4"#fileName
call([command], shell=True)
print("video converted.")



