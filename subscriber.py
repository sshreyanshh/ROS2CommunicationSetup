import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RobotSubscriber(Node):

    def __init__(self):
        super().__init__('robot_subscriber')

        self.subscription = self.create_subscription(
            String,
            '/robot_command',
            self.command_callback,
            10
        )

    def command_callback(self, msg):

        print(f"Received: {msg.data}")

        if msg.data == "LEFT":
            print("🤖 Action: Turning LEFT")

        elif msg.data == "RIGHT":
            print("🤖 Action: Turning RIGHT")

        elif msg.data == "CENTER":
            print("🤖 Action: Moving FORWARD")

        elif msg.data == "STOP":
            print("🤖 Action: STOPPED")

        else:
            print("⚠️ Unknown command")


def main(args=None):
    rclpy.init(args=args)

    node = RobotSubscriber()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()