import numpy as np #Used to Handle Matrices Effectively
import math #For Cosine and Sine Functions

def get_rotation_matrix(roll, pitch, yaw): #Generating Rotation matrix from Rover Rotation Angles
    roll  = math.radians(roll) #Rotation around X axis by angle roll
    pitch = math.radians(pitch) #Rotation around Y axis by angle pitch
    yaw   = math.radians(yaw) #Rotation around Z axis by angle yaw

    Rx = np.array([
        [1,           0,            0],
        [0,  math.cos(roll), -math.sin(roll)],   #Standard Rotation Matrices for all 3 axes
        [0,  math.sin(roll),  math.cos(roll)]
    ])

    Ry = np.array([
        [ math.cos(pitch), 0, math.sin(pitch)],
        [0,                1,              0  ],
        [-math.sin(pitch), 0, math.cos(pitch)]
    ])

    Rz = np.array([
        [math.cos(yaw), -math.sin(yaw), 0],
        [math.sin(yaw),  math.cos(yaw), 0],
        [0,              0,             1]
    ])

    R = Rz @ Ry @ Rx #Final Rotation Matrix is the Matrix Product of Rz Ry and Rx in order
    return R #Returning Final Matrix

def transform_to_world(obj_cam, rover_pos, rover_rotation): #Transforming Into World Frame
    P_rover = np.array(obj_cam, dtype=float) #Converting Position Tuple of object camera into Numpy Array
    roll, pitch, yaw = rover_rotation #Unpacking Tuple Angles
    R = get_rotation_matrix(roll, pitch, yaw) # Getting The Final Rotation Matrix from the function

    T = np.array(rover_pos, dtype=float)#Converting Position Tuple of rover into Numpy Array


    P_world = R @ P_rover + T #Formula to convert the coordinates from Rover camera frame to World Frame
    return P_world

if __name__ == "__main__":
    # ── Object coordinates in camera frame ──
    x_cam = float(input("Enter object X (camera frame): "))
    y_cam = float(input("Enter object Y (camera frame): "))
    z_cam = float(input("Enter object Z (camera frame): "))

    # ── Rover position in world frame ──
    x_rov = float(input("Enter rover X (world frame): "))
    y_rov = float(input("Enter rover Y (world frame): "))
    z_rov = float(input("Enter rover Z (world frame): "))

    # ── Rover rotation in degrees ──
    roll  = float(input("Enter rover roll  (degrees): "))
    pitch = float(input("Enter rover pitch (degrees): "))
    yaw   = float(input("Enter rover yaw   (degrees): "))

    # ── Run transformation ──
    obj_cam   = (x_cam, y_cam, z_cam)
    rover_pos = (x_rov, y_rov, z_rov)
    rover_rot = (roll, pitch, yaw)

    result = transform_to_world(obj_cam, rover_pos, rover_rot)

    # ── Output ──
    print(f"\nObject in Camera Frame : {obj_cam}")
    print(f"Rover Position (World) : {rover_pos}")
    print(f"Rover Rotation (deg)   : {rover_rot}")
    print(f"Object in World Frame  : ({result[0]:.4f}, {result[1]:.4f}, {result[2]:.4f})")