#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from ros2_hydrotest_turusov_interfaces.srv import CountChar

class CharCountClient(Node):
    def __init__(self):
        super().__init__('char_count_client') # имя узла
        self.client = self.create_client(CountChar, 'count_chars') # тип из файла .srv вернее его имя. 
        # count_chars bvz имя сервиса . Оно должно совпадать у сервера и клиента 
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Сервис недоступен, ждём...')

    def send_request(self, text):
        t = CountChar.Request()
        t.stroka = text
        ss = self.client.call_async(t) # обращение к серверу : отправка запроса и получение контейнера
        rclpy.spin_until_future_complete(self, ss) # а это что ? 
        return ss.result() # что такое result ?  

def main(args=None):
    rclpy.init(args=args)
    nod = CharCountClient() # объект клиента
    strings = ["Hello", "ROS2", "Testing", "Привет мир"]
    for s in strings:
        resp = nod.send_request(s) # 
        nod.get_logger().info(f'Длина строки "{s}" = {resp.dlina}')
    nod.destroy_node() # уничтожение узла
    rclpy.shutdown() # завершение процесса

if __name__ == '__main__':
    main()