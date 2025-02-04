import pybullet as p  
import pybullet_data 
import math  
import time  

# -------- Simulation Initialization --------
# Connect to PyBullet physics server in GUI mode
p.connect(p.GUI)

# Add PyBullet's built-in data path to search path
# This allows loading built-in URDF models, textures, etc.
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Set gravity in the simulation environment (in m/s²)
p.setGravity(0, 0, -9.81)

# Load the ground plane URDF model
planeId = p.loadURDF("plane.urdf")
# Load the Franka Panda robot URDF model
# useFixedBase=True: Robot base is fixed in space (won't fall)
# basePosition: Initial position of the robot [x, y, z]
robotId = p.loadURDF("franka_panda/panda.urdf", useFixedBase=True, basePosition=[0, 0, 0])

# -------- Joint Information --------
# Get the total number of joints in the robot
num_joints = p.getNumJoints(robotId)
# Print information about each joint
for i in range(num_joints):
    joint_info = p.getJointInfo(robotId, i)
    print(f"Joint {i}: Name: {joint_info[1].decode('utf-8')}, Type: {joint_info[2]}")

# -------- Main Simulation Loop --------
for _ in range(10000):  # Run simulation for 10000 steps
    # Calculate target angle for joint 0
    # 1.57 ≈ π/2 radians (90 degrees)
    # sin(_ * 0.01) creates smooth oscillation between -1 and 1
    # Multiplied by 0.5 and added to 1 gives range of 0.5 to 1.5
    # Final angle oscillates between 0.785 (45°) and 2.355 (135°) radians
    angle = 1.57 * (1 + 0.5 * math.sin(_ * 0.01))

    # Control joint 0 of the robot
    # Parameters:
    # - robotId: ID of the robot
    # - 0: Joint index
    # - p.POSITION_CONTROL: Control mode (position-based)
    # - angle: Target position
    # - force: Maximum force applied to reach target (500 N*m)
    p.setJointMotorControl2(robotId, 0, p.POSITION_CONTROL, angle, force=500)

    # Step the simulation forward
    p.stepSimulation()

    # Control simulation speed
    # 1/240 seconds per step (240 Hz simulation rate)
    time.sleep(1/240)

# -------- Cleanup --------
# Disconnect from the physics server when done
p.disconnect()