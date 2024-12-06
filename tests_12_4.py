"""
coding: utf-8
Дегтярев Виталий (группа 22/08)
Домашнее задание №12.4
Домашнее задание по теме "Логирование"
"""


import unittest, logging
from rt_with_exceptions import Runner


logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="utf-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):


    def test_walk(self):
        try:
            runner1 = Runner('Oleg', -1)
            for _ in range(10): runner1.walk()
            self.assertEqual(runner1.distance, 100)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для объекта Runner', exc_info=True)


    def test_run(self):
        try:
            runner2 = Runner(1, 10)
            for _ in range(10): runner2.run()
            self.assertEqual(runner2.distance, 200)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


    def test_challenge(self):
        runner3 = Runner('John', 15)
        runner4 = Runner('Mike', 20)
        for _ in range(10): runner3.run()
        for _ in range(10): runner4.walk()
        self.assertNotEqual(runner3.distance, runner4.distance)


if __name__ == '__main__':
    unittest.main()


