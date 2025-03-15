#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleMover(Node):
    def __init__(self):
        super().__init__('turtle_mover')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(1.0, self.move_turtle)
        self.step = 0  # Track movement steps
        self.get_logger().info("Turtle Mover Node has started!")

    def move_turtle(self):
        cmd = Twist()
        if self.step % 4 == 0:
            cmd.linear.x = 2.0  # Move forward
        elif self.step % 4 == 1:
            cmd.angular.z = 1.57  # Turn 90 degrees
        elif self.step % 4 == 2:
            cmd.linear.x = 2.0  # Move forward
        elif self.step % 4 == 3:
            cmd.angular.z = 1.57  # Turn 90 degrees
        self.publisher_.publish(cmd)
        self.step += 1

def main(args=None):
    rclpy.init(args=args)
    node = TurtleMover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
