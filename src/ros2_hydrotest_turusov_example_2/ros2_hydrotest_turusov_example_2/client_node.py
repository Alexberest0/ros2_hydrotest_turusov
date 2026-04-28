#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from ros2_hydrotest_turusov_interfaces.srv import CountChar

class CharCountClient(Node):
    def __init__(self):
        super().__init__('char_count_client')
        self.client = self.create_client(CountChar, 'count_chars')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Сервис недоступен, ждём...')

    def send_request(self, text):
        t = CountChar.Request()
        t.stroka = text
        ss = self.client.call_async(t)
        rclpy.spin_until_future_complete(self, ss)
        return ss.result()

def main(args=None):
    rclpy.init(args=args)
    nod = CharCountClient()
    strings = ["Hello", "ROS2", "Testing", "Привет мир"]
    for s in strings:
        resp = nod.send_request(s)
        nod.get_logger().info(f'Длина строки "{s}" = {resp.dlina}')
    nod.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()