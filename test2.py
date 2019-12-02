import cozmo
import time
def cozmo_program(robot: cozmo.robot.Robot):
    robot.camera.image_stream_enabled = True
    
    time.sleep(1)
    #image = None
    for i in range(10):
        #image = None
        #time.sleep(1)
        #while image is None:
        image = robot.world.latest_image
        print(image)
        print(image.image_number)
        print(image.image_recv_time)
        image.raw_image.save("%s.jpg" % i)
        time.sleep(.1)
    
    
cozmo.run_program(cozmo_program)
