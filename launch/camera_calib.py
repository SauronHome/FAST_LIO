from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from pathlib import Path


def generate_launch_description():
    # Create the LaunchDescription object
    ld = LaunchDescription()
    # Get the lidar_calib.yaml file path
    lidar_calib_file = str("/ssd/adam/mordor/configs/lidar/lidar_calib.yaml")

    # rosbag_play = Node(
    #     package='rosbag2',
    #     executable='play',
    #     name='rosbag_play',
    #     output='screen',
    #     arguments=['/ssd/adam/mordor/outputs/rosbag/rosbag2_2024_09_03-23_25_23']
    # )
    # ld.add_action(rosbag_play)

    # LiDAR-Camera calibration node
    lidar_camera_calib = Node(
        package='lidar_camera_calib',
        executable='lidar_camera_calib',
        name='lidar_camera_calib',
        output='screen',
        parameters=[lidar_calib_file]
    )
    ld.add_action(lidar_camera_calib)

    return ld