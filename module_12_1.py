"""
coding: utf-8
Дегтярев Виталий (группа 22/08)
Домашнее задание №12.1
Домашнее задание по теме "Простые Юнит-Тесты"
"""


import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner1 = Runner('Oleg')
        for _ in range(10): runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner2 = Runner('Vasia')
        for _ in range(10): runner2.run()
        self.assertEqual(runner2.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner3 = Runner('John')
        runner4 = Runner('Mike')
        for _ in range(10): runner3.run()
        for _ in range(10): runner4.walk()
        self.assertNotEqual(runner3.distance, runner4.distance)


if __name__ == '__main__':
    unittest.main()