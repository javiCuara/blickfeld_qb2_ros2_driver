#!/usr/bin/env python

from launch import LaunchDescription
from launch_ros.descriptions import ComposableNode
from launch_ros.actions import ComposableNodeContainer
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Get the path to the parameters file
    config_file = os.path.join(
        get_package_share_directory('blickfeld_qb2_ros2_driver'),
        'config',
        'terra.yaml'
    )
    
    container = ComposableNodeContainer(
        name="blickfeld_qb2_component",
        namespace="",
        package="rclcpp_components",
        executable="component_container",
        composable_node_descriptions=[
            ComposableNode(
                package="blickfeld_qb2_ros2_driver",
                plugin="blickfeld::ros_interop::Qb2Driver",
                name="blickfeld_qb2_driver",
                parameters=[config_file],
            ),
        ],
        output="screen",
    )
    
    return LaunchDescription([container])
