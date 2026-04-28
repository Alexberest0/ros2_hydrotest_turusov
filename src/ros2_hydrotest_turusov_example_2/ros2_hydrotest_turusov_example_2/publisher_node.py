#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32   # тип сообщения: 32-битное целое

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node') # publisher_node - имя узла
        # Создаём издателя (publisher) для топика 'counter'
        # Аргументы: тип сообщения, имя топика, размер очереди (сколько сообщений хранить, если подписчик не успевает)
        self.publisher = self.create_publisher(Int32, 'counter', 10)

        # Создаём таймер с периодом 1.0 секунда
        # Он будет вызывать функцию timer_callback каждую секунду
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.counter = 0

    def timer_callback(self): # ф-ия вызывется по таймеру
        self.counter += 1
        #объект сообщения типа Int32
        msg = Int32()
        msg.data= self.counter

        # Публикуем сообщение в топик
        self.publisher.publish(msg)

        # лог в консоль
        self.get_logger().info(f'Опубликовано: {self.counter}')

def main(args=None):
    rclpy.init(args=args)                # инициализация ROS2
    node = PublisherNode()               # создаём узел-публикатор
    rclpy.spin(node)                     # запускаем цикл обработки 
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()