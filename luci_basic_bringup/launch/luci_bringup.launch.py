from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_prefix
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import TimerAction
import os


def generate_launch_description():

    grpc_pkg_prefix = get_package_prefix('luci_grpc_interface')
    grpc_executable = os.path.join(
        grpc_pkg_prefix,
        'lib',
        'luci_grpc_interface',
        'grpc_interface_node'
    )

    luci_grpc_node = ExecuteProcess(
        cmd=[grpc_executable, '-a', '192.168.0.200'],
        output='screen'
    )

    ekf_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_filter_node',
        output='screen',
        parameters=[{
            'frequency': 50.0,
            'sensor_timeout': 0.1,
            'two_d_mode': True,
            'odom0': '/odom',   # raw encoder odometry
            'odom0_config': [True, True, False,
                             False, False, True,
                             True, False, False,
                             False, False, False,
                             False, False, False],
            'imu0': '/luci/imu',
            'imu0_config': [False, False, False,
                            False, False, True,   # yaw orientation
                            False, False, False,
                            False, False, True,   # yaw velocity
                            False, False, False],
            'map_frame': 'map',           
            'odom_frame': 'odom',         
            'base_link_frame': 'base_link',
            'world_frame': 'odom',         
        }]
    )

    luci_control_node = Node(
        package="luci_core_control",
        executable="luci_state_manager_node",
        name="luci_core_control_node",
    )

    luci_odom_node = Node(
        package="luci_encoder_odometry",
        executable="encoder_to_odom_node",
        name="encoder_to_odom_node",
    )

    luci_wheelchair_node = Node(
        package="luci_transforms",
        executable="luci_dev_kit_tf_node",
        name="quickie_500m_tf_node",
    )

    # twist_to_luci_node = Node(
    #     package='luci_basic_teleop',
    #     executable='twist_to_luci',
    #     name='twist_to_luci_node',
    #     output='screen'
    # )
    central_controller_node = Node(
        package='luci_core_control',
        executable='luci_central_controller',
        name='luci_central_controller_node',
    )

    return LaunchDescription ([
        luci_grpc_node,
        luci_wheelchair_node,
        luci_odom_node,
        ekf_node,
        luci_control_node,
        central_controller_node,
    ])