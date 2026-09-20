import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RobotPublisher(Node):

    def __init__(self):
        super().__init__('robot_publisher')

        self.publisher = self.create_publisher(
            String,
            '/robot_command',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_command
        )

    def publish_command(self):
        msg = String()

        msg.data = "LEFT"

        self.publisher.publish(msg)

        print(f"Publishing: {msg.data}")


def main(args=None):
    rclpy.init(args=args)

    node = RobotPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()