#!/usr/bin/env python3
import rclpy                    
from rclpy.node import Node      
from ros2_hydrotest_turusov_interfaces.srv import CountChar  # импорт из srv


class CountCharServer(Node):     # класс узла-сервера (имя любое) наследник Node  
    def __init__(self):
        super().__init__('Server_count_chars')   # имя узла
        # Создаём сервис с типом CountChar имя srv файла и в нем же поля- описания класса,
        # имя сервиса сервер + клиент - 'count_chars' и callback-функцией f
        self.server = self.create_service(CountChar, 'count_chars', self.f)

    def f(self, request, response):
        # request - входные данные на сервер. Получить входную строку request.stroka
        # response - выходные данные response.dlina
        response.dlina = len(request.stroka)
        self.get_logger().info(f'Получено: "{request.stroka}" -> длина {response.dlina}')
        return response   


def main(args=None):
    rclpy.init(args=args)                # 1. Инициализируем ROS2
    node = CountCharServer()             # 2. Создаём экземпляр нашего узла
    rclpy.spin(node)                     # 3. Запускаем цикл обработки событий (сервер ждёт запросы)
    node.destroy_node()                  # 4. Освобождаем ресурсы после остановки
    rclpy.shutdown()                     # 5. Завершаем работу ROS2


if __name__ == '__main__':
    main()