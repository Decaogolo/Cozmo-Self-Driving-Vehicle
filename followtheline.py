import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
def cozmo_program(robot: cozmo.robot.Robot):
    robot.camera.image_stream_enabled = True
    
    time.sleep(1)
    robot.set_lift_height(cozmo.robot.MAX_LIFT_HEIGHT_MM).wait_for_completed()
    robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE).wait_for_completed()
    for i in range(100):
        
        
        image = robot.world.latest_image.raw_image
        #image = image.crop((40,120,280,140))
        image = image.crop((0,180,320,200))
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(10.0)
        image = ImageOps.invert(image)
        image = image.convert(mode="1")
        image.save("%s.jpg" % i)
        left_side = image.crop((0,0,(image.width/2),image.height))
        right_side = image.crop(((image.width/2),0,image.width,image.height))
        #left_side.save("left%s.jpg" % i)
        #right_side.save("right%s.jpg" % i)
        left_pixels = list(left_side.getdata())
        right_pixels = list(right_side.getdata())
        left_pixels = left_pixels.count(255)
        right_pixels = right_pixels.count(255)
        print(i)
        print("left pixels = %s" % left_pixels)
        print("right pixels = %s" % right_pixels)
        diff = right_pixels - left_pixels
        print(diff)
        if diff < -2000:
            print("hard left")
            robot.turn_in_place(degrees(20)).wait_for_completed()
            robot.drive_straight(distance_mm(10), speed_mmps(50), should_play_anim=False).wait_for_completed()
            #robot.drive_wheels(-20,10)
            
        if diff > 2000:
            print("hard right")
            robot.turn_in_place(degrees(-20)).wait_for_completed()
            robot.drive_straight(distance_mm(10), speed_mmps(50), should_play_anim=False).wait_for_completed()
            
            #robot.drive_wheels(10,-20)
        if diff < -1000 and diff >= -2000:
            print("turning left")
            robot.turn_in_place(degrees(10)).wait_for_completed()
            robot.drive_straight(distance_mm(10), speed_mmps(50), should_play_anim=False).wait_for_completed()
            #robot.drive_wheels(0,20)
            
        if diff > 1000 and diff <= 2000:
            print("turning right")
            robot.turn_in_place(degrees(-10)).wait_for_completed()
            robot.drive_straight(distance_mm(10), speed_mmps(50), should_play_anim=False).wait_for_completed()
            #robot.drive_wheels(20,0)
        if diff < -500 and diff >= -1000:
            print("slight left")
            robot.turn_in_place(degrees(5)).wait_for_completed()
            robot.drive_straight(distance_mm(10), speed_mmps(50), should_play_anim=False).wait_for_completed()
            #robot.drive_wheels(0,10)
        if diff > 500 and diff <= 1000:
            print("slight right")
            robot.turn_in_place(degrees(-5)).wait_for_completed()
            robot.drive_straight(distance_mm(10), speed_mmps(50), should_play_anim=False).wait_for_completed()
            #robot.drive_wheels(10,0)
            
        if diff > -500 and diff < 500:
            print("driving straight")
            robot.drive_straight(distance_mm(20), speed_mmps(50), should_play_anim=False).wait_for_completed()
            #robot.drive_wheels(10,10)
        robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE).wait_for_completed()
        #robot.drive_straight(distance_mm(50), speed_mmps(50), should_play_anim=False).wait_for_completed()
        #robot.turn_in_place(degrees(90)).wait_for_completed()
        
        
        time.sleep(1)
    
    
cozmo.run_program(cozmo_program, use_viewer = False)
