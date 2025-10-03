# LUCI Basic Teleop Package

The `luci_basic_bringup` package provides launch files and configurations to initialize and manage LUCI, a robotic wheelchair. This package is designed for Linux-based systems and is compatible with the [luci_ros2_sdk](https://github.com/lucimobility/luci-ros2-sdk).

---

## Overview

### Nodes
- `/luci_bringup_node`: Manages the initialization and configuration of LUCI.

### Topics 
- **Name**: `/luci/camera_points`  
    **Message Type**: `[sensor_msgs/msg/PointCloud2]`  

- **Name**: `/luci/chair_profile`  
    **Message Type**: `[std_msgs/msg/Int32]` 

- **Name**: `/luci/encoders`  
    **Message Type**: `[luci_messages/msg/LuciEncoders]`  

- **Name**: `/luci/imu`  
    **Message Type**: `[luci_messages/msg/LuciImu, sensor_msgs/msg/Imu]`  

- **Name**: `/luci/joystick_position`  
    **Message Type**: `[luci_messages/msg/JoystickPosition]`  

- **Name**: `/luci/joystick_scaling`  
    **Message Type**: `[luci_messages/msg/JoystickScaling]`  

- **Name**: `/luci/odom`  
    **Message Type**: `[nav_msgs/msg/Odometry]`  

- **Name**: `/luci/override_button_data`  
    **Message Type**: `[std_msgs/msg/Int32]`  

- **Name**: `/luci/override_button_press_count_data`  
    **Message Type**: `[std_msgs/msg/Int32]`  

- **Name**: `/luci/radar_points`  
    **Message Type**: `[sensor_msgs/msg/PointCloud2]`  

- **Name**: `/luci/remote_joystick`  
    **Message Type**: `[luci_messages/msg/LuciJoystick]`  

- **Name**: `/luci/scaling`  
    **Message Type**: `[luci_messages/msg/LuciZoneScaling]`  

- **Name**: `/luci/speed_setting`  
    **Message Type**: `[std_msgs/msg/Int32]`  

- **Name**: `/luci/ultrasonic_points`  
    **Message Type**: `[sensor_msgs/msg/PointCloud2]`  

- **Name**: `/odom`  
    **Message Type**: `[nav_msgs/msg/Odometry]`  

- **Name**: `/odometry/filtered`  
    **Message Type**: `[nav_msgs/msg/Odometry]`  

---

## Prerequisiteshttps://docs.ros.org/en/melodic/api/robot_localization/html/state_estimation_nodes.html

Ensure your ROS2 workspace includes the following packages:  
```bash
ros_ws
└── src
    ├── luci-ros2-grpc
    ├── luci-ros2-msgs
    ├── luci-ros2-odom
    └── luci-ros2-transforms
```

### LUCI SDK Dependencies
- [luci-ros2-grpc](https://github.com/UW-CTRL/luci-ros2-grpc): Handles gRPC communication with LUCI.  
- [luci-ros2-msgs](https://github.com/UW-CTRL/luci-ros2-msgs): Defines ROS2 message types for LUCI. 
- [luci-ros2-odom](https://github.com/UW-CTRL/luci-ros2-odom): Creates the odom values from the wheelchair's encoders.
- [luci-ros2-transforms](https://github.com/lucimobility/luci-ros2-transforms): Provides transformation utilities for LUCI. 
- [efk_localization_node](https://docs.ros.org/en/melodic/api/robot_localization/html/state_estimation_nodes.html): Create the filtered odom topic for better localization using the wheelchair's IMU

---

## Build Instructions

1. Navigate to your ROS2 workspace:
   ```bash
   cd ~/ros_ws
   ```
2. Build the workspace:
   ```bash
   colcon build
   ```
3. Source the workspace:
   ```bash
   source install/setup.bash
   ```

---

## Running the Package

### Using Launch Files

1. Launch the bringup configuration:
   ```bash
   ros2 launch luci_basic_bringup luci_bringup_launch.py
   ```
2. This will start the necessary nodes and establish communication with LUCI.

**Note**: Update the IP address in the launch file to match the robot's IP.

---

### Running Without Launch Files

1. Start the gRPC interface node:
   ```bash
   ros2 run luci_grpc_interface grpc_interface_node -a <robot_ip>
   ```
2. Run the bringup node:
    ```bash
    ros2 run luci_basic_bringup luci_bringup_node
    ```
3. Open a new terminal and run the encoder node:
    ```bash
    ros2 run luci_encoder_odometry encoder_to_odom_node
    ```

4. Open a new terminal and run the wheelchair node:
    ```bash
    ros2 run luci_transforms quickie_500m_tf_node
    ```

---

## Changing the Robot's IP Address

To ensure proper communication with LUCI, you must update the IP address in the launch files or when running nodes manually. Replace `<robot_ip>` with the actual IP address of the robot.

### Updating the Launch Files
1. Open the relevant launch file (e.g., `luci_bringup_launch.py`) in a text editor.
2. Locate the parameter for the gRPC interface node's IP address.
3. Update the IP address to match the robot's IP.


**Note**: Ensure the robot's IP address is reachable from your network.  

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
