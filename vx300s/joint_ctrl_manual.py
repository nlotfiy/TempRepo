from interbotix_xs_modules.arm import InterbotixManipulatorXS
import numpy as np
import sys
import time


# To get started, open a terminal and type 'roslaunch interbotix_xsarm_control xsarm_control.launch robot_model:=wx250'
# Then change to this directory and type 'python bartender.py  # python3 bartender.py if using ROS Noetic'
# self.joint_names = ['waist', 'shoulder', 'elbow', 'forearm_roll', 'wrist_angle', 'wrist_rotate']

# Default joint limits for VX300S model (in degrees)

# 'waist': (-180, 180),
# 'shoulder': (-101, 101),
# 'elbow': (-101, 92),
# 'forearm_roll': (-180, 180),
# 'wrist_angle': (-107, 130),
# 'wrist_rotate': (-180, 180)

def main():
    bot = InterbotixManipulatorXS("vx300s", "arm", "gripper")

    bot.arm.go_to_home_pose()
    joint_name = input("Please enter the joint name: ")
    try:
        while True:
            joint_var = float(input("Please enter the desired angle in degrees: "))
            joint_var_rad = (np.pi/180)*joint_var
            bot.arm.set_single_joint_position(joint_name, joint_var_rad)
            print(bot.arm.T_sb)
            time.sleep(2)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
    
    bot.arm.go_to_sleep_pose()

   

if __name__=='__main__':
    main()

