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

    luci_grpc_node = TimerAction(
            period=3.0,
            actions=[
                ExecuteProcess(
                    cmd=[grpc_executable, '-a', '192.168.0.200'],
                    output='screen'
                )
        ]
    )

    luci_wheelchair_node = Node(
        package="luci_transforms",
        executable="quickie_500m_tf_node",
        name="quickie_500m_tf_node",
    )
    return LaunchDescription ([
        luci_grpc_node,
        luci_wheelchair_node
    ])